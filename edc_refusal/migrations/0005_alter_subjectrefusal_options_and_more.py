# Generated by Django 4.2.1 on 2023-07-05 02:16

import django.db.models.manager
import edc_sites.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edc_refusal", "0004_refusalreasons_plural_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subjectrefusal",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Subject Refusal",
                "verbose_name_plural": "Subject Refusals",
            },
        ),
        migrations.AlterModelManagers(
            name="subjectrefusal",
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
                ("objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
