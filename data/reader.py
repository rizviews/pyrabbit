import json
from uuid import uuid4
from datetime import timedelta,datetime
from random import randint


class reader(object):
    """description of class"""
    def __init__(self):
        self.todaydate = datetime.today()
        self.tomorrowdate = self.todaydate+timedelta(days=1)

    def read(self,testcase):
        
        with open(testcase) as data_file:
            content =  data_file.read()            
            data = json.loads(content)
            data = data['request']
        return json.dumps(self.recurse(data))

    def recurse(self,d):
        item = {}
        for k, v in d.items():
            if isinstance(v, dict):
                v = self.recurse(v)
            elif isinstance(v,list):
                for each in v:
                    if isinstance(v, dict):
                        v = self.recurse(v)
            if isinstance(v,str):  
                number = randint(10000,99999)              
                item[k] = v.replace("$uid",str(uuid4())).replace("$tomorrowdate",str(self.tomorrowdate.date()))\
                            .replace("$todaydate",str(self.todaydate.date())).replace("$number",str(number))
            else: 
                item[k] = v
            
        return item








