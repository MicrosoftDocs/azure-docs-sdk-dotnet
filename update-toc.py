# This script is intended for use in intermediate doc repos generated from docs.ms CI.
# Given a reference ToC and a set of namespaces, limit the reference to ToC entries that contain
# namespaces in our set.

import argparse
import os
import fnmatch
import re
import json
import xml.etree.ElementTree as ET

# by default, yaml does not maintain insertion order of the dicts
# given that this is intended to generate TABLE OF CONTENTS values,
# maintaining this order is important.
# The drop-in replacement oyaml is a handy solution for us.
import oyaml as yaml

MONIKER_REPLACEMENTS = ['{moniker}','<moniker>']


def fail_reference_shape(path, expected, actual):
    raise ValueError(
        f"{path}: expected {expected}, found {type(actual).__name__}"
    )


def validate_reference_node(node, path):
    if not isinstance(node, dict):
        fail_reference_shape(path, "a mapping", node)

    if "children" in node:
        children = node["children"]
        if not isinstance(children, list):
            fail_reference_shape(f"{path}.children", "a list of namespace strings", children)

        for index, child in enumerate(children):
            if not isinstance(child, str):
                fail_reference_shape(
                    f"{path}.children[{index}]",
                    "a namespace string",
                    child,
                )

    if "items" in node:
        items = node["items"]
        if not isinstance(items, list):
            fail_reference_shape(f"{path}.items", "a list of mappings", items)

        for index, item in enumerate(items):
            validate_reference_node(item, f"{path}.items[{index}]")


def validate_reference_toc(reference_toc):
    if not isinstance(reference_toc, list) or not reference_toc:
        fail_reference_shape("root", "a non-empty list", reference_toc)

    validate_reference_node(reference_toc[0], "root[0]")

class PathResolver:
    def __init__(self, doc_repo_location = None, moniker = ""):
        self.excluded_href_paths = []
        self.target_moniker = moniker

        self.doc_repo_location = doc_repo_location

        if self.doc_repo_location:
            self.excluded_href_paths = self.get_non_standard_hrefs(self.doc_repo_location)

    # the doc builds have the capability to reference readmes from external repos (they resolve during publishing)
    # this means that we can't simply check the href values for existence. If they are an href that STARTS with one of the
    # "dependent repositories" than we should leave them exactly as is.
    # amend_href is the core of the logic for handling referenced files and ensures that we cannot refer to the same readme twice
    # from two different reference ymls
    def amend_href(self, toc_dict):
        if not self.doc_repo_location:
            return toc_dict

        input_string = toc_dict["href"]

        # if this is an external readme, we should not attempt to resolve the file to a different one, just return with no changes
        if any([input_string.startswith(href) for href in self.excluded_href_paths]):
            return toc_dict 

        # create a resolvable path to the readme on disk, without any of the docs ms specificity
        resolvable_path = os.path.normpath(os.path.join(self.doc_repo_location, input_string.replace("~/", "")))

        # apply moniker folder adjustments if necessary
        if self.target_moniker is not None:
            for replacement in MONIKER_REPLACEMENTS:
                # input string maintains leading ~/ necessary for docs. update the moniker folder if it exists
                input_string = input_string.replace(replacement, self.target_moniker)

                # the resolvable path is different from the input_string in that it is actually a resolvable path.
                # update it with the moniker folder so we can test for existence of the file
                resolvable_path = resolvable_path.replace(replacement, self.target_moniker)

        possible_target_readme = os.path.splitext(resolvable_path)[0] + ".md"

        if os.path.exists(possible_target_readme):
            toc_dict["href"] = input_string
        else:
            toc_dict.pop("href")
            toc_dict["landingPageType"] = "Service"

        return toc_dict

    # the doc builds have the capability to reference readmes from external repos (they resolve during publishing)
    # this means that we can't simply check the href values for existence. If they are an href that STARTS with one of the
    # "dependent repositories" than we should leave them exactly as is. This function returns the start paths
    def get_non_standard_hrefs(self, doc_repo_location):
        excluded_href_paths = []

        target = os.path.join(doc_repo_location, ".openpublishing.publish.config.json")
        with open(target, "r") as f:
            data = json.load(f)

        for dependent_repo in data["dependent_repositories"]:
            excluded_href_paths.append("~/{}".format(dependent_repo["path_to_root"]))

        return excluded_href_paths


def filter_children(targeted_ns_list, known_namespaces):
    amended_list = []

    for ns in targeted_ns_list:
        # also need to handle when the namespace grep is a pattern
        # azure-eventhubs* <-- for instance
        if ns in known_namespaces:
            amended_list.append(ns)

    return amended_list

# a post-order recursive function that returns a modified reference.yml
# based on the set of namespaces that we've grabbed from autogenerated ToC.yml
def filter_toc(toc_dict, namespaces, path_resolver):
    if toc_dict is None:
        return None
    # internal node
    if "items" in toc_dict:
        # recurse as mant times as necessary
        item_list = []
        for item in toc_dict['items']:
            result_n = filter_toc(item, namespaces, path_resolver)
            # only append the result if we know it exists
            if result_n:
                item_list.append(result_n)
        if item_list:
            toc_dict["items"] = item_list
        else:
            return None

    # handle href
    if "href" in toc_dict:
        toc_dict = path_resolver.amend_href(toc_dict)

    # leaf node
    if "children" in toc_dict:
        filtered_children = filter_children(toc_dict["children"], namespaces)
        # if we filter out all the children, this node should simply cease to exist
        if not filtered_children:
            return None
    elif "href" not in toc_dict and "items" not in toc_dict:
        return None

    return toc_dict

def grep_children_namespaces(autogenerated_toc_xml):

    return [ns.attrib['Name'] for ns in ET.parse(args.namespaces).getroot()[1:] if ns.tag == 'Namespace'] + ['**']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
      Combines a reference and target ToC. The new target ToC mirrors the reference, omitting ToC
      entries that are NOT present in the preview output.
      """
    )

    parser.add_argument("-r", "--reference", help="The source ToC.yml", required=True)

    parser.add_argument("-t", "--target", help="The target ToC.yml", required=True)

    parser.add_argument(
        "-n",
        "--namespaces",
        help="The ToC.yml where target autogenerated documentation exists",
        required=True,
    )

    parser.add_argument(
        "-d",
        "--docrepo",
        help="The root directory of the target documentation repository.",
        required=True,
    )
    
    parser.add_argument(
        "-m",
        "--moniker",
        help="Selected moniker. Used when filling in moniker-folder path updates.",
        default="",
        required=False,
    )

    args = parser.parse_args()
    try:
        with open(args.reference, "r") as reference_yml:
            base_reference_toc = yaml.safe_load(reference_yml)
        validate_reference_toc(base_reference_toc)
    except Exception:
        print(
            "Execution requires the known reference yml be defined and have children values as namespace strings."
        )
        raise SystemExit(4)
    try:
        target_autogenerated_toc = ET.parse(args.namespaces).getroot()[0]
    except Exception:
        print(
            "Execution requires the known namespaces yml be defined. Please check if the target xml has assembly tags."
        )
        raise SystemExit(2)

    present_in_target = grep_children_namespaces(target_autogenerated_toc)

    print(
        "Here are the visible namespaces in target autogenerated ToC. Constraining reference.yml."
    )
    for ns in sorted(present_in_target):
        print(" |__ " + ns)

    path_resolver = PathResolver(doc_repo_location=args.docrepo, moniker=args.moniker)

    base_reference_toc[0] = filter_toc(base_reference_toc[0], present_in_target, path_resolver)

    updated_content = yaml.dump(base_reference_toc, default_flow_style=False)

    with open(args.target, "w") as f:
        f.write(updated_content)
