from django.test import TestCase
from calculator.models import Loan

# Create your tests here.

class LoanModelTest(TestCase):
    def setUp(self):
        Loan.objects.create(
        loan_id = '1',
        amount = 1000,
        term = 12,
        rate = 0.05,
        data_initial = "2019-05-09T03:18:00Z"
        )    
    def test_create(self):
        self.assertTrue(Loan.objects.exists())

