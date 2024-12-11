# Generated by Django 5.1.3 on 2024-12-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nueva1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='metodo_pago',
            field=models.CharField(choices=[('EFECTIVO', 'EFECTIVO'), ('TARJETA', 'TARJETA'), ('TRANSFERENCIA', 'TRANSFERENCIA')], default='EFECTIVO', max_length=100, verbose_name='Método de Pago'),
        ),
        migrations.DeleteModel(
            name='MetodoPago',
        ),
    ]
