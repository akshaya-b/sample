# Generated by Django 2.2.6 on 2019-10-25 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kingdoms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingdom',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='kingdom', to='kingdoms.Region'),
        ),
    ]