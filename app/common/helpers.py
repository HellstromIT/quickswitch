def addDirectory(folder):
    config.addFolder(folder)
    config.writeConfig()


def listDirectories():
    for directory in config.getDirectories():
        for dirs in walklevel(directory):
            print(dirs[0])

