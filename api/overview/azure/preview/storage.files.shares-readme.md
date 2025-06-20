---
title: Azure Storage File Shares client library for .NET
keywords: Azure, dotnet, SDK, API, Azure.Storage.Files.Shares, storage
ms.date: 06/09/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: storage
---
# Azure Storage File Shares client library for .NET - version 12.24.0-beta.1 


> Server Version: 2021-02-12, 2020-12-06, 2020-10-02, 2020-08-04, 2020-06-12, 2020-04-08, 2020-02-10, 2019-12-12, 2019-07-07, and 2019-02-02

Azure File Shares offers fully managed file shares in the cloud that are accessible
via the industry standard Server Message Block (SMB) protocol. Azure file
shares can be mounted concurrently by cloud or on-premises deployments of
Windows, Linux, and macOS. Additionally, Azure file shares can be cached on
Windows Servers with Azure File Sync for fast access near where the data is
being used.

[Source code][source] | [Package (NuGet)][package] | [API reference documentation][docs] | [REST API documentation][rest_docs] | [Product documentation][product_docs]

## Getting started

### Install the package

Install the Azure Storage File Shares client library for .NET with [NuGet][nuget]:

```dotnetcli
dotnet add package Azure.Storage.Files.Shares
```

### Prerequisites

You need an [Azure subscription][azure_sub] and a
[Storage Account][storage_account_docs] to use this package.

To create a new Storage Account, you can use the [Azure Portal][storage_account_create_portal],
[Azure PowerShell][storage_account_create_ps], or the [Azure CLI][storage_account_create_cli].
Here's an example using the Azure CLI:

```Powershell
az storage account create --name MyStorageAccount --resource-group MyResourceGroup --location westus --sku Standard_LRS
```

### Authenticate the client

In order to interact with the Azure Blobs Storage service, you'll need to create an instance of the ShareServiceClient class. The [Azure Identity](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/identity/Azure.Identity/README.md) library makes it easy to add Azure Active Directory support for authenticating Azure SDK clients with their corresponding Azure services.

```C# Snippet:ShareFile_TokenCredential
// Create a TokenCredential that we can use to authenticate
TokenCredential credential = new DefaultAzureCredential();

// Create a client that can authenticate with a TokenCredential
ShareServiceClient shareServiceClient = new ShareServiceClient(
    StorageAccountFileUri,
    credential);
```

## Key concepts

Azure file shares can be used to:

- Completely replace or supplement traditional on-premises file servers or NAS devices.
- "Lift and shift" applications to the cloud that expect a file share to store file application or user data.
- Simplify new cloud development projects with shared application settings, diagnostic shares, and Dev/Test/Debug tool file shares.

### Thread safety
We guarantee that all client instance methods are thread-safe and independent of each other ([guideline](https://azure.github.io/azure-sdk/dotnet_introduction.html#dotnet-service-methods-thread-safety)). This ensures that the recommendation of reusing client instances is always safe, even across threads.

### Additional concepts
<!-- CLIENT COMMON BAR -->
[Client options](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/core/Azure.Core/README.md#configuring-service-clients-using-clientoptions) |
[Accessing the response](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/core/Azure.Core/README.md#accessing-http-response-details-using-responset) |
[Long-running operations](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/core/Azure.Core/README.md#consuming-long-running-operations-using-operationt) |
[Handling failures](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/core/Azure.Core/README.md#reporting-errors-requestfailedexception) |
[Diagnostics](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/core/Azure.Core/samples/Diagnostics.md) |
[Mocking](https://learn.microsoft.com/dotnet/azure/sdk/unit-testing-mocking) |
[Client lifetime](https://devblogs.microsoft.com/azure-sdk/lifetime-management-and-thread-safety-guarantees-of-azure-sdk-net-clients/)
<!-- CLIENT COMMON BAR -->

## Examples

### Create a share and upload a file

```C# Snippet:Azure_Storage_Files_Shares_Samples_Sample01a_HelloWorld_Upload
// Get a connection string to our Azure Storage account.  You can
// obtain your connection string from the Azure Portal (click
// Access Keys under Settings in the Portal Storage account blade)
// or using the Azure CLI with:
//
//     az storage account show-connection-string --name <account_name> --resource-group <resource_group>
//
// And you can provide the connection string to your application
// using an environment variable.
string connectionString = "<connection_string>";

// Name of the share, directory, and file we'll create
string shareName = "sample-share";
string dirName = "sample-dir";
string fileName = "sample-file";

// Path to the local file to upload
string localFilePath = @"<path_to_local_file>";

// Get a reference to a share and then create it
ShareClient share = new ShareClient(connectionString, shareName);
share.Create();

// Get a reference to a directory and create it
ShareDirectoryClient directory = share.GetDirectoryClient(dirName);
directory.Create();

// Get a reference to a file and upload it
ShareFileClient file = directory.GetFileClient(fileName);
using (FileStream stream = File.OpenRead(localFilePath))
{
    file.Create(stream.Length);
    file.UploadRange(
        new HttpRange(0, stream.Length),
        stream);
}
```

### Download a file

```C# Snippet:Azure_Storage_Files_Shares_Samples_Sample01a_HelloWorld_Download
string connectionString = "<connection_string>";

// Name of the share, directory, and file we'll download from
string shareName = "sample-share";
string dirName = "sample-dir";
string fileName = "sample-file";

// Path to the save the downloaded file
string localFilePath = @"<path_to_local_file>";

// Get a reference to the file
ShareClient share = new ShareClient(connectionString, shareName);
ShareDirectoryClient directory = share.GetDirectoryClient(dirName);
ShareFileClient file = directory.GetFileClient(fileName);

// Download the file
ShareFileDownloadInfo download = file.Download();
using (FileStream stream = File.OpenWrite(localFilePath))
{
    download.Content.CopyTo(stream);
}
```

### Traverse a share

```C# Snippet:Azure_Storage_Files_Shares_Samples_Sample01a_HelloWorld_Traverse
// Connect to the share
string connectionString = "<connection_string>";
string shareName = "sample-share";
ShareClient share = new ShareClient(connectionString, shareName);

// Track the remaining directories to walk, starting from the root
var remaining = new Queue<ShareDirectoryClient>();
remaining.Enqueue(share.GetRootDirectoryClient());
while (remaining.Count > 0)
{
    // Get all of the next directory's files and subdirectories
    ShareDirectoryClient dir = remaining.Dequeue();
    foreach (ShareFileItem item in dir.GetFilesAndDirectories())
    {
        // Print the name of the item
        Console.WriteLine(item.Name);

        // Keep walking down directories
        if (item.IsDirectory)
        {
            remaining.Enqueue(dir.GetSubdirectoryClient(item.Name));
        }
    }
}
```

### Async APIs

We fully support both synchronous and asynchronous APIs.

```C# Snippet:Azure_Storage_Files_Shares_Samples_Sample01b_HelloWorldAsync_DownloadAsync
string connectionString = "<connection_string>";

// Name of the share, directory, and file we'll download from
string shareName = "sample-share";
string dirName = "sample-dir";
string fileName = "sample-file";

// Path to the save the downloaded file
string localFilePath = @"<path_to_local_file>";

// Get a reference to the file
ShareClient share = new ShareClient(connectionString, shareName);
ShareDirectoryClient directory = share.GetDirectoryClient(dirName);
ShareFileClient file = directory.GetFileClient(fileName);

// Download the file
ShareFileDownloadInfo download = await file.DownloadAsync();
using (FileStream stream = File.OpenWrite(localFilePath))
{
    await download.Content.CopyToAsync(stream);
}
```

## Troubleshooting

All Azure Storage File Shares service operations will throw a
[RequestFailedException][RequestFailedException] on failure with
helpful [`ErrorCode`s][error_codes].  Many of these errors are recoverable.
If multiple failures occur, an [AggregateException][AggregateException] will be thrown,
containing each failure instance.

```C# Snippet:Azure_Storage_Files_Shares_Samples_Sample01a_HelloWorld_Errors
// Connect to the existing share
string connectionString = "<connection_string>";
string shareName = "sample-share";
ShareClient share = new ShareClient(connectionString, shareName);

try
{
    // Try to create the share again
    share.Create();
}
catch (RequestFailedException ex)
    when (ex.ErrorCode == ShareErrorCode.ShareAlreadyExists)
{
    // Ignore any errors if the share already exists
}
```

## Next steps

Get started with our [File samples][samples]:

1. [Hello World](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/storage/Azure.Storage.Files.Shares/samples/Sample01a_HelloWorld.cs): Upload files, download files, and traverse shares (or [asynchronously](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/storage/Azure.Storage.Files.Shares/samples/Sample01b_HelloWorldAsync.cs))
2. [Auth](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/storage/Azure.Storage.Files.Shares/samples/Sample02_Auth.cs): Authenticate with connection strings, shared keys, and shared access signatures.

## Contributing

See the [Storage CONTRIBUTING.md][storage_contrib] for details on building,
testing, and contributing to this library.

This project welcomes contributions and suggestions.  Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution. For
details, visit [cla.microsoft.com][cla].

This project has adopted the [Microsoft Open Source Code of Conduct][coc].
For more information see the [Code of Conduct FAQ][coc_faq]
or contact [opencode@microsoft.com][coc_contact] with any
additional questions or comments.

<!-- LINKS -->
[source]: https://github.com/Azure/azure-sdk-for-net/tree/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/storage/Azure.Storage.Files.Shares/src
[package]: https://www.nuget.org/packages/Azure.Storage.Files.Shares/
[docs]: https://learn.microsoft.com/dotnet/api/azure.storage.files.shares
[rest_docs]: https://learn.microsoft.com/rest/api/storageservices/file-service-rest-api
[product_docs]: https://learn.microsoft.com/azure/storage/files/storage-files-introduction
[nuget]: https://www.nuget.org/
[storage_account_docs]: https://learn.microsoft.com/azure/storage/common/storage-account-overview
[storage_account_create_ps]: https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-powershell
[storage_account_create_cli]: https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-cli
[storage_account_create_portal]: https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-portal
[azure_cli]: https://learn.microsoft.com/cli/azure
[azure_sub]: https://azure.microsoft.com/free/dotnet/
[RequestFailedException]: https://github.com/Azure/azure-sdk-for-net/tree/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/core/Azure.Core/src/RequestFailedException.cs
[error_codes]: https://learn.microsoft.com/rest/api/storageservices/file-service-error-codes
[samples]: https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/storage/Azure.Storage.Files.Shares/samples/
[storage_contrib]: https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Files.Shares_12.24.0-beta.1/sdk/storage/CONTRIBUTING.md
[cla]: https://cla.microsoft.com
[coc]: https://opensource.microsoft.com/codeofconduct/
[coc_faq]: https://opensource.microsoft.com/codeofconduct/faq/
[coc_contact]: mailto:opencode@microsoft.com
[AggregateException]: https://learn.microsoft.com/dotnet/api/system.aggregateexception?view=net-9.0

