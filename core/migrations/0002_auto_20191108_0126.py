# Generated by Django 2.2.6 on 2019-11-08 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type', models.CharField(default='unknown', max_length=200)),
                ('profile_picture', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('breed', models.CharField(default='unknown', max_length=200)),
                ('color', models.CharField(default='unknown', max_length=200)),
                ('age', models.IntegerField()),
                ('euth_date', models.DateField()),
                ('id_number', models.CharField(default='unknown', max_length=200)),
                ('current_pledges', models.IntegerField()),
                ('goal', models.IntegerField()),
                ('neutered_spayed', models.BooleanField()),
                ('name', models.CharField(default='unknown', max_length=200)),
                ('description', models.TextField()),
                ('hw', models.BooleanField()),
                ('surrender_reason', models.CharField(default='unknown', max_length=200)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='location_gps_latitude',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='location_gps_longitude',
        ),
        migrations.AddField(
            model_name='shelter',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=100),
        ),
        migrations.AddField(
            model_name='shelter',
            name='phone',
            field=models.CharField(default='555-555-5555', max_length=200),
        ),
        migrations.AddField(
            model_name='shelter',
            name='primary_contact',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='shelter',
            name='website',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='address',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.DeleteModel(
            name='Animals',
        ),
        migrations.AddField(
            model_name='animal',
            name='current_shelter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Shelter'),
        ),
    ]
