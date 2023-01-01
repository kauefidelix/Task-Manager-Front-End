# Generated by Django 4.1 on 2022-12-31 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_card_assignee_alter_card_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="assignee",
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name="card",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="card",
            name="epic_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.epic",
            ),
        ),
        migrations.AlterField(
            model_name="epic",
            name="assignee",
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name="epic",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
    ]