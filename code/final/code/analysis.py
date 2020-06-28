import sqlite3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']


def scatterplot(x_data, y_data, x_label, y_label, title):
    # 创建一个绘图对象
    fig, ax = plt.subplots()
    # 设置数据、点的大小、点的颜色和透明度
    ax.scatter(x_data, y_data, s = 10, color = '#539caf', alpha = 0.9)
    # 添加标题和坐标说明
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.xticks(rotation=90)
    plt.ylim((6, 10))
    plt.savefig("pic1.png",bbox_inches = 'tight')
    plt.show()

def overlaid_histogram(data1, data1_name, data1_color, data2, data2_name, data2_color, x_label, y_label, title):
    # 归一化数据区间，对齐两个直方图的bins
    max_nbins = 10
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins
    bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth) # 生成直方图bins区间

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data1, bins = bins, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(data2, bins = bins, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')
    plt.savefig("pic2.png",bbox_inches = 'tight')
    plt.show()

def barplot(x_data, y_data, error_data, x_label, y_label, title):
    _, ax = plt.subplots()
    # 柱状图
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')
    # 绘制方差
    # ls='none'去掉bar之间的连线
    ax.errorbar(x_data, y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 5)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    plt.xticks(rotation=90)
    plt.ylim((8, 10))
    plt.savefig("pic3.png",bbox_inches = 'tight')
    plt.show()

def boxplot(x_data, y_data, base_color, median_color, x_label, y_label, title):
    _, ax = plt.subplots()
    # 设置样式
    ax.boxplot(y_data
               # 箱子是否颜色填充
               , patch_artist = True
               # 中位数线颜色
               , medianprops = {'color': base_color}
               # 箱子颜色设置，color：边框颜色，facecolor：填充颜色
               , boxprops = {'color': base_color, 'facecolor': median_color}
               # 猫须颜色whisker
               , whiskerprops = {'color': median_color}
               # 猫须界限颜色whisker cap
               , capprops = {'color': base_color})

    # 箱图与x_data保持一致
    ax.set_xticklabels(x_data)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    plt.xticks(rotation=90)
    plt.savefig("pic4.png",bbox_inches = 'tight')
    plt.show()

def pic1():
    with sqlite3.connect('db/movie.db') as conn:
        genre1 = pd.read_sql(
            'select type,score '
            'from movie inner join genre on movie.movie_name = genre.movie_name ', conn)
        genre1 = {'x1': list(genre1.type), 'x2': list(genre1.score)}
        scatterplot(genre1['x1'], genre1['x2'], '类别', '评分', '豆瓣TOP250类别评分')

def pic2():
    with sqlite3.connect('db/movie.db') as conn:
        genre1 = pd.read_sql(
            'select score  '
            'from movie inner join genre on movie.movie_name = genre.movie_name '
            'where genre.type =\'喜剧\' ', conn)
        genre1 = genre1.score
        genre2 = pd.read_sql(
            'select score  '
            'from movie inner join genre on movie.movie_name = genre.movie_name '
            'where genre.type =\'爱情\' ', conn)
        genre2 = genre2.score

        overlaid_histogram(data1=genre1
                           , data1_name='喜剧'
                           , data1_color='#d6d40f'
                           , data2=genre2
                           , data2_name='爱情'
                           , data2_color='#3cbda4'
                           , x_label='score'
                           , y_label='Frequency'
                           , title='爱情与喜剧类别的比较')

def pic3():
    with sqlite3.connect('db/movie.db') as conn:
        country = pd.read_sql(
            'select country, score from movie ', conn)
        country = {'x': list(country.country), 'y': list(country.score)}
        country=pd.DataFrame(country)
        mean_total_co_day = country.groupby('x').agg([np.mean, np.std])
        mean_total_co_day.columns = mean_total_co_day.columns.droplevel()  # 变成一维columns
        barplot(x_data=mean_total_co_day.index.values
                , y_data=mean_total_co_day['mean']
                , error_data=mean_total_co_day['std']
                , x_label='国家/地区'
                , y_label='评分'
                , title='豆瓣TOP250国家/地区评分方差图')

def pic4():
    with sqlite3.connect('db/movie.db') as conn:
        genre1 = pd.read_sql(
            'select type,score '
            'from movie inner join genre on movie.movie_name = genre.movie_name ', conn)
        genre1 = {'x1': list(genre1.type), 'x2': list(genre1.score)}

        test = np.unique(genre1['x1'])  # np.unique返回排好序的出现值（集合）
        data = []
        for item in test:
            tmp =[]
            for index,item2 in enumerate(genre1['x1'] ):
                if item2 == item:
                    tmp.append(genre1['x2'][index])
            data.append(tmp)

        print(test[1])
        # print(data)
        print(data)
        boxplot(x_data=test
                , y_data=data
                , base_color='#286594'
                , median_color='#b1cbde'
                , x_label='分类'
                , y_label='评分'
                , title='豆瓣TOP250分类箱式图')

# def pic5():
#     with sqlite3.connect('db/movie.db') as conn:
#         genre1 = pd.read_sql(
#             'select country,type,score '
#             'from movie inner join genre on movie.movie_name = genre.movie_name ', conn)
#         genre1 = {'x1': list(genre1.type), 'x2': list(genre1.score), 'x3': list(genre1.country)}
#         country = pd.DataFrame(genre1)
#         print(country)
#         sns.set()
#         # 用行和列标签绘制
#         flights = country.pivot("x1", "x3", "x2")
#         # 绘制x-y-z的热力图，比如 年-月-销量 的热力图
#         f, ax = plt.subplots(figsize=(9, 6))
#         sns.heatmap(flights, ax=ax)
#         # 设置坐标字体方向
#         label_y = ax.get_yticklabels()
#         plt.setp(label_y, rotation=360, horizontalalignment='right')
#         label_x = ax.get_xticklabels()
#         plt.setp(label_x, rotation=45, horizontalalignment='right')
#         plt.show()



if __name__ == '__main__':
    sns.set()
    pic1()
    pic2()
    pic3()
    pic4()
