---
title: Azure Search SDK for .NET
description: Reference for Azure Search SDK for .NET
ms.date: 06/06/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: cognitive-search
---
# Azure AI Search libraries for .NET

## Overview

[Azure AI Search](/azure/search/) (formerly known as "Azure Cognitive Search") is an AI-powered information retrieval platform that helps developers build rich search experiences and generative AI apps that combine large language models with enterprise data.

Although Azure AI Search is renamed, many API descriptions continue to use the former name, "Azure Cognitive Search". API string descriptions will get updated over time.

## Libraries for data access

After an Azure AI Search resource is created and configured, use data access libraries to create and consume search objects in client applications.

### Version 11

The **`Azure.Search.Documents`** is a client library  for .NET developers who want to use search technology in their applications. In contrast with the v10 legacy client library, this version takes dependencies on **`Azure.Core`** and **`System.Text.Json`**, implementing standard approaches in terms of service configuration, authentication, document serialization, and other tasks.

Use the **`Azure.Search.Documents`** library when creating new projects that use Azure AI Search objects. Moving forward, all new features and enhancements will roll out here.

|    Library    |    Reference    |    Package    |    Source    |
|---------------|-----------------|----------------|-------------|
| Azure.Search.Documents | [Reference](/dotnet/api/azure.search.documents) | [NuGet](https://www.nuget.org/packages/Azure.Search.Documents/) | [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/search/Azure.Search.Documents) |

There is only one package and one client library for this version.

If you have existing search applications that call the v10 legacy libraries, be aware that v11 has different clients, namespaces, and class names. You will need to migrate existing code to use the new library. When reviewing code samples and content, be sure to check for the namespace (`using Azure.Search.Documents;`) to confirm whether the v11 client library is demonstrated.

### Version 10 (legacy)

Use **`Microsoft.Azure.Search`** libraries to maintain existing solutions. This version is supported, but with the exception of security hotfixes, no further updates are planned for this library. For an introduction, see [How to use Microsoft.Azure.Search (v10)](/azure/search/search-howto-dotnet-sdk).

|    Library    |    Reference    |    Package    |    Source    |
|---------------|-----------------|----------------|-------------|
| Microsoft.Azure.Search | [Reference](/dotnet/api/microsoft.azure.search) | [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Search/) | [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/search/Microsoft.Azure.Search) |
| Microsoft.Azure.Search.Common | [Reference](/dotnet/api/microsoft.azure.search.common) |   |  |
| Microsoft.Azure.Search.Models | [Reference](/dotnet/api/microsoft.azure.search.models) |   |  |
| Microsoft.Azure.Search.Models.Internal | [Reference](/dotnet/api/microsoft.azure.search.models.internal) | |  |
| Microsoft.Azure.Search.Serialization | [Reference](/dotnet/api/microsoft.azure.search.serialization) |   |  |
| Microsoft.Azure.Search.Serialization.internal | [Reference](/dotnet/api/microsoft.azure.search.serialization.internal) |  |  |

## Libraries for resource management

Use the Azure AI Search management library to provision a service, manage api-keys, and adjust resources. Service management has a dependency on Azure Resource Manager for subscriber and tenant identification. Typically, authentication and application registration with Azure Active Directory is also necessary to support the workflow. For an introduction to Azure AI Search service provisioning, see [How to use the Management REST API](/rest/api/searchmanagement/search-howto-management-rest-api).

|    Library    |    Reference    |    Package    |    Source    |
|---------------|-----------------|----------------|-------------|
| Microsoft.Azure.Management.Search | [Reference](/dotnet/api/overview/azure/search/management) | [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Management.Search) | [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/search/Microsoft.Azure.Management.Search)