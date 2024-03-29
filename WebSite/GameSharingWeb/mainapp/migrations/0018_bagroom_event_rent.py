# Generated by Django 3.1.7 on 2021-04-08 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20210331_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('slug', models.SlugField(unique=True)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Стоимость аренды')),
                ('cells', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Количество ячеек')),
                ('free_cells', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Количество свободных ячеек')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('game_booked', 'Клиент забронировал игры'), ('deposit_pay', 'Клиент внес депозит'), ('game_rent', 'Клиент арендовал игры'), ('rent_end', 'клиент вернул игры'), ('deposit_return', 'Мы вернули депозит')], default='game_booked', max_length=100, verbose_name='Статус аренды')),
                ('booked_time', models.DateTimeField(auto_now=True, verbose_name='Дата/время начала брони')),
                ('rent_time_start', models.DateTimeField(auto_now=True, verbose_name='Дата/время начала аренды')),
                ('rent_time_finish', models.DateTimeField(auto_now=True, verbose_name='Дата/время окончания аренды')),
                ('rent', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость аренды')),
                ('booked', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость брони')),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость залога')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_rent', to='mainapp.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(blank=True, choices=[('booked', 'Игра забронирована'), ('passed check', 'Игра прошла проверку клиентом'), ('passed check employee', 'Игра прошла проверку сотрудником'), ('no passed check', 'Игра НЕ прошла проверку клиентом'), ('no passed check employee', 'Игра НЕ прошла проверку сотрудником'), ('start rent', 'Начало бронирования'), ('finish rent', 'Конец бронирования'), ('buy', 'Купили игру')], max_length=100, verbose_name='Тип события')),
                ('game_box', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.gamebox', verbose_name='Игра')),
                ('rent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.rent', verbose_name='Аренда')),
            ],
        ),
    ]
