# Proxima Network : A network of connected AI computers

Since the year 2020, when I got into the whole world of Generative AI, I had one big struggle. Finding a good, reliable and affordable infrastructure. In the process of making [Mann-E](https://mann-e.com) I could find tons of web service/cloud providers which were good and reliable but not really affordable and this is not really a surprising fact at all. GPU's are god damn expensive. Since models were open source and built by me, using API's wasn't an option unless someone hosts the models somewhere and give me access to the API.

So since I had a huge interest in _Web 3_ and _Bitcoin_ as well, I took a page from their book and tried to make something very similar to a blockchain but for computers which are running AI network. Why? Because there is a good chance that you, the person who is reading this page right now, have an NVIDIA card and you also were curious about [Ollama](https://ollama.com) and have it installed as well. So why not sharing the model with other people? and probably monetize your resources? 

The whole goal of _Proxima Network_ is to let you give other people access to your resources and get rewarded by the network. This repository will be a monorepo for both _Tunneling Tool_ and _Resource Sharing Scripts_. The super node will be closed source until we find a good way to have multiple of them and then it'll become open as well. 

## Table of Contents

- [Disclaimers](#disclaimers)
- [Definitions](#definitions)
- [Phases](#phases)
- [Overview](#overview-of-the-network)

## Disclaimers

- At current state, Proxima Network _is not_ decentralized _nor_ a blockchain of its own. Consider this. According to a poll I did on various communities, most of people voted for _Semi Decentralized_ system. So we call it a _Semi Decentralized_ network for now. 
- Currently the project is lead by one person and that's me, [Muhammadreza Haghiri](https://haghiri75.com/en). More devs are always welcome as well (so don't be shy to open a PR). 
- This is the only repository for _Proxima Network_. No github organization is made. There is also no public Telegram channel or group yet.
- Every phase of the project will be described in this `README.md` file and there will be a _status_ flag for each phase as well. So this may make you feel a little better every time visiting this repo 😁
- Finally, although a token (as rewards of nodes/users) may be considered, but we're not offering any coins or tokens _for presales_ or _trading_. Personal preference is actually collecting donations first then using that money to back the token. 

## Definitions

- **Super Node**: A Super Node is a computer/server running the main API which connects multiple _Nodes_ together. 
- **Node**: A Node is a computer which runs AI tools (as of now only _Ollama_) and can be accessed via a supernode. 
- **Tunneling Tool**: Tunneling Tool is the tool which exposes the nodes to the internet and lets them be seen by the super node. 

## Phases

- [x] Building and testing the tunneling tool. 
    - [x] Exposing a simple web server to the internet
    - [x] Exposing Ollama's OpenAI compatible endpoint to the internet using the tool. 
- [ ] Building the infrastructure for the tunneling tool. 
    - [ ] Configuring a subdomain on nginx for being _multi tenant_ when tunneling occurs.
- [ ] Building the python API 
    - [ ] Registering a Node to the super node's database 
    - [ ] Letting the node be tunneled for future use. 
- [ ] Building the super node 
- [ ] Reward Procedure

## Overview of the network

The basics of _Proxima Network_ has been pictured as following: 

<p align="center">
    <img src="basic_diagram.jpg" />
</p>

In this diagram, you can see that the users are sending a request to an OpenAI compatible endpoint which is located on the super node. Super node has the duty to collect information about models from the different nodes (and also I personally foresaw the feature were people can decide which models on their system will be exposed to the general public) and also has the duty to call different nodes on requests. 

Each node on that particular diagram is also called _Computer with Ollama Installed_ which is the first phase of AI tools being added to the network. These computers have strong enough resources for the models they exposed (The _Python API_ will have a JSON configuration format which lets you determine which models on your computer should go to the network). For example in order to run `aya-expanse:8b` on Ollama, I personally use a single 2050 and it works very well so this will be the model I will make public. So there will be a guide on models and how much hardware they consume. 

Lastly we have _users_. Users are people who are using Proxima Network in many different ways. The OpenAI compatible endpoint will let them have access to a big repository of models every time they want and it'll make AI more fun. 