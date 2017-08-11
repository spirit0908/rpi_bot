import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import sys 
import subprocess

"""
After **inserting token** in the source code, run it:

```
$ python2.7 diceyclock.py
 ```

[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

pizza_list = ['Buffalo', 'Calzone', 'Chicken BBQ', 'Chicken cheese', 'Chorizo',
              'Delicatessen', 'Hot fever', 'Merguez', 'Regina', 'Royal', 'Special',
              'Vegetarienne', 'Fajitas', 'Oceane', '4 Fromages', 'Chevre miel',
              'Grand large', 'Mythic burger', 'Raclette', 'Rustique au chevre', 'Steak roquefort',
              'Tartiflette', 'Dauphinoise', 'Magret cepes', 'Pizza cheezy s', 'Savoyarde',
              'Primavera', '2 Saumons', 'Fois gras', 'Margherita']

grimpette_choice = [
    'Allez go maintenant!',
    'Ce soir',
    'Oui demain, oublies pas tes affaires',
    'Hum ca fait beaucoup de grimpe en ce moment...',
    'Falaise ce weekend!',
    'Tu veux pas une biere plutot...',
    'Grimpe, pizza, biere... Elle est pas belle la vie!',
    'Ouais on motive Arthur pour demain!']

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    username= msg['from']['first_name']

    print 'Got command: %s' % command
    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/pizza':
        pizza_num = random.randint(0, len(pizza_list)-1)
        bot.sendMessage(chat_id, pizza_list[pizza_num])
    elif command == '/grimpe':
        grimpette_num = random.randint(0, len(grimpette_choice)-1)
        bot.sendMessage(chat_id, grimpette_choice[grimpette_num])
    elif command == '/portail':
        bot.sendMessage(chat_id, "Calling...")
        subprocess.call('call_gate.sh', shell=True)
        subprocess.call('gate_announce.sh ' + format(username) + ' & ', shell=True )
        bot.sendMessage(chat_id, "Done. go go go!")
    elif command == '/intercom':
        bot.sendMessage(chat_id, "Openning door...")
        subprocess.call('interphone.sh', shell=True)
        bot.sendMessage(chat_id, "Done.")

bot = telepot.Bot('*** API Token ***')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
   time.sleep(10)
