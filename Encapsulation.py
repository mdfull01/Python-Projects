

class Employee:
    _companyName = 'Amazon' # protected class attribute
    __location = 'Seattle'  # private class attribute

    def __init__(self, fname, lname, age):
        self._fname = fname # protected object/instance attribute
        self._lname = lname # protected object/instance attribute
        self.__age = age # private object/instance attribute

    def __companyInfo(self):
        print('This is where the company information goes.')

emp = Employee('John', 'Doe', '31') # create object emp which is an instance of the Employee class

emp._Employee__companyInfo()
        
    
