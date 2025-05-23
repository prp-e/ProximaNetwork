import os 
import requests 
from uuid import uuid4
from random import randint

os.system("ssh -R 15000:localhost:11434 debian@tunnel.proximagemini.com")