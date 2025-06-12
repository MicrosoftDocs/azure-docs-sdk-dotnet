---
title: Azure Data Lake Store SDK for .NET
description: Reference for Azure Data Lake Store SDK for .NET
ms.date: 06/12/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: datalakestore
---
# Azure Data Lake Store libraries for .NET

## Overview

Azure Data Lake Store is an enterprise-wide hyper-scale repository for big data analytic workloads. Azure Data Lake enables you to capture data of any size, type, and ingestion speed in one single place for operational and exploratory analytics.

To learn more, see [Overview of Azure Data Lake Store](/azure/data-lake-store/data-lake-store-overview).

## Client library

Use the client library to perform filesystem operations on Data Lake Store, such as creating folders in a Data Lake Store account, uploading files, and downloading files.  For a full tutorial on using Data Lake Store with .NET, see [Filesystem operations on Azure Data Lake Store using .NET SDK](/azure/data-lake-store/data-lake-store-data-operations-net-sdk).

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.DataLake.Store) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.DataLake.Store
```

```dotnetcli
dotnet add package Microsoft.Azure.DataLake.Store
```

### Authentication

* For end-user authentication for your application, see [End-user authentication with Data Lake Store using .NET SDK](/azure/data-lake-store/data-lake-store-end-user-authenticate-net-sdk).
* For service-to-service authentication for your application, see [Service-to-service authentication with Data Lake Store using .NET SDK](/azure/data-lake-store/data-lake-store-service-to-service-authenticate-net-sdk).

### Code Example

The following snippet creates the Data Lake Store filesystem client object, which is used to issue requests to the service.

```csharp
// Create client objects
AdlsClient client = AdlsClient.CreateClient(_adlsAccountName, adlCreds);
```

> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/microsoft.azure.datalake.store.adlsclient)


## Management library

Use the management library to connect to and manage your big data repositories.

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.DataLake.Store) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Management.DataLake.Store
```

```dotnetcli
dotnet add package Microsoft.Azure.Management.DataLake.Store
```

> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/overview/azure/datalakestore/management)

## Samples

* [Azure Data Lake .NET Client Example](https://azure.microsoft.com/resources/samples/data-lake-dotnet-client/)

Explore more [sample .NET code](https://azure.microsoft.com/resources/samples/?platform=dotnet) you can use in your apps.

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package