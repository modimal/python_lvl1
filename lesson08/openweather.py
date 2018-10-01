# coding: utf-8

import csv
import json
import sqlite3
import urllib.error
import urllib.request
from datetime import datetime

country_codes = {}


def get_country_codes():
    with open('wikipedia-iso-country-codes.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for line in file:
            country_codes[line['English short name lower case'].lower()] = line['Alpha-2 code']


class DBController:
    def __init__(self):
        self._dbname = 'weather_data.db'
        self.date_format = '%d/%m/%Y %H:%M'
        try:
            with sqlite3.connect(self.dbname) as conn:
                cur = conn.cursor()
                cur.execute("""
                    create table Погода (
                        id_города integer primary key,
                        Код_страны text,
                        Город text,
                        Дата text,
                        Температура integer,
                        id_погоды integer
                    );
                    """)
        except sqlite3.OperationalError:
            pass

    @property
    def dbname(self):
        return self._dbname

    def add_city(self, city):
        try:
            self._insert_data(city)
        except sqlite3.IntegrityError:
            self._update_data(city)

    def _insert_data(self, city):
        with sqlite3.connect(self.dbname) as conn:
            cur = conn.cursor()
            cur.execute("""
                insert into Погода (id_города, Код_страны, Город, Дата, Температура, id_погоды)
                values (?, ?, ?, ?, ?, ?)
                """, (
                    city.json_data['id'],
                    city.json_data['sys']['country'],
                    city.json_data['name'].lower(),
                    datetime.utcfromtimestamp(city.json_data['dt']).strftime(self.date_format),
                    city.json_data['main']['temp'],
                    city.json_data['weather'][0]['id']
                )
            )
            conn.commit()

    def _update_data(self, city):
        newcd = datetime.utcfromtimestamp(city.json_data['dt']).strftime(self.date_format)
        with sqlite3.connect(self.dbname) as conn:
            cur = conn.cursor()
            cur.execute("""
                select Дата from Погода where id_города=?
                """, [city.json_data['id']]
            )
            oldcd = cur.fetchone()
            if oldcd[0] != newcd:
                cur.execute("""
                    update Погода set Дата=:date,Температура=:temp,id_погоды=:idw where id_города=:idc
                    """, {'date': newcd,
                          'temp': city.json_data['main']['temp'],
                          'idw': city.json_data['weather'][0]['id'],
                          'idc': city.json_data['id']}
                )
                conn.commit()

    def show_data(self, name=None, code=None, mode='one'):
        with sqlite3.connect(self.dbname) as conn:
            cur = conn.cursor()
            if mode == 'one':
                name, code = name.lower(), code.upper()
                sql = "select * from Погода where Код_страны=? and Город=?"
                cur.execute(sql, [code, name])
            elif mode == 'all':
                sql = "select * from Погода"
                cur.execute(sql)
            formatted = '\nПогода:\n'
            for cd in cur.fetchall():
                formatted += '\nКод страны:\t\t{}\nГород:\t\t\t{}\nДата:\t\t\t{}\nТемпература:\t{}'\
                    .format(cd[1], cd[2].capitalize(), cd[3], str(round(cd[4])) + '\u2103')
            print(formatted)


class CityData:
    def __init__(self, name, code):
        self._name = name.lower()
        self._code = code
        with open('app.id', 'r', encoding='utf-8') as f:
            self._appid = f.readline()
        self._req = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'\
            .format(self.name, self.code, self._appid)
        self._json_data = self._req_json()

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def json_data(self):
        return self._json_data

    def _req_json(self):
        resp = urllib.request.urlopen(self._req)
        resp = resp.read().decode('utf-8')
        return json.loads(resp)


if __name__ == '__main__':
    get_country_codes()
    dbcontroller = DBController()

    try:
        user_cities = input('Type cities and countries in english '
                            '(Moscow,Russian Federation;Kazan,Russian Federation):\n').strip().lower().split(';')

        for c in user_cities:
            if not c:
                raise ValueError('incorrect input, expected full_city_name,full_country_name;'
                                 'full_city_name,full_country_name.')
            city = c.split(',')
            dbcontroller.add_city(CityData(city[0], country_codes[city[1].lower()]))
            dbcontroller.show_data(city[0], country_codes[city[1].lower()])

    except urllib.error.HTTPError as e:
        print('Error: city was not found: {}.'.format(e))
        exit(0)
