from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_org_admin = models.BooleanField(default=False)
    email_address = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=100)


class OrgAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    org_name = models.CharField(max_length=100)
    org_location = models.CharField(max_length=100)
    org_bio = models.CharField(max_length=300)


class ReliefEffort(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    org_admin_id = models.ForeignKey(OrgAdmin,
    models.SET_NULL,
    blank=True,
    null=True)
    def __str__(self):
	    return self.name

class ItemRequest(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=100)
    is_fulfilled = models.BooleanField(default=False)
    relief_effort_id = models.ForeignKey(ReliefEffort,
    on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Donation(models.Model):
    item_request_id = models.ForeignKey(ItemRequest,
    models.SET_NULL,
    blank=True,
    null=True)
    donor_id = models.ForeignKey(Donor,
    models.SET_NULL,
    blank=True,
    null=True)
    created_at = models.DateTimeField(auto_now_add=True)
