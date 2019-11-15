import json
import os

class Configuration:


    def __init__(self):
        self.config_file = os.path.join(os.path.expanduser('~'), '.config', 'quickswitch.json')
        try:
            with open(self.config_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = { 'Directories': [] }
            with open(self.config_file, 'w') as f:
                json.dump(self.data, f, indent=2)
                f.close()

    
    def addFolder(self, folder):
        self.data['Directories'].append(folder)


    def writeConfig(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.data, f, indent=2)
                f.close()
        except Exception as e:
            print('Failed to write config file')


    def getDirectories(self):
        return self.data['Directories']
