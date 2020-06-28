# -*- coding: utf-8 -*-
import sqlite3


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline:
    def __init__(self):
        # 初始化数据库连接
        self.conn = sqlite3.connect('../db/movie.db')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            if item['entity'] == 'movie':
                self.process_movie(item)
            elif item['entity'] == 'comment':
                self.process_comment(item)
        except:
            pass
        return item

    def process_movie(self, item):
        sql = f'''INSERT INTO movie
        (movie_name, year, length, score, img_url, rank, country)
        VALUES
        ('{item['movie']}', '{item['year']}', {item['length']}, {item['score']}, 
        '{item['img_url']}', {item['rank']}, '{item['country']}')'''
        self.cursor.execute(sql)
        for director in item['director']:
            sql = f'''INSERT INTO director
            (director_name, movie_name) 
            VALUES
            ('{director}', '{item['movie']}')'''
            self.cursor.execute(sql)
        for actor in item['actor']:
            sql = f'''INSERT INTO actor
            (actor_name, movie_name) 
            VALUES
            ('{actor}', '{item['movie']}')'''
            self.cursor.execute(sql)
        for genre in item['genre']:
            sql = f'''INSERT INTO genre
            (type, movie_name)
            VALUES
            ('{genre}', '{item['movie']}')'''
            self.cursor.execute(sql)
        self.conn.commit()

    def process_comment(self, item):
        for comm in item['comment']:
            sql = f'''INSERT INTO comment
            (comm, movie_name)
            VALUES
            ('{comm}', '{item['movie']}')'''
            print(sql)
            self.cursor.execute(sql)
        self.conn.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect('../../db/movie.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO movie
        (movie_name, year, length, score, img_url, rank, country)
        VALUES
        ('肖申克的救赎', '1994', 142, 9.7,
        'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg', 1, '美国')
''')
    conn.commit()
    print(cursor)
