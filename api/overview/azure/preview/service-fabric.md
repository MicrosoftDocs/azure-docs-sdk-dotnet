---
title: Azure Service Fabric SDK for .NET
description: Reference for Azure Service Fabric SDK for .NET
ms.date: 06/12/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: servicefabric
---
# Azure Service Fabric libraries for .NET

## Overview

Azure Service Fabric is a distributed systems platform that makes it easy to package, deploy, and manage scalable and reliable microservices and containers.  For more information, see the [Azure Service Fabric Documentation](/azure/service-fabric/).

## Client library

Use the Service Fabric client library to interact with an existing Service Fabric cluster.  The library contains three categories of APIs:

* **Client** APIs are used to manage, scale, and recycle the cluster, as well as deploy application packages.
* **Runtime** APIs are used for the running application to interact with its hosting cluster.
* **Common** APIs contain types used in both **client** and **runtime** APIs.

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.ServiceFabric) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.ServiceFabric
```

```dotnetcli
dotnet add package Microsoft.ServiceFabric
```

### Code Examples

The following example uses the Service Fabric **client** APIs to copy an application package to the image store, provisions the application type, and create an application instance.

```csharp
/* Include these dependencies
using System.Fabric;
using System.Fabric.Description;
*/

// Connect to the cluster.
FabricClient fabricClient = new FabricClient(clusterConnection);

// Copy the application package to a location in the image store
fabricClient.ApplicationManager.CopyApplicationPackage(imageStoreConnectionString, packagePath, packagePathInImageStore);

// Provision the application.
fabricClient.ApplicationManager.ProvisionApplicationAsync(packagePathInImageStore).Wait();

//  Create the application instance.
ApplicationDescription appDesc = new ApplicationDescription(new Uri(appName), appType, appVersion);
fabricClient.ApplicationManager.CreateApplicationAsync(appDesc).Wait();
```

> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/overview/azure/servicefabric/client)

This example uses the Service Fabric **runtime** and **common** APIs from within a hosted application to update a [Reliable Collection](/azure/service-fabric/service-fabric-reliable-services-reliable-collections) at runtime.

```csharp
using System.Fabric;
using Microsoft.ServiceFabric.Data.Collections;
using Microsoft.ServiceFabric.Services.Communication.Runtime;
using Microsoft.ServiceFabric.Services.Runtime;

/// <summary>
/// This is the main entry point for your service replica.
/// This method executes when this replica of your service becomes primary and has write status.
/// </summary>
/// <param name="cancellationToken">Canceled when Service Fabric needs to shut down this service replica.</param>
protected override async Task RunAsync(CancellationToken cancellationToken)
{
    var myDictionary = await this.StateManager.GetOrAddAsync<IReliableDictionary<string, long>>("myDictionary");
    while (true)
    {
        cancellationToken.ThrowIfCancellationRequested();
        using (var tx = this.StateManager.CreateTransaction())
        {
            var result = await myDictionary.TryGetValueAsync(tx, "Counter");
            await myDictionary.AddOrUpdateAsync(tx, "Counter", 0, (key, value) => ++value);

            // If an exception is thrown before calling CommitAsync, the transaction aborts, all changes are
            // discarded, and nothing is saved to the secondary replicas.
            await tx.CommitAsync();
        }
        await Task.Delay(TimeSpan.FromSeconds(1), cancellationToken);
    }
}
```

> [!div class="nextstepaction"]
> [Explore the runtime APIs](/dotnet/api/overview/azure/servicefabric/runtime)

> [!div class="nextstepaction"]
> [Explore the common APIs](/dotnet/api/overview/azure/servicefabric/common)

## Management Library

The management library is used to create, update, and delete Service Fabric clusters.

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.ServiceFabric) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Management.ServiceFabric
```

```dotnetcli
dotnet add package Microsoft.Azure.Management.ServiceFabric
```

> [!div class="nextstepaction"]
> [Explore the management APIs](/dotnet/api/overview/azure/servicefabric/management)

## Samples

* [Deploy and remove applications using FabricClient](/azure/service-fabric/service-fabric-deploy-remove-applications-fabricclient)

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package