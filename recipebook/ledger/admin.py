from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    can_delete = False


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    readonly_fields = ('created_on', 'updated_on')


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
