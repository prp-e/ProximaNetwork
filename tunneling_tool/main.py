import os 
import requests 
import random
from uuid import uuid4
from random import randint

random.seed()

def generate_credentials():
    computer_name = uuid4()
    port = randint(11000, 65535)