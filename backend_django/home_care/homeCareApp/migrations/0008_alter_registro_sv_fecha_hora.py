# Generated by Django 4.1.1 on 2022-09-16 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeCareApp', '0007_alter_registro_sv_fecha_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_sv',
            name='Fecha_Hora',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 3, 16, 57, 525025, tzinfo=datetime.timezone.utc)),
        ),
    ]
