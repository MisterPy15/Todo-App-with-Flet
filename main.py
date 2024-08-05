from flet import *
from custom_checkbox import CustomCheckBox




def main (page: Page):
    hauteur = 720
    largeur = 400
    BG = '#041955'
    FWG = '#9b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    ORANGE = '#ffa500'
    page.adaptive = True
        
    
    
    
    create_task_view = Container(content=Container(on_click=lambda _: page.go('/') ,
                                                   height=40, width=40, content=Text('x')))
    
    
    taches = Column(
        height=400,
        scroll='auto',
    )
    
    for i in range(10):
        taches.controls.append(Container(height=50, width=400, bgcolor=BG,
                                         border_radius=25,padding=padding.only(left=20, top=15), 
                                         content=CustomCheckBox(
                                             color=ORANGE,
                                             label='Créé un cotenu intéressant!'
                                         )))
        
    
    
    categories_cards = Row(scroll='auto')
    categories = ['Famille', 'Busnesse', 'Amis', 'Travail', 'Loisir']
    
    for i, Catego in enumerate(categories):
        categories_cards.controls.append(Container(bgcolor=BG, height=100, 
                                                    width=170, border_radius=15, padding=15, content=Column(
                                                        controls=[
                                                            Text('0 Tâche'),
                                                            Text(Catego),
                                                            Container(width=160, height=5, bgcolor='white12', 
                                                                      border_radius=20, padding=padding.only(right=i*30), 
                                                                      content=Container(bgcolor=ORANGE))
                                                        ]
                                                    )))




    first_page_contents = Container(
        content = Column( controls = [
                                    Row(alignment='spaceBetween',
                                                controls=[Container(content=Icon(icons.MENU)),
                                            Row(controls=[Icon(icons.SEARCH),
                                                          Icon(icons.NOTIFICATIONS_OUTLINED)]),]
                                            ),
        Text(value='Comment Vous allez Mister Py'),
        Text(value='CATEGORIES'),
        Container(padding = padding.only(top=10, bottom=20),
                  content = categories_cards
                  ),
        Container(height=20),
        Text("Tâches d'aujourd'huis"),
        Stack(controls=[taches, FloatingActionButton(bottom=35,right=20,bgcolor=ORANGE, icon=icons.ADD, 
                                                     on_click=lambda _: page.go('/créé tâche')
                                                    )
                        ]
             )
                                    
                                    ]
        )
    )
    
    
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=largeur, height=hauteur, 
                bgcolor=FG, border_radius=35, padding=padding.only(top=50, left=20, 
                                                                   right=20, bottom=5),
                content=Column(controls=[
                    first_page_contents
                ])
            )
        ]
    )


    container = Container(width=largeur, height=hauteur,
                         bgcolor=BG, border_radius=35, content=Stack(
                             controls=[
                                 page_1,
                                 page_2,
                             ]
                         ))
    
    
        
    pages={
        '/':View(
            "/",
            [
                container
            ],
        ),
            '/créé tâche' : View(
                            "/créé tâche",
                            [
                                create_task_view
                            ],
            )
}



    def  route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
            )
    
   

    
    page.add(container)




    page.on_route_change = route_change
    page.go(page.route)
    
app(target=main)