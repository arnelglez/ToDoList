from flet import *

from mod.modLogin import mLogin
from views.ToDo import ToDo
import config


class ResetPass(UserControl):
    def __init__(self, h, w):
        self.h = h
        self.w = w
        
        self._container_buttom = Container(
                            content = Row(
                                alignment = 'center',
                                controls = [
                                    ElevatedButton(
                                        on_click = self.back_todo,
                                        bgcolor = 'transparent',
                                        content = Text(
                                            value = "Back",
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
                                        width = 120,
                                    ),
                                    ElevatedButton(
                                        on_click = self.reset_password,
                                        bgcolor = colors.BLUE_700,
                                        content = Text(
                                            value = "Reset",
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
                                        width = 120,
                                    ),
                                ]
                            )   
                        )  
                
        self._container = Container(
                #height =  520,
                alignment = alignment.center,
                content = Column(
                    horizontal_alignment = "center",
                    alignment = MainAxisAlignment.CENTER,
                    spacing = 15,
                    controls = [
                        Container(
                          content=Column(
                                horizontal_alignment = "center",
                                alignment = MainAxisAlignment.CENTER,
                                controls = [
                                  Text(
                                    value = config._eLogin.euser.get_username(),
                                    size = 15,
                                  ),
                                  Text(
                                    value = config._eLogin.euser.get_email(),
                                    size = 15,
                                  ),
                                  Text(
                                    value = config._eLogin.euser.get_first_name() + config._eLogin.euser.get_last_name(),
                                    size = 15,
                                  ),
                              ]
                          )  
                        ),
                        TextField(
                            width = 250,
                            height = 40,
                            label = 'Password',
                            color = colors.WHITE24,
                            border_color = colors.WHITE24,
                            border_width = 2,
                            password = True,
                            can_reveal_password=True,
                        ),
                        TextField(
                            width = 250,
                            height = 40,                            
                            label = 'Repit Password',
                            color = colors.WHITE24,
                            border_color = colors.WHITE24,
                            border_width = 2,
                            password = True,
                            can_reveal_password=True,
                        ),
                        self._container_buttom                      
                    ]
                )
            )
        
        super().__init__()
        
    def back_todo(self, e):        
        e.page.controls.pop()
        e.page.controls.append(ToDo(self.h, self.w))
        e.page.update()
        
    def reset_password(self,e):
        mlogin = mLogin()
        password1 = self._container.content.controls[1].value
        password2 = self._container.content.controls[2].value
        
        self._container.content.controls[1].value = ''
        self._container.content.controls[2].value = ''
        
        response = mlogin.change_password(password1, password2, config._eLogin.get_token())
        
        if response == '':
            e.page.controls.pop()
            e.page.controls.append(ToDo(self.h, self.w))
        else:                
            e.page.controls[0].content.value = response
            e.page.controls[0].open = True      
            
        e.page.update()
    
    def build(self):
        return  Container(
                height = self.h,
                width = self.w,
                bgcolor = colors.BLACK,
                content = Stack(
                    controls = [
                        self._container
                    ]
                )        
            )   