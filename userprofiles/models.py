from django.db import models

from django.contrib.auth.models import User

from locales.models import Store, Puesto


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    store = models.ForeignKey(Store)
    puesto = models.ForeignKey(Puesto)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
