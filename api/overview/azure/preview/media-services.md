---
title: Azure Media Services SDK for .NET
description: Reference for Azure Media Services SDK for .NET
ms.date: 06/02/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: mediaservices
---
# Azure Media Services libraries for .NET

## Overview

Microsoft Azure Media Services is an extensible cloud-based platform that enables developers to build scalable media management and delivery applications. Media Services is based on REST APIs that enable you to securely upload, store, encode, and package video or audio content for both on-demand and live streaming delivery to various clients (for example, TV, PC, and mobile devices). 

To learn more, see [Overview](/azure/media-services/media-services-overview) and [Getting started with .NET](/azure/media-services/media-services-dotnet-how-to-use). 

## Client library

The Azure Media Services .NET SDK library enables you to program against Media Services using .NET. Use the Azure Media Services client library to connect, authenticate, and develop against Media Services APIs.  

For more information, see [Get started with delivering content on demand using .NET SDK](/azure/media-services/media-services-dotnet-get-started).

Install the [NuGet package](https://www.nuget.org/packages/windowsazure.mediaservices) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package windowsazure.mediaservices
```

### Code Example

The following code example uses Media Services .NET SDK to perform the following tasks:

- Create an encoding job.
- Get a reference to the Media Encoder Standard encoder.
- Specify to use the Adaptive Streaming preset.
- Add a single encoding task to the job.
- Specify the input asset to be encoded.
- Create an output asset to receive the encoded asset.
- Submit the job.


```csharp
/* Include this 'using' directive:
using Microsoft.WindowsAzure.MediaServices.Client;
*/

CloudMediaContext context = new CloudMediaContext(new Uri(mediaServiceRESTAPIEndpoint), tokenProvider);

// Get an uploaded asset.
IAsset asset = context.Assets.FirstOrDefault();

// Encode and generate the output using the "Adaptive Streaming" preset.
// Declare a new job.
IJob job = context.Jobs.Create("Media Encoder Standard Job");
// Get a media processor reference, and pass to it the name of the 
// processor to use for the specific task.
IMediaProcessor processor = context.MediaProcessors.Where(p => p.Name == mediaProcessorName)
    .ToList().OrderBy(p => new Version(p.Version)).LastOrDefault();
if (processor == null) 
{
    throw new ArgumentException(string.Format("Unknown media processor", mediaProcessorName));
}

// Create a task with the encoding details, using a string preset.
// In this case "Adaptive Streaming" preset is used.
ITask task = job.Tasks.AddNew("My encoding task", processor, "Adaptive Streaming", TaskOptions.None);

// Specify the input asset to be encoded.
task.InputAssets.Add(asset);
// Add an output asset to contain the results of the job. 
// This output is specified as AssetCreationOptions.None, which 
// means the output asset is not encrypted. 
task.OutputAssets.AddNew("Output asset", AssetCreationOptions.None);

job.Submit();
job.GetExecutionProgressTask(CancellationToken.None).Wait();
```

> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/overview/azure/mediaservices/client(legacy))

## Samples

- [Stream your HLS content Protected with Apple FairPlay](https://azure.microsoft.com/resources/samples/media-services-dotnet-dynamic-encryption-with-fairplay/)
- [Copy blob into an Azure Media Services asset using .NET SDK Extensions](https://azure.microsoft.com/resources/samples/media-services-dotnet-copy-blob-into-asset/)
- [Encode and Deliver a Live Stream with Azure Media Services using .NET SDK](https://azure.microsoft.com/resources/samples/media-services-dotnet-encode-live-stream-with-ams-clear/)

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=dotnet&service=media-services) of Azure Media Services samples.


[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package