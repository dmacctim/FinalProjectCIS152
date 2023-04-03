import tkinter
from Event import Event


def popup_event():
    add_event_window = tkinter.Toplevel(window)
    add_event_window.wm_geometry('330x100')

    event_name_label = tkinter.Label(add_event_window, text='Event Name: ')
    event_name_label.grid(row=1, column=1, padx=(10, 0), pady=10)

    event_entry = tkinter.Entry(add_event_window, font=FONT)
    event_entry.grid(row=1, column=2, padx=(0, 10), pady=10)

    submit_event_button = tkinter.Button(add_event_window, text='Add Event', font=FONT, command=lambda: [add_event(event_entry.get()), add_event_window.destroy()])
    submit_event_button.grid(row=2, column=1, padx=(50, 0), pady=10)
    cancel_button = tkinter.Button(add_event_window, text='Cancel', font=FONT, command=add_event_window.destroy)
    cancel_button.grid(row=2, column=2, pady=10)


def add_event(event):
    event_to_add = Event(event)
    events.append(event_to_add)
    event_names.append(event_to_add.name)
    print(events)
    print(event_names)
    event_dropdown["menu"].delete(0, 'end')

    for event in event_names:
        event_dropdown["menu"].add_command(label=event)


window = tkinter.Tk()
window.title("Rubik's Cubing Event Manager")
window.option_add('*font', 'Arial 12')
window.geometry('900x500')
frame = tkinter.Frame(window)
frame.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)
FONT = ('Arial', 12)
event_3x3 = Event('3x3')

event_names = [event_3x3.name]
events = [event_3x3]
clicked = tkinter.StringVar()
clicked.set('Select an Event')

event_dropdown = tkinter.OptionMenu(frame, clicked, *event_names)
event_dropdown.grid(row=1, column=0)
add_event_button = tkinter.Button(frame, text='Add Event', font=FONT, command=popup_event)
add_event_button.grid(row=2, column=0)


if __name__ == '__main__':
    window.mainloop()
