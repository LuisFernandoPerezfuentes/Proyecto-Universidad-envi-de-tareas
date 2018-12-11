# Generated by Django 2.1.3 on 2018-12-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademica', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='curso',
            new_name='Curso',
        ),
        migrations.AddField(
            model_name='alumno',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='My_Folder/'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='DNI',
            field=models.CharField(max_length=10),
        ),
    ]