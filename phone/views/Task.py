from flet import *

from mod.modToDo import eToDo, mToDo
from ent.entLogin import eLogin

class Task(UserControl):
    def __init__(self, etodo:eToDo , elogin:eLogin, ):
        
                
        self._task_container = Container(
            alignment = alignment.top_left,
            bgcolor = colors.BLUE_GREY,
            border_radius = 20,
            padding = 10,
            content=Column(
                controls= [
                    Container( # this container contain task id
                        visible = False,
                        content=Text(
                                value = etodo.get_id(),
                            ),
                    ),
                    Text(
                        value = etodo.get_task(),
                        size = 13,
                        weight = "bold",
                        text_align = "center",
                    ),
                    Text(
                        value = etodo.get_description(),
                        size = 11,
                    ),
                    Container(
                        alignment = alignment.center_right,
                        content=Row(
                            alignment = MainAxisAlignment.END,
                            controls = [
                                IconButton(
                                    icon = icons.EDIT_NOTE,
                                    icon_color = colors.GREEN_ACCENT_700,                                    
                                    icon_size = 20,
                                    on_click= self.update_click,
                                ),
                                IconButton(
                                    icon = icons.DELETE,
                                    icon_color = colors.RED_600,                                    
                                    icon_size = 20,
                                    on_click= self.delete,
                                ),
                            ]
                        )
                    ),
                ]
            )
        )        
        
        self._dialog_add = AlertDialog(
                    content = Container(
                        height = 250,
                        width = 250,
                        alignment = alignment.center,
                        content = Column(
                            alignment = MainAxisAlignment.CENTER,
                            spacing = 25,
                            controls=[
                                TextField(
                                    width = 150,
                                    border="underline",
                                    text_size = 12,
                                    label = 'Task',                
                                    color = colors.WHITE24,
                                    border_color = colors.WHITE24,
                                ),
                                TextField(
                                    width = 150,
                                    border="underline",
                                    text_size = 12,
                                    label = 'Description',                                    
                                    multiline = True,
                                    color = colors.WHITE24,
                                    border_color = colors.WHITE24,
                                ),
                                ElevatedButton(
                                    on_click = self.update,
                                    bgcolor = colors.BLUE_700,
                                    content = Text(
                                        value = "Update",
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
                                    width = 150,
                                )
                            ]
                        )
                    )
                )
        
        self._snack_bar = SnackBar(
                bgcolor = colors.RED,
                content = Text(
                    value = "",
                    color = colors.WHITE,
                )        
            )
        
        self.mToDo = mToDo(elogin.get_token())
        self.eLogin = elogin
        self.id = self._task_container.content.controls[0].content.value
        super().__init__()
    
    def create(self, e):
        eTodo = eToDo()
        eTodo.set_task(self._task_container.content.controls[2].value)
        eTodo.set_description(self._task_container.content.controls[1].value)
        response, eTodo = self.mToDo.create_toDo(eTodo)
        
        if response == '':
            self._task_container.content.controls[0].content.value = eTodo.get_id()
            self._task_container.content.controls[1].value = eTodo.get_description() 
            self._task_container.content.controls[2].content.value = eTodo.get_task()
            self._task_container.content.update()
        else:
            self._snack_bar.content.value = response
            self._snack_bar.open = True
            self.update()
            
        e.page.update()
    
    def update_click(self, e):
        self._dialog_add.content.content.controls[1].value = self._task_container.content.controls[2].value
        self._dialog_add.content.content.controls[0].value = self._task_container.content.controls[1].value        
        e.page.dialog = self._dialog_add
        self._dialog_add.open = True
        e.page.update()      
        
    def update(self, e):
        eTodo = eToDo()
        eTodo.set_id(self.id)
        eTodo.set_task(self._dialog_add.content.content.controls[0].value)
        eTodo.set_description(self._dialog_add.content.content.controls[1].value)
        
        response, eTodo = self.mToDo.update_toDo(eTodo)
                
        if response == '':
            self._task_container.content.controls[0].content.value = eTodo.get_id()
            self._task_container.content.controls[1].value = eTodo.get_description() 
            self._task_container.content.controls[2].content.value = eTodo.get_task()
            self._task_container.content.update()
        else:
            self._snack_bar.content.value = response
            self._snack_bar.open = True
            self.update()
            
        e.page.update()
            
    
    def delete(self, e):
        
        response = self.mToDo.delete_toDo(self.id)        
        
        if response == '':
            e.page.controls[0].controls[0].content.controls[0].content.controls.remove(self)
            e.page.controls[0].controls[0].content.controls[0].content.update()

        else:
            self.snack.content.value = response
            self.snack.content.open = True
       
        e.page.update()
        
    def build(self):
        return Container (
            content = self._task_container
        )
        