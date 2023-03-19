# Create your model tests here.# 
from django.test import TestCase
from .models import Idea, FootNote

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

