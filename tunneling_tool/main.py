import os 
import requests 
import random
from uuid import uuid4
from random import randint

random.seed()

def generate_credentials():
    computer_name = uuid4()
    port = randint(11000, 65535)

    return computer_name, port


if __name__ == "__main__":
    user_data = generate_credentials()

    res = requests.post(
        "https://nodemaker.proximagemini.com/node",
        json = {"computer_name" : str(user_data[0]), "port" : user_data[1]},
        headers={"content-type" : "application/json"}
    )

    print(f"Your node is up at https://{user_data[1]}.tunnel.proximagemini.com")

    os.system(f"ssh -R {user_data[1]}:localhost:11434 debian@tunnel.proximagemini.com")