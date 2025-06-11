---
title: Azure Resource Manager SDK for .NET
description: Reference for Azure Resource Manager SDK for .NET
ms.date: 06/11/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: resourcemanager
---
# Azure Resource Manager libraries for .NET

## Overview

Azure Resource Manager enables you to work with the resources in your solution as a group.  For more information about Resource Manager, see [Azure Resource Manager overview](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-overview).

## Management library

The Azure Resource Manager library for .NET enables you to create, update, delete, and list resources and resource groups.

Install the [NuGet package](https://www.nuget.org/packages/Azure.ResourceManager/) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Azure.ResourceManager
```

```dotnetcli
dotnet add package Azure.ResourceManager
```

### Example

This example creates a new resource group.

```csharp
// First, initialize the ArmClient and get the default subscription
ArmClient client = new ArmClient(new DefaultAzureCredential());

// Now we get a ResourceGroupResource collection for that subscription
SubscriptionResource subscription = await client.GetDefaultSubscriptionAsync();
ResourceGroupCollection resourceGroups = subscription.GetResourceGroups();

// With the collection, we can create a new resource group with an specific name
string resourceGroupName = "myRgName";
AzureLocation location = AzureLocation.WestUS2;
ResourceGroupData resourceGroupData = new ResourceGroupData(location);
ArmOperation<ResourceGroupResource> operation = await resourceGroups.CreateOrUpdateAsync(WaitUntil.Completed, resourceGroupName, resourceGroupData);
ResourceGroupResource resourceGroup = operation.Value;
```

> [!div class="nextstepaction"]
> [Explore the management APIs](/dotnet/api/overview/azure/resourcemanager-readme)


## Samples

* [Manage resource groups](https://github.com/Azure-Samples/resources-dotnet-manage-resource-group)
* [Manage resources](https://github.com/Azure-Samples/resources-dotnet-manage-resource)
* [Deploy resources with ARM templates](https://github.com/Azure-Samples/resources-dotnet-deploy-using-arm-template)
* [Deploy resources with ARM templates (with progress)](https://github.com/Azure-Samples/resources-dotnet-deploy-using-arm-template-with-progress)


[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package