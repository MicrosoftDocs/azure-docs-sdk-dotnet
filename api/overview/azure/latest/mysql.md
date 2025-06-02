---
title: Azure MySQL SDK for .NET
description: Reference for Azure MySQL SDK for .NET
ms.date: 06/02/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: mysql
---
# Azure Database for MySQL libraries for .NET

## Overview

Work with data and resources stored in [Azure Database for MySQL](/azure/mysql/overview).

## Client APIs

The recommended client library for accessing Azure Database for MySQL is MySQL's [Connector/Net](https://dev.mysql.com/doc/connector-net/en). Use the package to connect to the database and execute SQL statements directly. 

Install the [NuGet package](https://www.nuget.org/packages/MySql.Data) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package MySql.Data
```

#### .NET Core CLI

```dotnetcli
dotnet add package MySql.Data
```

### Code Example

Connect to a MySQL database and execute a query:

```csharp
/* Include this "using" directive...
using MySql.Data.MySqlClient;
*/

string connectionString = "Server=[servername].mysql.database.azure.com; " +
    "Database=myDataBase; Uid=[userid]@[servername]; Pwd=myPassword;";

// Best practice is to scope the MySqlConnection to a "using" block
using (MySqlConnection conn = new MySqlConnection(connectionString))
{
    // Connect to the database
    conn.Open();

    // Read rows
    MySqlCommand selectCommand = new MySqlCommand("SELECT * FROM MyTable", conn);
    MySqlDataReader results = selectCommand.ExecuteReader();
    
    // Enumerate over the rows
    while(results.Read())
    {
        Console.WriteLine("Column 0: {0} Column 1: {1}", results[0], results[1]);
    }
}
```

## Samples

- [ADO.NET code examples](/dotnet/framework/data/adonet/ado-net-code-examples)
- [Design a MySQL database using the Azure CLI](https://docs.microsoft.com/azure/mysql/tutorial-design-database-using-cli) 

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package