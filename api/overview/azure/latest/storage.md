---
title: Azure Storage SDK for .NET
description: Reference for Azure Storage SDK for .NET
ms.date: 05/27/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: storage
---
# Azure Storage client libraries for .NET

The Azure Storage client libraries for .NET offer a convenient interface for making calls to Azure Storage. For more information about Azure Storage, see [Introduction to Azure Storage](/azure/storage/common/storage-introduction).

## Libraries for data access

The latest version of the Azure Storage client library for data access is version 12.x.x. Microsoft recommends using version 12.x.x for new applications.

If you cannot update existing applications to version 12.x.x, then Microsoft recommends using version 11.x.x.

### Version 12.x.x

The version 12.x.x client libraries for .NET are part of the Azure SDK for .NET. The source code for the Azure Storage client libraries for .NET is available on [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage).

Use the following version 12.x.x libraries to work with blobs, files, and queues:

| Library | Reference | Package | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    Azure.Storage.Blobs.Batch    |         |    [NuGet](https://www.nuget.org/packages/Azure.Storage.Blobs.Batch/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Blobs.Batch)    |
|    Azure.Storage.Blobs    |    [Reference](/dotnet/api/azure.storage.blobs)    |    [NuGet](https://www.nuget.org/packages/Azure.Storage.Blobs/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Blobs)    |
|    Azure.Storage.Common    |         |    [NuGet](https://www.nuget.org/packages/Azure.Storage.Common/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Common)    |
|    Azure.Storage.Files.DataLake    |    [Reference](/dotnet/api/azure.storage.files.datalake)    |    [NuGet](https://www.nuget.org/packages/Azure.Storage.Files.DataLake/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Files.DataLake)    |
|    Azure.Storage.Files.Shares    |    [Reference](/dotnet/api/azure.storage.files.shares)    |    [NuGet](https://www.nuget.org/packages/Azure.Storage.Files.Shares/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Files.Shares)    |
|    Azure.Storage.Queues    |    [Reference](/dotnet/api/azure.storage.queues)    |    [NuGet](https://www.nuget.org/packages/Azure.Storage.Queues/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Queues)    |

### Version 11.x.x

The source code for the Azure Storage client libraries for .NET is available on [GitHub](https://github.com/Azure/azure-storage-net).

Use the following version 11.x.x libraries to work with blobs, files, and queues:

| Library | Reference | Package | Source |
|--------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|    Microsoft.Azure.Storage.Blob    |    [Reference](/dotnet/api/microsoft.azure.storage.blob)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Storage.Blob/)    |    [GitHub](https://github.com/Azure/azure-storage-net/tree/master/Blob)    |
|    Microsoft.Azure.Storage.Common    |      |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Storage.Common/)    |    [GitHub](https://github.com/Azure/azure-storage-net/tree/master/Common)    |
|    Microsoft.Azure.Storage.File    |    [Reference](/dotnet/api/microsoft.azure.storage.file)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Storage.File/)    |    [GitHub](https://github.com/Azure/azure-storage-net/tree/master/File)    |
|    Microsoft.Azure.Storage.Queue    |    [Reference](/dotnet/api/microsoft.azure.storage.queue)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Storage.Queue/)    |    [GitHub](https://github.com/Azure/azure-storage-net/tree/master/Queue)    |

## Libraries for resource management

The latest version of the Azure Storage client library for resource management is version 1.x.x. Microsoft recommends using version 1.x.x for new applications.

If you cannot update existing applications to version 1.x.x, then Microsoft recommends using version 25.x.x.

### Version 1.x.x

Use the following version 1.x.x library to work with the Azure Storage resource provider:

|    Library    |    Reference    |    Package    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    Azure.ResourceManager.Storage    |    [Reference](/dotnet/api/azure.resourcemanager.storage)    |    [NuGet](https://www.nuget.org/packages/Azure.ResourceManager.Storage/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.ResourceManager.Storage)    |

### Version 25.x.x

Use the following version 25.x.x library to work with the Azure Storage resource provider:

|    Library    |    Reference    |    Package    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    Microsoft.Azure.Management.Storage    |    [Reference](/dotnet/api/microsoft.azure.management.storage)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Management.Storage/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Microsoft.Azure.Management.Storage)    |

## Known issues

This section details known issues for the Azure Storage client libraries for .NET.

### Client-side encryption bug when using `BlobClient.UpdateClientSideEncryptionKey` with an unauthenticated symmetric encryption algorithm

#### Issue description

A bug was found in `BlobClient.UpdateClientSideEncryptionKey` that might affect customers who are using an unauthenticated symmetric encryption algorithm for key wrapping. If a customer using an [impacted version](#issue-details) of **Azure.Storage.Blobs** attempts to rotate an unauthenticated symmetric encryption key using `BlobClient.UpdateClientSideEncryptionKey`, the key might silently rotate incorrectly, and decryption with the SDK might not be possible without additional steps. Only a small subset of key wrapping algorithms can cause this situation. Most key wrapping algorithms safely throw an exception during key rotation and don't actually rotate the key. For remediation guidance, see [Recommended steps](#recommended-steps).

This bug does *not* affect customers who use an authenticated symmetric key wrapping algorithm, and does *not* affect customers who use asymmetric keys. Asymmetric keys are used by Azure Key Vault and are not affected by this bug. Also, the async API `BlobClient.UpdateClientSideEncryptionKeyAsync` is *not* affected by this bug.

#### Issue details

| Client library | Versions impacted | Minimum safe version | Recommended action |
|--|--|--|--|
| Azure Storage Blob | 12.11.0-beta.2 to 12.21.1 | 12.21.2 | [Update to latest version or minimum 12.21.2](https://www.nuget.org/packages/Azure.Storage.Blobs/) |

#### Recommended steps

- Update client library version according to the table above.
- If you rotated an unauthenticated symmetric encryption key with `BlobClient.UpdateClientSideKeyEncryptionKey` and an affected version of **Azure.Storage.Blobs**, it might be possible to restore your data by encrypting the affected key twice.

### InvalidHeaderValue error message when using beta or generally available version of SDK

In rare scenarios, applications that have upgraded to the latest beta or generally available version of the SDK can receive an `InvalidHeaderValue` error message. This issue can occur when using any of the Storage libraries. The error message looks similar to the following sample:

```console
HTTP/1.1 400 The value for one of the HTTP headers is not in the correct format.
Content-Length: 328
Content-Type: application/xml
Server: Microsoft-HTTPAPI/2.0
x-ms-request-id: <REMOVED>
Date: Fri, 19 May 2023 17:10:33 GMT
 
<?xml version="1.0" encoding="utf-8"?><Error><Code>InvalidHeaderValue</Code><Message>The value for one of the HTTP headers is not in the correct format.
RequestId:<REMOVED>
Time:2023-05-19T17:10:34.2972651Z</Message><HeaderName>x-ms-version</HeaderName><HeaderValue>yyyy-mm-dd</HeaderValue></Error> 
```

If you've upgraded to the latest beta or generally available version of the SDK and you experience this error, it's recommended that you downgrade to the previous generally available version of the SDK to see if the issue resolves. If the issue persists, or if the recommendation is not feasible, [open a support ticket](https://ms.portal.azure.com/#create/Microsoft.Support) to explore further options.

### Download calls might hang when using Azure.Storage.Blobs version 12.20.0

#### Issue description

**Azure.Storage.Blobs** version 12.20.0 references an older version of **Azure.Core** with a known issue during authentication. This issue can cause download calls to hang indefinitely. For remediation guidance, see [Recommended steps](#recommended-steps-1).

#### Issue details

| Client library | Versions impacted | Minimum safe version | Recommended action |
|--|--|--|--|
| Azure Storage Blob | 12.20.0 | 12.23.0 | [Update to latest version or minimum 12.23.0](https://www.nuget.org/packages/Azure.Storage.Blobs/) |

#### Recommended steps

- Upgrade client library version according to the table above.
- Continue to keep your client library versions up to date to ensure that you have the latest bug fixes and performance improvements.