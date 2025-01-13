**Encapsulation**
--
Encapsulation combines data and methods into one unit, hiding internal details from public access.

1. Defining the Class:

    class Warga:

A class named Warga is defined. This class will serve as a blueprint for creating objects that represent citizens.

2. The Constructor Method (__init__):

    def __init__(self):
        self.__nik = None

The __init__ method is the constructor. It initializes the object when it is created.
Inside the constructor:
An instance variable __nik is defined with a default value of None.
The double underscores (__) before nik make this variable private, meaning it cannot be accessed directly outside the class. This is an example of encapsulation.

3. Setter Method (set_nik):

    def set_nik(self, nik):
        self.__nik = nik
This is a setter method that allows the value of the private attribute __nik to be set.
It takes one parameter, nik, and assigns it to the private variable __nik.

4. Getter Method (get_nik):

    def get_nik(self):
        return self.__nik
This is a getter method that allows the value of the private attribute __nik to be accessed.
It returns the current value of __nik.

5. Creating an Object (galuh):

    galuh = Warga()

An object named galuh is created using the Warga class.
The __init__ method is automatically called, initializing __nik to None.

6. Using the Setter Method:

    galuh.set_nik(1234567890)

The set_nik method is called on the galuh object.
The private variable __nik is updated with the value 1234567890.

7. Using the Getter Method:

    print(galuh.get_nik())

The get_nik method is called on the galuh object.
It retrieves the value of the private variable __nik (1234567890) and prints it.

