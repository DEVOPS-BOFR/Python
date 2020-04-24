import requests

class Controller():
    def Run_Lab(self):
        pass


# Connect
connect = requests.get('http://127.0.0.1:5000/init')


# Disconnect
disconnect = requests.post('http://127.0.0.1:5000/init')


# New lab or resume lab
    # load new
    # load saved

# Initiate lab
    # yaml
    # config

# Load solution


# Compare while user works
    # display progress

# Submit or save
    # save config
        # display results