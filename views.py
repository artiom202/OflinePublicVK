#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Imports

import time
from bottle import run, route, template, post, request, get, static_file, redirect
from main import Post, Comments, get_all_content, test_content, Pic, Doc

#/Imports

# Static Routes


@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')


@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')


@get('/')
def index():
    return template('templates/index.html')

@route('/<g_id:re:\d+><test:re:\D*$>')
def pabl(g_id,test):
    if test == '&test':
        print('test_content')
        test_content(g_id)
    else:
        get_all_content(g_id)
    ids = []
    count = 0
    for post in Post.select().where(Post.group_id == g_id):
        if post.id in ids:
            continue
        else:
            count += 1
            ids.append(post.id)
    print(count)
    return template('templates/pabl.html', ids=ids, Comments=Comments, Pic=Pic, Post=Post, Doc=Doc)


run(host='localhost', port=9999, debug=True)


