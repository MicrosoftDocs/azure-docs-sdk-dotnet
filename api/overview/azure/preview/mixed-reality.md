---
title: Azure Mixed Reality SDK for .NET
description: Reference for Azure Mixed Reality SDK for .NET
ms.date: 06/11/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: mixedreality
---
# Azure Mixed Reality Resource Management Libraries for .NET

## Overview

Microsoft provides a series of Azure services to empower Mixed Reality devices and applications. The following services are provided:

* [Azure Remote Rendering](https://azure.microsoft.com/services/remote-rendering/) (preview)

## Management library

Use the Azure Mixed Reality Resource Management libraries to manage the lifecycle of Azure Mixed Reality resources. To automate the configuration of Azure Mixed Reality resources, use the Azure portal, CLI, or PowerShell.

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.MixedReality) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

To install:

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Management.MixedReality
```

#### .NET Core CLI

```dotnetcli
dotnet add package Microsoft.Azure.Management.MixedReality
```

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package