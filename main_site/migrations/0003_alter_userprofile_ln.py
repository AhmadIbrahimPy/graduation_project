# Generated by Django 4.0.3 on 2022-03-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_userprofile_ln'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ln',
            field=models.CharField(blank=True, default='ar', max_length=5, null=True),
        ),
    ]