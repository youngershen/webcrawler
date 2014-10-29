#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com

import json
from flask import Flask
from flask import render_template
from utils import find_page
from utils import json_decode

app = Flask(__name__)

@app.route('/<page>')
def index(page):
    
    current_page = int(page)
    items = find_page(int(page))[0]
    prev_page = 1
    next_page = 1

    if current_page == 1:
        prev_page = 1
    else:
        prev_page = current_page - 1
    
    if current_page == items[1]:
        next_page = items[1]
    else:
        next_page = current_page + 1
    
    return render_template('index.html', items=json_decode(items), prev_page = prev_page, next_page = next_page)


def main():
    app.debug=True
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
