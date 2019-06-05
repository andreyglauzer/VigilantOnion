import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class NameCategories(models.Model):
    categorie = models.CharField(
        'Categorie',
        max_length=100
    )

    def __str__(self):
        return self.categorie

    class Meta:
        verbose_name = 'Categorie Name'
        verbose_name_plural = 'Categories Names'

class Categories(models.Model):
    categorie = models.ForeignKey(
        NameCategories,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    term = models.CharField(
        'Term',
        max_length=100
    )

    def __str__(self):
        return self.term

    class Meta:
        verbose_name = 'Categorie Term'
        verbose_name_plural = 'Categories Terms'


class CompanyName(models.Model):
    name = models.CharField(
        'Name',
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company Name'
        verbose_name_plural = 'Company Names'


class CompanyTerm(models.Model):
    name = models.ForeignKey(
        CompanyName,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    term = models.CharField(
        'Term',
        max_length=100
    )

    def __str__(self):
        return self.term

    class Meta:
        verbose_name = 'Company Term'
        verbose_name_plural = 'Company Terms'



class Source(models.Model):
    source = models.CharField(
        'source',
        max_length=100
    )

    def __str__(self):
        return self.source

    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'


class MoreURLS(models.Model):

    url_more = models.CharField(
        'More URL',
        max_length=1000,
        null=True,
    )

    status_more = models.BooleanField(
        'Status',
        blank=True,
        default=False,
        null=True
    )

    def __str__(self):
        return self.url_more

    class Meta:
        verbose_name = 'More Url'
        verbose_name_plural = 'More Url'


class UrlOnion(models.Model):
    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    url = models.CharField(
        'URL',
        max_length=1000,
        null=True,
    )

    more = models.ManyToManyField(
        MoreURLS,
        related_name='MoreURLS',
        blank=True
    )

    status = models.BooleanField(
        'Status',
        blank=True,
        default=False,
        null=True
    )

    created_in = models.DateTimeField(
        'Registration Date',
        auto_now_add=True,
        blank=True,
        null=True
    )

    last_date = models.DateTimeField(
        'Last Date',
        blank=True,
        null=True
    )

    categorie = models.ForeignKey(
        NameCategories,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    company = models.ManyToManyField(
        CompanyTerm,
        related_name='company_url',
        blank=True
    )


    cover = models.ImageField(
        upload_to='sites/cover',
        help_text='Printscreen of the site.',
        verbose_name='cover',
        null=True,
        blank=True,
        default=False
    )
    


    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'



class CustomUser(AbstractBaseUser, PermissionsMixin, models.Model):
    username = models.CharField(
        'User Name',
    	max_length=30,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'The username can only contain letters, digits or the '
                'following characters: @/./+/-/_', 'Invalid'
            )
        ]
    )
    email = models.EmailField(
        'E-mail',
        unique=True
    )
    name = models.CharField(
        'Name',
        max_length=100,
        blank=True
    )
    is_staff = models.BooleanField(
        'Is Staff',
        blank=True,
        default=True
    )

    datejoined = models.DateTimeField(
        'Registration Date',
        auto_now_add=True
    )
    telephone = models.CharField(
    	'Telephone',
        null=True,
        blank=True,
        max_length=17,

    )
    cellphone = models.CharField(
    	'Cellphone',
    	max_length=17,
    	null=True,
        blank=True,
    )

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
