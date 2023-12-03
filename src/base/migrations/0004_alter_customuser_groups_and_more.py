# Generated by Django 4.2.5 on 2023-12-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0028_alter_user_logo'),
        ('base', '0003_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, to='auth.permission'),
        ),
    ]
