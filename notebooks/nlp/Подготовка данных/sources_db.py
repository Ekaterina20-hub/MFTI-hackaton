import psycopg2
from psycopg2.extras import DictCursor

DATABASES = {
    'prod': {
        'NAME': 'hakaton2_db',
        'USER': 'hakaton_admin',
        'PASSWORD': 'fyT6r5Kd94Nko4d',
        'HOST': '94.142.142.59',
        'PORT': '5432',
    },
    'home': {
        'NAME': 'hakaton1_db',
        'USER': 'anketa_admin',
        'PASSWORD': 'f4uh4uhu34fuy34fd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

def runQuery(query, db_name='prod'):
    global DATABASES
    rows = []
    pg_connection = psycopg2.connect(
        dbname=DATABASES[db_name]['NAME'],
        user=DATABASES[db_name]['USER'],
        password=DATABASES[db_name]['PASSWORD'],
        host=DATABASES[db_name]['HOST'],
        port=DATABASES[db_name]['PORT'],
    )
    with pg_connection.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    cols = list(map(lambda x: x[0], cursor.description))
    cursor.close()
    pg_connection.close()
    data = []
    for row in rows:
        item = {}
        for index, col in enumerate(cols):
            item[col] = row[index]
        data.append(item)
    return data

def execQuery(query, db_name='prod'):
    global DATABASES
    pg_connection = psycopg2.connect(
        dbname=DATABASES[db_name]['NAME'],
        user=DATABASES[db_name]['USER'],
        password=DATABASES[db_name]['PASSWORD'],
        host=DATABASES[db_name]['HOST'],
        port=DATABASES[db_name]['PORT'],
    )
    with pg_connection.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(query)
        add_data = pg_connection.commit()
    cursor.close()
    pg_connection.close()
    return add_data

def generateUpdateQuery(row, columns):
    q = []
    for column in columns:
        s = column + '='
        value = row[column]
        if type(value) == str:
            s += f"'{value}'"
        elif type(value) == bool:
            s += str(value)
        elif value is None:
            s += 'null'
        else: s += str(value)
        q.append(s)
    return ', '.join(q)