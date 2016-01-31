# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tentagarden', '0004_auto_20151020_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.ForeignKey(related_name=b'+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
