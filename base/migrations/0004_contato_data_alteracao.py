# Generated by Django 4.0.6 on 2022-09-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_tarefa_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='data_alteracao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]