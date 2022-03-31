from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Access(models.Model):
    sno = models.AutoField(primary_key=True)
    department = models.CharField(
            max_length=100,
            help_text='Enter a Department (e.g. IT)',
            validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    accesscd = models.CharField(max_length=100)

    def __str__(self):
        return self.department
