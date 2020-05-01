from genie.conf import Genie


class Initiate():
    def __init__(self):
        self.testbed = Genie.init('/home/hh/Documents/Python/testbed.yml')
        self.dev = self.testbed.devices.R1

        print("Class {0} instantiated".format(self) + '\n')

    # Connect to devices
    def connect(self):
        self.dev.connect()

        print('Connected to {0}'.format(self.dev) + '\n')

    # Disconnect from devices
    def disconnect(self):
        self.dev.disconnect()
        
        print('Disconnected from {0}'.format(self.dev) + '\n')
    

class Prepare_Lab():
    def __init__(self):
        self.R1_unconfig_file = '/home/hh/Documents/Python/R1_unconfig'
        
    # Clean device for new lab
    def wipe(self, dev, conf):
        dev.execute('write erase')
        dev.configure(conf)

        print('wiped {0}'.format(dev) + '\n')

    
class Resume_Lab():
    def __init__(self):
        self.resume_config = '/home/hh/Documents/Python/resume'

    # Load/resume lab
    def load(self, dev, conf):
        dev.configure(conf)
        
        print('Resumed lab' + '\n')

    # Save/pause lab
    def save(self, dic):
        self.conf = ''
        #remove building and current from dict

        for k in dic.keys():
            if k.startswith('Building') or k.startswith('Current') or k.startswith('end'):
                pass
            else:
                self.conf += k + '\n'
    
            for v in dic[k].keys():
                self.conf += ' ' + v + '\n'


class Lab_Progress():
    def __init__(self):
        self.solution_config_file = '/home/hh/Documents/Python/R1_config'

    # Check lab progress
    def check(self, dev, conf):
        sol_dict = dev.api.get_config_dict(conf)
    
        R1_conf_str = dev.execute('show running-config')
        self.R1_conf_dict = dev.api.get_config_dict(R1_conf_str)

        comp_str = sol_dict.keys() & self.R1_conf_dict.keys()

        l = []

        for k in sol_dict:
            if k.startswith('line') or k.startswith('int') or k.startswith('router') in sol_dict:
                l.append(str(sol_dict[k].keys() & self.R1_conf_dict[k].keys()))

        seperator = ','
        
        fin = seperator.join(l)
        lis = list(fin.split(seperator))        

        conf_len = len(comp_str) + len(lis)
        sol_len = len(open(self.solution_config_file).readlines())
        self.progress = conf_len / sol_len * 100

        print('Your lab progress is {0}%'.format(self.progress) + '\n')


class End_Lab():
    def __init__(self):
        self.res = '/home/hh/Documents/Python/result'

    def save_result(self, result):
        with open(self.res, 'w') as f:
            f.write(str(result))