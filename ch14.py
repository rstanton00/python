import re #for regular expressions
import sqlite3
import twurl
import json
import urllib.parse
from urllib.request import urlopen

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
  cur.close()


def spiderTwitter():
  TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
  conn = sqlite3.connect('spider.sqlite3')
  cur = conn.cursor()
  cur.execute('''
  CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)''')
  while True:
    acct = raw_input('Enter a Twitter account, or quit: ')
    if ( acct == 'quit' ) : break
    if ( len(acct) < 1 ) :
      cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
      try:
        acct = cur.fetchone()[0]
      except:
        print 'No unretrieved Twitter accounts found'
        continue
  
  url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'} )
  print 'Retrieving', url
  connection = urllib.urlopen(url)
  data = connection.read()
  headers = connection.info().dict
  # print 'Remaining', headers['x-rate-limit-remaining']
  js = json.loads(data)
  # print json.dumps(js, indent=4)

  cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ) )
  countnew = 0
  countold = 0
  for u in js['users'] :
    friend = u['screen_name']
    print friend
    cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ) )
    try:
      count = cur.fetchone()[0]
      cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend) )
      countold = countold + 1
    except:
      cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES ( ?, 0, 1 )''', ( friend, ) )
      countnew = countnew + 1
    print 'New accounts=',countnew,' revisited=',countold
    conn.commit()
  cur.close()


if __name__ == "__main__":
  useSqlite()
  spiderTwitter()
