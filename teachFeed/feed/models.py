from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
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

class Feed(models.Model):
    sno = models.AutoField(primary_key=True)
    branch = models.CharField(
        max_length=100,
        help_text='Enter a Department (e.g. IT)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    depTeach = models.CharField(
        max_length=100,
        help_text='Enter a Department (e.g. IT)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    teacherName = models.CharField(
        max_length=100,
        help_text='Enter a Teacher\'s name',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    sem = models.IntegerField(help_text='Sem of student (e.g. 1')
    subject = models.CharField(
        max_length=100,
        help_text='Enter a Subject (e.g. DSA)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    interact = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    softSkill = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    notes = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    ans = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    pInteract = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    quality = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    extra = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    assignment = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    interrupt = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    mst = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    lecture = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    mooc = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)],help_text='1-10')
    virtualLab = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    curriculum = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')
    topic = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], help_text='1-10')

    def __str__(self):
        x=str(self.sno)
        return x
