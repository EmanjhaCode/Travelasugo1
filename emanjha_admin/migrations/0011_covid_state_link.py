# Generated by Django 2.2.4 on 2020-12-21 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emanjha_admin', '0010_auto_20200702_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid_state_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('usa_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emanjha_admin.Usa_state')),
            ],
        ),
    ]
