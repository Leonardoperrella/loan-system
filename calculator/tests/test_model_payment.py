from django.test import TestCase
from calculator.models import Payment

# Create your tests here.

class PaymentModelTest(TestCase):
    
    def setUp(self):
        Payment.objects.create(
        status = 'missed',
        loan_id = '1',
        date = "2019-05-09T03:18:00Z"
        )    
    def test_create(self):
        self.assertTrue(Payment.objects.exists())        

