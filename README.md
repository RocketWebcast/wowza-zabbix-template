wowza-zabbix-template
=====================

Description
-----------

This is a fork from vicendominguez/wowza-zabbix-template. I had a hard time finding a script that would work with current versions of python, most of them are 8+ years old. They use depreciated libraries, so I re-wrote this one - it uses urllib3 to fetch the data. I also expanded on the information getting back from Wowza.
This is a minimal template to get info about your wowza rest url into your Zabbix Platform.

You will get the following metrics out of Wowza:

* Global current connections in Wowza
* Global Live streams number
* Server Uptime
* Global total connections
* Global incoming bytes
* Global outgoing bytes
* All of the above combined

The template uses Zabbix macros to define the user/pass Wowza server url.

It permits a fast configuration because of you can apply the same template to all your Wowza servers without modification/installation in the agents.

Of course, it can work in the agent/client side too.

Install
-------

You should look for the external scripts directory in your Zabbix configuration file. 
In the CentOS 9 installation is: 

``` 
 /usr/lib/zabbix/externalscripts 
```

Copy the python script there. A chmod/chown to 755 is necessary to get execution permission.

Now, in your Zabbix frontend: Data Collection -> Templates, click the Import button in the top right corner.
Choose the XML file and import.

Apply this new template to your Wowza servers.
Make sure the firewall is not preventing zabbix from accessing the port (8086 by default).

To enable the user/pass you will need to create four macros wherever you prefer. I am using the Macros tag in the host config screen.

Four host macros should be created:

* {$WOWZAHOST}
* {$WOWZAPORT}
* {$WOWZAUSER}
* {$WOWZAPASS}

Environment
-----------

I am using this script in my production environment:

* Wowza 4.x
* Zabbix > 6.4.x 


Screenshots
-----

![zabbix_wowza_screenshot1](https://github.com/RocketWebcast/wowza-zabbix-template/assets/135097798/f083251b-115c-40eb-b2aa-d892fc8a53a9)


![zabbix_wowza_screenshot2](https://github.com/RocketWebcast/wowza-zabbix-template/assets/135097798/a3f892e1-730d-4fb9-80ff-54e0a345bc72)



