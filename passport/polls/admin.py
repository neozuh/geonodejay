from django.contrib import admin
from passport.polls.models import *

class PollAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'pub_date')


admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
