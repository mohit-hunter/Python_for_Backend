import subprocess
import platform
import psutil
import logging

class AndroidVirtualSystem:
    def __init__(self, avd_name='test_avd'):
        self.avd_name = avd_name
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def create_virtual_system(self):
        try:
            # Create Android Virtual Device (AVD)
            create_cmd = [
                'avdmanager', 'create', 'avd', 
                '-n', self.avd_name, 
                '-k', 'system-images;android-30;google_apis;x86_64'
            ]
            subprocess.run(create_cmd, check=True)
            self.logger.info(f"Virtual Android system {self.avd_name} created")
        except Exception as e:
            self.logger.error(f"Error creating virtual system: {e}")

    def launch_virtual_system(self):
        try:
            # Launch emulator
            launch_cmd = ['emulator', '-avd', self.avd_name]
            subprocess.Popen(launch_cmd)
            self.logger.info(f"Launching virtual Android system {self.avd_name}")
        except Exception as e:
            self.logger.error(f"Error launching virtual system: {e}")

    def get_system_info(self):
        system_info = {
            'os_version': platform.system(),
            'os_release': platform.release(),
            'device_model': platform.machine(),
            'total_memory': f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
            'available_memory': f"{psutil.virtual_memory().available / (1024**3):.2f} GB"
        }
        
        self.logger.info("System Information:")
        for key, value in system_info.items():
            self.logger.info(f"{key}: {value}")
        
        return system_info

    def install_apk(self, apk_path):
        try:
            install_cmd = ['adb', 'install', apk_path]
            result = subprocess.run(install_cmd, capture_output=True, text=True)
            self.logger.info(f"APK Installation Result: {result.stdout}")
        except Exception as e:
            self.logger.error(f"Error installing APK: {e}")

if __name__ == '__main__':
    android_system = AndroidVirtualSystem()
    android_system.create_virtual_system()
    android_system.launch_virtual_system()
    android_system.get_system_info()
    # Uncomment and replace with actual APK path
    # android_system.install_apk('/path/to/sample.apk')
