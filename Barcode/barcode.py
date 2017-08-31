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


def UPC_lookdown(code):
    

    link = "http://www.upcitemdb.com/upc/" + str(code)
    source_code = requests.get(link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    table = soup.find('p')
    name = table.find('b').get_text()
    
    return name

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
            scan = int(raw_input())
            try:
                item = KAN_lookup(scan)
                print "Scanned barcode : '{0}'".format(scan)
                print item
                add_grocery_item(item)
                    

            except AttributeError:
                try:
                     item = UPC_lookup(scan)
                     
                     print "Scanned barcode : '{0}'".format(scan)
                     if len(item)== 0:
                        try:
                            can = UPC_lookdown(scan)
                            print "Scanned barcode : '{0}'".format(scan)
                            print can
                            add_grocery_item(can)
                        except:
                            pass 
                     else:
                         print item
                         add_grocery_item(item)
                except AttributeError:
                    print "Sorry No Barcode Information"                                         

                except KeyboardInterrupt:
                    break;

                    
    finally:
        print "Grocery list completed!"


