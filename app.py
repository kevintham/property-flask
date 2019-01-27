#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 09:03:02 2019

@author: kevintham
"""

import json

from flask import Flask, render_template
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql

app = Flask(__name__)

@app.route("/")
def index():
    connection = pg.connect(host='localhost',
                            dbname='nine2property',
                            user='kevintham')
    df = psql.read_sql("SELECT * FROM property", connection)
    chart_data = json.dumps(df.to_dict(orient='records'), indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)