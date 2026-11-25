import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_equipo_resumen_campana'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicadorOfensivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_indicador', models.CharField(default='Goles anotados por partido', max_length=100)),
                ('promedio', models.DecimalField(decimal_places=2, default=1.06, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorDefensivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_indicador', models.CharField(default='Goles recibidos por partido', max_length=100)),
                ('promedio', models.DecimalField(decimal_places=2, default=0.89, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RendimientoPuntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_indicador', models.CharField(default='Puntos por partido', max_length=100)),
                ('promedio', models.DecimalField(decimal_places=2, default=1.50, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_jugador', models.CharField(max_length=100)),
                ('goles_anotados', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rival', models.CharField(max_length=100)),
                ('condicion', models.CharField(max_length=50)),
                ('goles_favor', models.IntegerField(default=0)),
                ('goles_contra', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('indicador_ofensivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos', to='tasks.indicadorofensivo')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionPartido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_en_campo', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.jugador')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.partido')),
            ],
        ),
        migrations.AddField(
            model_name='partido',
            name='jugadores',
            field=models.ManyToManyField(through='tasks.ParticipacionPartido', to='tasks.jugador'),
        ),
        migrations.CreateModel(
            name='FichaTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjetas_resumen', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('partido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.partido')),
            ],
        ),
    ]