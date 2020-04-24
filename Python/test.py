# Configure device features and config 
R1.configure('')
R1.api.configure_device('', 100)


# Initiate files
solution = '/home/hh/Documents/Python/R1_config'
saveconfig = '/home/hh/Documents/Python/saved'
unconfig = '/home/hh/Documents/Python/R1_unconfig'


# Save list
with open(file, 'w') as g:
    for element in lines:
        g.write(element)
        g.write('\n')


# Save string
with open(file, 'w') as g:
    for element in lines:
        g.write(element)


# Load list
with open(sol) as f:
    lines = f.read().splitlines()


# Load string
with open(sol) as f:
    lines = f.read()
--------------------------------------------------------------

class Resume_Lab(Resource):
    resume_config = '/home/hh/Documents/Python/resume'

    def post(self, ):
        a = ''

        for k in solution_conf_dict.keys(): 
            a += k + '\n'
    
        for v in solution_conf_dict[k].keys():
            a += ' ' + v + '\n'  

    #Compare a with some filter...

        with open(resume_config, 'w') as g:
            for element in a:
                g.write(element)




class Lab_Progress(Resource):
    solution_config_file = '/home/hh/Documents/Python/R1_config'

    def get(self, dev = Initiate.R1, sol = solution_config_file):
        with open(sol) as f:
            sol_str = f.read()
        
        sol_dict = dev.api.get_config_dict(sol_str)
        
        R1_conf_str = dev.execute('show running-config')
        R1_conf_dict = dev.api.get_config_dict(R1_conf_str)

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