# Generated by Django 4.2.1 on 2023-05-31 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_m7', '0007_pedido_id_detalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='id_detalle',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core_m7.detalle', verbose_name='Detalle'),
        ),
    ]
