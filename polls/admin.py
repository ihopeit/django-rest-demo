from django.contrib import admin

# Register your models here.
from polls.models import Question

admin.site.register(Question)

#generate tokens for old users:
#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token

#for user in User.objects.all():
#    Token.objects.get_or_create(user=user)
