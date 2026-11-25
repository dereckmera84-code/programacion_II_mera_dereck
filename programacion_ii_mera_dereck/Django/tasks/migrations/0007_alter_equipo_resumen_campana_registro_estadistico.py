import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_promedios_y_rendimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='resumen_campana',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RegistroEstadistico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_metrica', models.CharField(max_length=200)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('estado_analisis', models.CharField(choices=[('PENDIENTE', 'Por analizar'), ('EN_REVISION', 'En revisión'), ('COMPLETADO', 'Completado')], default='PENDIENTE', max_length=20)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros_estadisticos', to='tasks.equipo')),
            ],
        ),
    ]