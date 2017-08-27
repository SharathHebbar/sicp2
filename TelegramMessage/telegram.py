import telepot
from telepot.loop import MessageLoop
from pprint import pprint
# Put your own bot token inside the bracket
bot = telepot.Bot('397297646:AAGKc3jby4gORPHoigqcW3p7oxeYfnMHGtE')


def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()

#### After bot.sendMessage(input id that you want to send message, "Message")
bot.sendMessage(334674957, 'Hey!')

