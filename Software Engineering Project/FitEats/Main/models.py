from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models

ACTIVITY_FACTORS = [
    ('S', 'Sedentary'),
    ('L', 'Lightly Active'),
    ('M', 'Moderately Active'),
    ('V', 'Very Active'),
    ('E', 'Extremely Active'),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    age = models.PositiveIntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    gender = models.CharField(null=True,max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    activity_factor = models.CharField(max_length=20, choices=ACTIVITY_FACTORS)
    tdee = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    fat_percentage = models.FloatField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    

    def calculate_tdee(self):
        if self.weight and self.height and self.age:
            if self.gender == 'M':
                bmr = 88.36 + (13.4 * self.weight) + (4.8 * self.height) - (5.7 * self.age)
            else:
                bmr = 447.6 + (9.2 * self.weight) + (3.1 * self.height) - (4.3 * self.age)

            if self.activity_factor == 'S':
                af = 1.2
            elif self.activity_factor == 'L':
                af = 1.375
            elif self.activity_factor == 'M':
                af = 1.55
            elif self.activity_factor == 'V':
                af = 1.725
            else:
                af = 1.9

            self.tdee = round(bmr * af, 2)

    def calculate_bmi(self):
        if self.weight and self.height:
            self.bmi = round(self.weight / ((self.height / 100) ** 2), 2)



    def save(self, *args, **kwargs):
        self.calculate_tdee()
        self.calculate_bmi()
        super().save(*args, **kwargs)
    
        
    