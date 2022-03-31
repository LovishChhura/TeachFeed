from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Department(models.Model):
    sno = models.AutoField(primary_key=True)
    department = models.CharField(
            max_length=100,
            help_text='Enter a Department (e.g. IT)',
            validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        return self.department

class Teacher(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        help_text='Enter a name of Teacher',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        help_text='Enter a name of Subject (e.g. DSA)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, help_text='Teacher teaching this subject')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=False, help_text='Department under which this subject comes')

    def __str__(self):
        return self.name