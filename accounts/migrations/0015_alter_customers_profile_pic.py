# Generated by Django 5.1.3 on 2024-12-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]
