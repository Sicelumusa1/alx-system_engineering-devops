Project Title: SSH

Introduction

This project provides a set of Bash scripts and instructions for managing SSH key authentication,
SSH key pair generation, and SSH client configuration. These scripts and guidlines simplify the 
process of SSH key management and enhance security by allowing passwordless authentication and 
secure key generation

Table of Contents

0. Use a Private Key
1. Create an SSH Key Pair
2. Client Confuguration File
3. Adding SSH Public Keys

0. Use a Private Key
Objective
Connect to your server using an SSH private key

Instructions
Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase

1. Create an SSH Key Pair
Objective
Generate an RSA key pair with specific requirements

Instructions
Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty

2. Client Configuration File
Objective
Confugure the local SSH client to enable passordless authentication and security

Instructions
Your machine has an SSH configuration file for the local SSH client, let’s configure it 
to our needs so that you can connect to a server without typing a password.

Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password

3. Adding SSH Public Key
Objective
Enable another user to connect to your sever using the 'ubuntu' user

Instructions
Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

By Following these instructions and using the provided Bash scripts, you can effectively manage 
SSH key authentication, enhance security, and facilitate romote access to your server without the 
need for passwords. Enjoy secure and convenient server access with SSH key management.

