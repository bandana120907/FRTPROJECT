
# Azure Network Monitoring Tool

This tool allows you to perform various operations related to Azure network monitoring using the Azure SDK for Python. It leverages Azure Identity and Azure Resource and Network Management libraries to interact with Azure services.

## Prerequisites

Before using this tool, make sure you have the following prerequisites installed:

- Python 3.x
- Azure Identity (`pip install azure-identity`)
- Azure Management (`pip install azure-mgmt-network azure-mgmt-resource`)
- matplotlib (`pip install matplotlib`)

## Configuration

Before running the tool, make sure to set the following configuration parameters in the script:

- Subscription ID (`subs_id`)
- Resource Group (`resource_group`)


## Features

### 1. **Create Virtual Network**
Effortlessly create a virtual network with a specified name and IP range. This feature streamlines the process of establishing the foundation for your Azure network architecture.

### 2. **Create Network Watcher**
Establish a network watcher with a user-defined name, providing a crucial component for monitoring and diagnosing network issues in your Azure environment.

### 3. **Get Packet Capture**
Retrieve detailed information about packet captures, including their start time. This feature is invaluable for analyzing network traffic patterns and identifying potential issues.

### 4. **Delete Packet Capture**
Enhance control over your network monitoring data by selectively deleting packet captures. This function ensures efficient data management and compliance with your organization's policies.

### 5. **Generate Graph**
Unleash the power of data visualization with the graph feature. This dynamically generated graph showcases the number of packet captures over time. Real-life implications of this feature include:

- **Performance Analysis:** Understand how network activity fluctuates over time, enabling proactive performance optimization.
  
- **Security Insights:** Identify irregularities or spikes in packet captures, aiding in the detection of potential security threats or anomalies.

- **Capacity Planning:** Plan network resources effectively by analyzing historical data trends and making informed decisions about scaling resources.


## Usage

```bash
python azure_network_monitoring_tool.py [options]
```

Options:
- `create virtual network`: Create a virtual network.
- `create network watcher`: Create a network watcher.
- `get packet capture`: Retrieve packet capture details.
- `delete packet capture`: Delete a packet capture.
- `graph`: Create a graph for the number of packet captures over a virtual network against time

## Examples

```bash
# Create a virtual network
python azure_network_monitoring_tool.py create virtual network

# Create a network watcher
python azure_network_monitoring_tool.py create network watcher

# Get packet capture details
python azure_network_monitoring_tool.py get packet capture

# Delete a packet capture
python azure_network_monitoring_tool.py delete packet capture
```



