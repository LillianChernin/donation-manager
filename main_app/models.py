from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_org_admin = models.BooleanField(default=False)

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email_address = models.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()

class ReliefEffort(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    org_admin_id = models.ForeignKey(User,
    models.SET_NULL,
    blank=True,
    null=True)
    def __str__(self):
	    return self.name

class Need(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    relief_effort_id = models.ForeignKey(ReliefEffort,
    on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Donation(models.Model):
    need_id = models.ForeignKey(Need,
    models.SET_NULL,
    blank=True,
    null=True)
    donor_id = models.ForeignKey(Donor,
    models.SET_NULL,
    blank=True,
    null=True)
    created_at = models.DateTimeField(auto_now_add=True)
