---
title: Azure Functions SDK for .NET
description: Reference for Azure Functions SDK for .NET
ms.date: 06/12/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: functions
---
# Azure Functions libraries for .NET

## Overview

[Azure Functions](/azure/azure-functions/functions-overview) is a solution for easily running small pieces of code, or _functions_, in Azure. Azure Functions supports a [serverless](https://azure.microsoft.com/solutions/serverless/) execution model.

## Durable Functions extension

*Durable Functions* is an extension of [Azure Functions](/azure/azure-functions/functions-overview) that lets you write stateful functions in a serverless compute environment. The extension lets you define stateful workflows by writing [*orchestrator functions*](/azure/azure-functions/durable/durable-functions-orchestrations) and stateful entities by writing [*entity functions*](/azure/azure-functions/durable/durable-functions-entities) using the Azure Functions programming model. Behind the scenes, the extension manages state, checkpoints, and restarts for you, allowing you to focus on your business logic.

Install the extension [NuGet package](https://www.nuget.org/packages/Microsoft.Azure.WebJobs.Extensions.DurableTask) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

The Azure API reference documentation supports [version 2.x of the Durable Functions extension](/dotnet/api/overview/azure/functions/runtime). 

### Visual Studio package manager

```powershell
Install-Package Microsoft.Azure.WebJobs.Extensions.DurableTask
```

### .NET Core CLI

```dotnetcli
dotnet add package Microsoft.Azure.WebJobs.Extensions.DurableTask
```

### Getting started

> [!div class="nextstepaction"]
> [Durable Functions quickstart](/azure/azure-functions/durable/durable-functions-create-first-csharp)

## Samples

View the [complete list](/samples/browse/?products=azure-functions&languages=csharp) of Azure Functions samples.

[PackageManager]: /nuget/tools/package-manager-console
[DotNetCLI]: /dotnet/core/tools/dotnet-add-package