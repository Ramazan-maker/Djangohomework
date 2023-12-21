# Generated by Django 4.2.7 on 2023-12-21 12:54

import bboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_alter_bb_options_bb_is_active_bb_kind_bb_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[bboard.models.validate_positive], verbose_name='Цена'),
        ),
    ]
