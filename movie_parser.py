#!/usr/bin/env python

from lxml.html import parse
import re
import sqlite3
import urllib2


def gross_value(movie_file):
    """
    Returns the gross value of movies
    
    Parameters
    ----------
    movie_file : str
        web address of the movie to be parsed
    
    Example
    -------
    >>> gross_value("http://www.imdb.com/title/tt0111161/?ref_=chttp_tt_1")
    3258645.11
    """
    file_tree = parse(movie_file)
    # Finding the div element having gross value if present else returns zero
    try:
        div = file_tree.findall("//div[@id='titleDetails']/div[h4='Gross:']")[0]
    except IndexError:
        return 0
    txt = div.text_content()
    # searching the gross value from the text
    gross = float(re.search(r'[\d,]+', txt).group().replace(',', ''))
    # if the value is in euros then converted to dollar
    if 'UK' in txt:
        gross = gross * 1.39
    return gross

if __name__ == '__main__':
    tree = parse("http://www.imdb.com/chart/top")

    movie_list = [movie for movie in
                  tree.findall("//tbody[1]/tr/td[@class='titleColumn']/a")]

    rating_list = [rating.text for rating in
                   tree.findall("//tbody[1]/tr/td[@class='ratingColumn']/strong")]

    pass_list = {movie.text: rating
                 for movie, rating in zip(movie_list, rating_list)
                 if gross_value(urllib2.urlparse.urljoin("http://www.imdb.com/", movie.attrib['href'])) > 50000000}

    li =  [(i, pass_list[i]) for i in pass_list]
    conn = sqlite3.connect('rating_list.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE rating_list (Movie_name,Rating)''')
    c.executemany('INSERT INTO rating_list VALUES (?,?)',li)
    for row in c.execute('SELECT AVG(Rating) AS Avg FROM rating_list'):
        print row

    conn.commit()
    conn.close()
