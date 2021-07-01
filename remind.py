import argparse
import sys
import time
import tkinter as tk


def set_arguments(p):
    # Setting options for command line arguments
    p.add_argument('-t', '--text', dest='text', help='Text to remind about')
    p.add_argument('-m', '--minutes', dest='local_time', help='Time duration in minutes', type=float)


def get_arguments(p):
    # Parsing the command line arguments and returning the arguments
    arguments = p.parse_args()
    if arguments.text is None:
        p.error(f'Please specify a reminder text. Type {sys.argv[0]} -h for more info.')
    elif arguments.local_time is None:
        p.error(f'Please specify the time duration in minutes. Type {sys.argv[0]} -h for more info.')
    else:
        return arguments


root = tk.Tk()
parser = argparse.ArgumentParser()  # ArgumentParser() class to parse the command line arguments
set_arguments(parser)
# Getting the command line arguments
args = get_arguments(parser)
time.sleep(args.local_time)
# print(f'Reminding about: {args.text}')
tk.Label(root, text=f'Reminding about: {args.text}').pack()
root.mainloop()
