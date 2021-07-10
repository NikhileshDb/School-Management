from django.db import models
from django.contrib.auth.models import AbstractUser

#Overriding Default USER
class CustomUser(AbstractUser):
    data = (
        (1,"Principal"), (2, "Teachers"), (3, "Students")
    )
    user_type = models.CharField(default=1, choices=data, max_length=10)



class Principal(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    objects = models.Manager()
 

class Teachers(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Teachers"


    def __str__(self):
        return self.name

        


class Students(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    # firstName = models.CharField(max_length=40, null=True, blank=True)
    middleName = models.CharField(max_length=40)
    # lastName = models.CharField(max_length=40)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=20)
    fatherName= models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    current_address = models.CharField(max_length=200)
    parmanent_address = models.CharField(max_length=200)
    religion = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=13)
    nationality = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,)
    blood_group = models.CharField(max_length=5)
    classRoom = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=2, null=True, blank=True)
    objects = models.Manager()
    