from random import choice
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
book = Actor("matt")
book_titles = ['matt', 'carrie', 'pythonkids', 'sensors', 'meerkat']
book.pos = 255, 340 
  
WIDTH = 510
HEIGHT = 680

book_number = 1
    
def draw():
    global book, book_number
    screen.clear()
    book.draw()
    clock.schedule_interval(check_shake,1.0)
    
def check_shake():
    global book, book_number
    x, y, z = sense.get_accelerometer_raw().values()
    if x>2 or y>2 or z>2:
        book = Actor(book_titles[book_number])
        book_number += 1
        book_number = book_number % len(book_titles)
        
