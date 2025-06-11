---
title: Azure Data Lake Analytics SDK for .NET
description: Reference for Azure Data Lake Analytics SDK for .NET
ms.date: 06/11/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: datalakeanalytics
---
# Azure Data Lake Analytics libraries for .NET

## Overview

Azure Data Lake Analytics is an on-demand analytics job service to simplify big data analytics.

To learn more, see [Overview of Microsoft Azure Data Lake Analytics](/azure/data-lake-analytics/data-lake-analytics-overview).

## Management library

Use the management library to connect to the service and manage analytics jobs.

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.DataLake.Analytics) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Management.DataLake.Analytics
```

```dotnetcli
dotnet add package Microsoft.Azure.Management.DataLake.Analytics
```

### Code Example

This example creates the clients to connect with and manage the analytics account.

```csharp
/*
using AdlClient 
*/

// Setup authentication for this demo
Authentication auth = new Authentication("microsoft.onmicrosoft.com"); // change this to YOUR tenant
auth.Authenticate();

// Identify the accounts
AnalyticsAccountRef adla_account = new AnalyticsAccountRef(subscriptionId, resourceGroup, userName);

// Create the clients
AzureClient az = new AzureClient(auth);
AnalyticsClient adla = new AnalyticsClient(auth, adla_account);
```

> [!div class="nextstepaction"]
> [Explore the management APIs](/dotnet/api/overview/azure/datalakeanalytics/management)

## Samples
* [Azure Data Lake .NET Client Example](https://azure.microsoft.com/resources/samples/data-lake-dotnet-client/)

Explore more [sample .NET code](https://azure.microsoft.com/resources/samples/?platform=dotnet) you can use in your apps.

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package