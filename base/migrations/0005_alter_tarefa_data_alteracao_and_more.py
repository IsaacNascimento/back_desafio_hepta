# Generated by Django 4.0.6 on 2022-09-14 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_contato_data_alteracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_alteracao',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]