#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size


    @property
    def size(self):
        return self._size
    
    #setter 
    @size.setter
    def size(self,size):
        if isinstance(size,int):
            self._size = size  
        else:
            print("size must be an integer")
            

    
    #getter 
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition= "New"
        
stan = Shoe("Adidas", 9) 
stan.cobble()
        


        
