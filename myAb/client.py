# coding=utf-8
import pythonAb
from Tkinter import *
MENU_ITEMS = ['File', 'Edit', 'Format', 'Run', 'Options', 'Windows', 'Help', 'Test']


def set_tk_geometry(tk, size):
    # 设置窗口大小，size的格式为：width x height, 如：size = '200x100'.
    if size is not None and size != '':
        tk.geometry(size)
    else:
        tk.geometry('650x600')


def set_tk_title(tk, title):
    # 给窗口定义title
    if title is not None and title != '':
        tk.title(title)
    else:
        tk.title('PythonAb v1.0')


def get_tk():
    # 获取一个Tk对象
    return Tk()


def get_null_label(tk,size):
    return Label(tk, width=size)


def get_label(tk, te):
    return Label(tk, text=te)


def get_entry(tk, text):
    e = StringVar()
    e.set(text)
    return Entry(tk, textvariable=e, width=50)


def get_text(tk):
    return Text(tk, background='gray')


def get_button(tk, text):
    return Button(tk, text=text)


def get_menu(tk):
    # 获取一个菜单条
    return Menu(tk)


root = get_tk()
text = get_text(root)
text_log = get_text(root)
entry = get_entry(root, '-h -V -c 10 -n 20 -e www.baidu.com')
set_tk_geometry(root, '600x820')
set_tk_title(root, "PythonAb")


def read_file(file_name):
    file_object = open(file_name)
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    return all_the_text

def mouse_event(event):
    # pythonAb.tran_command("-h -V -c  10  -n  20  -e  www.baidu.com")
    result = pythonAb.tran_command(entry.get())
    text.delete(0.0, END)
    text_log.delete(0.0, END)
    text.insert(INSERT, result)
    text_log.insert(INSERT,read_file('ab.log'))

def ini_ui(tk,text,text_log,entry):
    result_label = get_label(tk, "测试结果:")
    log_label = get_label(tk, "日志结果:")
    left_label1 = get_null_label(tk, 1)
    label = get_label(tk, "命令:")
    button = get_button(tk, '提测')
    label.grid(row=1, column=1)
    entry.grid(row=1, column=2)
    button.grid(row=1, column=3)
    left_label1.grid(row=1, column=0)
    result_label.grid(row=2, column=1, columnspan=3)
    text.grid(row=3, column=1, columnspan=3)
    log_label.grid(row=4, column=1, columnspan=3)
    text_log.grid(row=5, column=1, columnspan=3)
    button.bind('<Button-1>', mouse_event)


ini_ui(root,text,text_log,entry)
root.mainloop()






