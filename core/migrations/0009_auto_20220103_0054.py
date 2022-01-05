# Generated by Django 3.2.10 on 2022-01-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220103_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='newuser',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]