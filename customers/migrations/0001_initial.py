# Generated by Django 5.1.2 on 2024-10-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'customer_table',
            },
        ),
    ]
