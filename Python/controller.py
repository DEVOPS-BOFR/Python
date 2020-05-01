from model import Initiate, Prepare_Lab, Resume_Lab, Lab_Progress, End_Lab
from controller_test import CommonSetup, CommonCleanup, Test
from view import Result
import requests


class Run_Lab():
    def __init__(self):
        self.init = Initiate()
        self.prep = Prepare_Lab()
        self.resum = Resume_Lab()
        self.progr = Lab_Progress()
        self.end = End_Lab()
        self.testsetup = CommonSetup()
        self.testclean = CommonCleanup() 
        self.test = Test()
        self.res = Result()

    def run(self):
        self.testsetup.prepare()

        self.test.setup()
        self.test.test1()
        self.test.cleanup()

        self.testclean.clean()


        print('Connecting...')
        self.init.connect()

        self.get_input()

        if self.user_input == 0:
            self.prep.conf = self.get_conf(self.prep.R1_unconfig_file)
            self.prep.wipe(self.init.dev, self.prep.conf)
        elif self.user_input == 1:
            self.prep.conf = self.get_conf(self.prep.R1_unconfig_file)
            self.prep.wipe(self.init.dev, self.prep.conf)
            
            self.resum.conf = self.get_conf(self.resum.resume_config)
            self.resum.load(self.init.dev, self.resum.conf)
        else:
            self.get_input()

        self.progr.sol = self.get_conf(self.progr.solution_config_file)


        while(True):
            self.progr.check(self.init.dev, self.progr.sol)

            print('Press "p" to pause the lab')
            print('Press "s" to submit the lab')
            
            inp = input()
            
            if inp == 'p':
                self.resum.save(self.progr.R1_conf_dict)
                self.set_conf(self.resum.resume_config, self.resum.conf)

                print('Quitting...')

                break

            elif inp == 's':
                self.end.save_result(self.progr.progress)

                input('''
                The lab result will now be shown on http://127.0.0.1:5555 
                
                press 'enter' to show the result''')

                self.res.show()

                print('Quitting...')
                
                break

        self.init.disconnect()

    def get_input(self):
        print('New lab or Resume lab?: ')
        print('0: New lab')
        print('1: Resume lab')
        
        try:
            self.user_input = int(input())
        except:
            print('Please try again...' + '\n')

            self.get_input()

    def get_conf(self, path):
        files = {'file': path}

        response = requests.get('http://127.0.0.1:5000/conf', files)

        return response.json()

    def set_conf(self, path, conf):
        files = {'file': path}
        requests.post('http://127.0.0.1:5000/conf', params=files, data=conf)


start = Run_Lab()
start.run()