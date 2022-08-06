Comments #

Multiline comments """     """

- No declaration of variables. Use as it is:
      a = 1
      b = "Hello"
      c = 1.5
      
      
List

      b = [ "Hello", "World" ]
      
      c = [ "Hola", 1, 2 ]
      
      b[1]
      -> World
      
      b + [ 1, 2, 3, 4, 5 ]
      -> "Hello", "World", 1, 2, 3, 4, 5
      
Dictionaries

      c = { "FavoriteColour" : "Orange" }
      
      c["FavoriteColour"]
      -> Orange
      
Set

      d = { 1, 2, 3, 4, 4, 4, 5, 5, 5 }
      -> 1,2,3,4,5
      
Conditions

     if 1 == 1:
          print ("Of course")
     if 1 == 2:
          print ("Obviously not")
          
     Operators: !=, <, >, <=, >=
     Boolean: True, False
Loops

      b = ["Helllo" , "World" ]
      for item in b:
           print (item)
      for i in range(0,10):
           print(i)
           
      x = 10
      while x > 0:
           print(x)
           x -= 1
           
Exception

     try :
         print (b[2])
     except IndexError:
         print("Item not on list"
         
Function

     def func():
         print("Hello World")
         
Objeccts

     class Person:
           def __init__(self):
                 print("New person")
                 
     p = Person()
     
Inheritance

    class Francis(Person):
          def __init__(self):
               super().__init__()
               print(" I am Francis")
    f = Francis()
    -> New Person
    -> I am Francis
    
Modules

    import math
    
    print (math.pi)
