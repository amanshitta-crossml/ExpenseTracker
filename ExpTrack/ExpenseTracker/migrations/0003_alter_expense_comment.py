# Generated by Django 3.2.6 on 2021-08-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseTracker', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='comment',
            field=models.TextField(max_length=300, null=True),
        ),
    ]