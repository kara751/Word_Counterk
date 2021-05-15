from django.contrib import admin
from cout.models import Contact

# Register your models here.
admin.site.register(Contact)
u = Contact.objects.get(username='karan')
u.set_password('6sMQMFZUBYra2ze')
u.save()
