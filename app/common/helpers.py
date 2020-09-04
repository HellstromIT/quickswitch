from pyfzf.pyfzf import FzfPrompt
from app.common.walk import walklevel 

def addDirectory(config, folder):
    config.addFolder(folder)
    config.writeConfig()


def listDirectories(config):
    directories = []
    for directory in config.getDirectories():
        for dirs in walklevel(directory):
            directories.append(dirs[0])
    return(directories)

def selectDirectory(config, cwd):
    fzf = FzfPrompt()
    directories = listDirectories(config)
    try:
        directory = fzf.prompt(directories)
        print(directory[0])
    except:
        print(cwd)
