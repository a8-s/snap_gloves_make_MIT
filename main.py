import sampleCode as sc
import time
import os

#
import classHandlerList as CHL
class_handler_list = CHL.get_list_of_imports()
def run():
    p = Main()

class Main:
    def __init__(self):
        print("****************program*************")
        self.Boot()
        
    def Boot(self):
        for i in class_handler_list:
            try:
                i.isTypeCH == True
            except:
                print(i,"faulty")
                class_handler_list.remove(i)
        self.Setup()
        self.Loop()
    def Setup(self):
        print("runs once")
        for i in class_handler_list:
                i.Start()
                
        
    def Loop(self):
        while 1==1:
            for i in class_handler_list:
                i.Update()
                print(i)
        print("loop")
        time.sleep_ms(500)
        #self.Loop() #for recursion
            
#p = Main()