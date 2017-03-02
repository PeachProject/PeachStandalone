# PeachStandalone

```
______               _     
| ___ \             | |    
| |_/ /__  __ _  ___| |__  
|  __/ _ \/ _` |/ __| '_ \ 
| | |  __/ (_| | (__| | | |
\_|  \___|\__,_|\___|_| |_|
                STANDALONE


License:    GPLv3
Authors:    Christian Bierstedt
            Henry Müssemann
```

## Concept

Peach is a platform for distributed data analysis that enables the user to define and execute workflows. Peach is built for data analysis specialists and developers that may be interested in building their own application around the components.

The system consists of the following major components:
  - The Peach client that is a web application giving the user access to his data and workflows.
  - The Peach backend that translates the peach workflow to a specific workflow management domain (e.g. [dask](http://dask.pydata.org)).
  - A MySQL server where workflows are queued and progress is stored.
  - An [XNAT](https://www.xnat.org/) server that acts as central data storage.
  - An [Apache Kafka](https://kafka.apache.org) server that acts as central messaging bus.
  - An LDAP server for user management.

Peach is similar to [OpenMOLE](https://www.openmole.org/). However built with the idea in mind to be a combination of already available tools it is designed to easily exchange or extend the major components allowing further developers to tailor the system to their specific needs with your custom scripts or grown eco system. The web application gives access to design and monitor workflows anywhere even for none computer scientists.

## Setting up the standalone version

  ```
  . setup.sh
  ```

  Requirements:
    - Ubuntu 14+
    - Internet Access
    - root access (sudo)

  You will be guided through the installation process. When ldap server configuration pops up memorize or write down what you've put in, please. Later on you will need it. Same with mysql server installation.
  
  Next you will be asked if you would like to auto-install the php ldap manager. We highly suggest doing so. Afterwards you will have to manually configure the php ldap manager. You can find a walk-through [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-a-basic-ldap-server-on-an-ubuntu-12-04-vps#configure-phpldapadmin)

  Afterwards you will be asked for a username for a kafka user. Kafka recommends adding a separate kafka user for settings up a kafka server. At this point we are asking for the username of the user that should either be created or extended to be the kafka server host user. If unsure, just enter `kafka` and give it a strong password.

  You will be asked to put in the mysql root password. Please do so.

  Last but not least please enter your ldap domain / server.

  You have successfully set up the working peach server at this point.

## Starting your peach standalone server

  ```
  . start.sh
  ```

  Requirements:
    - Ubuntu 14+
    - gnome-terminal
    - At least 1 min of free time

  The load up can take up to one minute. If you access your web address (default: `http://localhost:5000/`) and none of your services show when creating a workflow, just wait for the minute to finish and update the page again. It will work then
