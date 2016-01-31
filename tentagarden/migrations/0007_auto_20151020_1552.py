# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tentagarden', '0006_auto_20151020_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.OneToOneField(related_name=b'+', to=settings.AUTH_USER_MODEL),
        ),
    ]
