# Generated by Django 4.1.1 on 2022-09-15 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeCareApp', '0003_alter_medico_id_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_sv',
            name='Paciente_ID_PACIENTE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeCareApp.paciente'),
        ),
    ]