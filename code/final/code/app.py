from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis')
def analysis():
    with sqlite3.connect('db/movie.db') as conn:
        country = pd.read_sql(
            'select country, count(*) as cnt from movie group by country order by cnt desc limit 20', conn)
        country = {'x': list(country.country), 'y': list(country.cnt)}

        country_rank = pd.read_sql(
            'select country,count(*) as cnt, max(score) as maxx, min(score) as minn, avg(score) as avg from movie group by country order by cnt desc limit 10', conn)
        country_rank = {'x1': list(country_rank.country), 'x2': list(country_rank.avg),'x3':list(country_rank.maxx),'x4': list(country_rank.minn)}

        actor = pd.read_sql(
            'select actor_name, count(*) as cnt from actor group by actor_name order by cnt desc limit 10', conn)
        actor = {'x': list(actor.actor_name)[::-1], 'y': list(actor.cnt)[::-1]}

        director = pd.read_sql(
            'select director_name,avg(score) as sc, count(*) as cnt '
            'from director inner join movie on movie.movie_name = director.movie_name '
            'group by director_name order by cnt desc limit 20',
            conn)
        director = {'x': list(director.director_name), 'y': list(director.cnt), 'z': list(director.sc)}

        score = pd.read_sql(
            'select score from movie', conn
        )
        score = list(score.score)

        year = pd.read_sql(
            'select year from movie', conn
        )
        year = list(year.year.astype(int))

        year_score = pd.read_sql(
            'select year,avg(score)as test,max(score) as maxx,min(score) as minn from movie group by year order by year asc',
            conn)
        year_score = {'x1': list(year_score.year), 'x2': list(year_score.test), 'x3': list(year_score.maxx),
                      'x4': list(year_score.minn)}

        genre1 = pd.read_sql(
            'select type,count(*) as cnt,avg(movie.score) as sc '
            'from movie inner join genre on movie.movie_name = genre.movie_name '
            'group by genre.type '
            'order by cnt desc limit 15', conn)
        genre1 = {'x1': list(genre1.type), 'x2': list(genre1.cnt), 'x3': list(genre1.sc)}

        genre2 = pd.read_sql(
            'select type,score '
            'from movie inner join genre on movie.movie_name = genre.movie_name order by score desc ', conn)
        genre2 = {'x1': list(genre2.type), 'x2': list(genre2.score)}

    return render_template('analysis.html', country=country,country_rank=country_rank,
                           actor=actor, director=director, score=score, year=year,
                           year_score=year_score,genre1=genre1,genre2=genre2)


@app.route('/data')
def data():
    return data1(0)


@app.route('/wc')
def wc():
    return wc1(0)


@app.route('/wc/<int:page>')
def wc1(page):
    limit = 9
    print(page)
    next = page + 1 if page * limit < 250 else page
    prev = page - 1 if page > 0 else page
    with sqlite3.connect('db/movie.db') as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            f'select movie_name as movie, img_path as path from image limit {limit} offset {limit * page}')
        res = list(res)
        img = []
        for i in range(0, len(res), 3):
            img.append((
                [item[0] for item in res[i:i + 3]],
                [item[1] for item in res[i:i + 3]]
            ))
        # print(img)
    return render_template('wc.html', img=img, next=next, prev=prev)


@app.route('/data/<int:page>')
def data1(page):
    limit = 25
    next = page + 1 if page * limit < 250 else page
    prev = page - 1 if page > 0 else page
    with sqlite3.connect('db/movie.db') as conn:
        cursor = conn.cursor()
        data = cursor.execute(
            f'select movie_name as name, year, length, country, score, img_url from movie order by rank limit {limit} offset {page * limit}')
        movies = list(data)
    return render_template('data.html', movies=movies, next=next, prev=prev)


if __name__ == '__main__':
    app.run()
