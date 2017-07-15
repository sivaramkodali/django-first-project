from django.contrib import admin
from first_app.models import accessrecord,topic,webpage,db_users,UserProfileInfo

# Register your models here.

admin.site.register(accessrecord)
admin.site.register(topic)
admin.site.register(webpage)
admin.site.register(db_users)

admin.site.register(UserProfileInfo)
