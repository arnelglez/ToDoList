from flet import *

from mod.modToDo import eToDo,mToDo

from views.Task import Task
import config

class ToDo(UserControl):
        
    def __init__(self, h, w):
        
        self.mToDo = mToDo(config._eLogin.get_token())
        self.h = h
        self.w = w
        
        self._container = Container(
                padding = 8,
                content = Column(
                    scroll = True, 
                    controls=[
                    ]
                )
            )  
        
        self._dialog_add = AlertDialog(
                    content = Container(
                        height = 250,
                        width = 300,
                        alignment = alignment.center,
                        content = Column(
                            alignment = MainAxisAlignment.CENTER,
                            spacing = 25,
                            controls=[
                                TextField(
                                    width = 250,
                                    border="underline",
                                    label = 'Task',                
                                    color = colors.WHITE24,
                                    border_color = colors.WHITE24,
                                ),
                                TextField(
                                    width = 250,
                                    border="underline",
                                    label = 'Description',                                    
                                    multiline = True,
                                    color = colors.WHITE24,
                                    border_color = colors.WHITE24,
                                ),
                                ElevatedButton(
                                    on_click = self.task_add,
                                    bgcolor = colors.BLUE_700,
                                    content = Text(
                                        value = "ADD",
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
                                    width = 250,
                                )
                            ]
                        )
                    )
                )

        super().__init__()
    
    def task_add(self, e):
        etodo = eToDo()
        etodo.set_id('')
        etodo.set_task(self._dialog_add.content.content.controls[0].value)
        etodo.set_description(self._dialog_add.content.content.controls[1].value)
        self._dialog_add.content.content.controls[0].value = ''
        self._dialog_add.content.content.controls[1].value = ''
        
        response, etodo = self.mToDo.create_toDo(etodo)
        
        if response == '':
            self._container.content.controls.append(Task(etodo))
        else:
            e.page.controls[0].content.value = response
            e.page.controls[0].open = True             
        
        self._dialog_add.open = False
        e.page.update()
        
        
        self._container.content.update()
    
    def task_click(self, e):
        e.page.dialog = self._dialog_add
        self._dialog_add.open = True
        e.page.update()      
        
    def build(self):
               
        _button = Column(
            width = self.w,
            alignment = MainAxisAlignment.END,
            horizontal_alignment = 'end',
                controls = [
                    Container(
                        padding=padding.only(right=30, bottom=40),
                        content = FloatingActionButton(
                            icon = icons.ADD,
                            on_click = self.task_click,
                            bgcolor = colors.BLUE_700,
                            shape = CircleBorder(),
                        )
                    )
                ]
            )
        
        _, taskList = self.mToDo.list_toDo()        
        
        for etodo in taskList:
            self._container.content.controls.append(Task(etodo))
            
        return  Container(
                    height = self.h,
                    width = self.w,
                    bgcolor = colors.BLACK,
                    content = Stack(
                        controls = [
                            self._container,
                            _button
                        ]
                    )        
                )   