from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadisticaGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidos_jugados', models.IntegerField(default=36)),
                ('victorias', models.IntegerField(default=15)),
                ('empates', models.IntegerField(default=9)),
                ('derrotas', models.IntegerField(default=12)),
                ('goles_a_favor', models.IntegerField(default=38)),
                ('goles_en_contra', models.IntegerField(default=32)),
                ('diferencia_goles', models.IntegerField(default=6)),
                ('puntos', models.IntegerField(default=54)),
            ],
        ),
    ]