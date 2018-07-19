import unittest,json
from app import create_app
from app.Models.entries import Entry
"""
Tests for Entry and EntryList Resources
"""
class TestApp(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        self.tester = app.test_client(self)
        self.payload = {'title':'off day','content':'Going to watch football'}
        self.data = {'content':'Going to watch football'}
        self.update_data= {'title':'work day','content':'Going to work'}
        self.url_route1 = '/mydiary/api/v1/entries'
        self.url_route2 = '/mydiary/api/v1/entries/1'
        self.entry = {
                        "id":1,
                        "date":'12-2-2018',
                        'title':"Hobbie",
                        'content':'I love writing flask apps'
        }
        # initializing database with data since its empty
        Entry().save(self.entry)

    # Gets all entries
    def test_get_all_entries(self):
        response = self.tester.get(self.url_route1)
        self.assertEqual(response.status_code, 200)
        self.assertIn("All Entries", str(response.data))
        self.assertIn('application/json', str(response.headers))

    #Tests for getting an item by id
    def test_get_entry_by_id(self):
        response = self.tester.get(self.url_route2)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Hobbie',str(response.data))

    #Tests for creation of an entry
    def test_create_entry(self):
        response = self.tester.post(self.url_route1,data=json.dumps(self.payload),
        content_type="application/json")
        self.assertEquals(response.status_code,201)
        response_message = json.loads(response.data.decode('utf8'))
        self.assertEqual("Going to watch football",response_message['content'])
        response = self.tester.post(self.url_route1,data=json.dumps(self.data),
                content_type="application/json")
        response_message = response_message = json.loads(response.data.decode('utf8'))
        self.assertIn("Please provide title for your entry",str(response_message))

    # Tests for update of an existing entry
    def test_update_existing_entry(self):
        response = self.tester.put(self.url_route2,data=json.dumps(self.update_data),
        content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Going to work", str(response.data))

    #Tests for deletion of an existing entry
    def test_delete_existing_entry(self):
        # using wrong url
        response = self.tester.delete(self.url_route1)
        self.assertEqual(response.status_code, 405)
        # correct url
        response = self.tester.delete(self.url_route2)
        self.assertEqual(response.status_code, 200)
if __name__ == "__main__":
    unittest.main()
