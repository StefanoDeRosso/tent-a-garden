# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentagarden', '0014_auto_20151020_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
    ]
