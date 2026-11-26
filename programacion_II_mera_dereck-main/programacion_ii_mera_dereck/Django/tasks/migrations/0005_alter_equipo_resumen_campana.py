from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_estadistica_general_estadisticageneral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='resumen_campana',
            field=models.TextField(blank=True, null=True),
        ),
    ]