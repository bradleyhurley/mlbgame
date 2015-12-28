'''
This module gets the XML data that other functions use.
It checks if the data is cached first, and if not, 
gets the data from mlb.com
'''
import os
import urllib2 as url

def get_scoreboard(year, month, day):
    '''
    Return the game file for a certain day matching certain criteria
    '''
    monthstr = str(month).zfill(2)
    daystr = str(day).zfill(2)
    filename = "gameday-data/year_%i/month_%s/day_%s/scoreboard.xml.gz" % (year, monthstr, daystr)
    file = os.path.join(os.path.dirname(__file__), filename)
    if os.path.isfile(file):
        data = file
    else:
        data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/scoreboard.xml" % (year, monthstr, daystr))
    return data

def get_box_score(game_id):
    '''
    Return the box score file of a game with matching id
    '''
    year, month, day, rest = game_id.split('_', 3)
    filename = "gameday-data/year_%s/month_%s/day_%s/gid_%s/boxscore.xml" % (year, month, day, game_id)
    file = os.path.join(os.path.dirname(__file__), filename)
    if os.path.isfile(file):
        data = file
    else:
        data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_%s/month_%s/day_%s/gid_%s/boxscore.xml" % (year, month, day, game_id))
    return data