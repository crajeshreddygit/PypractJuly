import datetime
import logging
#logging.basicConfig(filename="plog.txt",level=logging.DEBUG, filemode='a')       #level =10 , filemode = a , w
#logging.basicConfig()
#logging.basicConfig(format="%(levelname)s")
#logging.basicConfig(format="%(levelname)s:%(message)s")
#logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
#logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
print("logging Demo")

logging.critical("criticals ")
logging.warning("warnings")
logging.error("errors")
logging.info("infos")
logging.debug("debugs")


