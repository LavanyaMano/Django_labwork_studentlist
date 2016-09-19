from django.test import TestCase
from django.core.urlresolvers import reverse



class StudentViewTests(TestCase):
    
    def test_view_index(self):
        index_url = reverse('student_app:index')
        response = self.client.get(index_url)
        self.assertEqual(response.status_code,200)