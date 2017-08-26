#!/usr/bin/python
import sys
import requests
import json
from bs4 import BeautifulSoup
from trello import TrelloClient
import trello

# put YOUR OWN tokens and links: Acessing Trello API
client = TrelloClient(
    api_key = 'b73de31e08da26472b075844c721b1bd',
    api_secret = '4f97c7e74b53d73da621bded40e788096489739c1d8e11e641dedad8ec57310a',
    token = 'c55dd42607c284779a785be12ee7fcf55e4b2ca5f47e15fcd7cdd9c7b880adbf'
    )

all_boards = client.list_boards()
grocery = all_boards[0]
all_list = grocery.list_lists()
shoplist = all_list[0]

print shoplist

def barcode_reader():

    """Barcode code obtained from 'brechmos' 
    https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=55100"""
    hid = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm',
           17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y',
           29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ',
           45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';', 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}

    hid2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',
            17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y',
            29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ',
            45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}

    fp = open('/dev/hidraw0', 'rb')

    ss = ""
    shift = False

    done = False

    while not done:

        ## Get the character from the HID
        buffer = fp.read(8)
        for c in buffer:
            if ord(c) > 0:

                ##  40 is carriage return which signifies
                ##  we are done looking for characters
                if int(ord(c)) == 40:
                    done = True
                    break;

                ##  If we are shifted then we have to
                ##  use the hid2 characters.
                if shift:

                    ## If it is a '2' then it is the shift key
                    if int(ord(c)) == 2:
                        shift = True

                    ## if not a 2 then lookup the mapping
                    else:
                        ss += hid2[int(ord(c))]
                        shift = False

                ##  If we are not shifted then use
                ##  the hid characters

                else:

                    ## If it is a '2' then it is the shift key
                    if int(ord(c)) == 2:
                        shift = True

                    ## if not a 2 then lookup the mapping
                    else:
                        ss += hid[int(ord(c))]
    return ss

## United States version made by Jaekeun LEE ##

def UPC_lookup(code):

    link = "https://www.upcdatabase.com/item/" + str(code)
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    table = soup.find('table')
    x = (len(table.findAll('tr')) - 1)
    title = []
    for row in table.findAll('tr')[1:x]:
        col = row.findAll('td')

        b = col[2].get_text()

        title.append(b)

    return (title[1:2])


## KOREAN VERSION MADE BY JAEKEUN LEE ##
def KAN_lookup(code):
    link = "http://www.koreannet.or.kr/home/hpisSrchGtin.gs1?gtin=" + str(code)
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    pars = soup.find("div", {"class" : "productTit"})
    raw = pars.get_text()
    clean = unicode.split(raw)
    alpha = clean[1:]
    product = u''.join(alpha)
    return product




def add_grocery_item(item):
    """Adds the given item to the grocery list """
    shoplist.add_card(name = unicode(item))   



if __name__ == '__main__':
    try:
        while True:
            print 'Waiting for Scanning...'
            scan = barcode_reader()
            try:
                item = KAN_lookup(scan)
                print "Scanned barcode : '{0}'".format(scan)
                print item
                add_grocery_item(item)
                    

            except AttributeError:
                try:
                     item = UPC_lookup(scan)
                     print "Scanned barcode : '{0}'".format(scan)
                     print item
                     add_grocery_item(item)
                except AttributeError:
                     print "no barcode information"
                                         

                except KeyboardInterrupt:
                    break
    finally:
        print "Grocery list completed!"










