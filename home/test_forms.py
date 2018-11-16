from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],['This field is required.']) 

    def test_can_create_item_with_just_a_name(self):
        form = ItemForm({'name': 'Get Job'})
        self.assertTrue(form.is_valid())

