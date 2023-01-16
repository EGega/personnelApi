from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
  name = models.CharField(max_length=50)
  # def personnel_count(self):
  #   return self.personnel.count()
  def __str__(self):
    return self.name

# class Personnel(models.Model):
#   first_name = models.CharField(max_length=50 )
#   last_name = models.CharField(max_length=50)
#   # title
#   is_staffed = models.BooleanField(default=False)

#   MALE = 'Male'
#   FEMALE = 'Female'
#   OTHER = 'Other'
#   PREFERNOTTOSAY = 'Prefer not to say'
#   YEAR_IN_SCHOOL_CHOICES = [
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#         (OTHER, 'Other'),
#         (PREFERNOTTOSAY, 'Prefer Not to Say'),
#     ]
#   gender = models.CharField(
#         max_length=17,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default= MALE
#     )
#   TEAMLEAD = 'Team Lead'
#   MIDLEAD = 'Mid Lead'
#   JUNIOR = 'Junior'
#   WORK_TITLE = [
#         (TEAMLEAD, 'Team lead'),
#         (MIDLEAD, 'Mid Lead'),
#         (JUNIOR, 'Junior'),
#     ]
#   title = models.CharField(
#     max_length=9,
#     choices=WORK_TITLE,
#     default=JUNIOR
#   )
#   created_date = models.DateTimeField(auto_now_add=True)
#   department = models.ForeignKey(Department, null=True, related_name='personnel', on_delete=models.CASCADE)  
#   def __str__(self):
#     return f'{self.first_name} {self.last_name} ID: {self.id}'
  


TITLE = (
        ("Team Lead", "LEAD"),
        ("Mid Lead", "MID"),
        ("Junior", "JUN"),
)

GENDER = (
    ("Female", "F"),
    ("Male", "M"),
    ("Other", "O"),
    ("Prefer Not Say", "N"),
)

class Personnel(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='personnel')
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, choices=TITLE)
    gender = models.CharField(max_length=50, choices=GENDER)
    salary = models.IntegerField(default=1250)
    start_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} : {self.first_name}"