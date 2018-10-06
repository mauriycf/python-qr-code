class Person:

    def __init__(self, first_name, last_name, address, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return ''.join(['{key}: {value} \n'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

#example class
#person = Person(first_name='Joe', last_name='Doe', address='California, L.A.', phone='1144148493', email='joedoe@example.com')
