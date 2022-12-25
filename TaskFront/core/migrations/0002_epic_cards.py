# Generated by Django 4.1 on 2022-12-25 05:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('epic_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=264, unique=True)),
                ('content', models.TextField()),
                ('creation_date', models.DateField()),
                ('last_modified', models.DateField()),
                ('assignee', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('card_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=264, unique=True)),
                ('content', models.TextField()),
                ('creation_date', models.DateField()),
                ('last_modified', models.DateField()),
                ('column', models.CharField(max_length=264, unique=True)),
                ('assignee', models.CharField(max_length=264, unique=True)),
                ('card_type', models.CharField(max_length=264, unique=True)),
                ('epic_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.epic')),
            ],
        ),
    ]
