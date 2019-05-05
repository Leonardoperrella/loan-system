from django.db import models
from django.utils import timezone


# Create your models here.

class Loan(models.Model):
    amount = models.DecimalField(max_digits=1000000000, decimal_places=2)
    term = models.IntegerField()
    rate = models.DecimalField(max_digits=100, decimal_places=2)
    data_initial = models.DateTimeField(default=timezone.now)

    @property
    def installment(self):
        r = self.rate / 12
        installment = (r + r / ((1 + r) ** self.term - 1)) * self.amount
        return installment
    '''
    @property
    def balance(self, date):
        return installment * [ for n in  amount]
    '''

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=6, choices=(('missed','Missed'),('made','Made')))
    date = models.DateTimeField(default=timezone.now)


