import tkinter
from Event import Event
from Participant import Participant


# def popup_event():
#     add_event_window = tkinter.Toplevel(window)
#     add_event_window.wm_geometry('330x100')
#
#     event_name_label = tkinter.Label(add_event_window, text='Event Name: ')
#     event_name_label.grid(row=1, column=1, padx=(10, 0), pady=10)
#
#     event_entry = tkinter.Entry(add_event_window, font=FONT)
#     event_entry.grid(row=1, column=2, padx=(0, 10), pady=10)
#
#     submit_event_button = tkinter.Button(add_event_window, text='Add Event', font=FONT, command=lambda: [add_event(event_entry.get()), add_event_window.destroy()])
#     submit_event_button.grid(row=2, column=1, padx=(50, 0), pady=10)
#     cancel_button = tkinter.Button(add_event_window, text='Cancel', font=FONT, command=add_event_window.destroy)
#     cancel_button.grid(row=2, column=2, pady=10)
#
#
# def add_event(event):
#     event_to_add = Event(event)
#     events.append(event_to_add)
#     event_names.append(event_to_add.name)
#     print(events)
#     print(event_names)
#     event_dropdown["menu"].delete(0, 'end')
#
#     for event in event_names:
#         event_dropdown["menu"].add_command(label=event)


def update_participants_listbox(event):
    selected_event_index = event_names.index(clicked_event.get())
    participant_listbox.delete(0, tkinter.END)
    for curr_participant in events[selected_event_index].participants:
        participant_listbox.insert(tkinter.END, curr_participant.name)


def popup_participant():
    add_participant_window = tkinter.Toplevel(window)
    add_participant_window.wm_geometry('400x100')

    participant_name_label = tkinter.Label(add_participant_window, text='Participant Name: ')
    participant_name_label.grid(row=1, column=1, padx=(10, 0), pady=10)

    participant_entry = tkinter.Entry(add_participant_window, font=FONT)
    participant_entry.grid(row=1, column=2, padx=(0, 10), pady=10)

    submit_participant_button = tkinter.Button(add_participant_window, text=f'Add Participant', font=FONT,
                                               command=lambda: [add_participant(participant_entry.get()),
                                                                add_participant_window.destroy()])
    submit_participant_button.grid(row=2, column=1, padx=(50, 0), pady=10)
    cancel_button = tkinter.Button(add_participant_window, text='Cancel', font=FONT,
                                   command=add_participant_window.destroy)
    cancel_button.grid(row=2, column=2, pady=10)


def add_participant(participant_name):
    event_index = event_names.index(clicked_event.get())
    participant_id = next(participant_id_gen)
    participant_to_add = Participant(participant_name, participant_id)
    events[event_index].add_participant(participant_to_add)
    participant_listbox.delete(0, tkinter.END)
    for curr_participant in events[event_index].participants:
        participant_listbox.insert(tkinter.END, curr_participant.name)


def popup_times():
    selected_participant = participant_listbox.curselection()[0]
    add_times_window = tkinter.Toplevel(window)
    add_times_window.wm_geometry('400x300')

    time_1_label = tkinter.Label(add_times_window, text='Time 1: ')
    time_1_label.grid(row=1, column=1, padx=(10, 0), pady=10)
    time_2_label = tkinter.Label(add_times_window, text='Time 2: ')
    time_2_label.grid(row=2, column=1, padx=(10, 0), pady=10)
    time_3_label = tkinter.Label(add_times_window, text='Time 3: ')
    time_3_label.grid(row=3, column=1, padx=(10, 0), pady=10)
    time_4_label = tkinter.Label(add_times_window, text='Time 4: ')
    time_4_label.grid(row=4, column=1, padx=(10, 0), pady=10)
    time_5_label = tkinter.Label(add_times_window, text='Time 5: ')
    time_5_label.grid(row=5, column=1, padx=(10, 0), pady=10)

    time_1_entry = tkinter.Entry(add_times_window, font=FONT)
    time_1_entry.grid(row=1, column=2, padx=(0, 10), pady=10)
    time_2_entry = tkinter.Entry(add_times_window, font=FONT)
    time_2_entry.grid(row=2, column=2, padx=(0, 10), pady=10)
    time_3_entry = tkinter.Entry(add_times_window, font=FONT)
    time_3_entry.grid(row=3, column=2, padx=(0, 10), pady=10)
    time_4_entry = tkinter.Entry(add_times_window, font=FONT)
    time_4_entry.grid(row=4, column=2, padx=(0, 10), pady=10)
    time_5_entry = tkinter.Entry(add_times_window, font=FONT)
    time_5_entry.grid(row=5, column=2, padx=(0, 10), pady=10)

    submit_times_button = tkinter.Button(add_times_window, text=f'Add Times', font=FONT, command=lambda: [
        add_times(selected_participant, time_1_entry.get(), time_2_entry.get(), time_3_entry.get(), time_4_entry.get(),
                  time_5_entry.get()), add_times_window.destroy()])
    submit_times_button.grid(row=6, column=1, padx=(50, 0), pady=10)
    cancel_button = tkinter.Button(add_times_window, text='Cancel', font=FONT, command=add_times_window.destroy)
    cancel_button.grid(row=6, column=2, pady=10)


def add_times(participant_index, time_1, time_2, time_3, time_4, time_5):
    event = events[event_names.index(clicked_event.get())]
    participant = event.participants[participant_index]
    participant.add_score(time_1)
    participant.add_score(time_2)
    participant.add_score(time_3)
    participant.add_score(time_4)
    participant.add_score(time_5)


def get_next_participant_id():
    num = 1
    while True:
        yield num
        num += 1


window = tkinter.Tk()
window.title("Rubik's Cubing Event Manager")
window.option_add('*font', 'Arial 12')
window.geometry('900x500')
frame = tkinter.Frame(window)
frame.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)
FONT = ('Arial', 12)
participant_id_gen = get_next_participant_id()

events = [Event(f'{i}x{i}') for i in range(2, 8)]
event_names = [event.name for event in events]
clicked_event = tkinter.StringVar()
clicked_event.set(event_names[0])

event_label = tkinter.Label(frame, text='Event: ', font=FONT)
event_label.grid(row=0, column=0)
event_dropdown = tkinter.OptionMenu(frame, clicked_event, *event_names, command=update_participants_listbox)
event_dropdown.grid(row=0, column=1)
participant_label = tkinter.Label(frame, text='Participants', font=FONT)
participant_label.grid(row=2, column=0, columnspan=2, pady=(40, 0))
participant_listbox = tkinter.Listbox(frame, font=FONT, selectmode='SINGLE')
participant_listbox.grid(row=3, column=0, columnspan=2)
add_participant_button = tkinter.Button(frame, text='Add Participant', font=FONT, command=popup_participant)
add_participant_button.grid(row=4, column=0, columnspan=2)
add_times_button = tkinter.Button(frame, text='Add Times', font=FONT, command=popup_times)
add_times_button.grid(row=5, column=0, columnspan=2)


if __name__ == '__main__':
    window.mainloop()
