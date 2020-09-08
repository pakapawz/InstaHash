from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from api_request import get_top_post_hashtags
from hashtag_processing import get_final_sorted_hashtag
from validations import is_user_online, is_valid_topic

clipboard = ''


def show_error_message():
    messagebox.showinfo('Invalid Input', 'Input is either blank or contains non-alpha-numeric character')


def show_offline_message():
    messagebox.showinfo('No connection', 'Internet connection is required')


def copy_to_clipboard():
    copyToClipboard = Tk()
    copyToClipboard.withdraw()
    copyToClipboard.clipboard_clear()
    copyToClipboard.clipboard_append(clipboard)
    copyToClipboard.update()
    copyToClipboard.destroy()
    messagebox.showinfo('Copy to Clipboard', 'Hashtags successfully copied to clipboard')


def show_cannot_retrieve_error():
    messagebox.showinfo('Unexpected Error', 'Unexpected error occurred. Please try again later')


def show_final_recommendation():
    frm_hashtag = LabelFrame(root, text='Recommendation for [' + ent_topic.get() + ']', fg='#1f1f1f')
    frm_hashtag.pack(padx=12, pady=(24, 12), fill=BOTH)

    counter = 1
    hashtags_string = ''

    file_hashtag = open('file_hashtags_final_sorted', 'r')

    for hashtag in file_hashtag:
        hashtag = hashtag.rstrip('\n')

        if hashtag == '#cannot_retrieve_hashtag':
            show_cannot_retrieve_error()
            return

        hashtags_string += hashtag

        if counter % 5 == 0:
            hashtags_string += '\n'
        else:
            hashtags_string += ' '
        counter += 1

        if counter > 30:
            break

    lbl_test2 = Label(frm_hashtag, text=hashtags_string, fg='#1f1f1f')
    lbl_test2.pack(pady=4)

    btn_copy = Button(root, text='Copy to Clipboard', command=copy_to_clipboard,
                      font=('Calibri', 10, 'bold'), bg='#38857f', fg='white', padx=12, borderwidth=0)
    global clipboard
    clipboard= hashtags_string
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


# GUI PART
root = Tk()
root.title('InstaHash')
root.resizable(width=False, height=False)

window_width = 500
window_height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coor = (screen_width / 2) - (window_width / 2)
y_coor = (screen_height / 2) - (window_height / 2)

root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coor, y_coor))  # [width]x[height]+[x_coor]+[y_coor]

root.iconbitmap('z.ico')
img = Image.open('z_black.jpg')
img = img.resize((window_width, window_height))
bg_img = ImageTk.PhotoImage(img)
Label(root, image=bg_img).place(relwidth=1, relheight=1)

lbl_title = Label(root, text='Instagram Hashtag\nFinder',
                  font=('Futura', 20, 'bold'), fg='#1f1f1f', bg='#f2f2f2')
lbl_insert = Label(root, text='Insert your topic below',
                   font=('Calibri', 14), fg='#3f3f3f', bg='#f2f2f2')
lbl_warning = Label(root, text='(no whitespace and symbol allowed)',
                    font=('Calibri', 10, 'italic'), fg='#5f5f5f', bg='#f2f2f2')
ent_topic = Entry(root,width=20, font=('Calibri', 12))
btn_search = Button(
    root, text='Search', command=button_clicked,
    font=('Calibri', 10, 'bold'), bg='#38857f', fg='white',
    padx=20, borderwidth=0)

lbl_title.pack(pady=(32, 16))
lbl_insert.pack()
lbl_warning.pack()
ent_topic.pack(pady=4)
btn_search.pack(pady=4)

root.mainloop()
