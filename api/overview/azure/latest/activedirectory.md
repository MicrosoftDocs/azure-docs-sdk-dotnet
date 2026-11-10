---
title: Azure Active Directory libraries for .NET
description: Reference for Azure Active Directory libraries for .NET
ms.date: 07/24/2020
ms.topic: reference
ms.service: active-directory
---
# Azure Active Directory libraries for .NET

## Overview

Sign in users and access protected web APIs with Azure Active Directory (Azure AD).

To get started developing applications with Azure Active Directory, see the [Microsoft identity platform](/azure/active-directory/develop/v2-overview).

## Client library

Provide scoped access to web APIs protected by Azure AD using OpenID Connect and OAuth 2.0 with the Microsoft Authentication Library for .NET ([MSAL.NET](/azure/active-directory/develop/msal-net-initializing-client-applications)).

Install the [NuGet package](https://www.nuget.org/packages/Microsoft.Identity.Client) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Identity.Client
```

#### .NET Core CLI

```dotnetcli
dotnet add package Microsoft.Identity.Client
```

### Code example

Retrieve an access token for the Microsoft Graph API in a desktop application (public client).

```csharp
/* Include this using directive:
using Microsoft.Identity.Client;
*/

string ClientId = "11111111-1111-1111-1111-111111111111"; // Application (client) ID
string Tenant = "common";
string Instance = "https://login.microsoftonline.com/";

string graphAPIEndpoint = "https://graph.microsoft.com/v1.0/me";
string[] scopes = new string[] { "user.read" };

AuthenticationResult authResult = null;

var app = PublicClientApplicationBuilder.Create(ClientId)
                .WithAuthority($"{Instance}{Tenant}")
                .WithRedirectUri("http://localhost")
                .Build();

var accounts = await app.GetAccountsAsync();
var firstAccount = accounts.FirstOrDefault();

try
{
    // Always first try to acquire a token silently.
    authResult = await app.AcquireTokenSilent(scopes, firstAccount)
        .ExecuteAsync();
}
catch (MsalUiRequiredException ex)
{
    // If an MsalUiRequiredException occurred when AcquireTokenSilent was called,
    // it indicates you need to call AcquireTokenInteractive to acquire a token.
    System.Diagnostics.Debug.WriteLine($"MsalUiRequiredException: {ex.Message}");

    try
    {
        authResult = await app.AcquireTokenInteractive(scopes)
            .WithAccount(firstAccount)
            .WithPrompt(Prompt.SelectAccount)
            .ExecuteAsync();
    }
    catch (MsalException msalex)
    {
        System.Diagnostics.Debug.WriteLine($"Error acquiring Token:{System.Environment.NewLine}{msalex}");
    }
}
catch (Exception ex)
{
    System.Diagnostics.Debug.WriteLine($"Error acquiring token silently:{System.Environment.NewLine}{ex}");
    return;
}

if (authResult != null)
{
    System.Diagnostics.Debug.WriteLine($"Signed in as {authResult.Account?.Username}. Token expires on: {authResult.ExpiresOn}");
}
```

> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/overview/azure/activedirectory/client)

### Samples

* [ASP.NET Core web app - sign in users](https://aka.ms/aspnetcore-webapp-sign-in)
* [Windows desktop app (WPF) - sign in users](https://github.com/azure-samples/active-directory-dotnet-desktop-msgraph-v2)
* [Use role-based access control (RBAC) in an application](https://github.com/Azure-Samples/active-directory-aspnetcore-webapp-openidconnect-v2/tree/master/5-WebApp-AuthZ/5-1-Roles)

Explore the full collection of [Microsoft identity platform code samples](/azure/active-directory/develop/sample-v2-code).

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package

