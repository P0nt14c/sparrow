# Install PreReqs


This ansible role installs the pre-requiste packages for this webserver. 

It first installs python3 and pip3 using APT. 

Then, it uses pip3 to install the follow python libraries:
- cryptography
- datetime
- enum
- json
- os
- socket
- ssl
- sys