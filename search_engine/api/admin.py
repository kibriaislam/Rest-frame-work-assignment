from django.contrib import admin
from .models import SearchEngineUser,SearchHistory

# Register your models here.
admin.site.register(SearchEngineUser)

admin.site.register(SearchHistory)