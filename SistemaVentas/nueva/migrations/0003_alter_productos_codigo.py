# Generated by Django 5.1.3 on 2024-12-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nueva', '0002_marca_alter_productos_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='codigo',
            field=models.PositiveBigIntegerField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]