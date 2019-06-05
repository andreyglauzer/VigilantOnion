from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *


class NameCategories_Admin(admin.ModelAdmin):
    list_display = (
        'categorie',
    )
    model = NameCategories
    can_delete = False


class Source_Admin(admin.ModelAdmin):
    list_display = (
        'source',
    )
    model = Source
    can_delete = False

class Categories_Admin(admin.ModelAdmin):
    list_display = (
        'categorie',
        'term',
    )
    model = Categories
    can_delete = False

class CompanyName_Admin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    model = CompanyName
    can_delete = False

class CompanyTerm_Admin(admin.ModelAdmin):
    list_display = (
        'name',
        'term',
    )
    model = CompanyTerm
    can_delete = False

class MoreURLS_Admin(admin.ModelAdmin):
    list_display = (
        'url_more',
    )

    model = MoreURLS
    can_delete = False

class UrlOnion_Admin(admin.ModelAdmin):
    list_display = (
        'source',
        'url',
        'status',
        'created_in',
        'last_date',
        'categorie',

    )
    model = UrlOnion
    can_delete = False

class CustomUser_Admin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'name',
        'is_staff',
        'datejoined',
    )
    model = CustomUser
    can_delete = False

admin.site.register(CustomUser, CustomUser_Admin)
admin.site.register(NameCategories, NameCategories_Admin)
admin.site.register(Categories, Categories_Admin)
admin.site.register(CompanyName, CompanyName_Admin)
admin.site.register(CompanyTerm, CompanyTerm_Admin)
admin.site.register(UrlOnion, UrlOnion_Admin)
admin.site.register(Source, Source_Admin)
admin.site.register(MoreURLS, MoreURLS_Admin)
