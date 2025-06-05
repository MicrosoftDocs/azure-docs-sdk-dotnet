---
title: Azure Key Vault SDK for .NET
description: Reference for Azure Key Vault SDK for .NET
ms.date: 06/05/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: keyvault
---
# Azure Key Vault libraries for .NET

The Azure Key Vault libraries for .NET offer a convenient interface for making calls to Azure Key Vault. For more information about Azure Key Vault, see [Introduction to Azure Key Vault](https://docs.microsoft.com/azure/key-vault/general/overview).

## Libraries for data access

The latest version of the Azure Key Vault library is version 4.x.x. Microsoft recommends using version 4.x.x for new applications.

If you cannot update existing applications to version 4.x.x, then Microsoft recommends using version 3.x.x.

### Version 4.x.x

The version 4.x.x libraries for .NET are part of the Azure SDK for .NET. The source code for the Key Vault libraries for .NET is available on [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault).

Use the following version 4.x.x libraries to work with certificates, keys, and secrets:

| Library | Reference | Package | Source |
|----------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|    Azure.Security.KeyVault.Administration    |      [Reference](https://docs.microsoft.com/dotnet/api/azure.security.keyvault.administration)       |    [NuGet](https://www.nuget.org/packages/Azure.Security.KeyVault.Administration/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Azure.Security.KeyVault.Administration)    |
|    Azure.Security.KeyVault.Certificates    |      [Reference](https://docs.microsoft.com/dotnet/api/azure.security.keyvault.certificates)       |    [NuGet](https://www.nuget.org/packages/Azure.Security.KeyVault.Certificates/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Azure.Security.KeyVault.Certificates)    |
|    Azure.Security.KeyVault.Keys    |     [Reference](https://docs.microsoft.com/dotnet/api/azure.security.keyvault.keys)    |    [NuGet](https://www.nuget.org/packages/Azure.Security.KeyVault.Keys/)      |     [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Azure.Security.KeyVault.Keys)|
|    Azure.Security.KeyVault.Secrets    |    [Reference](https://docs.microsoft.com/dotnet/api/azure.security.keyvault.secrets)    |    [NuGet](https://www.nuget.org/packages/Azure.Security.KeyVault.Secrets/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Azure.Security.KeyVault.Secrets)    |

### Version 3.x.x

The source code for the Azure Key Vault libraries for .NET is available on [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault).

Use the following version 3.x.x libraries to work with certificates, keys, and secrets:

| Library | Reference | Package | Source |
|--------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|    Microsoft.Azure.KeyVault.Core    |    [Reference](https://docs.microsoft.com/dotnet/api/microsoft.azure.keyvault.core)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.KeyVault.Core)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Microsoft.Azure.KeyVault.Core)    |
|    Microsoft.Azure.KeyVault.Cryptography    |    [Reference](https://docs.microsoft.com/dotnet/api/microsoft.azure.keyvault.cryptography)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.KeyVault.Cryptography)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Microsoft.Azure.KeyVault.Cryptography)    |
|    Microsoft.Azure.KeyVault.Extensions    |      |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.KeyVault.Extensions)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Microsoft.Azure.KeyVault.Extensions)    |
|    Microsoft.Azure.KeyVault.WebKey    |    [Reference](https://docs.microsoft.com/dotnet/api/microsoft.azure.keyvault.webkey)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.KeyVault.WebKey)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Microsoft.Azure.KeyVault.WebKey)    |
|    Microsoft.Azure.KeyVault    |    [Reference](https://docs.microsoft.com/dotnet/api/microsoft.azure.keyvault)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.KeyVault)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Microsoft.Azure.KeyVault)    |

## Libraries for resource management

Use the following library to work with the Azure Key Vault resource provider:

|    Library    |    Reference    |    Package    |    Source    |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|    Microsoft.Azure.Management.KeyVault    |    [Reference](https://docs.microsoft.com/dotnet/api/microsoft.azure.management.keyvault)    |    [NuGet](https://www.nuget.org/packages/Microsoft.Azure.Management.KeyVault/)    |    [GitHub](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/keyvault/Microsoft.Azure.Management.KeyVault)    |