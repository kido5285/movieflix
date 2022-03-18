import requests
import json
from flask import Flask, jsonify, render_template, request, redirect
from dotenv import dotenv_values
config = dotenv_values(".env")
app = Flask(__name__)

@app.route('/')
def home():
    page = request.args.get('page')
    if not page:
        page = 1
    return render_template('home.html', search=request.args.get('search'), page=page)

@app.route('/movie')
def movie():
    movietype = request.args.get('type')
    page = request.args.get('page')
    if not page:
        page = 1
    if movietype == 'hot' or movietype == 'top-rated' or movietype == 'now-playing':
        return render_template('movie.html', movietype=movietype, moviepage=page)
    else: 
        return redirect('/notfound')

@app.route('/movies')
def movies():
    page = request.args.get('page')
    if not page:
        page = 1
    return render_template('movies.html', page=page)

@app.route('/genre/<gen>')
def moviegenres(gen):
    page = request.args.get('page')
    if not page:
        page = 1
    return render_template('genres.html', gen=gen, page=page)

@app.route('/country/<country>')
def country(country):
    page = request.args.get('page')
    if not page:
        page = 1
    return render_template('countries.html', country=country, page=page)

@app.route('/tvshows-genre/<genre>')
def tvshowsGenre(genre):
    page = request.args.get('page')
    if not page:
        page = 1
    return render_template('tvshows-genres.html', genre=genre, page=page)

@app.route('/tvshows')
def tvshows():
    page = request.args.get('page')
    if not page:
        page = 1
    return render_template('tvshows.html', page=page)

@app.route('/tvshows/<int:id>')
def indtvshow(id): 
    if request.args.get('action') == 'want-to-watch':
        seas = 1
        eps = 1
        if request.args.get('epsandseas'):
            if len(request.args.get('epsandseas').split('x')) == 2:
                seas = request.args.get('epsandseas').split('x')[0] 
                eps = request.args.get('epsandseas').split('x')[1]
        return render_template('watchtv.html', id=str(id), iframeurl=f'https://www.2embed.ru/embed/tmdb/tv?id={id}&s={seas}&e={eps}', seas=seas, eps=eps)
    else:
        return render_template('indtv.html', id=str(id), redurl=f'/tvshows/{id}?action=want-to-watch&epsandseas=1x1')

@app.route('/<int:movieid>')
def indmovie(movieid):
    if request.args.get('action') == 'want-to-watch':
        return render_template('watchmovie.html', id=str(movieid), iframeurl=f'https://www.2embed.ru/embed/tmdb/movie?id={movieid}')
    else:
        return render_template('indmovie.html', id=str(movieid), redurl=f'/{movieid}?action=want-to-watch')

@app.route('/tvshows-country/<country>')
def tvshowscountry(country):
    page = request.args.get('page')
    if not page:
        page = 1
    country2 = country.split('-')
    return render_template('tvshows-country.html', country=country, country2=' '.join(country2), page=page)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True) 