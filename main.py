from flet import *
from custom_checkbox import CustomCheckBox




def main (page: Page):
    hauteur = 785
    largeur = 400
    BG = '#041955'
    GRAY = '#808080'
    FG = '#3450a1'
    ORANGE = '#ffa500'
    page.adaptive = True
    
    hautPage = Container(bgcolor='#000', height=30, width=400)
    
    
        
    Photo_profil = Stack(
        controls=[
        Container(
            width=100,
            height=100,
            border_radius=50,
            bgcolor='white12'
            ),
        Container(
                    gradient=SweepGradient(
                        center=alignment.center,
                        start_angle=0.0,
                        end_angle=3,
                        stops=[0.5,0.5],
                    colors=['#00000000', ORANGE],
                    ),
                    width=100,
                    height=100,
                    border_radius=50,
                    content=Row(alignment='center',
                        controls=[
                            Container(padding=padding.all(5),
                            bgcolor=BG,
                            width=90,height=90,
                            border_radius=50,
                            content=Container(bgcolor=FG,
                                height=80,width=80,
                                border_radius=40,
                            content=CircleAvatar(opacity=0.8,
                                                 foreground_image_src='/Users/misterpy/Desktop/todo-app-with-flet/images/Profil.JPG'
                    # foreground_image_url="/Users/misterpy/Desktop/todo-app-with-flet/images/Profil.JPG"
                )
                            )
                            )
                        ],
                    ),
                ),
        
        ]
    )

        
    
    
    
    
    
    def shrink(e):
        page_2.controls[0].width=120
        page_2.controls[0].scale=transform.Scale(0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius=border_radius.only(top_left=35, top_right=0, bottom_left=35,
                                                            bottom_right=0)
        page_2.update()
    
    
    
    
    
    def restore(e):
        page_2.controls[0].width=400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale=transform.Scale(1, alignment=alignment.center_right)
        page_2.update()
    
    
    
    create_task_view = Container(content=Container(on_click=lambda _: page.go('/') ,
                                                   height=40, width=40, content=Text('x')))
    
    
    taches = Column(
        height=400,
        scroll='auto',
    )
   
   
    
    for i in range(10):
        taches.controls.append(Container(height=50, width=400, bgcolor=BG,
                                         border_radius=15,padding=padding.only(left=20, top=15), 
                                         content=CustomCheckBox(
                                             color=ORANGE,
                                             label=f'Tache {i+1}'
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
                                                                      border_radius=20, padding=padding.only(right=60, left=60), 
                                                                      content=Container(bgcolor=ORANGE))
                                                        ]
                                                    )))




    first_page_contents = Container(
        
        content = Column(controls = [
                                    Row(alignment='spaceBetween',
                                                controls=[Container(on_click=lambda e: shrink(e), content=Icon(icons.MENU)),
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
        Stack(controls=[taches, FloatingActionButton(bottom=120,right=20,bgcolor=ORANGE, icon=icons.ADD,
                                                     on_click=lambda _: page.go('/créé tâche')
                                                    )
                        ]
             )
                                    
                                    ]
        )
    )
    
    
    page_1 = Container(
        width=largeur, height=hauteur, bgcolor=BG, border_radius=35, padding=padding.only(left=50, top=50, right=200),
            
        content=Column(controls = [Row(alignment='end', controls = [Container(border_radius=25,padding=padding.only(top=13, left=15),height=50, width=50, 
                                                    border=border.all(color=ORANGE, width=2), on_click=lambda e: restore(e), content=Text('<'))
                                                ]
                                        ),
                                   Container(height=10),
                                   Photo_profil,
                                   Text('Agoh Chris', size=25, color=ORANGE, font_family='sans serif',weight='bold'),
                                   Container(height=10),
                                   Row(controls=[Icon(icons.FAVORITE_BORDER_SHARP, color='white80'), 
                                                 Text('Favoris', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                                                  
                                                  ]
                                       ),
                                   
                                   Container(height=10),
                                   
                                   Row(controls=[Icon(icons.CARD_TRAVEL_SHARP, color='white80'), 
                                                 Text('Catégories', size=15, weight=FontWeight.W_300, color='white', font_family='poppins')
                                                  
                                                  ]
                                       ),
                                   Container(height=10),
                                   
                                   Row(controls = [Icon(icons.CALCULATE_ROUNDED, color='white80'),
                                                    Text('Statistique', size=15, weight=FontWeight.W_300, color='white', font_family='poppins'),
                                                  
                                                 ]
                                       ),
                                    Image(src=f"/Users/misterpy/Desktop/todo-app-with-flet/images/1.png", width=300, height=100),
                                    
                                    Row(alignment='end', controls=[Text('Tout Droit Réservé', color=GRAY, font_family='poppins')]),
                                    Row(alignment='end', controls=[Text('🐍', size=40, weight='bold')])
                                   
                                    ])
    )
    
    
    
    page_2 = Row(alignment='end',
        controls=[
            Container(
                    Row(height=30, width=400, ),
                width=largeur, height=hauteur, 
                bgcolor=FG, border_radius=35, animate=animation.Animation(600, AnimationCurve.DECELERATE),
                                              animate_scale = animation.Animation(400, curve='decelerate'),
                                              padding = padding.only(top=50, left=20, right=20, bottom=5),
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
    
app(target=main, assets_dir='assets')