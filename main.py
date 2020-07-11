import pyautogui as bot
import sys
import time as t
from config import *

# functions

def wait(x):
    t.sleep(x)


def move(x, direction):

    for i in range(x):
        bot.press(direction)


# inputs

projectName = sys.argv[1]
projectType = sys.argv[2]
projectNumber = sys.argv[3]
codepen = sys.argv[4]
auth = sys.argv[5]


# open terminal

bot.hotkey('ctrl', 'alt', 't')

wait(3)

# move to Code folder

bot.write('cd Code/')

bot.press('enter')

# check type of the project

if (projectType == 'html'):
    bot.write('cd HCode')
elif (projectType == 'js'):
    bot.write('cd JCode')

bot.press('enter')

# create project folder

bot.write('mkdir {}'.format(projectName))

bot.press('enter')

# change to new folder

bot.write('cd {}'.format(projectName))

bot.press('enter')

bot.write('cp ~/Downloads/Screenshot.png .')

bot.press('enter')

# copy templates for folder

bot.write('cp ~/Code/PyCode/autocodepush/templates/index.html .')

bot.press('enter')

bot.write('cp ~/Code/PyCode/autocodepush/templates/style.css .')

bot.press('enter')

bot.write('cp ~/Code/PyCode/autocodepush/templates/script.js .')

bot.press('enter')

bot.write('cp ~/Code/PyCode/autocodepush/templates/README.md .')

bot.press('enter')

bot.write('code .')

bot.press('enter')

wait(10)

bot.hotkey('ctrl', 'p')

bot.write('index.html')

wait(2)

bot.press('enter')

wait(2)

# go to first line

bot.hotkey('ctrl', 'g')

bot.write('1')

bot.press('enter')

# move and edit

move(5, 'down')

move(11, 'right')

if (projectType == 'html'):
    
    bot.write('{} | UI to Code (HTML5 & CSS3)'.format(projectName))

elif(projectType == 'js'):

    bot.write('{} | Vanilla Javascript'.format(projectName))

# save index.html

bot.hotkey('ctrl', 's')

wait(2)

# search for README and open

bot.hotkey('ctrl', 'p')

wait(2)

bot.write('README.md')

bot.press('enter')

wait(2)

# go to line 1

bot.hotkey('ctrl', 'g')

bot.write('1')

bot.press('enter')

wait(2)

# edit title




if (projectType == 'html'):

    bot.write('# {} | UI to Code (HTML5 & CSS3)'.format(projectName))

elif (projectType == 'js'):

    bot.write('# {} | Vanilla Javascript'.format(projectName))


# edit codepen link

bot.press('enter')

bot.press('enter')



bot.write('> Checkout Project on Codepen : https://codepen.io/vishnu_dileesh/pen/{}'.format(codepen))

# change screenshot title

bot.press('enter')

bot.press('enter')

bot.write('> ![{}](Screenshot.png)'.format(projectName))


# save README

bot.hotkey('ctrl', 's')

wait(1)

# close vs code

bot.hotkey('ctrl', 'q')

# git init

wait(2)

bot.write('git init')

bot.press('enter')

bot.write('git add .')

bot.press('enter')

bot.write('git commit -m "Initial Commit"')

bot.press('enter')

# git create repo

bot.write('gh repo create --public')

bot.press('enter')

wait(60)

if(auth == 'true'):


    bot.write(username)

    bot.press('enter')

    wait(2)

    bot.write(password)

    bot.press('enter')


wait(5)

bot.write('git remote set-url origin git@github.com:VishnuDileesh/{}.git'.format(projectName))

bot.press('enter')

bot.write('git push -u origin master')

bot.press('enter')






















