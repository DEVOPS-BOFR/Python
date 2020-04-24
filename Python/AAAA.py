import pprint

# Show result

import requests

response = requests.get('http://127.0.0.1:5000')
response = requests.post('http://127.0.0.1:5000', json = {json_data})
print(response.json())

# Test

from pyats import aetest
from some_lib import configure_interface

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_device(self, testbed):
        # connect to testbed devices
        for device in testbed:
            device.connect()

class SimpleTestcase(aetest.Testcase):
    @aetest.test
    def simple_test(self, testbed):
        # configure each device interface
        for device in testbed:
            for intf in device:
                configure_interface(intf)

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        # disconnect_all
        for device in testbed:
            device.disconnect()