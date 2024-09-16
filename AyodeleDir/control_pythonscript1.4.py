#!/usr/bin/python
import logging
import time
import commands

logging.basicConfig(filename='python.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)
logging.info("starting code run at %s"%TS)

hostname=commands.getoutput('hostname')
logging.info(hostname)

#logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(level=logging.INFO)
servers={
	"WINDOWS-URLDJ5Q":"patchprod"
	}
def patchprod():
	logging.info("This is the patchprod function")
if hostname in servers:
	logging.info("Calling the "+servers[hostname]+" function")
	if servers[hostname] == "patchpraod":
		patchprod()
	else:
		logging.info("invalid function")
else:
	logging.info("specified server does not exit")

tring=time.localtime()
TS=time.strftime("%d%m%y%M%S",time_string)
logging.info("ending code run at %s"%TS)
