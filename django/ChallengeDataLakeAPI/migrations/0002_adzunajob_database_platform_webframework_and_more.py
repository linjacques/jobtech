# Generated by Django 5.2.3 on 2025-07-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChallengeDataLakeAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdzunaJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('industry', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('skills', models.TextField()),
            ],
            options={
                'db_table': 'adzuna_job',
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('database', models.CharField(max_length=100)),
                ('usage_count', models.IntegerField()),
            ],
            options={
                'db_table': 'database',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('platform', models.CharField(max_length=100)),
                ('usage_count', models.IntegerField()),
            ],
            options={
                'db_table': 'platform',
            },
        ),
        migrations.CreateModel(
            name='WebFramework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('web_framework', models.CharField(max_length=100)),
                ('usage_count', models.IntegerField()),
            ],
            options={
                'db_table': 'web_framework',
            },
        ),
        migrations.RenameModel(
            old_name='TopTechnosVoulues',
            new_name='TopTech',
        ),
        migrations.DeleteModel(
            name='AdzunaJobs',
        ),
        migrations.DeleteModel(
            name='BaseDeDonnees',
        ),
        migrations.DeleteModel(
            name='FrameworkWeb',
        ),
        migrations.DeleteModel(
            name='Plateformes',
        ),
        migrations.RenameField(
            model_name='toptech',
            old_name='nb_offres',
            new_name='offer_count',
        ),
        migrations.RenameField(
            model_name='toptech',
            old_name='techno',
            new_name='technology',
        ),
        migrations.AlterModelTable(
            name='toptech',
            table='top_tech',
        ),
    ]
