# Generated by Django 3.0.2 on 2020-03-24 04:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'House must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('power', models.PositiveIntegerField()),
                ('spell', models.CharField(max_length=300)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizards.House')),
            ],
        ),
    ]
