import re
import tkinter as tk
from tkinter import ttk
import source
from Controller import Controller
from Model import Model


window = tk.Tk()
window.title("EVOT_printer")
window.geometry('660x480')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)




class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(tab0, text='Email:')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(tab0, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.email_var1 = tk.StringVar()
        self.email_entry1 = ttk.Entry(tab1, textvariable=self.email_var1, width=30)
        self.email_entry1.grid(row=2, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(tab0, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

