# Generated by Django 4.1.1 on 2022-09-17 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.BigIntegerField()),
                ("endereco", models.CharField(max_length=255)),
                ("data_de_cadastro", models.DateField()),
                ("faturamento_declarado", models.FileField(upload_to="faturamentos/")),
            ],
            options={"db_table": "cliente",},
        ),
        migrations.CreateModel(
            name="Banco",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("agencia", models.BigIntegerField()),
                ("conta", models.BigIntegerField()),
                ("banco", models.CharField(max_length=255)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="banco",
                        to="cliente.cliente",
                    ),
                ),
            ],
            options={"db_table": "banco",},
        ),
    ]
