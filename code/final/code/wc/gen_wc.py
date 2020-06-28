import sqlite3
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import jieba

if __name__ == '__main__':
    with sqlite3.connect('../db/movie.db') as conn:
        df = pd.read_sql('select * from comment', conn)
        cursor = conn.cursor()
        ser = df.groupby('movie_name').comm.apply('。'.join)
        wc = WordCloud(font_path='msyh.ttc')
        for index in ser.index:
            wc.generate_from_text(' '.join(jieba.cut(ser[index])))
            wc.to_file('../static/img/wc/' + index + '.png')
            sql = f'''INSERT INTO image(movie_name, img_path) VALUES
            ('{index}', '{'/static/img/wc/' + index + '.png'}')'''
            cursor.execute(sql)
        conn.commit()
        cursor.close()
        # wc.generate_from_text(' '.join(jieba.cut(df['霸王别姬'])))
        # wc.to_file('../static/img/wc/霸王别姬.png')
        # plt.imshow(wc)
        # plt.show()
