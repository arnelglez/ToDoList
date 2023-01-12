
from flet import *

from views.ToDo import ToDo
from mod.modLogin import mLogin

import config

class Login(UserControl):
    
    def __init__(self, h, w):
        
        self.mLogin = mLogin()
        self.h = h
        self.w = w
        
        self._container = Container(
                #height =  520,
                alignment = alignment.center,
                content = Column(
                    horizontal_alignment = "center",
                    alignment = MainAxisAlignment.CENTER,
                    height = 250,
                    width = 300,
                    spacing = 15,
                    controls = [
                        Icon(
                        name = icons.ACCOUNT_CIRCLE_SHARP,  
                        size = 100,
                        color = colors.WHITE24,
                        ),
                        TextField(
                            width = 250,
                            height = 40,
                            prefix_icon = icons.ACCOUNT_CIRCLE,
                            label = 'Username',
                            border_width = 2,
                            color = colors.WHITE24,
                            border_color = colors.WHITE24,
                            border_radius = 10,
                            value = 'aglez', #borrar
                        ),
                        TextField(
                            width = 250,
                            height = 40,
                            prefix_icon = icons.KEY,
                            label = 'Password',
                            border_width = 2,
                            color = colors.WHITE24,
                            border_color = colors.WHITE24,
                            border_radius = 10,
                            password = True,
                            can_reveal_password=True,
                            value = 'Pepe123++', #borrar
                        ),
                        ElevatedButton(
                            on_click = self.login_click,
                            bgcolor = colors.BLUE_700,
                            content = Text(
                                value = "Login",
                                weight = 'bold',
                                color = 'white',
                            ),
                            style = ButtonStyle(
                                shape = {
                                    "": RoundedRectangleBorder(radius=8),
                                },
                                color = {
                                    "": 'white',
                                },
                            ),   
                            height = 40,
                            width = 250,
                        )
                        
                    ]
                )
            )
        
        self._dialog_ring = AlertDialog(
                content = Container(
                    height = 50,
                    padding = padding.only(top=20),
                    alignment = alignment.center,
                    content = ProgressRing(
                    )
                )
            )
                
        super().__init__()
        
    def login_click(self, e):
                
        e.page.dialog = self._dialog_ring
        self._dialog_ring.open = True
        e.page.update()
        
        username = self._container.content.controls[1].value
        password = self._container.content.controls[2].value        
        
        self._container.content.controls[1].value = ''
        self._container.content.controls[2].value = ''

        response, config._eLogin = self.mLogin.login(username, password)
        
        if response == '':
            e.page.controls.pop()            
            e.page.appbar.actions[0].visible = True
            e.page.controls.append(ToDo(self.h, self.w))
            
        else:
            e.page.controls[0].content.value = response
            e.page.controls[0].open = True
            self.update()
        
        # progress ring close
        self._dialog_ring.open = False
        e.page.update()
        
    def build(self):
        return  Container(
                    bgcolor = colors.BLACK,
                    height = self.h,
                    content = Stack(
                        controls = [
                            self._container,
                        ]
                    )        
                )   