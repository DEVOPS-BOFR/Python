{'Solution': {
    'R1': {
        'Device': {
            'Domain': 'test.com',
            'Crypto': 'True',
            'SSHv2': 'True',
            'Banner': 'Something'
            },
        'Line': {
            'Vty_0_4': 'login',
            'Password': 'ccna'
            },
        'Interface': {
            'GigabitEthernet0/0': {
                'Description': 'Link to R2',
                'IP': '172.16.0.5',
                'Netmask': '255.255.255.252',
                'Shutdown': 'False'
                },
            'GigabitEthernet1/0': {
                'Description': 'Link to R3',
                'IP': '172.16.0.9',
                'Netmask': '255.255.255.252',
                'Shutdown': 'False'
                },
            'Loopback0': {
                'IP': '10.10.10.10',
                'Netmask': '255.255.255.255',
                'Shutdown': 'False'
                },
            },
        'OSPF': {
            'Process': '1',
            'Area': '0'
            }      
        },
    'R2': {
        'Device': {
            'Domain': 'test.com',
            'Crypto': 'True',
            'SSHv2': 'True',
            'Banner': 'Something'
            },
        'Line': {
            'Vty_0_4': 'login',
            'Password': 'ccna'
            },
        'Interface': {
            'GigabitEthernet0/0': {
                'Description': 'Link to R1',
                'IP': '172.16.0.6',
                'Netmask': '255.255.255.252',
                'Shutdown': 'False'
                },
            'GigabitEthernet1/0': {
                'Description': 'Link to R3',
                'IP': '172.16.0.1',
                'Netmask': '255.255.255.252',
                'Shutdown': 'False'
                },
            'Loopback0': {
                'IP': '10.20.30.40',
                'Netmask': '255.255.255.255',
                'Shutdown': 'False'
                },
            },
        'OSPF': {
            'Process': '1',
            'Area': '0'
            }    
        },
    'R3': {
        'Device': {
            'Domain': 'test.com',
            'Crypto': 'True',
            'SSHv2': 'True',
            'Banner': 'Something'
            },
        'Line': {
            'Vty_0_4': 'login',
            'Password': 'ccna'
            },
        'Interface': {
            'GigabitEthernet0/0': {
                'Description': 'Link to R2',
                'IP': '172.16.0.2',
                'Netmask': '255.255.255.252',
                'Shutdown': 'False'
                },
            'GigabitEthernet1/0': {
                'Description': 'Link to R1',
                'IP': '172.16.0.10',
                'Netmask': '255.255.255.252',
                'Shutdown': 'False'
                },
            'Ethernet2/7': {
                'Description': 'Link to S1',
                'IP': '192.168.200.1',
                'Netmask': '255.255.255.0',
                'Shutdown': 'False'
                },
            'Loopback0': {
                'IP': '10.11.12.13',
                'Netmask': '255.255.255.255',
                'Shutdown': 'False'
                },
            },
        'OSPF': {
            'Process': '1',
            'Area': '0'
            }
        },
    'S1': {
        'Device': {
            'Banner': 'Something'
            },
        'Line': {
            'Vty_0_4': 'login',
            'Password': 'ccna'
            },
        'Interface': {
            'Vlan2': {
                'Description': 'Management',
                'IP': '192.168.200.2',
                'Netmask': '255.255.255.0',
                'Shutdown': 'False'
                },
            'Ethernet0/0': {
                'Description': 'Link to R3',
                'VLAN': '2',
                'Shutdown': 'False'
                },
            },
        }
    }
}