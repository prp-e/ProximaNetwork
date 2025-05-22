# Content of this file will be used in AI to get better ideas for implementation

# Tunneling Tool Explanation

We're about to develop a tool which exposes our computer to the internet. For this purpose, we're working on a tool with these features: 

- Behaving like `ngrok` and tunneling the local tools to the outer internet. 
- The only port needing to be exposed is 11434 port. 
- The tool is being written in python. 

Also on the server side we need these:

- Each computer has a name.
- The server must be multitenant. 
- We're using `sudo certbot -d example.com --nginx` to setup the https. 

Based on the above description, just provide a good step-by-step guide on both sides implementation.