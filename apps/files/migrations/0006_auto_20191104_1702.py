# Generated by Django 2.2.3 on 2019-11-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20191028_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(blank=True, max_length=300, verbose_name='公用电脑ip')),
            ],
            options={
                'verbose_name': '公用电脑ip',
                'verbose_name_plural': '公用电脑ip',
            },
        ),
        migrations.DeleteModel(
            name='WhiteList',
        ),
    ]