---
title: Azure Logic Apps connectors client library for .NET
description: Reference for the Azure.Connectors.Sdk .NET package that provides typed clients to call Azure Logic Apps managed connectors from your apps
keywords: Azure, dotnet, SDK, API, Azure.Connectors.Sdk, connector-namespace
ms.date: 07/06/2026
ms.topic: reference
ms.devlang: dotnet
ms.service: connector-namespace
---
# Azure Logic Apps connectors client library for .NET - version 0.13.0-preview.1

The `Azure.Connectors.Sdk` package provides typed .NET clients for Azure Logic Apps connectors, so you can call Office 365, SharePoint, Teams, Dataverse, and other managed connectors directly from Azure Functions and other .NET apps without running a workflow host. The public API is auto-generated from the managed connector contracts, which gives you strongly typed async methods, request and response models, and IntelliSense for each connector operation.

> [!CAUTION]
> This package is an early preview and is under active development. Use it for evaluation and feedback only, not for production. Expect breaking changes across APIs, data models, and behavior in future releases. This package is released outside the Azure SDK engineering system.

## Getting started

### Install the package

Install the Azure Logic Apps connectors client library for .NET with [NuGet](https://www.nuget.org/packages/Azure.Connectors.Sdk):

```dotnetcli
dotnet add package Azure.Connectors.Sdk --prerelease
```

### Prerequisites

* You must have an [Azure subscription](https://azure.microsoft.com/free/dotnet/).
* You must have a Connector Namespace and a connection for the connector you want to call. The connection provides the runtime URL that the typed client targets.

### Authenticate the client

The generated clients accept an Azure.Core `TokenCredential`, so any credential from the [Azure Identity library](/dotnet/api/overview/azure/identity-readme) works. Azure-hosted apps default to `ManagedIdentityCredential`. For local development, pass a credential such as `AzureCliCredential` explicitly.

## Key concepts

* **Connector** — A shared REST service hosted by Azure that wraps a specific SaaS or PaaS API, such as Office 365 or SharePoint. Each connector exposes actions and, optionally, triggers.
* **Connector Namespace** — The Azure Resource Manager resource that groups your connections and holds the managed identity used for connector access.
* **Connection** — An authorized link to a single connector. Each connection exposes a runtime URL that you pass to the typed client.
* **Generated client** — A strongly typed class, such as `Office365Client`, with one async method per connector operation.

## Examples

The following example constructs a connector client and calls a single operation. Replace the runtime URL with the connection runtime URL from your Connector Namespace.

```csharp
using System;
using Azure.Connectors.Sdk;
using Azure.Connectors.Sdk.Office365;
using Azure.Connectors.Sdk.Office365.Models;
using Azure.Identity;

// Get the connection runtime URL from your Connector Namespace connection.
var connectionRuntimeUrl = new Uri("https://...");

// For local development, pass AzureCliCredential explicitly.
// Azure-hosted apps can omit the credential to use a system-assigned managed identity.
using var client = new Office365Client(connectionRuntimeUrl, new AzureCliCredential());

// Call a typed operation.
await client.SendEmailAsync(new SendEmailInput
{
    To = "recipient@example.com",
    Subject = "Hello from the connectors SDK",
    Body = "<p>Email body</p>",
});
```

## Documentation

* [Connector Namespace conceptual documentation](/azure/connector-namespace/)
* [API reference for the Azure Logic Apps connectors SDK](/dotnet/api/) <!-- TODO: confirm the moniker-scoped API reference path for azure.connectors.sdk once the package is indexed. -->
* [Connectors SDK samples](https://github.com/Azure/Connectors-NET-Samples)

## Troubleshooting

* File an issue through [GitHub issues](https://github.com/Azure/Connectors-NET-SDK/issues).

## Next steps

* Set up a Connector Namespace connection for the connector you want to call.
* Browse the [validated connectors and operations](https://github.com/Azure/Connectors-NET-SDK) to see what's available today.
