from flet import *
from threading import Thread

from views.Login import Login

def main(page:Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"    
    page.padding = 5
    page.bgcolor = colors.BLACK
    
    h = page.window_height
    w = page.window_width
    
    page.add(Login(h, w))   
    page.update()    

    
if __name__ == '__main__':
    app(target=main)