from flask import Flask, request
from flask_restful import Resource, Api
from genie.conf import Genie

app = Flask(__name__)
api = Api(app)


class Initiate(Resource):
    testbed = Genie.init('/home/hh/Documents/Python/testbed.yml')
    R1 = testbed.devices.R1

    def __init__(self):
        print('Hi')

# Connect to devices
    def get(self, dev = R1):
        dev.connect()

        print('Connected to {0}'.format(dev))

# Disconnect from devices
    def post(self, dev = R1):
        dev.disconnect()

        print('Disconnected from {0}'.format(dev))


class Prepare_Lab(Resource):
    R1_unconfig_file = '/home/hh/Documents/Python/R1_unconfig'
    R2_config_file = '/home/hh/Documents/Python/R2_config'
    R3_config_file = '/home/hh/Documents/Python/R3_config'

    def __init__(self):
        pass

# Clean device for new lab
    def post(self, dev = Initiate.R1, reset = R1_unconfig_file):
        dev.execute('write erase')

        uncon = Config()                # move?
        dev.configure(uncon.get(reset))

        print('wiped {0}'.format(dev))


class Resume_Lab(Resource):
    resume_config = '/home/hh/Documents/Python/resume'

    def __init__(self):
        pass

# Load/resume lab
    def get(self, dev = Initiate.R1, res = resume_config):
        a = Config()
        dev.configure(a.get(res))
        
        #print('Resume: ' + str(resume))

# Save/pause lab
    def post(self, res = resume_config ):
        a = ''
                                                    # dict
        #remove building and current from dict

        for k in solution_conf_dict.keys(): 
            a += k + '\n'
    
        for v in solution_conf_dict[k].keys():
            a += ' ' + v + '\n'  

        conf = Config()
        conf.post()

        with open(resume_config, 'w') as g:     # move
            for element in a:
                g.write(element)


class Lab_Progress(Resource):
    solution_config_file = '/home/hh/Documents/Python/R1_config'

    def __init__(self):
        pass

# Check lab progress
    def get(self, dev = Initiate.R1, sol = solution_config_file):
        b = Config()
        sol_str = b.get(sol)
        sol_dict = dev.api.get_config_dict(sol_str)
        
        R1_conf_str = dev.execute('show running-config')
        R1_conf_dict = dev.api.get_config_dict(R1_conf_str) # dict

        comp_str = sol_dict.keys() & R1_conf_dict.keys()

        l = []

        for k in sol_dict:
            if k.startswith('line') or k.startswith('int') or k.startswith('router'):
                l.append(str(sol_dict[k].keys() & R1_conf_dict[k].keys()))

        seperator = ','
        
        fin = seperator.join(l)
        lis = list(fin.split(seperator))        

        conf_len = len(comp_str) + len(lis)
        sol_len = len(open(sol).readlines())
        progress = conf_len / sol_len * 100

        print('Your lab progress is {0}%'.format(progress))


class Lab_Test(Resource):
    def __init__(self):
        pass

# Run unit tests
    def post(self):
        pass


class Convert(Resource):
    def __init__(self):
        pass

# Convert string to dictionary
    def get(self, dev = Initiate.R1, s):
        dic = dev.api.get_config_dict(s)
        return dic


class Config(Resource):
    def __init__(self):
        pass

# Load config file
    def get(self, fil):
        with open(fil) as f:
            var = f.read()
        print('File read: ' + fil)
        return var

# Save config file
    def post(self, fil):
        with open(fil, 'w') as g:
            for element in fil:
                g.write(element)


api.add_resource(Initiate, '/init')
api.add_resource(Prepare_Lab, '/prep')
api.add_resource(Resume_Lab, '/resume')
api.add_resource(Lab_Progress, '/prog')
api.add_resource(Lab_Test, '/test')
api.add_resource(Convert, '/conv')
api.add_resource(Config, '/conf')


if __name__ == '__main__':
    app.run(debug=True)



'''
Load config
Save config
'''


'''
Test
'''