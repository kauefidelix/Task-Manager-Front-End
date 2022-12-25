# Generated by Django 4.1 on 2022-12-25 06:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_epic_epic_id_alter_epic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='epic_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='epic',
            name='name',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]
