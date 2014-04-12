#!/usr/bin/env python

import sqlite3

pass_list =  li = {'Platoon': '8.1', 'Hotel Rwanda': '8.1', 'Stand by Me': '8.1', 'The Avengers': '8.1', 'L.A. Confidential': '8.3', 'Kill Bill: Vol. 1': '8.1', 'The Shining': '8.4', 'Unforgiven': '8.3', 'Inception': '8.7', 'Ben-Hur': '8.1', 'The Wolf of Wall Street': '8.3', 'Million Dollar Baby': '8.1', 'The Dark Knight Rises': '8.5', '12 Years a Slave': '8.2', 'Taxi Driver': '8.4', 'The Silence of the Lambs': '8.6', 'The Lord of the Rings: The Return of the King': '8.9', 'The Help': '8.0', 'The Hobbit: The Desolation of Smaug': '8.0', "The King's Speech": '8.1', 'Barry Lyndon': '8.0', 'Aliens': '8.4', 'Requiem for a Dream': '8.4', 'The Sixth Sense': '8.1', 'The Lion King': '8.4', 'The Lego Movie': '8.1', 'The Sting': '8.3', 'A Beautiful Mind': '8.1', 'The Green Mile': '8.5', 'Sin City': '8.1', 'Gravity': '8.1', 'The Matrix': '8.7', "Howl's Moving Castle": '8.2', 'The Godfather': '9.2', 'Star Wars: Episode V - The Empire Strikes Back': '8.8', 'Saving Private Ryan': '8.5', 'The Lord of the Rings: The Two Towers': '8.7', 'Castle in the Sky': '8.0', 'Indiana Jones and the Last Crusade': '8.3', 'Downfall': '8.3', 'Jaws': '8.1', 'The Deer Hunter': '8.2', 'Butch Cassidy and the Sundance Kid': '8.1', 'American Beauty': '8.4', 'Groundhog Day': '8.0', 'The Celebration': '8.0', 'Django Unchained': '8.5', 'Life Is Beautiful': '8.6', 'Jurassic Park': '8.0', 'The Prestige': '8.4', 'Die Hard': '8.3', 'The Dark Knight': '8.9', 'No Country for Old Men': '8.1', 'V for Vendetta': '8.2', 'Monsters, Inc.': '8.0', u'L\xe9on: The Professional': '8.6', 'Slumdog Millionaire': '8.0', 'Gran Torino': '8.2', 'The Bourne Ultimatum': '8.1', 'Rocky': '8.0', 'In the Mood for Love': '8.0', 'Shutter Island': '8.0', 'Star Wars: Episode VI - Return of the Jedi': '8.4', 'Fanny and Alexander': '8.1', 'Pirates of the Caribbean: The Curse of the Black Pearl': '8.0', 'Star Wars': '8.7', 'Gone with the Wind': '8.2', 'Batman Begins': '8.3', 'The Elephant Man': '8.2', 'Gladiator': '8.5', 'Toy Story 3': '8.4', 'The Godfather: Part II': '9.0', 'Good Will Hunting': '8.2', 'Black Swan': '8.0', 'Inglourious Basterds': '8.3', '2001: A Space Odyssey': '8.3', 'Per un pugno di dollari': '8.0', 'Beauty and the Beast': '8.0', 'For a Few Dollars More': '8.3', u'WALL\xb7E': '8.4', 'Eternal Sunshine of the Spotless Mind': '8.4', 'Terminator 2: Judgment Day': '8.5', 'The Lord of the Rings: The Fellowship of the Ring': '8.8', 'Gandhi': '8.1', 'Harry Potter and the Deathly Hallows: Part 2': '8.0', 'The Departed': '8.5', "One Flew Over the Cuckoo's Nest": '8.7', 'Finding Nemo': '8.1', 'Captain America: The Winter Soldier': '8.1'}

li =  [(i,pass_list[i]) for i in pass_list]

conn = sqlite3.connect('rating_list.db')
c = conn.cursor()
c.execute('''CREATE TABLE rating_list (Movie_name,Rating)''')
c.executemany('INSERT INTO rating_list VALUES (?,?)',li)
for row in c.execute('SELECT AVG(Rating) AS Avg FROM rating_list'):
    print row

conn.commit()
conn.close()
