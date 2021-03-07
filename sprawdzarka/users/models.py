from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    term = models.CharField(max_length=4)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name + '_' + self.year.replace('/','_') + '_' + self.term

    @property
    def group(self):
        return self.name + '_' + self.year.replace('/','_') + '_' + self.term

    @property
    def str_id(self):
        return str(self.id)
        

class MyAccountManager(BaseUserManager):
    def create_user(self, username, password, snumber):
        if not snumber:
            raise ValueError("Numer indexu musi zostać podany!")
        if not username:
            raise ValueError("username nie może byc pusty")
        user = self.model(
            snumber = snumber,
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, username, password, snumber = 111111):
        user = self.create_user(
            snumber = snumber,
            username = username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    snumber = models.CharField(verbose_name="Numer indeksu", unique=True, primary_key=True, max_length=6)
    username = models.CharField(verbose_name="Login", unique=True,max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_username = models.DateTimeField(verbose_name='last username', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    group_id = models.CharField(verbose_name='Grupa', max_length=100, default = '0')
    points = models.IntegerField(default=0)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['snumber']

    objects = MyAccountManager()

    def __str__(self):
        return self.snumber

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
