'''
Sample tests
docker-compose run --rm app sh -c "python manage.py test"
''' 
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    
    def test_add_numbers(self):
        res= calc.add(5,6)
        self.assertEqual(res,11)
        
    def test_subtract_numbers(self):
        rest = calc.substract (10,15)
        self.assertEqual(rest,5)
        
    