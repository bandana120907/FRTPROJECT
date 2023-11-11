


# Azure Networking Command-Line Tool

The Azure Networking Command-Line Tool is a Python-based utility designed to simplify the management of networking resources within Microsoft Azure. This tool focuses on creating a streamlined experience for tasks such as virtual network creation, network monitoring, and packet capture. Additionally, it provides a graphical representation of packet capture activities over time, enhancing user comprehension.

## Features

- **Virtual Network Management:** Easily create and manage Azure Virtual Networks with a user-friendly command-line interface.

- **Network Watcher Creation:** Simplify the process of creating Azure Network Watchers for efficient monitoring and diagnostics.

- **Packet Capture Operations:** Streamline packet capture tasks, allowing users to initiate captures with specified configurations.

- **Graphical Visualization:** Visualize the timeline of packet captures over time through an interactive graph using `matplotlib`.


## Prerequisites

- Python 3.x
- Azure SDK for Python (`azure-mgmt-network`)
- `matplotlib` library for graph plotting

## Usage

1. Run the script from the command line.
2. Choose operations (create virtual networks, network watchers, packet captures, or plot captures over time).
3. Provide necessary parameters for each operation.

## Example

```bash
python main.py create virtual network
```

## Acknowledgments

- Special thanks to the Azure SDK for Python community.
- Graph plotting powered by `matplotlib`.

Feel free to contribute or report issues! Happy coding!


