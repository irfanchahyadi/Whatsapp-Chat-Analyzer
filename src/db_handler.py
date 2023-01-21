import random, string
from datetime import datetime
from sqlalchemy import create_engine
import sqlite3
import pandas as pd
from src.settings import DATABASE_URL

def generate_url(n, unique=True):
    """Generate url key."""
    def rand_url(n):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    if unique:
        chat_id = ['']
        while len(chat_id) > 0:
            url = rand_url(n)
            chat_id = get_chat_id(url)
    else:
        url = rand_url(n)
    return url

def get_engine():
    """Create sqlalchemy engine."""
    engine = create_engine(DATABASE_URL)
    return engine

def get_df(sql):
    """Return dataframe from sql syntax."""
    db_engine = get_engine()
    df = pd.read_sql(sql, db_engine)
    return df

def execute(sql, params=None, result_back=True):
    """Execute and return result from sql syntax."""
    db_engine = get_engine()
    with db_engine.connect() as con:
        if params:
            res = con.execute(sql, params)
        else:
            res = con.execute(sql)
        if result_back:
            res = [i for i in res]
    return res

def get_chat_id(url):
    """Return chat id from specific url key."""
    return execute("select id, chat_type, lang from uploaded where url=?;", (url,))

def get_chat(url):
    """Return chat data from specific url key."""
    chat_id = get_chat_id(url)
    if len(chat_id) > 0:
        return get_df(f'select * from chat where id_chat={chat_id[0][0]};'), chat_id[0][1], chat_id[0][2]
    else:
        return pd.DataFrame(), 'not_found'

def add_chat(df, lang, chat_type, url):
    """Save chat history into database."""
    sql = "insert into uploaded (datetime, chat_type, url, lang) values (%s, %s, %s, %s) returning id;"
    id_chat = execute(sql, (datetime.now(), chat_type, url, lang))[0][0]
    df.insert(0, 'id_chat', id_chat)
    db_engine = get_engine()
    df.to_sql('chat', db_engine, if_exists='append')
    return url

def reset_chat():
    """Reset database."""
    sql_script = [
        "drop table if exists uploaded;",
        "drop table if exists chat;",
        "create table uploaded (id serial primary key, datetime timestamp, chat_type varchar, url varchar, lang varchar);",
        "create table chat (id serial primary key, id_chat integer, datetime timestamp, contact varchar, message varchar);",
        "insert into uploaded (id, datetime, chat_type, url, lang) values(1, '2022-01-01 00:00:00', 'groupchat', 'DEMO', 'eng');",
        "insert into chat (id, id_chat, datetime, contact, message) values(1, 1, '2022-01-01 00:00:00', 'irfan', 'encrypted');",
    ]
    for sql in sql_script:
        execute(sql, result_back=False)