# Generated by Django 4.2.4 on 2023-08-30 20:32

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('seats', models.IntegerField(default=0, verbose_name='nombre de places')),
            ],
            options={
                'verbose_name': 'Chauffeur',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Groupe de coureurs',
                'verbose_name_plural': 'Groupes de coureurs',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('gpx', models.FileField(upload_to='gpx/', verbose_name='fichier GPX')),
            ],
            options={
                'verbose_name': 'Tronçon',
            },
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('progress', models.FloatField(default=0.0, verbose_name='avancement')),
                ('medical_certificate', models.FileField(blank=True, null=True, upload_to='certificates/', verbose_name='certificat médical')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runners', to='course_drapeau.group')),
            ],
            options={
                'verbose_name': 'Coureur',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='sections',
            field=models.ManyToManyField(blank=True, to='course_drapeau.section', verbose_name='tronçons'),
        ),
    ]
