from flet import *
from threading import Thread

from mod.modLogin import mLogin
from views.Login import Login
from views.ResetPass import ResetPass

import config


def main(page:Page):
    
    def logout(e):        
        mlogin = mLogin()
        status, response = mlogin.logout(config._eLogin.get_token())
        
        if status == '':
            page.controls.pop()
            _app_bar.actions[0].visible = False
            page.controls.append(Login(h, w))
        else:
            _snack_bar.value = response
            _snack_bar.open = True
        
        page.update()        
    
    def reset_password(e):
        page.controls.pop()
        page.controls.append(ResetPass(h, w))
        page.update()
    
    _app_bar = AppBar(
        title=Text(
                value = "ToDo App",
            ),
        center_title=False,
        bgcolor=colors.BLUE_700,
        actions = [            
            PopupMenuButton( 
                visible = False,
                items = [
                    PopupMenuItem(
                            text="Reset Password",
                            on_click = reset_password
                        ),
                    PopupMenuItem(),
                    PopupMenuItem(
                            text="Logout",
                            on_click = logout
                        ),
                ]
            ),       
        ]
    )
            
    _snack_bar = SnackBar(
            bgcolor = colors.RED,
            content = Text(
                value = "",
                color = colors.WHITE,
            )        
        )
    
    
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 5   
    page.appbar = _app_bar
    page.bgcolor = colors.BLACK
    h = page.window_height - 75
    w = page.window_width
    
    page.add(_snack_bar, Login(h, w))   
    #page.add(_snack_bar, ResetPass(h, w))   
    page.update()    

    
if __name__ == '__main__':
    app(target=main)