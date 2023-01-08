from flet import *
import requests


HEIGHT = 590
WIDTH = 280

def main(page:Page):
    
    
    ############################################################################
    ################################## LOGIN ###################################
        
    def login_function(e):
        username = _login_container.content.controls[1].value
        password = _login_container.content.controls[2].value
        
        url = 'http://localhost:8000/login/'
        data = {
            "username" : username,
            "password" : password
        }

        r = requests.post(url=url, data=data)
        
        if r.status_code == 200:
            token = r.json()
            _login_container.visible = False
            _todo_container.visible = True
            _main_container.content.update()
        else:
            _snack_bar.content.value = r.json()
            _snack_bar.open = True
            _main_container.content.update()

    _snack_bar = SnackBar(
                    bgcolor = colors.RED,
                    content = Text(
                        value = "",
                        color = colors.WHITE,
                    )            
                )

    _login_container = Container(
        height =  520,
        width = WIDTH,
        visible = True,
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
                    on_click = login_function,
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
    
    
############################################################################
################################## ToDo ####################################
    _todo_container = Container(
        height =  HEIGHT,
        width = WIDTH,
        bgcolor = colors.WHITE,
        visible = False,
        content = Column()
    )
    

############################################################################
################################## MAIN ####################################
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    _main_container = Container(
        height = HEIGHT,
        width = WIDTH,
        bgcolor = colors.BLACK,
        border_radius=25,
        content = Stack(
            height = HEIGHT,
            width = WIDTH,
            controls = [
                _login_container,
                _todo_container,
                _snack_bar,
            ]
        )        
    )    
    
    page.add(_main_container)   
    page.update()    
    
if __name__ == '__main__':
    app(target=main)
    
