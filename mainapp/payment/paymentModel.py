from django.db import models
from mainapp.students.studentModel import student
from mainapp.models import SessionYear




"""Invoice Category Model"""
class invoice_category(models.Model):
    invoice_cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.category_name


"""Expense Category Model"""
class expense_category(models.Model):
    expense_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name




"""Invoice Event Model shows status and payment method"""
class invoice(models.Model):
    status_data = (
        ('paid', 'paid'), 
        ('unpaid', 'unpaid')
    )
    payment_method_data = (
        ('cash', 'cash'),
        ('cheque', 'cheque'),
        ('online', 'online')
    )
    invoice_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    category = models.ForeignKey(invoice_category, on_delete = models.DO_NOTHING, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    creation_timestamp  = models.DateField()
    amount = models.BigIntegerField(null=True, blank=True)
    amount_paid = models.BigIntegerField(null=True, blank=True)
    due = models.BigIntegerField(null=True, blank=True) #In the view create totalamount - amountpaid
    payment_method = models.CharField(max_length=100, choices=payment_method_data, null=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices = status_data)



"""Payment Model"""
class payment(models.Model):
    method_data = (
     ('cash', 'cash'),
    ('cheque', 'cheque'),
    ('online', 'online')
    )
    payment_id = models.AutoField(primary_key=True)
    expense_category = models.ForeignKey( expense_category , on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    payment_type = models.CharField(max_length = 100, default="Income",null=True)
    invoice = models.ForeignKey(invoice, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(student, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=100, choices=method_data, null=True)
    amount = models.BigIntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    session_year = models.ForeignKey(SessionYear, on_delete=models.CASCADE, null=True)
    due_from_inv = models.BigIntegerField(null=True, blank=True)


