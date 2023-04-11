import tkinter
from Event import Event
from Participant import Participant


def get_next_participant_id():
    num = 1
    while True:
        yield num
        num += 1


class App:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Rubik's Cubing Event Manager")
        self.main_window.option_add('*font', 'Arial 12')
        self.main_window.geometry('900x500')
        self.frame = tkinter.Frame(self.main_window)
        self.frame.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)
        self.FONT = ('Arial', 12)
        self.participant_id_gen = get_next_participant_id()

        self.events = [Event(f'{i}x{i}') for i in range(2, 8)]
        self.event_names = [event.name for event in self.events]
        self.clicked_event = tkinter.StringVar()
        self.clicked_event.set(self.event_names[0])

        self.event_label = tkinter.Label(self.frame, text='Event: ', font=self.FONT)
        self.event_label.grid(row=0, column=0)
        self.event_dropdown = tkinter.OptionMenu(self.frame, self.clicked_event, *self.event_names,
                                                 command=self.update_participants_listbox)
        self.event_dropdown.grid(row=0, column=1)
        self.participant_label = tkinter.Label(self.frame, text='Participants', font=self.FONT)
        self.participant_label.grid(row=2, column=0, columnspan=2, pady=(40, 0))
        self.participant_listbox = tkinter.Listbox(self.frame, font=self.FONT, selectmode='SINGLE')
        self.participant_listbox.grid(row=3, column=0, columnspan=2)
        self.add_participant_button = tkinter.Button(self.frame, text='Add Participant', font=self.FONT,
                                                     command=self.popup_participant)
        self.add_participant_button.grid(row=4, column=0, columnspan=2)
        self.add_times_button = tkinter.Button(self.frame, text='Add Times', font=self.FONT, command=self.popup_times)
        self.add_times_button.grid(row=5, column=0, columnspan=2)

    def update_participants_listbox(self, event):
        selected_event_index = self.event_names.index(self.clicked_event.get())
        self.participant_listbox.delete(0, tkinter.END)
        for curr_participant in self.events[selected_event_index].participants:
            self.participant_listbox.insert(tkinter.END, curr_participant.name)

    def popup_participant(self):
        self.add_participant_window = tkinter.Toplevel(self.main_window)
        self.add_participant_window.wm_geometry('400x120')

        participant_name_label = tkinter.Label(self.add_participant_window, text='Participant Name: ')
        participant_name_label.grid(row=1, column=1, padx=(10, 0), pady=10)

        participant_entry = tkinter.Entry(self.add_participant_window, font=self.FONT)
        participant_entry.grid(row=1, column=2, padx=(0, 10), pady=10)

        submit_participant_button = tkinter.Button(self.add_participant_window, text=f'Add Participant', font=self.FONT,
                                                   command=lambda: self.add_participant(participant_entry.get()))
        submit_participant_button.grid(row=2, column=1, padx=(50, 0), pady=10)
        cancel_button = tkinter.Button(self.add_participant_window, text='Cancel', font=self.FONT,
                                       command=self.add_participant_window.destroy)
        cancel_button.grid(row=2, column=2, pady=10)

    def add_participant(self, participant_name):
        if participant_name:
            participant_name = participant_name.title()
            event_index = self.event_names.index(self.clicked_event.get())
            participant_id = next(self.participant_id_gen)
            participant_to_add = Participant(participant_name, participant_id)
            self.events[event_index].add_participant(participant_to_add)
            self.participant_listbox.delete(0, tkinter.END)
            for curr_participant in self.events[event_index].participants:
                self.participant_listbox.insert(tkinter.END, curr_participant.name)
            self.add_participant_window.destroy()
        else:
            empty_name_label = tkinter.Label(self.add_participant_window, text='Name cannot be empty', fg='#f00')
            empty_name_label.grid(row=3, column=1, columnspan=2)

    def popup_times(self):
        selected_participant = self.participant_listbox.curselection()[0]
        self.add_times_window = tkinter.Toplevel(self.main_window)
        self.add_times_window.wm_geometry('400x300')

        time_1_label = tkinter.Label(self.add_times_window, text='Time 1: ')
        time_1_label.grid(row=1, column=1, padx=(10, 0), pady=10)
        time_2_label = tkinter.Label(self.add_times_window, text='Time 2: ')
        time_2_label.grid(row=2, column=1, padx=(10, 0), pady=10)
        time_3_label = tkinter.Label(self.add_times_window, text='Time 3: ')
        time_3_label.grid(row=3, column=1, padx=(10, 0), pady=10)
        time_4_label = tkinter.Label(self.add_times_window, text='Time 4: ')
        time_4_label.grid(row=4, column=1, padx=(10, 0), pady=10)
        time_5_label = tkinter.Label(self.add_times_window, text='Time 5: ')
        time_5_label.grid(row=5, column=1, padx=(10, 0), pady=10)

        time_1_entry = tkinter.Entry(self.add_times_window, font=self.FONT)
        time_1_entry.grid(row=1, column=2, padx=(0, 10), pady=10)
        time_2_entry = tkinter.Entry(self.add_times_window, font=self.FONT)
        time_2_entry.grid(row=2, column=2, padx=(0, 10), pady=10)
        time_3_entry = tkinter.Entry(self.add_times_window, font=self.FONT)
        time_3_entry.grid(row=3, column=2, padx=(0, 10), pady=10)
        time_4_entry = tkinter.Entry(self.add_times_window, font=self.FONT)
        time_4_entry.grid(row=4, column=2, padx=(0, 10), pady=10)
        time_5_entry = tkinter.Entry(self.add_times_window, font=self.FONT)
        time_5_entry.grid(row=5, column=2, padx=(0, 10), pady=10)

        submit_times_button = tkinter.Button(self.add_times_window, text=f'Add Times', font=self.FONT,
                                             command=lambda: self.add_times(selected_participant, [time_1_entry.get(),
                                                                                                   time_2_entry.get(),
                                                                                                   time_3_entry.get(),
                                                                                                   time_4_entry.get(),
                                                                                                   time_5_entry.get()]))
        submit_times_button.grid(row=6, column=1, padx=(50, 0), pady=10)
        cancel_button = tkinter.Button(self.add_times_window, text='Cancel', font=self.FONT,
                                       command=self.add_times_window.destroy)
        cancel_button.grid(row=6, column=2, pady=10)

    def add_times(self, participant_index, times):
        if not all(times):
            empty_times_label = tkinter.Label(self.add_times_window, text='Time entries cannot be empty', fg='#f00')
            empty_times_label.grid(row=7, column=1, columnspan=2)
        else:
            if all([time.replace('.', '', 1).isnumeric() for time in times]):
                event = self.events[self.event_names.index(self.clicked_event.get())]
                participant = event.participants[participant_index]
                if not participant.scores:
                    for time in times:
                        participant.add_score(time)
                    self.add_times_window.destroy()
                else:
                    times_already_exist_label = tkinter.Label(self.add_times_window,
                                                              text='Time entries already exist for this participant',
                                                              fg='#f00')
                    times_already_exist_label.grid(row=7, column=1, columnspan=2)
            else:
                times_input_val_label = tkinter.Label(self.add_times_window, text='Time entries must only be numbers',
                                                      fg='#f00')
                times_input_val_label.grid(row=7, column=1, columnspan=2)
