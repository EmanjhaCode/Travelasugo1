# Generated by Django 2.2.4 on 2021-07-19 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emanjha_admin', '0015_facilities_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guideline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=20)),
                ('guide', models.CharField(max_length=150)),
                ('img', models.FileField(default='', upload_to='Guideline_img')),
                ('img_status', models.CharField(choices=[('Active Image', 'active'), ('Block Image', 'block')], default='block', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Guideline_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_detail1', models.CharField(max_length=350)),
                ('img1', models.FileField(default='', upload_to='guideline_detail1')),
                ('guide_detail2', models.CharField(max_length=350)),
                ('img2', models.FileField(default='', upload_to='guideline_detail2')),
                ('guide_detail3', models.CharField(max_length=350)),
                ('img3', models.FileField(default='', upload_to='guideline_detail3')),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emanjha_admin.Guideline')),
            ],
        ),
    ]