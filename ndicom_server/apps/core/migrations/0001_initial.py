# Generated by Django 2.0.6 on 2018-06-08 19:46

import apps.core.managers
import apps.core.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surname', models.CharField(max_length=30, verbose_name='Surname')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin?')),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2018, 6, 8, 19, 46, 49, 947801, tzinfo=utc))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', apps.core.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DicomNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('peer_url', models.CharField(max_length=255, verbose_name='Peer URL')),
                ('instances_url', models.CharField(default='/instances', max_length=255, verbose_name='WADO Instances URL')),
                ('instance_file_url', models.CharField(default='/instances/{id}/file', max_length=255, verbose_name='WADO Instance Image URL')),
            ],
            options={
                'db_table': 'dicom_nodes',
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sop_instance_uid', models.CharField(max_length=80, unique=True, verbose_name='SOP Instance UID')),
                ('instance_number', models.IntegerField(verbose_name='Instance Number')),
                ('rows', models.IntegerField(verbose_name='Rows')),
                ('columns', models.IntegerField(verbose_name='Columns')),
                ('color_space', models.CharField(blank=True, max_length=30, null=True, verbose_name='Color Space')),
                ('photometric_interpretation', models.CharField(blank=True, max_length=30, null=True, verbose_name='Photometric Interpretation')),
                ('smallest_image_pixel_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Smallest Image Pixel Value')),
                ('largest_image_pixel_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Largest Image Pixel Value')),
                ('pixel_aspect_ratio', models.CharField(blank=True, max_length=30, null=True, verbose_name='Pixel Aspect Ratio')),
                ('pixel_spacing', models.CharField(blank=True, max_length=30, null=True, verbose_name='Pixel Spacing')),
                ('image', models.FileField(upload_to=apps.core.models.image_file_path)),
            ],
            options={
                'db_table': 'instances',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Patient')),
                ('patient_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Patient ID')),
                ('patient_sex', models.CharField(blank=True, max_length=10, null=True, verbose_name='Patient Sex')),
                ('patient_age', models.CharField(blank=True, max_length=30, null=True, verbose_name='Patient Age')),
                ('patient_birthdate', models.DateField(blank=True, null=True, verbose_name='Patient Birthdate')),
            ],
            options={
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('display_name', models.CharField(default='', max_length=150, verbose_name='Display Name')),
                ('version', models.CharField(max_length=20, verbose_name='Version')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Author')),
                ('info', models.CharField(blank=True, max_length=500, null=True, verbose_name='Information')),
                ('docs', models.TextField(blank=True, max_length=500, null=True, verbose_name='Documentation')),
                ('modalities', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Modalities')),
                ('tags', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Tags')),
                ('params', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Parameters')),
                ('result', jsonfield.fields.JSONField(verbose_name='Result')),
                ('type', models.CharField(default='ANALYZER', max_length=40, verbose_name='Type')),
                ('plugin', models.FileField(blank=True, null=True, upload_to=apps.core.models.plugin_file_path)),
                ('is_installed', models.BooleanField(default=False, verbose_name='Is installed')),
            ],
            options={
                'db_table': 'plugins',
            },
        ),
        migrations.CreateModel(
            name='ProcessingResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_date', models.DateTimeField()),
                ('image', models.FileField(blank=True, null=True, upload_to=apps.core.models.processed_image_path, verbose_name='Image')),
                ('json', jsonfield.fields.JSONField(verbose_name='JSON')),
                ('session_token', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'processing_results',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_instance_uid', models.CharField(max_length=80, unique=True, verbose_name='Series Instance UID')),
                ('protocol_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Protocol Name')),
                ('modality', models.CharField(max_length=80, verbose_name='Modality')),
                ('series_number', models.CharField(blank=True, max_length=80, null=True, verbose_name='Series Number')),
                ('patient_position', models.CharField(max_length=30, verbose_name='Patient Position')),
                ('body_part_examined', models.CharField(blank=True, max_length=50, null=True, verbose_name='Body Part Examined')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
                'db_table': 'series',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_instance_uid', models.CharField(max_length=80, unique=True, verbose_name='Study Instance UID')),
                ('study_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Study ID')),
                ('study_date', models.DateField(blank=True, null=True, verbose_name='Study Date')),
                ('study_description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Study Description')),
                ('referring_physician_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Referring Physician')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='core.Patient')),
            ],
            options={
                'verbose_name_plural': 'Studies',
                'db_table': 'studies',
            },
        ),
        migrations.AddField(
            model_name='series',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='core.Study'),
        ),
        migrations.AddField(
            model_name='instance',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='core.Series'),
        ),
    ]
