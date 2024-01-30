import logging
# logging.basicConfig(filename="C:\\Users\\Srikanth\\Documents\\python\\python_learning\\text.log" , filemode='w' , )
# print("file created")
#DEBUG
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
# log.debug("This is debug log")
# log.info("This is info log")
# log.warning("This is warning log")
# log.error("This is error log")
# log.critical("This is critical log")

#WARNING
# log = logging.getLogger()
# log.setLevel(logging.WARNING)
# log.debug("This is debug log")
# log.info("This is info log")
# log.warning("This is warning log")
# log.error("This is error log")
# log.critical("This is critical log")


#INFO

# log = logging.getLogger()
# log.setLevel(logging.INFO)
# log.debug("This is debug log")
# log.info("This is info log")
# log.warning("This is warning log")
# log.error("This is error log")
# log.critical("This is critical log")


#CRITICAL
# log = logging.getLogger()
# log.setLevel(logging.CRITICAL)
# log.debug("This is debug log")
# log.info("This is info log")
# log.warning("This is warning log")
# log.error("This is error log")
# log.critical("This is critical log")

logging.basicConfig(filename='text.log' , level=logging.DEBUG)
logging.disable()
def Namecheck(name):
    if len(name) <2:
        logging.debug('Check name length')
        return 'invalid name'
    elif name.isspace():
        logging.debug('Check name space')
        return 'invalid name'
    elif name.isalpha():
        logging.debug('Check name isalpha')
        return 'Name is valid'
    elif name.repalce(' ','').isalpha():
        logging.debug('Check full name')
        return 'Name is valid'
    else:
        logging.debug('Failed all check')
        return 'Name is valid'
Namecheck('sri')

