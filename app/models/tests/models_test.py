from ..model import User
import unittest

# User = model.User
# pitch = model.Piches

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("engineer","engineer@gmail.com","12345")
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"engineer")
        self.assertEqual(self.new_user.email,"engineer@gmail.com")
        self.assertEqual(self.new_user.password,"12345")
    
    def test_validate_user(self):
        '''
        test_validate_user to test the password that the user uses to create the account and the password the user uses to login are the same.
        '''
        self.new_user = User("engineer","engineer@gmail.com","12345")
        # new_user = User.validate_user("12345")

        self.assertEqual(User.validate_user("12345"), 1)






       