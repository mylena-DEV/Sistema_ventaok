# Generated by Django 5.1.3 on 2024-12-06 21:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nueva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='el campo solo debe contener letras y espacios', regex='^[a-zA-Z\\s]+$')])),
            ],
        ),
        migrations.AlterField(
            model_name='productos',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nueva.marca'),
        ),
    ]