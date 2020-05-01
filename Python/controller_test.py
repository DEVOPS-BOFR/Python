from model import Initiate
from pyats import aetest


#log = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def prepare(self):
        print('CommonSetup...not used')
        input('Press "enter" to continue...')


class Test(aetest.Testcase):
    @aetest.setup
    def setup(self):
        self.init = Initiate()
        self.init.connect()

        self.enable = self.init.dev.execute('show running-config | include enable')

        print(f'Getting enable password: {self.enable}')
        input('Press "enter" to continue...')

    @aetest.test
    def test1(self):
    
        assert self.enable == 'enable password ccna'

        print('Asserting...looks good...')
        input('Press "enter" to continue...')

    @aetest.cleanup
    def cleanup(self):
        input('Press "enter" to clean up...')
        self.init.disconnect()
        

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def clean(self):
        print('CommonCleanup...not used')
        input('Press "enter" to continue...')

'''
a = CommonSetup()
a.connect()

b = Test()
b.setup()
b.test1()

c = CommonCleanup()
c.disconnect()
'''