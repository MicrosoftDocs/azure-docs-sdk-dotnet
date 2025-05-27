---
title: Azure Traffic Manager SDK for .NET
description: Reference for Azure Traffic Manager SDK for .NET
ms.date: 05/27/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: trafficmanager
---
# Azure Traffic Manager libraries for .NET

## Overview

Microsoft Azure Traffic Manager allows you to control the distribution of user traffic for service endpoints in different datacenters. Service endpoints supported by Traffic Manager include Azure VMs, Web Apps, and cloud services. You can also use Traffic Manager with external, non-Azure endpoints.

Learn more about [Azure Traffic Manager](/azure/traffic-manager/traffic-manager-overview).	

## Management library

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.TrafficManager.Fluent) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET CLI][DotNetCLI]. This package is deprecated and no longer recommended for use.  The suggested alternative is [Azure.ResourceManager.TrafficManager](https://www.nuget.org/packages/Azure.ResourceManager.TrafficManager/). For more information, refer to [this](https://learn.microsoft.com/dotnet/api/overview/azure/resourcemanager.trafficmanager-readme?view=azure-dotnet) article.

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Management.TrafficManager.Fluent
```

```dotnetcli
dotnet add package Microsoft.Azure.Management.TrafficManager.Fluent
```

> [!div class="nextstepaction"]
> [Explore the management APIs](/dotnet/api/overview/azure/trafficmanager/management)

## Samples

Explore more [sample .NET code](https://azure.microsoft.com/resources/samples/?platform=dotnet) you can use in your apps.

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package