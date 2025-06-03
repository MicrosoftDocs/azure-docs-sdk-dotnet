---
title: Azure Notification Hubs SDK for .NET
description: Reference for Azure Notification Hubs SDK for .NET
ms.date: 06/03/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: notificationhubs
---
# Azure Notification Hubs libraries for .NET

Azure Notification Hubs provide an easy-to-use, multi-platform, scaled-out push engine. With a single cross-platform API call, you can easily send targeted and personalized push notifications to any mobile platform from any cloud or on-premises backend.

## Client library

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.NotificationHubs) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

> [!NOTE]
> The [Azure Notification Hubs NuGet package](https://www.nuget.org/packages/Microsoft.Azure.NotificationHubs) now supports .NET Standard, which allows using .NET core for backend use of Notifications Hubs

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.NotificationHubs
```

```dotnetcli
dotnet add package Microsoft.Azure.NotificationHubs
```

### Code Example

This example connects to a Notification Hub and sends a Windows Push Notification Service (WNS) message.

```csharp
NotificationHubClient hub = NotificationHubClient
                                .CreateClientFromConnectionString("<connection string with full access>", "<hub name>");
string toast = @"<toast><visual><binding template=""ToastText01""><text id=""1"">Hello from a .NET App!</text></binding></visual></toast>";
await hub.SendWindowsNativeNotificationAsync(toast);
```

> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/overview/azure/notificationhubs/client)

## Management library

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.NotificationHubs) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Management.NotificationHubs
```

```dotnetcli
dotnet add package Microsoft.Azure.Management.NotificationHubs
```

> [!div class="nextstepaction"]
> [Explore the management APIs](/dotnet/api/overview/azure/notificationhubs/management)

## Samples

- [Getting Started with Windows Universal](https://github.com/Azure/azure-notificationhubs-samples/tree/master/dotnet/GetStartedWindowsUniversal)

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package