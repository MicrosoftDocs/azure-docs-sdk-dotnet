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