from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):
    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        TrigramExtension(),
    ]
