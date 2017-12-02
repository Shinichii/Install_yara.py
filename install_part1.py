import os
import urllib

currentDirectory = os.path.dirname(os.path.abspath(__file__))
version="3.7.0"
yaraVersion="yara-"+version
os.system("apt-get install automake libtool make gcc libssl-dev python-pip")
urllib.urlretrieve("https://github.com/VirusTotal/yara/archive/v"+version+".tar.gz", yaraVersion + "tar.gz")

os.system("tar -zxf  "+ yaraVersion + ".tar.gz")
os.system("pip install yara-python")

print("Le telechargement des fichiers sources est desormais termine. Pour finir l'installation, veuillez lancer le script install_yara.py dans le dossier" + currentDirectory + "/" + yaraVersion)
