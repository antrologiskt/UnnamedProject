from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

# initiate app and set grid layout for invisible widget grid
app = App(title='Second GUI app', width=300, height=200, layout='grid')

# combo widget - grid arg = x,y 00 = top left corner
film_choice = Combo(app, options=['Star Wars',
                    'Batman', 'Indiana Jones'],
                    grid=[0,1], align='left')

# text widget that goes with combo
film_description = Text(app, text='Which film?', grid=[0,0], align='left')

# checkbox widget
vip_seat = CheckBox(app, text='VIP seat?', grid=[1,1], align='left')

# text widget that goes with checkbox
seat_question = Text(app, text='Seat type', grid=[1,0], align='left')

# buttongroup widget
row_choice = ButtonGroup(app, options=[['Front', 'F'], ['Middle', 'M'], ['Back', 'B']],
                         selected='M', horizontal=True, grid=[2,1], align='left')

# text widget for row_choice
seat_loc = Text(app, text='Seat location?', grid=[2,0], align='left')

user_film = []
user_seat = []
user_row = []
def do_booking():
    info('Booking', 'Thank you for booking')
    user_film.append(film_choice.get())
    user_seat.append(vip_seat.get_value())
    user_row.append(row_choice.get())
    print(user_film, user_seat, user_row)
# pushbutton widget to book seats
book_seats = PushButton(app, command=do_booking, text='Book seat', grid=[3,1], align='left')

app.display()

