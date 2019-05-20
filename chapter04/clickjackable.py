#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run


@route('/')
def hello():
    html = '<h2> target web site </h2>'
    html += '<button type="button" value="button"'
    html += 'onclick="alert({})">'.format('Bought item A')
    html += 'Buy item A </button>'
    return html


def main():
    run(host='localhost', port=8000, debug=True)


if __name__ == '__main__':
    main()
