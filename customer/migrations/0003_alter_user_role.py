# Generated by Django 3.2.5 on 2023-06-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Customer'), (2, 'Merchant')], null=True),
        ),
    ]