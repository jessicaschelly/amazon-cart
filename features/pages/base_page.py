from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
#--------------------------------------------------------------------------------------------------------#
# BasePage is a common class where the developer can write the necessary methods in python and re-use on #
# entire test, make sure the methods that you will write here are flexible, without constants or hardcode#
# data.                                                                                                  #
# Verify method names are readable to facilitate future maintenance and make it easier for other         #
# developers to use the method.                                                                          #
#--------------------------------------------------------------------------------------------------------#
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 5
        self.implicit_wait = 5

#----------------------------------------------------------------------------------------------------------------------#
# DATAPOOL_READ is a method use to get a collection of information from a source archive Dictionaries, Hashmaps, and   #
# Hash Tables. This method need 3 arguments: the dict's name, the collection's name and the key that you searching for.#
#                                                                                                                      #
#   Example:                                  result = datapool_read(DATA_SOURCE, valid_data, 'key_1')                 #
#       DATA_SOURCE ={                        print("Results is: ", result)                                            #
# 	        "valid_data" :[{                                                                                           #
# 	                 "key_1" : "value1",                                                                               #
#      	             "key_2" : "value2"       output:  Results is: value1                                              #
#      	     }],                                                                                                       #
#           "invalid_data" :[{                                                                                         #
# 	                "key_1" : "value1",                                                                                #
#      	            "key_2" : "value2"                                                                                 #
#      	            }]                                                                                                 #
# }                                                                                                                    #                                                                          #
#----------------------------------------------------------------------------------------------------------------------#


    def datapool_read(self, source, data, key):
        """Get a list of arguments named as 'data' on the 'source' and search the 'key' on that list."""
        data_args = source.get(data.replace(' ', '_'))
        dt_key = key.replace(' ', '_')
        if data_args is not None:
            #Search the 'key' on that list
            if data_args[0].get(dt_key)is not None:
                return data_args[0].get(dt_key)
            else:
                message = "No matching results for parameter data = "+ data +" on the key = " + key +" was found in DataPool."
                raise Exception(message)
        else:
            message = "No matching results for parameter data = "+ data +" on the key = " + key +" was found in DataPool."
            raise Exception(message)
