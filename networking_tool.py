from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
import sys
from datetime import datetime

import matplotlib.pyplot as plt



subs_id=YOUR_SUBSCRIPTION_ID
resource_group=RESOURCE_GROUP_NAME
subnet="default"
network_profile=YOUR_NETWORK_PROFILE
credential=DefaultAzureCredential()
storage_acc_name=STORAGE_ACCOUNT_NAME
vm_resource_group=VIRTUALMACHINE_RESOURCE_GROUP
vm_name=VIRTUALMACHINE_NAME

#network and resource Azure SDK clients
network_client = NetworkManagementClient(credential, subs_id)
resource_client= ResourceManagementClient(credential,subs_id)


#creating a vnet
def create_virtual_network(vnet_name='DefaultVnet' , ip_range="10.0.0.0/16"):
  network_client.virtual_networks.begin_create_or_update(
      resource_group,
      vnet_name,
      {
        "address_space": {
          "address_prefixes": [
          ip_range
          ]
        },
        "location": "eastus"
      }
  ).result()
  

#creating a network watcher
def create_network_watcher(network_watcher_name='DefaultWatcher'):
  network_client.network_watchers.create_or_update(
      resource_group,
      network_watcher_name,
      {
        'location':'eastus'
      }
  )




#getting packet capture with required argument network wtcher name
def get_packet_capture(network_watcher_name:str,packet_capture_name:str):
  packet_capture=network_client.packet_captures.get(
      resource_group,
      network_watcher_name,
      packet_capture_name
  )
  return packet_capture


#getting the start timestamp of packet capture

def get_start_time(packet_label):
    response = network_client.packet_captures.begin_get_status(
        resource_group_name=resource_group,
        network_watcher_name='DefaultWatcher',
        packet_capture_name=packet_label,
      ).result()
    start_time=response.capture_start_time
      
    
    return start_time





def get_all_packet_capture_start_times():
      
      packet_capture_names = []

      packet_captures= network_client.packet_captures.list(resource_group,'DefaultWatcher')
      for item in packet_captures:
         packet_capture_names.append(item.name)

      start_times = []
      for packet_capture_name in packet_capture_names:
          response = network_client.packet_captures.begin_get_status(
              resource_group_name=resource_group,
              network_watcher_name='DefaultWatcher',
              packet_capture_name=packet_capture_name,
          ).result()

          start_time = response.capture_start_time
          start_times.append(start_time)

      return start_times




def delete_packet_capture(network_watcher:str, packet_capture_name:str ):
  network_client.packet_captures.begin_delete(
    resource_group,
    network_watcher,
    packet_capture_name
  )


def get_number_of_packet_captures(resource_group,network_watcher_name):
    packet_captures = list(network_client.packet_captures.list(resource_group, network_watcher_name))
    return len(packet_captures)



def get_graph():
  
  all_start_times = get_all_packet_capture_start_times()

  # Convert start times to datetime objects
  datetime_start_times = [datetime.strptime(time.isoformat(), "%Y-%m-%dT%H:%M:%S.%f%z") for time in all_start_times]
  datetime_start_times.sort()
  # Create a list of integers representing the number of captures at each time point
  captures_count = list(range(1, len(datetime_start_times) + 1))

  # Plotting the graph
  plt.plot(datetime_start_times, captures_count, marker='o')
  plt.xlabel('Capture Start Time')
  plt.ylabel('Number of Packet Captures')
  plt.title('Number of Packet Captures Against Time')
  plt.yticks(range(1, len(datetime_start_times) + 1))
  plt.xticks(rotation=45)
  plt.tight_layout()


  plt.show()




def main():
  flag=False
  while True:
    n+=1
    try:
        print("Press ctrl+d, or enter 'x' to exit")
        if n>1 or len(sys.argv) == 1: #in the first iteration of the loop, it'll check for command line but it prompts the user in the following iterations
            command = str(
                input(
                    'Enter a command:- \n 1. Create a virtual network \n 2. Create a network watcher \n 3. Get a packet capture \n 4. Delete a packet capture \n 5. Create a graph of the number of packet captures against time \n'
                )
            )

        else:
           command= ' '.join(sys.argv[1:])
      #  print(command)
        if command=='x':
          sys.exit('you pressed "x" :(')

        if "create" in command:
            if 'virtual' in command and 'network' in command:
                print('virtual' in command, 'network' in command)
                vnet_name = input("Enter the name for the Virtual Network(Press 'Enter' to set as default): ")
                if vnet_name=='':
                   create_virtual_network()
                else:
                  create_virtual_network(vnet_name)

            elif 'network' in command and 'watcher' in command:
                
                watcher_name = input("Enter the name for the Network Watcher: ")
                create_network_watcher(watcher_name)

        if 'graph' in command:
                
                get_graph()
        

        elif 'delete' in command and 'packet' in command:
            network_watcher_name = input("Enter Network Watcher name: ")
            packet_capture_name = input("Enter Packet Capture name: ")
            delete_confirm = input("Confirm deletion (y/n)? ")
            if delete_confirm.lower() == 'y':
                delete_packet_capture(network_watcher_name, packet_capture_name)
            else:
               sys.exit()

        #getting packet captures and printing the json in a readable format

        elif 'get' in command:
           packet_capture_name = input("Enter Packet Capture name: ")
           network_watcher_name = input("Enter Network Watcher name: ")
           packet_capture_result=get_packet_capture(network_watcher_name,packet_capture_name)
           print(packet_capture_result)
           print(get_start_time(packet_capture_name))
           print(get_number_of_packet_captures(resource_group,'DefaultWatcher'),'packet capture(s) found')
           print('All Packet Captures:-\n')
           for capture in network_client.packet_captures.list(resource_group,'DefaultWatcher'):
              print('Name: '+capture.name+' Start Time: ',get_start_time(capture.name))


        

    except (EOFError or KeyboardInterrupt):
        sys.exit("You pressed ctrl+d :(")
    





main()
