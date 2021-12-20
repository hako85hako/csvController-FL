import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import app
from tkinter import messagebox
import csv
import sys


class TkinterClass:
    def __init__(self):
        # ルートを作成
        root = Tk()
        # ''設定
        root.title('csvController')
        root.resizable(True, True)

        # フレーム作成
        frame1 = ttk.Frame(root, padding=(32))
        frame1.grid()

        # ラベル作成
        label1 = ttk.Label(frame1, text=' FL-ID', padding=(5, 2))
        label1.grid(row=0, column=0, sticky=E)

        label2 = ttk.Label(frame1, text='Site-Password', padding=(5, 2))
        label2.grid(row=1, column=0, sticky=E)
############################################################################################
##FL-IDの選択
############################################################################################        
        self.username = StringVar()
        username_entry = ttk.Entry(
            frame1,
            textvariable=self.username,
            width=20)
        username_entry.grid(row=0, column=1)
############################################################################################
##Site-Passwardの選択
############################################################################################
        self.passward = StringVar()
        username_entry = ttk.Entry(
            frame1,
            textvariable=self.passward,
            width=20)
        username_entry.grid(row=1, column=1)
############################################################################################
##入れ替え対象フォルダの選択
############################################################################################
        label3 = ttk.Label(frame1, text='対象フォルダの指定', padding=(5, 10))
        label3.grid(row=2, column=0, sticky=E)
        button = ttk.Button(frame1, text='参照')
        button.bind('<ButtonPress>', self.folder_dialog)
        button.grid(row=2, column=1,sticky=E)

        self.folder_name = tk.StringVar()
        self.folder_name.set('未選択です')
        label4 = ttk.Label(frame1,textvariable=self.folder_name,width=20)
        label4.grid(row=3, column=1,sticky=E)
############################################################################################
##入れ替え順序指定用CSVの選択
############################################################################################
        label4 = ttk.Label(frame1, text='入れ替え番号指定用CSV', padding=(5, 10))
        label4.grid(row=4, column=0, sticky=E)
        button = ttk.Button(frame1, text='参照')
        button.bind('<ButtonPress>', self.file_dialog)
        button.grid(row=4, column=1,sticky=E)

        self.file_name = tk.StringVar()
        self.file_name.set('未選択です')
        label4 = ttk.Label(frame1,textvariable=self.file_name,width=20)
        label4.grid(row=5, column=1,sticky=E)
############################################################################################
##オフセット選択
############################################################################################
        # Frame
        oprionFrame = ttk.Frame(frame1, padding=(5, 10))
        # Style - Theme
        #ttk.Style().theme_use('classic')
        # Label Frame
        label_frame = ttk.Labelframe(
            oprionFrame,
            text='オフセット',
            padding=(10),
            style='My.TLabelframe')

        # Radiobutton 1
        self.v1 = StringVar()
        rb1 = ttk.Radiobutton(
            label_frame,
            text='offset7',
            #value=6,
            value=7,
            variable=self.v1)

        # Radiobutton 2
        rb2 = ttk.Radiobutton(
            label_frame,
            text='offset8',
            #value=7,
            value=8,
            variable=self.v1)

        # Layout
        oprionFrame.grid(row=6,column=1)
        label_frame.grid(row=0, column=0)
        rb1.grid(row=0, column=0) # LabelFrame
        rb2.grid(row=0, column=1) # LabelFrame

############################################################################################
##取得範囲外のデータ形式
############################################################################################
        # Frame
        oprionFrame2 = ttk.Frame(frame1, padding=(5, 10))
        # Style - Theme
        #ttk.Style().theme_use('classic')
        # Label Frame
        label_frame2 = ttk.Labelframe(
            oprionFrame2,
            text='取得範囲外のデータ形式',
            padding=(10),
            style='My.TLabelframe')

        # Radiobutton 1
        self.v2 = StringVar()
        rb3 = ttk.Radiobutton(
            label_frame2,
            text='null',
            value='null',
            variable=self.v2)

        # Radiobutton 2
        rb4 = ttk.Radiobutton(
            label_frame2,
            text='0',
            value=0,
            variable=self.v2)
        
        # Radiobutton 2
        rb5 = ttk.Radiobutton(
            label_frame2,
            text='空白',
            value='',
            variable=self.v2)

        # Layout
        oprionFrame2.grid(row=6,column=0)
        label_frame2.grid(row=0, column=0)
        rb3.grid(row=0, column=0) # LabelFrame
        rb4.grid(row=0, column=1) # LabelFrame  
        rb5.grid(row=0, column=2) # LabelFrame        

############################################################################################
##取得範囲が空白だった場合に挿入するデータ
############################################################################################
        # Frame
        oprionFrame3 = ttk.Frame(frame1, padding=(5, 10))
        # Style - Theme
        #ttk.Style().theme_use('classic')
        # Label Frame
        label_frame3 = ttk.Labelframe(
            oprionFrame3,
            text='取得先が空白だった場合に挿入するデータ',
            padding=(10),
            style='My.TLabelframe')

        # Radiobutton 1
        self.v3 = StringVar()
        rb6 = ttk.Radiobutton(
            label_frame3,
            text='null',
            value='null',
            variable=self.v3)

        # Radiobutton 2
        rb7 = ttk.Radiobutton(
            label_frame3,
            text='0',
            value=0,
            variable=self.v3)
        
        # Radiobutton 2
        rb8 = ttk.Radiobutton(
            label_frame3,
            text='空白',
            value='',
            variable=self.v3)

        # Layout
        oprionFrame3.grid(row=7,column=1)
        label_frame3.grid(row=0, column=0)
        rb6.grid(row=0, column=0) # LabelFrame
        rb7.grid(row=0, column=1) # LabelFrame  
        rb8.grid(row=0, column=2) # LabelFrame        

############################################################################################
        endform = ttk.Frame(frame1, padding=(0, 5))
        endform.grid(column=1, sticky=W)

        button1 = ttk.Button(endform, text='OK')
        button1.bind('<ButtonPress>', self.createNewCSV)
        button1.pack(side=LEFT)

        button2 = ttk.Button(endform, text='Cancel', command=sys.exit())
        button2.pack(side=LEFT)
        root.mainloop()


    def file_dialog(self, event):
        fTyp = [("", "*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_name = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        if len(file_name) == 0:
            self.file_name.set('選択をキャンセルしました')
        else:
            self.file_name.set(file_name)

    def folder_dialog(self, event):
        iDir = os.path.abspath(os.path.dirname(__file__))
        folder_name = tk.filedialog.askdirectory(initialdir=iDir)
        if len(folder_name) == 0:
            self.folder_name.set('選択をキャンセルしました')
        else:
            self.folder_name.set(folder_name)

    def createNewCSV(self, event):
        ###################################################
        # 初期値の設定 #
        ###################################################
        #pathの指定
        #dataディレクトリの場所
        dir_name = self.folder_name.get()+'/'
        # dir_name = '/Users/sakaiyuunin/Documents/phython/csvController/'
        
        #入れ替えチャネルの指定
        ch_list_path = self.file_name.get()
        with open(ch_list_path) as fp:
            csvList = list(csv.reader(fp))
        pre_ch_list = [item for subList in csvList for item in subList]
        ch_list = []
        for s in pre_ch_list:
            if s == '' or s == '--':
                ch_list += [s]
            else:
                ch_list += [int(s)]
        #test_data
        #ch_list = [1,2,3,4,5,6,7]

        #入れ替え時対象には入らない場所に格納する値の指定
        #none_select_column = '0'
        none_select_column =  self.v2.get()
        
        #入れ替え時対象の数値がnullの場合に格納する値の指定
        #none_valiable_column = '-'
        none_valiable_column = self.v3.get()

        #案件ID
        # id = 'FL999-99999_0000'
        id = self.username.get()

        #パスワード
        password = self.passward.get()
        
        # オフセット指定
        offset = self.v1.get()

        ###################################################
        
        try:
            print(ch_list)
            app.main(dir_name,ch_list,none_select_column,none_valiable_column,offset,id,password)
        except FileNotFoundError:
            #メッセージボックス（エラー） 
            messagebox.showerror('エラー', 'ファイル指定に問題が発生しました。')
        except:
            #メッセージボックス（エラー） 
            messagebox.showerror('エラー', 'エラーが発生しました。')