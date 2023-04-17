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
        self.add_times_window = None
        self.add_participant_window = None
        self.main_window.title("Rubik's Cubing Event Manager")
        self.main_window.option_add('*font', 'Arial 12')
        self.main_window.geometry('950x500')
        self.frame = tkinter.Frame(self.main_window)
        self.frame.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)
        self.FONT = ('Arial', 12)
        self.BOLD_FONT = ('Arial', 12, 'bold')
        self.participant_id_gen = get_next_participant_id()

        self.events = [Event(f'{i}x{i}') for i in range(2, 8)]
        self.event_names = [event.name for event in self.events]
        self.clicked_event = tkinter.StringVar()
        self.clicked_event.set(self.event_names[0])

        self.event_label = tkinter.Label(self.frame, text='Event: ', font=self.FONT)
        self.event_label.grid(row=0, column=0, rowspan=2)
        self.event_dropdown = tkinter.OptionMenu(self.frame, self.clicked_event, *self.event_names,
                                                 command=self.update_participants_listbox)
        self.event_dropdown.grid(row=0, column=1, rowspan=2)
        self.participant_label = tkinter.Label(self.frame, text='Participants', font=self.FONT)
        self.participant_label.grid(row=2, column=0, columnspan=2, pady=(40, 0))
        self.participant_listbox = tkinter.Listbox(self.frame, font=self.FONT, selectmode='SINGLE')
        self.participant_listbox.grid(row=3, column=0, columnspan=2, rowspan=3)
        self.add_participant_button = tkinter.Button(self.frame, text='Add Participant', font=self.FONT,
                                                     command=self.popup_participant)
        self.add_participant_button.grid(row=6, column=0, columnspan=2)
        self.add_times_button = tkinter.Button(self.frame, text='Add Times', font=self.FONT, command=self.popup_times)
        self.add_times_button.grid(row=7, column=0, columnspan=2)
        self.determine_winners_button = tkinter.Button(self.frame, text='Determine Winners', font=self.FONT,
                                                       command=self.display_winners)
        self.determine_winners_button.grid(row=8, column=0, columnspan=2, pady=40)
        self.two_by_two_results_label = tkinter.Label(self.frame, text='2x2 Results', font=self.BOLD_FONT)
        self.three_by_three_results_label = tkinter.Label(self.frame, text='3x3 Results', font=self.BOLD_FONT)
        self.four_by_four_results_label = tkinter.Label(self.frame, text='4x4 Results', font=self.BOLD_FONT)
        self.five_by_five_results_label = tkinter.Label(self.frame, text='5x5 Results', font=self.BOLD_FONT)
        self.six_by_six_results_label = tkinter.Label(self.frame, text='6x6 Results', font=self.BOLD_FONT)
        self.seven_by_seven_results_label = tkinter.Label(self.frame, text='7x7 Results', font=self.BOLD_FONT)
        self.two_by_two_results_label.grid(row=0, column=2, columnspan=2, padx=70)
        self.three_by_three_results_label.grid(row=0, column=4, columnspan=2, padx=70)
        self.four_by_four_results_label.grid(row=0, column=6, columnspan=2, padx=70)
        self.five_by_five_results_label.grid(row=4, column=2, columnspan=2, padx=70)
        self.six_by_six_results_label.grid(row=4, column=4, columnspan=2, padx=70)
        self.seven_by_seven_results_label.grid(row=4, column=6, columnspan=2, padx=70)

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
            if all([time.replace('.', '', 1).isnumeric() or time.upper() == 'DNF' for time in times]):
                event = self.events[self.event_names.index(self.clicked_event.get())]
                participant = event.participants[participant_index]
                if not participant.times:
                    for time in times:
                        participant.add_time(float(time) if time.replace('.', '', 1).isnumeric() else time.upper())
                    print(participant.times)
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

    def display_winners(self):
        event = self.events[self.event_names.index(self.clicked_event.get())]

        if event.all_times_entered():
            event.calc_all_averages()
            event.sort_participants()
            winners = {participant.name: participant.average for participant in event.finished_participants[0:3]}
            event_label_index = self.events.index(event)
            winner_label_coordinates = [
                (1, 2),
                (1, 4),
                (1, 6),
                (5, 2),
                (5, 4),
                (5, 6)
            ]
            winners_text = ['1st Place: ', '2nd Place: ', '3rd Place: ']
            for key, value, i in zip(winners.keys(), winners.values(), range(3)):
                winners_text[i] += f'{key}, {value:0.2F}\n' if value != 'DNF' else f'{key}, {value}\n'
            winner_label = tkinter.Label(self.frame, text='\n'.join(winners_text), font=self.FONT)
            winner_label.grid(row=winner_label_coordinates[event_label_index][0],
                              column=winner_label_coordinates[event_label_index][1], columnspan=2, rowspan=3)
        else:
            self.display_remaining_participants(event.get_remaining_participants())

    def display_remaining_participants(self, remaining_participants):
        remaining_participants_window = tkinter.Toplevel(self.main_window)
        remaining_participants_window.wm_geometry('400x300')

        remaining_participants_label = tkinter.Label(remaining_participants_window,
                                                     text='These participants don\'t have times entered\n(copy if needed):')
        remaining_participants_label.pack()
        remaining_participants_textbox = tkinter.Text(remaining_participants_window, width=30, height=15)
        remaining_participants_textbox.pack(pady=(0, 20))
        remaining_participants_textbox.insert('1.0', remaining_participants)
        remaining_participants_textbox.configure(state='disabled')
