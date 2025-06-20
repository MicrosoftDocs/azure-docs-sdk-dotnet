---
title: Azure Storage Blobs client library for .NET
keywords: Azure, dotnet, SDK, API, Azure.Storage.Blobs, storage
ms.date: 06/10/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: storage
---
# Azure Storage Blobs client library for .NET - version 12.24.1 


> Server Version: 2021-02-12, 2020-12-06, 2020-10-02, 2020-08-04, 2020-06-12, 2020-04-08, 2020-02-10, 2019-12-12, 2019-07-07, and 2019-02-02

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob
storage is optimized for storing massive amounts of unstructured data.
Unstructured data is data that does not adhere to a particular data model or
definition, such as text or binary data.

[Source code][source] | [Package (NuGet)][package] | [API reference documentation][docs] | [REST API documentation][rest_docs] | [Product documentation][product_docs]

## Getting started

### Install the package

Install the Azure Storage Blobs client library for .NET with [NuGet][nuget]:

```dotnetcli
dotnet add package Azure.Storage.Blobs
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

In order to interact with the Azure Blobs Storage service, you'll need to create an instance of the BlobServiceClient class.  The [Azure Identity library][identity] makes it easy to add Azure Active Directory support for authenticating Azure SDK clients with their corresponding Azure services.

```C# Snippet:SampleSnippetsBlob_Auth
// Create a BlobServiceClient that will authenticate through Active Directory
Uri accountUri = new Uri("https://MYSTORAGEACCOUNT.blob.core.windows.net/");
BlobServiceClient client = new BlobServiceClient(accountUri, new DefaultAzureCredential());
```

Learn more about enabling Azure Active Directory for authentication with Azure Storage in [our documentation][storage_ad] and [our samples](#next-steps).

## Key concepts

Blob storage is designed for:

- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Writing to log files.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.

Blob storage offers three types of resources:

- The _storage account_ used via `BlobServiceClient`
- A _container_ in the storage account used via `BlobContainerClient`
- A _blob_ in a container used via `BlobClient`

Learn more about options for authentication _(including Connection Strings, Shared Key, Shared Key Signatures, Active Directory, and anonymous public access)_ [in our samples.](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.Blobs/samples/Sample02_Auth.cs)

### Thread safety
We guarantee that all client instance methods are thread-safe and independent of each other ([guideline](https://azure.github.io/azure-sdk/dotnet_introduction.html#dotnet-service-methods-thread-safety)). This ensures that the recommendation of reusing client instances is always safe, even across threads.

### Additional concepts
<!-- CLIENT COMMON BAR -->
[Client options](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/core/Azure.Core/README.md#configuring-service-clients-using-clientoptions) |
[Accessing the response](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/core/Azure.Core/README.md#accessing-http-response-details-using-responset) |
[Long-running operations](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/core/Azure.Core/README.md#consuming-long-running-operations-using-operationt) |
[Handling failures](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/core/Azure.Core/README.md#reporting-errors-requestfailedexception) |
[Diagnostics](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/core/Azure.Core/samples/Diagnostics.md) |
[Mocking](https://learn.microsoft.com/dotnet/azure/sdk/unit-testing-mocking) |
[Client lifetime](https://devblogs.microsoft.com/azure-sdk/lifetime-management-and-thread-safety-guarantees-of-azure-sdk-net-clients/)
<!-- CLIENT COMMON BAR -->

## Examples

### Uploading a blob

```C# Snippet:SampleSnippetsBlob_Upload
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
string containerName = "sample-container";
string blobName = "sample-blob";
string filePath = "sample-file";

// Get a reference to a container named "sample-container" and then create it
BlobContainerClient container = new BlobContainerClient(connectionString, containerName);
container.Create();

// Get a reference to a blob named "sample-file" in a container named "sample-container"
BlobClient blob = container.GetBlobClient(blobName);

// Upload local file
blob.Upload(filePath);
```

### Downloading a blob

```C# Snippet:SampleSnippetsBlob_Download
// Get a temporary path on disk where we can download the file
string downloadPath = "hello.jpg";

// Download the public MacBeth copy at https://www.gutenberg.org/cache/epub/1533/pg1533.txt
new BlobClient(new Uri("https://www.gutenberg.org/cache/epub/1533/pg1533.txt")).DownloadTo(downloadPath);
```

### Enumerating blobs

```C# Snippet:SampleSnippetsBlob_List
// Get a connection string to our Azure Storage account.
string connectionString = "<connection_string>";
string containerName = "sample-container";
string filePath = "hello.jpg";

// Get a reference to a container named "sample-container" and then create it
BlobContainerClient container = new BlobContainerClient(connectionString, containerName);
container.Create();

// Upload a few blobs so we have something to list
container.UploadBlob("first", File.OpenRead(filePath));
container.UploadBlob("second", File.OpenRead(filePath));
container.UploadBlob("third", File.OpenRead(filePath));

// Print out all the blob names
foreach (BlobItem blob in container.GetBlobs())
{
    Console.WriteLine(blob.Name);
}
```

### Async APIs

We fully support both synchronous and asynchronous APIs.
```C# Snippet:SampleSnippetsBlob_Async
// Get a temporary path on disk where we can download the file
string downloadPath = "hello.jpg";

// Download the public MacBeth copy at https://www.gutenberg.org/cache/epub/1533/pg1533.txt
await new BlobClient(new Uri("https://www.gutenberg.org/cache/epub/1533/pg1533.txt")).DownloadToAsync(downloadPath);
```

## Troubleshooting

All Blob service operations will throw a
[RequestFailedException][RequestFailedException] on failure with
helpful [`ErrorCode`s][error_codes].  Many of these errors are recoverable.
If multiple failures occur, an [AggregateException][AggregateException] will be thrown,
containing each failure instance.

```C# Snippet:SampleSnippetsBlob_Troubleshooting
// Get a connection string to our Azure Storage account.
string connectionString = "<connection_string>";
string containerName = "sample-container";

// Try to delete a container named "sample-container" and avoid any potential race conditions
// that might arise by checking if the container is already deleted or is in the process
// of being deleted.
BlobContainerClient container = new BlobContainerClient(connectionString, containerName);

try
{
    container.Delete();
}
catch (RequestFailedException ex)
    when (ex.ErrorCode == BlobErrorCode.ContainerBeingDeleted ||
          ex.ErrorCode == BlobErrorCode.ContainerNotFound)
{
    // Ignore any errors if the container being deleted or if it has already been deleted
}
```

## Next steps

Get started with our [Blob samples][samples]:

1. [Hello World](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.Blobs/samples/Sample01a_HelloWorld.cs): Upload, download, and list blobs (or [asynchronously](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.Blobs/samples/Sample01b_HelloWorldAsync.cs))
2. [Auth](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.Blobs/samples/Sample02_Auth.cs): Authenticate with connection strings, public access, shared keys, shared access signatures, and Azure Active Directory.

## Advanced Scenarios using Azure.DataMovement.Blobs

For more advanced scenarios like transferring blob virtual directories, we recommend looking into our [Azure.Storage.DataMovement](https://www.nuget.org/packages/Azure.Storage.DataMovement) and [Azure.Storage.DataMovement.Blob](https://www.nuget.org/packages/Azure.Storage.DataMovement.Blobs) packages. Get started with our [DataMovement Blob Samples](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.DataMovement.Blobs/samples/Sample01b_HelloWorldAsync.cs).

Upload a local directory to the root of the `BlobContainerClient`.
```C# Snippet:ExtensionMethodSimpleUploadToRoot
TransferOperation transfer = await container.UploadDirectoryAsync(WaitUntil.Started, localPath);

await transfer.WaitForCompletionAsync();
```

Upload a local directory to a virtual blob directory in the `BlobContainerClient` by specifying a directory prefix
```C# Snippet:ExtensionMethodSimpleUploadToDirectoryPrefix
TransferOperation transfer = await container.UploadDirectoryAsync(WaitUntil.Started, localPath, blobDirectoryPrefix);

await transfer.WaitForCompletionAsync();
```

Upload a local directory to a virtual blob directory in the `BlobContainerClient` specifying more advanced options
```C# Snippet:ExtensionMethodSimpleUploadWithOptions
BlobContainerClientTransferOptions options = new BlobContainerClientTransferOptions
{
    BlobContainerOptions = new BlobStorageResourceContainerOptions
    {
        BlobPrefix = blobDirectoryPrefix
    },
    TransferOptions = new TransferOptions()
    {
        CreationMode = StorageResourceCreationMode.OverwriteIfExists,
    }
};

TransferOperation transfer = await container.UploadDirectoryAsync(WaitUntil.Started, localPath, options);

await transfer.WaitForCompletionAsync();
```

Download the entire `BlobContainerClient` to a local directory
```C# Snippet:ExtensionMethodSimpleDownloadContainer
TransferOperation transfer = await container.DownloadToDirectoryAsync(WaitUntil.Started, localDirectoryPath);

await transfer.WaitForCompletionAsync();
```

Download a virtual blob directory in the `BlobContainerClient` by specifying a directory prefix
```C# Snippet:ExtensionMethodSimpleDownloadContainerDirectory
TransferOperation transfer = await container.DownloadToDirectoryAsync(WaitUntil.Started, localDirectoryPath2, blobDirectoryPrefix);

await transfer.WaitForCompletionAsync();
```

Download from the `BlobContainerClient` specifying more advanced options
```C# Snippet:ExtensionMethodSimpleDownloadContainerDirectoryWithOptions
BlobContainerClientTransferOptions options = new BlobContainerClientTransferOptions
{
    BlobContainerOptions = new BlobStorageResourceContainerOptions
    {
        BlobPrefix = blobDirectoryPrefix
    },
    TransferOptions = new TransferOptions()
    {
        CreationMode = StorageResourceCreationMode.OverwriteIfExists,
    }
};

TransferOperation transfer = await container.DownloadToDirectoryAsync(WaitUntil.Started, localDirectoryPath2, options);

await transfer.WaitForCompletionAsync();
```

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
[source]: https://github.com/Azure/azure-sdk-for-net/tree/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.Blobs/src
[package]: https://www.nuget.org/packages/Azure.Storage.Blobs/
[docs]: https://learn.microsoft.com/dotnet/api/azure.storage.blobs
[rest_docs]: https://learn.microsoft.com/rest/api/storageservices/blob-service-rest-api
[product_docs]: https://learn.microsoft.com/azure/storage/blobs/storage-blobs-overview
[nuget]: https://www.nuget.org/
[storage_account_docs]: https://learn.microsoft.com/azure/storage/common/storage-account-overview
[storage_account_create_ps]: https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-powershell
[storage_account_create_cli]: https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-cli
[storage_account_create_portal]: https://learn.microsoft.com/azure/storage/common/storage-quickstart-create-account?tabs=azure-portal
[azure_cli]: https://learn.microsoft.com/cli/azure
[azure_sub]: https://azure.microsoft.com/free/dotnet/
[identity]: https://github.com/Azure/azure-sdk-for-net/tree/Azure.Storage.Blobs_12.24.1/sdk/identity/Azure.Identity/README.md
[storage_ad]: https://learn.microsoft.com/azure/storage/common/storage-auth-aad
[storage_ad_sample]: samples/Sample02c_Auth_ActiveDirectory.cs
[RequestFailedException]: https://github.com/Azure/azure-sdk-for-net/tree/Azure.Storage.Blobs_12.24.1/sdk/core/Azure.Core/src/RequestFailedException.cs
[error_codes]: https://learn.microsoft.com/rest/api/storageservices/blob-service-error-codes
[samples]: https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/Azure.Storage.Blobs/samples/
[storage_contrib]: https://github.com/Azure/azure-sdk-for-net/blob/Azure.Storage.Blobs_12.24.1/sdk/storage/CONTRIBUTING.md
[cla]: https://cla.microsoft.com
[coc]: https://opensource.microsoft.com/codeofconduct/
[coc_faq]: https://opensource.microsoft.com/codeofconduct/faq/
[coc_contact]: mailto:opencode@microsoft.com
[AggregateException]: https://learn.microsoft.com/dotnet/api/system.aggregateexception?view=net-9.0

