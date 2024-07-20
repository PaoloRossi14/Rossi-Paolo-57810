# Generated by Django 5.0.7 on 2024-07-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0003_profesores_delete_productos_rename_edad_compras_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='compras',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='compras',
            name='size',
            field=models.CharField(max_length=50),
        ),
    ]