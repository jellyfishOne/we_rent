# Generated by Django 2.0.4 on 2018-04-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20180411_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]