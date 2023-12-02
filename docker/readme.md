# Docker


This directory contains docker configurations to deploy Sparrow in Docker containers. 

The only working deployment is with Caddy. 
To use: 
```docker-compose up -d```
within this directory

[Caddy](https://caddyserver.com/docs/) provides TLS Termination, load balancing, and reverse proxying. 

### Other Configurations
The are a number of other ways to configure web server setups. They can be implemented in the future.