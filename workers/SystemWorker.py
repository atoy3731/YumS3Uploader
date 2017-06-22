import tarfile
import Config

def untar_file(file):
    tar = tarfile.open(file)
    tar.extractall(Config.WORKING_DIRECTORY)
    tar.close()