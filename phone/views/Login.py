
from flet import *

from views.ToDo import ToDo
from mod.modLogin import eLogin, mLogin

class Login(UserControl):
    
    def __init__(self, h, w):
        
        self.eLogin = eLogin()
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
                    width = 250,
                    controls = [
                        Icon(
                        name = icons.ACCOUNT_CIRCLE_SHARP,  
                        size = 100,
                        color = colors.WHITE24,
                        ),
                        TextField(
                            width = 200,
                            height = 30,
                            prefix_icon = icons.ACCOUNT_CIRCLE,
                            text_size = 12,
                            label = 'Username',
                            color = colors.WHITE24,
                            border_color = colors.WHITE24,
                            border_radius = 10,
                        ),
                        TextField(
                            width = 200,
                            height = 30,
                            prefix_icon = icons.KEY,
                            text_size = 12,
                            label = 'Password',
                            color = colors.WHITE24,
                            border_color = colors.WHITE24,
                            border_radius = 10,
                            password = True,
                            can_reveal_password=True,
                        ),
                        ElevatedButton(
                            on_click = self.login_click,
                            bgcolor = colors.BLUE_700,
                            content = Text(
                                value = "Login",
                                size = 11,
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
                            height = 30,
                            width = 200,
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

        response, self.eLogin = self.mLogin.login(username, password)
        if response == '':
            e.page.controls.pop()
            # lista de tareas
            e.page.controls.append(ToDo(self.h, self.w, self.eLogin))
        else:
            e.page.controls[0].content.value = response
            e.page.controls[0].open = True
            self.update()
        
        # progress ring close
        self._dialog_ring.open = False
        e.page.update()
        
    def build(self):
        return  Container(
                    expand = True,
                    bgcolor = colors.BLACK,
                    border_radius=25,
                    content = Stack(
                        controls = [
                            self._container,
                        ]
                    )        
                )   