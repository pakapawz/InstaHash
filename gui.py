from tkinter import *
from tkinter import messagebox

from api_request import get_top_post_hashtags
from hashtag_processing import get_final_sorted_hashtag
from validations import is_user_online, is_valid_topic


def show_error_message():
    messagebox.showinfo('Invalid Input', 'Input is either blank or contains non-alpha-numeric character')


def show_offline_message():
    messagebox.showinfo('No connection', 'Internet connection is required')


def copy_to_clipboard():
    messagebox.showinfo('Copy to Clipboard', 'Hashtags successfully copied to clipboard')


def show_final_recommendation():

    frm_hashtag = LabelFrame(root, text='Recommendation for [' + ent_topic.get() + ']')
    frm_hashtag.pack(padx=12, pady=12, fill=BOTH)

    counter = 1
    hashtags_string = ''
    file_hashtag = open('file_hashtags_final_sorted', 'r')
    for hashtag in file_hashtag:
        hashtag = hashtag.rstrip('\n')
        hashtags_string += hashtag

        if counter % 5 == 0:
            hashtags_string += '\n'
        else:
            hashtags_string += ' '
        counter += 1

        if counter > 30:
            break

    lbl_test2 = Label(frm_hashtag, text=hashtags_string)
    lbl_test2.pack(pady=4)

    btn_copy = Button(root, text='Copy to Clipboard', command=copy_to_clipboard)
    btn_copy.pack(pady=4)


def button_clicked():
    if is_valid_topic(ent_topic.get()):
        if is_user_online():
            get_top_post_hashtags(ent_topic.get())  # comment this line to turn on/off the search feature; for debug/test
            get_final_sorted_hashtag()
            show_final_recommendation()
        else:
            show_offline_message()
    else:
        show_error_message()

    ent_topic.delete(0, END)  # clears the entry field


# GUI PART
root = Tk()
root.title('InstaHash')

window_width = 512
window_height = 312

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coor = (screen_width / 2) - (window_width / 2)
y_coor = (screen_height / 2) - (window_height / 2)

root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coor, y_coor))  # [width]x[height]+[x_coor]+[y_coor]

ent_topic = Entry(root)

lbl_title = Label(root, text='Automated Instagram Hashtag Finder')
lbl_insert = Label(root, text='Insert your topic here')
btn_search = Button(root, text='Search!', command=button_clicked)

lbl_title.pack(pady=4)
ent_topic.pack(pady=4)
btn_search.pack(pady=4)

root.mainloop()
