from data.reader import reader
from pprint import pprint
import os

class test_runner(object):
    """Class to test microservice"""
    def __init__(self,microservice_name=None,queue_name=None,test_dir=None):
        self.queue_name = queue_name
        self.batch_url = None
        self.reader = reader()
        self.test_dir = test_dir
        self.microservice = microservice_name
        self.record_count = 1

    def execute(self,publisher=None):
        publisher.queue_name = self.queue_name
        
        self.test_dir = self.test_dir+"\\"+self.microservice+"\\testcases\\"

        print ("test dir: {}".format(self.test_dir))
        for directory, subdirecotries, files in os.walk(self.test_dir):
            for file in files:
                filename = os.path.join(directory,file)
                print ("Executing {}".format(filename))


                for i in range (0,self.record_count):
                    data = self.reader.read(filename)
    
                    publisher.publish(data)

        publisher.close_connection()


