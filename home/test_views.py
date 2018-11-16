from django.test import TestCase
from .models import Item

# Create your tests here.
class TestHome(TestCase):
    
    def setUp(self):
        Item.objects.create(name="Get Bread", done=False)
        Item.objects.create(name="Get Milk", done=True)


    def test_root_is_valid_url(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        
        
    def test_root_uses_index_template(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, 'home/index.html')
        
        
    # Create Item 
    def test_get_create_item(self):
        resp = self.client.get("/add/")
        self.assertEqual(resp.status_code, 200)
         
         
    def test_post_create_item(self):
        resp = self.client.post("/add/", {'name': 'Create an Item'})
        self.assertEqual(resp.status_code, 302)
        item = Item.objects.latest('id')
        self.assertEqual(item.name, 'Create an Item')
        

    # def test_post_create_item_invalid_form(self):
    #     resp = self.client.post("/add/", {})
    #     self.assertEqual(resp.status_code, 200)
    #     item = Item.objects.latest('id')
    #     self.assertEqual(item.name, 'Write Test')


    # Edit Item    
    def test_get_edit_item_does_not_exist(self):
        resp = self.client.get("/edit/99")
        self.assertEqual(resp.status_code, 404)


    def test_post_edit_item_does_not_exist(self):
        resp = self.client.post("/edit/99", {'name': 'Edit Test'})
        self.assertEqual(resp.status_code, 404)
    
    
    def test_get_edit_item_that_exists(self):
        item=Item(name="Write Test", done = True)
        item.save()
        
        url = "/edit/{0}".format(item.id)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        
        
    def test_post_edit_item_that_exists(self):
        item=Item(name="Write Test", done = True)
        item.save()

        url = "/edit/{0}".format(item.id)
        resp = self.client.post(url, {'name': 'Edit Test'})
        self.assertEqual(resp.status_code, 302)

        item = Item.objects.get(pk=item.id)
        self.assertEqual(item.name, 'Edit Test')
        
        
    # Toggle Item
    def test_post_toggle_item_that_exists(self):
        item=Item.objects.get(pk=1)
        self.assertFalse(item.done)

        url = "/toggle/{0}".format(item.id)
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)

        item=Item.objects.get(pk=1)
        self.assertTrue(item.done)


    def test_post_toggle_item_that_does_not_exist(self):
        url = "/toggle/99")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 404)
