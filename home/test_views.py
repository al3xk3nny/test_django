from django.test import TestCase
from .models import Item

# Create your tests here.

class TestHome(TestCase):
    # Test to see if url is valid - i.e. returns 200.
    def test_root_is_valid_url(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    #  Test to see if page used is "index.html"
    def test_root_uses_index_template(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, "home/index.html")

    # Test to see if form is served to a vaid url.
    def test_get_create_item(self):
        resp = self.client.get("/add/")
        self.assertEqual(resp.status_code, 200)

    
    def test_post_create_item(self):
        resp = self.client.post("/add/", {"name": "Write Test"})
        self.assertEqual(resp.status_code, 302)


    def test_get_edit_item_that_does_not_exist(self):
        resp = self.client.get("/edit/1")
        self.assertEqual(resp.status_code, 404)


    def test_post_edit_item_that_does_not_exist(self):
        resp = self.client.post("/edit/1", {"name": "Edit Test"})
        self.assertEqual(resp.status_code, 404)

    # Create item within a function and run a test.
    def test_get_edit_item_that_exists(self):
        item=Item(name = "Write Test", done = True)
        item.save()
        
        url = "/edit/{0}".format(item.id)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)