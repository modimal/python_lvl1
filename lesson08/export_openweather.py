# coding: utf-8

import sys
import csv
import json
import sqlite3

country_codes = {}


def get_country_codes():
    with open('wikipedia-iso-country-codes.csv') as f:
        file = csv.DictReader(f, delimiter=',')
        for line in file:
            country_codes[line['English short name lower case'].lower()] = line['Alpha-2 code']


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


if __name__ == '__main__':
    if len(sys.argv) > 5:
        raise ValueError('incorrect country parameter, '
                         'separate words with underscore, expected [<city_name> [<country_name>]].')
    if len(sys.argv) == 3 or len(sys.argv) == 5:
        if sys.argv[1] != '--json':
            raise ValueError('wrong named parameter, expected --json.')
        with sqlite3.connect('weather_data.db') as conn:
            get_country_codes()
            conn.row_factory = dict_factory
            cur = conn.cursor()
            if len(sys.argv) == 3:
                sql = 'select * from Погода'
                cur.execute(sql)
            else:
                sql = 'select * from Погода where Город=? and Код_страны=?'
                try:
                    try:
                        city_name = sys.argv[3].lower().replace('_', ' ')
                    except KeyError:
                        city_name = sys.argv[3].lower()
                    try:
                        country_name = country_codes[sys.argv[4].lower().replace('_', ' ')]
                    except KeyError:
                        country_name = country_codes[sys.argv[4].lower()]
                except KeyError as e:
                    print('KeyError: wrong city or country name:', e)
                    sys.exit(2)

                cur.execute(sql, [city_name, country_name])
            res = cur.fetchall()

            if not res:
                raise ValueError('weather_data.db has no such data.')

            with open(sys.argv[2] + '.json', 'w', encoding='utf-8') as f:
                json.dump(res, f)
        sys.exit(2)
    raise TypeError('wrong number of parameters, expected <script.py> --json filename [<city_name> [<country_name>]].')
