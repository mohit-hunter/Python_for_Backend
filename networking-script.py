import socket
import requests
import json
import platform
import uuid

class AndroidNetworkManager:
    def __init__(self, server_url='http://localhost:5000'):
        self.server_url = server_url
        self.device_id = str(uuid.uuid4())

    def get_device_info(self):
        return {
            'device_id': self.device_id,
            'os_version': platform.system() + " " + platform.release(),
            'device_model': platform.machine(),
            'total_memory': f"{platform.processor()} processor"
        }

    def send_device_info(self):
        device_info = self.get_device_info()
        
        try:
            # Send device info to backend API
            response = requests.post(
                f'{self.server_url}/add-app', 
                json={
                    'app_name': 'DeviceInfoApp',
                    'version': '1.0.0',
                    'description': json.dumps(device_info)
                }
            )
            
            if response.status_code == 201:
                print("Device info successfully sent to server")
                print("Server Response:", response.json())
            else:
                print("Failed to send device info")
        
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")

    def tcp_connection_test(self, host='localhost', port=8000):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                s.sendall(json.dumps(self.get_device_info()).encode())
                data = s.recv(1024)
                print(f"Received from server: {data.decode()}")
        except Exception as e:
            print(f"TCP connection error: {e}")

if __name__ == '__main__':
    network_manager = AndroidNetworkManager()
    network_manager.send_device_info()
    network_manager.tcp_connection_test()
