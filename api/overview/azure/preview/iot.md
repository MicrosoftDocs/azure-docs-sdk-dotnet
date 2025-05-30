---
title: Azure IoT SDK for .NET
description: Reference for Azure IoT SDK for .NET
ms.date: 05/30/2025
ms.topic: reference
ms.devlang: dotnet
ms.service: iot
---
# Azure IoT libraries for .NET

## Overview

[Azure IoT Hub](https://azure.microsoft.com/services/iot-hub/) is a fully managed service that enables reliable and secure bi-directional communications between millions of devices and a solution back end.

Devices and data sources in an IoT solution can range from a simple network-connected sensor to a powerful, standalone computing device. Devices may have limited processing capability, memory, communication bandwidth, and communication protocol support. The IoT [device SDKs](https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-sdks) enable you to implement client applications for a wide variety of devices and back-end applications.

The device SDK for .NET facilitates building devices running .NET that connect to Azure IoT Hub.

The service SDK for .NET facilitates building back-end applications using .NET that manage and allow controlling devices from the Cloud.

[Learn more about Azure IoT](https://docs.microsoft.com/azure/iot-hub/).


## Client library

Use the .NET IoT devices client to connect and send messages to your IoT Hub.

Install the [NuGet package]( https://www.nuget.org/packages/Microsoft.Azure.Devices.Client) directly from the Visual Studio [Package Manager console][PackageManager] or with the [.NET Core CLI][DotNetCLI].

#### Visual Studio Package Manager

```powershell
Install-Package Microsoft.Azure.Devices.Client
```

```dotnetcli
dotnet add package Microsoft.Azure.Devices.Client
```

### Code Examples 

This example connects to the IoT Hub and sends one message per second.

```csharp
string deviceKey = "<deviceKey>";
string deviceId = "<deviceId>";
string iotHubHostName = "<IoTHubHostname>";
var deviceAuthentication = new DeviceAuthenticationWithRegistrySymmetricKey(deviceId, deviceKey);

DeviceClient deviceClient = DeviceClient.Create(iotHubHostName, deviceAuthentication, TransportType.Mqtt);

while (true)
{
    double currentTemperature = 20 + Rand.NextDouble() * 15;
    double currentHumidity = 60 + Rand.NextDouble() * 20;

    var telemetryDataPoint = new
    {
        messageId = _messageId++,
        deviceId = deviceId,
        temperature = currentTemperature,
        humidity = currentHumidity
    };
    string messageString = JsonConvert.SerializeObject(telemetryDataPoint);
    Message message = new Message(Encoding.ASCII.GetBytes(messageString));
    message.Properties.Add("temperatureAlert", (currentTemperature > 30) ? "true" : "false");

    await deviceClient.SendEventAsync(message);
    Console.WriteLine("{0} > Sending message: {1}", DateTime.Now, messageString);

    await Task.Delay(1000);
}
```


> [!div class="nextstepaction"]
> [Explore the client APIs](/dotnet/api/overview/azure/iot/client)

## Samples

View the [complete list](https://azure.microsoft.com/resources/samples/?platform=dotnet&service=iot-hub) of Azure IoT Upsamples.

View the [Azure IoT Hub developer guide](https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide) for more guidance.

[PackageManager]: https://docs.microsoft.com/nuget/tools/package-manager-console
[DotNetCLI]: https://docs.microsoft.com/dotnet/core/tools/dotnet-add-package