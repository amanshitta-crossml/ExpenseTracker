# Generated by Django 3.2.6 on 2021-08-23 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=72)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('TR', 'Travel'), ('ED', 'Education'), ('GD', 'Gifts & Donations'), ('INV', 'Investments'), ('BLNU', 'Bills & Utilities'), ('FD', 'Food & Dining'), ('HF', 'Health & Fitness'), ('PC', 'Personal Care'), ('FC', 'Fees & Charges'), ('OT', 'Others')], default='OT', max_length=70)),
                ('spent', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateTimeField()),
                ('comment', models.TextField(max_length=300)),
                ('user', models.ManyToManyField(to='ExpenseTracker.User')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpenseTracker.user')),
            ],
        ),
    ]
