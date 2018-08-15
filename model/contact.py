
class contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, home=None, address=None, mobile=None, email=None, address2=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.home = home
        self.address = address
        self.mobile = mobile
        self.email = email
        self.address2 = address2
        self.id = id

    def __repr__(self):
        return ("%s:%s") % (self.firstname)

    def __eq__(self, other):
        return self.firstname == other.firstname