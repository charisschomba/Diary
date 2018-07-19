import unittest
from . import create_app
from app.Models.entries import Entry

class TestModels(unittest.TestCase):
    """
    This class contains different tests
    to test models of the app.
    """
    def setUp(self):
        app = create_app('testing')
        self.tester = app.test_client(self)
        self.test_data = {
                    "id":1,
                     "date":"18-7-2018",
                     "title":"coding",
                     "content":"Andela challenge two"}
        self.test_data2 = {
                    "id":2,
                     "date":"23-7-2018",
                     "title":"Bootcamp",
                     "content":"Bootcamp day one"}
        self.updated_data = {'title':'python','content':'Am learning python'}
        self.db = Entry()
        self.db.save(self.test_data)
        self.db.save(self.test_data2)

    def tearDown(self):
        self.db.clear_all()

# tests whether this model saves an entry to db
    def test_save_entry(self):
        self.assertIn("Andela challenge two",str(self.db))
        self.assertIn('Bootcamp',str(self.db))

 # Tests whether get_by_id() filters entries by id correctly
    def test_get_by_id(self):
        self.db.save(self.test_data2)
        self.assertIn('Bootcamp day one',str(self.db.get_by_id(2)))

# tests whether this model deletes an entry to db
    def test_delete_entry(self):
        self.db.delete_entry(self.test_data2)
        self.assertEquals(1,len(self.db))

# tests whether this model update an entry given its id.
    def test_update_entry(self):
        self.db.update_entry(self.updated_data,1)
        self.assertTrue('python',self.db)
        self.assertIn('Am learning python',str(self.db))

# Tests whether this model gets entries from db
    def test_get_entries(self):
        self.assertEquals(2,len(self.db))

# Tests whether this model gets entries from db
    def test_clear_all(self):
        self.db.clear_all()
        self.assertEquals(0,len(self.db))
# This class contains test for testing magic methods
class TestsMagicMethods(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        self.tester = app.test_client(self)
        self.test_data = {
                    "id":1,
                     "date":"18-7-2018",
                     "title":"coding",
                     "content":"Andela challenge two"}
        self.test_data2 = {
                    "id":2,
                     "date":"23-7-2018",
                     "title":"Bootcamp",
                     "content":"Bootcamp day one"}
        self.db = Entry()
        self.db.save(self.test_data)
        self.db.save(self.test_data2)
    def tearDown(self):
        self.db.clear_all()

# Tests whether dunder __str__ method returns an object as a string
    def test__str__returns_str(self):
       self.assertTrue('[]',self.db)

# Tests whether dunder __len__ method returns length of an object
    def test__len__returns_length(self):
        self.assertEquals(2,len(self.db))

#Tests whether dunder __getitem__ method indexes objects
    def test__getitem__permits_indexing(self):
        self.assertEquals(2,(self.db[1]["id"]))
        self.assertEquals(1,(self.db[0]["id"]))
        self.assertNotEqual(2,(self.db[0]["id"]))
