# Generated by Django 4.0.5 on 2022-06-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=500)),
                ('compensation', models.IntegerField()),
                ('description', models.TextField()),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
    ]