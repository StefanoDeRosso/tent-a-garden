# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tentagarden', '0005_userprofile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.OneToOneField(related_name=b'+', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
