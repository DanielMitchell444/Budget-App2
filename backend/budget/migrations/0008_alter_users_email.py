# Generated by Django 5.1.2 on 2024-10-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Email',
            field=models.EmailField(default='', max_length=15),
        ),
    ]
