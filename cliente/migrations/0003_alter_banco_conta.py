# Generated by Django 4.1.1 on 2022-09-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0002_alter_cliente_email_alter_cliente_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banco", name="conta", field=models.BigIntegerField(unique=True),
        ),
    ]
