#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :manuals.py
#description     :This program helps new users to get started.
#author          :gnusse (https://github.com/GnussonNet)
#date            :2019-06-27
#version         :1.0.0
#usage           :First run the setup.py then just type "manuals" in terminal to launch
#notes           :
#python_version  :2.7.6  
#=======================================================================
 

# ✔ ✘


# Import the modules needed to run the script.
import sys, os, argparse


#Color
color = {'white':'\33[37m', 'bg':'\33[101m', 'blink' :'\33[5m', 'bold' :'\033[;1m', 'cyan' :'\033[96m', 'red' :'\033[1;31m', 'blue':'\033[1;34m', 'off' : '\033[0;0m'}

 
# Main definition - constants
menu_actions  = {}  
 
# =======================
#     MENUS FUNCTIONS
# =======================
 
# Main menu
def main_menu():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']
    #print color['red'] + logo + color['off']
    #print color['cyan'] + menu + color['off']


    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┃                                                                ┃"
    print "┃                                                                ┃"
    print "┃" + color['cyan'] + " [1] ✔ catt                              Chromecast hijacking   " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [2] ✔ twint                             Twitter scraper        " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [3] ✔ userrecon                         Account lookup         " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [4] ✔ cupp                              Personalized wordlist  " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [5] ✔ HiddenEye                         Social medias phishing " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [6] ✔ John                              Zip password cracker   " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [7] ✔ zip                               Create zip files       " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [9] ✔ Navigation                        Must know commands     " + color['red'] + "┃"
    print "┃" + color['cyan'] + " [0] ✔ Quit                              Quit                   " + color['red'] + "┃"
    print "┃                                                                ┃"
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    choice = raw_input(color['red'] + "Select>:")
    exec_menu(choice)
 
    return
 
# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return
 
# Menu 1
def menu1():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']

    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "git clone https://github.com/skorokithakis/catt.git" + color['off']
    print color['cyan'] + "cd catt" + color['off']
    print color['cyan'] + "chmod +x setup.py" + color['off']
    print color['cyan'] + "python3 setup.py" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Cast video from website:" + color['off']
    print color['cyan'] + "catt cast \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"" + color['off']
    print
    print color['blue'] + "Cast video local:" + color['off']
    print color['cyan'] + "catt cast ./myvideo.mp4" + color['off']
    print
    print color['blue'] + "Cast video with subtitle:" + color['off']
    print color['cyan'] + "catt cast -s ./mysubtitle.srt /myvideo.mp4" + color['off']
    print
    print color['blue'] + "Cast site:" + color['off']
    print color['cyan'] + "catt cast_site https://en.wikipedia.org/wiki/Rickrolling" + color['off']
    print
    print
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)	
 
 
# Menu 2
def menu2():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Scrape all the Tweets from user's timeline:" + color['off']
    print color['cyan'] + "twint -u username" + color['off']
    print
    print color['blue'] + "Scrape all Tweets from the user's timeline containing pineapple:" + color['off']
    print color['cyan'] + "twint -u username -s pineapple" + color['off']
    print
    print color['blue'] + "Collect every Tweet containing pineapple from everyone's Tweets:" + color['off']
    print color['cyan'] + "twint -s pineapple" + color['off']
    print
    print color['blue'] + "Collect Tweets that were tweeted before 2014:" + color['off']
    print color['cyan'] + "twint -u username --year 2014" + color['off']
    print
    print color['blue'] + "Collect Tweets that were tweeted since 2015-12-20:" + color['off']
    print color['cyan'] + "twint -u username --since 2015-12-20" + color['off']
    print
    print color['blue'] + "Scrape Tweets and save to file.txt:" + color['off']
    print color['cyan'] + "twint -u username -o file.txt" + color['off']
    print
    print color['blue'] + "Scrape Tweets and save as a csv file:" + color['off']
    print color['cyan'] + "twint -u username -o file.csv --csv" + color['off']
    print
    print color['blue'] + "Show Tweets that might have phone numbers or email addresses:" + color['off']
    print color['cyan'] + "twint -u username --email --phone" + color['off']
    print
    print color['blue'] + "Display Tweets by verified users that Tweeted about Donald Trump:" + color['off']
    print color['cyan'] + "twint -s \"Donald Trump\" --verified" + color['off']
    print
    print color['blue'] + "Scrape Tweets from a radius of 1km around a place in Paris and export them to a csv file:" + color['off']
    print color['cyan'] + "twint -g=\"48.880048,2.385939,1km\" -o file.csv --csv" + color['off']
    print
    print color['blue'] + "Output Tweets to Elasticsearch:" + color['off']
    print color['cyan'] + "twint -u username -es localhost:9200" + color['off']
    print
    print color['blue'] + "Scrape Tweets and save as a json file:" + color['off']
    print color['cyan'] + "twint -u username -o file.json --json" + color['off']
    print
    print color['blue'] + "Save Tweets to a SQLite database:" + color['off']
    print color['cyan'] + "twint -u username --database tweets.db" + color['off']
    print
    print color['blue'] + "Scrape a Twitter user's followers:" + color['off']
    print color['cyan'] + "twint -u username --followers" + color['off']
    print
    print color['blue'] + "Scrape who a Twitter user follows:" + color['off']
    print color['cyan'] + "twint -u username --following" + color['off']
    print
    print color['blue'] + "Collect all the Tweets a user has favorited (gathers ~3200 tweet):" + color['off']
    print color['cyan'] + "twint -u username --favorites" + color['off']
    print
    print color['blue'] + "Collect full user information a person follows:" + color['off']
    print color['cyan'] + "twint -u username --following --user-full" + color['off']
    print
    print color['blue'] + "Use a slow, but effective method to gather Tweets from a user's profile (Gathers ~3200 Tweets, Including Retweets):" + color['off']
    print color['cyan'] + "twint -u username --profile-full" + color['off']
    print
    print color['blue'] + "Use a quick method to gather the last 900 Tweets (that includes retweets) from a user's profile:" + color['off']
    print color['cyan'] + "twint -u username --retweets" + color['off']
    print
    print color['blue'] + "Resume a search starting from the last saved scroll-id:" + color['off']
    print color['cyan'] + "twint -u username --resume resume_file.txt" + color['off']
    print
    print color['blue'] + "To get user info of followers:" + color['off']
    print color['cyan'] + "twint -u username --followers --user-full" + color['off']
    print
    print color['blue'] + "To get user info of following users:" + color['off']
    print color['cyan'] + "twint -u username --following --user-full" + color['off']
    print
    print color['blue'] + "To get only user info of user:" + color['off']
    print color['cyan'] + "twint -u username --user-full" + color['off']
    print
    print color['blue'] + "To get user info of users from a userlist:" + color['off']
    print color['cyan'] + "twint --userlist inputlist --user-full" + color['off']
    print
    print
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)	


# Menu 3
def menu3():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "git clone https://github.com/thelinuxchoice/userrecon.git" + color['off']
    print color['cyan'] + "cd userrecon" + color['off']
    print color['cyan'] + "chmod +x userrecon.sh" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Start script:" + color['off']
    print color['cyan'] + "./userrecon.sh" + color['off']
    print
    print	
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)	


# Menu 4
def menu4():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "git clone https://github.com/Mebus/cupp.git" + color['off']
    print color['cyan'] + "cd cupp" + color['off']
    print color['cyan'] + "chmod +x cupp.py" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Start script:" + color['off']
    print color['cyan'] + "./cupp.py -i" + color['off']
    print
    print	
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)


# Menu 5
def menu5():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "git clone https://github.com/DarkSecDevelopers/HiddenEye.git" + color['off']
    print color['cyan'] + "cd HiddenEye" + color['off']
    print color['cyan'] + "sudo pip3 install -r requirements.txt" + color['off']
    print color['cyan'] + "chmod +x HiddenEye.py" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Start script:" + color['off']
    print color['cyan'] + "./HiddenEye.py" + color['off']
    print
    print	
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)


# Menu 6
def menu6():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "Preinstalled on Kali Linux" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Create hash file from zip:" + color['off']
    print color['cyan'] + "zip2john 'name'.zip > 'hash'.txt" + color['off']
    print
    print color['blue'] + "Crack the hash with wordlist:" + color['off']
    print color['cyan'] + "john --format=zip 'hash'.txt > 'password'.txt" + color['off']
    print
    print	
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)


# Menu 7
def menu7():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Installation:" + color['off']
    print color['cyan'] + "Preinstalled on Kali Linux" + color['off']
    print
    print
    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Create zip of file:" + color['off']
    print color['cyan'] + "zip -r 'name'.zip file" + color['off']
    print
    print color['blue'] + "Create zip with password:" + color['off']
    print color['cyan'] + "zip --password '1234' 'name'.zip 'file.txt'" + color['off']
    print
    print color['blue'] + "Unzip file:" + color['off']
    print color['cyan'] + "tar xvf filename.zip'" + color['off']
    print
    print color['blue'] + "Unzip file:" + color['off']
    print color['cyan'] + "unzip filename.zip'" + color['off']
    print
    print	
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)


# Menu 9
def menu9():
    os.system('clear')
    user = os.getuid()
    if user != 0:
	print color['blue'] + "    It's recomended to run this script with root privileges!      " + color['off']

    print color['red'] +"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
    print "┃                                                                ┃"
    print color['red'] + "┃ " + color['red'] + "███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     ██╔════╝ ┃"
    print color['red'] +  "┃ " + color['red'] + "██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     ███████╗ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     ╚════██║ ┃"
    print color['red'] +  "┃ " + color['red'] + "██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗███████║ ┃"
    print color['red'] +  "┃ " + color['red'] + "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ┃"
    print "┃                                                                ┃"
    print "┃  " + color['red'] + "======================== 𝓫𝔂 𝓰𝓷𝓾𝓼𝓼𝓮 =======================    ┃"# + color['off']
    print "┃                                                                ┃"
    print "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + color['off']


    print color['blink'] + color['white'] + color['bg'] + "Commands:" + color['off']
    print color['blue'] + "Edit terminal launch options:" + color['off']
    print color['cyan'] + "leafpad .bashrc" + color['off']
    print
    print color['blue'] + "Login as root:" + color['off']
    print color['cyan'] + "su" + color['off']
    print
    print color['blue'] + "Delete folder:" + color['off']
    print color['cyan'] + "rm -R folder/" + color['off']
    print
    print color['blue'] + "Create folder:" + color['off']
    print color['cyan'] + "mkdir folder" + color['off']
    print
    print color['blue'] + "Show files directory:" + color['off']
    print color['cyan'] + "ls" + color['off']
    print
    print color['blue'] + "Show current directory:" + color['off']
    print color['cyan'] + "pwd" + color['off']
    print
    print color['blue'] + "Open current directory in files:" + color['off']
    print color['cyan'] + "xdg-open ." + color['off']
    print
    print color['blue'] + "Create txt file:" + color['off']
    print color['cyan'] + "cat > 'name'.txt" + color['off']
    print
    print	
    choice = raw_input(color['red'] + "Press enter to continue..." + color['off'])
    exec_menu(choice)
	

 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()
 
# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    '9': menu9,
#    '9': back,
    '0': exit,
}
 
# =======================
#      MAIN PROGRAM
# =======================
 
# Main Program
if __name__ == "__main__":
    # Launch main menu

    #Check if /usr/share/doc/manuals exists
    if os.path.exists("/usr/share/doc/manuals"):
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--all", help="List all manuals in categories",
                            action="store_true")
        parser.add_argument("-ca", "--catt", help="List manuals for catt script",
                        action="store_true")
        parser.add_argument("-tw", "--twint", help="List manuals for twint script",
                            action="store_true")
        parser.add_argument("-us", "--userrecon", help="List manuals for userrecon script",
                            action="store_true")
        parser.add_argument("-cu", "--cupp", help="List manuals for cupp script",
                            action="store_true")
        parser.add_argument("-he", "--hiddeneye", help="List manuals for HiddenEye script",
                            action="store_true")
        parser.add_argument("-jo", "--john", help="List manuals for john script",
                            action="store_true")
        parser.add_argument("-zi", "--zip", help="List manuals for basic zip archives",
                            action="store_true")
        parser.add_argument("-nav", "--navigation", help="List manuals for must known navigation commands",
                            action="store_true")
        parser.add_argument("-ve", "--version", help="Display current version of manuals",
                            action="store_true")
        parser.add_argument("-up", "--update", help="Search and update to the newest version",
                            action="store_true")
        args = parser.parse_args()
        if args.all:
            main_menu()
        elif args.catt:
	    menu1()
        elif args.twint:
	    menu2()
        elif args.userrecon:
	    menu3()
        elif args.cupp:
	    menu4()
        elif args.hiddeneye:
	    menu5()
        elif args.john:
	    menu6()
        elif args.zip:
	    menu7()
        elif args.navigation:
	    menu9()
        elif args.version:
	    os.system('clear')
	    print color['white'] + color['bg'] + "Current version of manuals by gnusse is: 1.0.1" + color['off']
	    exit()
        elif args.update:
	    user = os.getuid()
    	    if user != 0:
	        os.system('clear')
	        print color['white'] + color['bg'] + "You need to run this script with root privileges! Type 'sudo ./manuals.py'" + color['off']
	        exit()
	    else:
                print color['white'] + color['bg'] + "Installing 'manuals.py'... Please wait and DO NOT EXIT this script!" + color['off']
                os.system('cd /usr/share/doc/manuals/updater && chmod +x update.sh && ./update.sh')
                exit()
        else:
	    main_menu()
    else:
	user = os.getuid()
    	if user != 0:
	    os.system('clear')
	    print color['white'] + color['bg'] + "You need to run this script with root privileges! Type 'sudo ./manuals.py'" + color['off']
	else:
            print color['white'] + color['bg'] + "Installing 'manuals.py'... Please wait and DO NOT EXIT this script!" + color['off']
            os.system("cd updater && chmod +x update.sh && bash ./update.sh")
            exit()




    
   
    





















