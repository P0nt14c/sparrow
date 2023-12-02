# Sparrow


CSEC 731 Python Web Server


Author: Jason Howe


## Installation

Clone the repository done </br>
`git clone https://github.com/P0nt14c/sparrow.git`


## Usage 
There are three different modes for Sparrow to run in:

### Request Checking
To check a HTTP Request in a file: </br>
`python3 sparrow.py <path/to/request>`

### HTTP Mode
To use Sparrow in HTTP only:
`python3 sparrow.py <ip> <port>`

### HTTPS Mode
To use Sparrow in HTTPS only:
`python3 sparrow.py <ip> <port> <crt.file> <key.file>`

## Structure

### Ansible
The [Ansible](ansible) directory contains the ansible code that will deploy the sparrow webserver on localhost. </br>
There are some weird permissioning errors with TMP, so that may prevent pages from being served. However, Sparrow works. </br>
The ansible will deploy Sparrow as a systemd service, which requires elevated permissions. Make sure to change the credentials specified in the inventory file to be able to run the playbook successful. </br>
The command to run the playbook, from the ansible directory is:
```ansible-playbook -t sparrow sparrow.yaml```

### Code
The [code](code) directory contains all of the code written to complete this project. See usage above to use sparrow. </br>
The files within the directory contain small explantations about what function they serve. </br>
As of right now, most funcitons are documented properly. </br>

### Docker
The [docker](docker) directory contains the docker-compose file to deploy Sparrow as a container. </br>
See the [readme](docker/readme.md) in the docker directory for more information.

### Documentation
The [documentation](documentation) directory contains all 10 progress reports for this project. 

### Documets
The [Docuemnts](documents) directory contains certificates and web requests used for testing.

### Log
The [log](documents) directory was used for logging the requests. The logging functionality has since been updated to log to /tmp/good.txt and /tmp/bad.txt

### Tests
The [tests](tests) directory has an non-comprehensive set of tests that was used for testing. It should be extended and fully comprehensive in the future. 

### Main
In the top level directory, you will find:
- [assessment.md](assessment.md) which is the risk assessment
- [writeup.md](writeup.md) which is the technical write up for the vulnerability
- this readme

Hopefully this description of the structure aids a developer or user in using this tool. 


## Future Work
This project could benefit from the following:
- [ ] documentation review
- [ ] full testing 
- [ ] develop documentation
