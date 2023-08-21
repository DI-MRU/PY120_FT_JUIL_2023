# Django Advanced Models

## Course Notes

### Django Signals

#### Set Up

```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
   pass


class UserProfile(models.Model):
   user = models. OneToOneField(User, on_delete=models .CASCADE) # Spacing


   def __str__(self):
       return self.user.username


class Lead (models.Model): # Spacing
   first_name = models. CharField (max_length=20) # Spacing
   last_name = models. Charfield(max_length=20) # Spacing
   age = models. IntegerField (default=0) # Spacing
   agent = models. ForeignKey("Agent", on_delete=models.CASCADE) # Spacing


   def __str__(self):
       return f"{self.first_name} {self. last_name}" # Spacing


class Agent (models.Model): # Spacing
   user = models. OneToOneField (User, on_delete=models. CASCADE) # Spacing
   Organization = models. ForeignKey (UserProfile, on_delete=models.CASCADE) # Spacing


   def __str__(self):
       return self.user.email
```

#### Usage

```python
class UserProfile(models.Model):
   user = models. OneToOneField(User, on_delete=models .CASCADE) # Spacing


   def __str__(self):
       return self.user.username


...


def post_user_created_signal(sender, instance, created, **kwargs):
   print(instance, created)


   if created:
       UserProfile.objects.create(user=instance)
```

### Class Based View #2

#### Set up the POST method

```python
from rest_framework.status import HTTP_200_OK, # Extra comma
HTTP_201_CREATED, HTTP_400_BAD_REQUEST
```
