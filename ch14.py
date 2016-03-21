import re #for regular expressions
import sqlite3

def useSqlite():
  conn = sqlite3.connect('music.sqlite3')
  cur = conn.cursor()
  cur.execute('drop table if exists Tracks')
  cur.execute('create table Tracks (title TEXT, plays INTEGER)')

  cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', ( 'Thunderstruck', 20 ) )
  cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', ( 'My Way', 15 ) )
  conn.commit()
  print('Tracks:')
  cur.execute('SELECT title, plays FROM Tracks')
  for row in cur :
    print(row)
  
  cur.execute('DELETE FROM Tracks WHERE plays < 100')
  conn.commit()

if __name__ == "__main__":
  useSqlite()
  #revisionCount('mbox-short.txt')
