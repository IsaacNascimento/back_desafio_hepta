# Generated by Django 4.0.6 on 2022-09-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_contato_tarefa_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='ativo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
