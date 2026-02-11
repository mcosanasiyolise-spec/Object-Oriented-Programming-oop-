class Parrot:

     # class attribute
     species ="bird"

     #instance attribute
     def_init_(self, name, age):
     self.name = name
     self.age = age

     # instaniate the Parrot class
     blu = Parrot("blu", 10)
     woo = Parrot("woo", 15)
    
    #acces the class attributes
    print("Blu is a {}".format(blu.species))
    print("Woo is also a {}".format(woo.species))


    #access the instance attributes
    print("{} is {} years old".format(blu.name, blu.age))
    print("{} is {} years old".format( woo.name, woo.age))
