from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    
    def test_completed_item_str_is_name_and_done(self):
        item = Item(name='Write Tests', done=True)
        self.assertEqual(str(item), 'Write Tests (done)')

    def test_uncompleted_item_str_is_name_and_not_done(self):
        item = Item(name='Write Tests', done=False)
        self.assertEqual(str(item), 'Write Tests (not done)')
