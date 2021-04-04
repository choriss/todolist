import tkinter
from tkinter import filedialog
import os
import datetime
from tkinter.scrolledtext import ScrolledText
import shutil

who_am_i = os.environ['USERNAME']

file_path = 'C:/Users/' + who_am_i + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/auto.py'
if os.path.exists(file_path):
    auto_up = 0
else:
    auto_up = 1
    

# 上書き判定初期化
uwa = 0

# 画面作成
tki = tkinter.Tk()
tki.geometry('900x430')
tki.title('TODOLIST')

# 空リスト作成
todo = [''] * 10
todo_hyouji = [''] * 10
todo_kigen = [datetime.datetime(1,1,1)] * 10
todo_kigen_hyouji = [''] * 10
todo_shousai = [''] * 10



# ラベル
def ref():
    global todo
    global todo_hyouji
    global todo_kigen
    global todo_kigen_hyouji

    # 表示リセット
    lbl_1 = tkinter.Label(text='①　　　　　　　　　　　　　　　　　　　　')
    lbl_1.place(x=30, y=70)
    lbl_2 = tkinter.Label(text='②　　　　　　　　　　　　　　　　　　　　')
    lbl_2.place(x=30, y=100)
    lbl_3 = tkinter.Label(text='③　　　　　　　　　　　　　　　　　　　　')
    lbl_3.place(x=30, y=130)
    lbl_4 = tkinter.Label(text='④　　　　　　　　　　　　　　　　　　　　')
    lbl_4.place(x=30, y=160)
    lbl_5 = tkinter.Label(text='⑤　　　　　　　　　　　　　　　　　　　　')
    lbl_5.place(x=30, y=190)
    
    lbl_6 = tkinter.Label(text='⑥　　　　　　　　　　　　　　　　　　　　')
    lbl_6.place(x=430, y=70)
    lbl_7 = tkinter.Label(text='⑦　　　　　　　　　　　　　　　　　　　　')
    lbl_7.place(x=430, y=100)
    lbl_8 = tkinter.Label(text='⑧　　　　　　　　　　　　　　　　　　　　')
    lbl_8.place(x=430, y=130)
    lbl_9 = tkinter.Label(text='⑨　　　　　　　　　　　　　　　　　　　　')
    lbl_9.place(x=430, y=160)
    lbl_10 = tkinter.Label(text='⑩　　　　　　　　　　　　　　　　　　　　')
    lbl_10.place(x=430, y=190)

    # 表示
    lbl_1 = tkinter.Label(text='①'+todo_hyouji[0]+' 期限:'+todo_kigen_hyouji[0])
    lbl_1.place(x=30, y=70)
    lbl_2 = tkinter.Label(text='②'+todo_hyouji[1]+' 期限:'+todo_kigen_hyouji[1])
    lbl_2.place(x=30, y=100)
    lbl_3 = tkinter.Label(text='③'+todo_hyouji[2]+' 期限:'+todo_kigen_hyouji[2])
    lbl_3.place(x=30, y=130)
    lbl_4 = tkinter.Label(text='④'+todo_hyouji[3]+' 期限:'+todo_kigen_hyouji[3])
    lbl_4.place(x=30, y=160)
    lbl_5 = tkinter.Label(text='⑤'+todo_hyouji[4]+' 期限:'+todo_kigen_hyouji[4])
    lbl_5.place(x=30, y=190)
    
    lbl_6 = tkinter.Label(text='⑥'+todo_hyouji[5]+' 期限:'+todo_kigen_hyouji[5])
    lbl_6.place(x=430, y=70)
    lbl_7 = tkinter.Label(text='⑦'+todo_hyouji[6]+' 期限:'+todo_kigen_hyouji[6])
    lbl_7.place(x=430, y=100)
    lbl_8 = tkinter.Label(text='⑧'+todo_hyouji[7]+' 期限:'+todo_kigen_hyouji[7])
    lbl_8.place(x=430, y=130)
    lbl_9 = tkinter.Label(text='⑨'+todo_hyouji[8]+' 期限:'+todo_kigen_hyouji[8])
    lbl_9.place(x=430, y=160)
    lbl_10 = tkinter.Label(text='⑩'+todo_hyouji[9]+' 期限:'+todo_kigen_hyouji[9])
    lbl_10.place(x=430, y=190)

# リセット・更新
def refresh():
    global todo
    global todo_hyouji
    global todo_kigen
    global todo_kigen_hyouji

    # 表示準備
    for i in range(len(todo)):
        if todo[i] == '':
            todo_hyouji[i] = '[追加]'
        else:
            todo_hyouji[i] = todo[i]
    for i in range(len(todo_kigen)):
        if todo_kigen[i] == datetime.datetime(1,1,1):
            todo_kigen_hyouji[i] = 'なし'
        else:
            todo_kigen_hyouji[i] = str(todo_kigen[i].year)+'年'+str(todo_kigen[i].month)+'月'+str(todo_kigen[i].day)+'日'
    ref()

# ボタン関数動的作成[DONE]
def make_btn_n_click(n):
    def btn_n_click():
        global todo
        global todo_kigen
        global todo_shousai
        del todo[n]
        del todo_kigen[n]
        del todo_shousai[n]
        todo.append('')
        todo_kigen.append(datetime.datetime(1,1,1))
        todo_shousai.append('')
        refresh()

    return btn_n_click

btn_n_click = {}
for i in range(10):
    btn_n_click[i] = make_btn_n_click(i)


# ボタン関数動的作成[詳細]
tki_shousai = ['']*10
shousai = ['']*10

def make_btn_n_shousai_click(n):
    def btn_n_shousai_click():
        tki_shousai[n] = tkinter.Toplevel()
        tki_shousai[n].geometry('400x200')
        tki_shousai[n].title(todo[n])
        shousai[n] = tkinter.Label(tki_shousai[n],text=todo_shousai[n])
        shousai[n].place(x=10, y=10)

    return btn_n_shousai_click

btn_n_shousai_click = {}
for i in range(10):
    btn_n_shousai_click[i] = make_btn_n_shousai_click(i)



# セーブ関数
def btn_save_click(uwagaki) :
    global todo
    global todo_kigen
    global todo_shousai

    # セーブ
    if uwagaki == 0:

        # ファイルダイアログ表示準備
        typ = [('text file','*.txt')] 
        dir = 'C:/Users/'+os.environ['USERNAME']+'/Documents'
        
        fle = filedialog.asksaveasfilename(initialdir = dir,title = "Save as",filetypes =  [("text file","*.txt")])
        
        # 書き込み
        with open(fle, 'w') as f:
            for d in todo:
                f.write("%s\n"%d)
            for d in todo_kigen:
                f.write("%s\n"%d)
            for i in range(0,10):
                todo_shousai[i] = todo_shousai[i].replace('\n','\\n')
            for d in todo_shousai:
                f.write("%s\n"%d)
            uwa = 1
    else:
        f = open(fle,'w')
        f.write(todo)
        f.close()

# btn_load_click
def btn_load_click():
    global todo
    global todo_kigen
    global todo_shousai
    
    # ファイルダイアログ表示準備
    typ = [('text file','*.txt')] 
    dir = 'C:/Users/'+os.environ['USERNAME']+'/Documents'
    
    fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
    
    # オープン
    with open(fle) as f:
        yomikomi = [s.strip() for s in f.readlines()]
        todo = yomikomi[0:10]
        todo_kigen = yomikomi[10:20]
        todo_shousai = yomikomi[20:30]
        for i in range (0,len(todo_shousai)):
            todo_shousai[i] = todo_shousai[i].replace('\\n','\n')
        for i in range (0,10):
            todo_kigen[i] = datetime.datetime.strptime(todo_kigen[i], '%Y-%m-%d %H:%M:%S')
    uwa = 1
    refresh()

# 初期化
refresh()

# btn_add_click
def btn_add_click():
    global todo
    global todo_kigen
    global todo_shousai
    
    # 格納
    if "" in todo:
        new = todo.index('')
        todo[new] = txt_1.get()
        
        # 期限設定
        dt = datetime.datetime.now()
        kigen_year = txt_kigen_year.get()
        kigen_month = txt_kigen_month.get()
        kigen_day = txt_kigen_day.get

        # 日時格納
        if kigen_year == '' and kigen_month == '' and kigen_day == '':
            todo_kigen[new] = datetime.datetime(0,0,0)
        elif kigen_year == '' and kigen_month == '':
            todo_kigen[new] = datetime.datetime(dt.year, dt.month, int(txt_kigen_day.get()),)
        elif kigen_month == '' and kigen_day == '':
            todo_kigen[new] = datetime.datetime(int(txt_kigen_year.get()), 12, 31)
        elif kigen_year == '':
            todo_kigen[new] = datetime.datetime(dt.year, int(txt_kigen_month.get()), int(txt_kigen_day.get()))
        elif kigen_month == '':
            todo_kigen[new] = datetime.datetime(int(txt_kigen_year.get()), dt.month, int(txt_kigen_day.get()))
        elif kigen_day == '':
            todo_kigen[new] = datetime.datetime(int(txt_kigen_year.get()), int(txt_kigen_month.get()), calendar.monthrange(int(txt_kigen_year.get()), int(txt_kigen_month.get))[1])
        else:
            todo_kigen[new] = datetime.datetime(int(txt_kigen_year.get()), int(txt_kigen_month.get()), int(txt_kigen_day.get()))

        # 詳細格納
        todo_shousai[new] = txt_shousai.get('1.0','end - 1c')+' '
    refresh()

def btn_check_click():
    auto_up = settei_button.get()

def user_list_up():
    global users
    global all_users
    users=subprocess.run(['powershell.exe', '-command', '(Get-WmiObject Win32_UserAccount).name'],encoding='utf-8',capture_output=True)
    all_users=users.stdout.split()

def btn_kakutei_click():
    # auto_up
    auto_up = settei_button.get()
    
    who_am_i = os.environ['USERNAME']

    who_am_i = who_am_i.lower()
    
    before_name = 'C:\\Users\\'
    after_name = '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\auto.py'
        
    if auto_up == 0:
        naiyou = '''import subprocess
subprocess.Popen(r"''' +os.path.abspath(__file__) +'''", shell=True)'''

        f1 = open(before_name + who_am_i + after_name,'w',encoding='utf-8')
        f1.write(naiyou)

        f1.close()

    else:
        if os.path.exists(before_name + who_am_i + after_name):
            os.remove(before_name + who_am_i + after_name)

    # auto_up_data
    auto_up_data_name = auto_up_data.get()
    #システムファイルがあるならその中にメモ帳を作成して、
    #そこに.get()の内容をぶち込む。
    #起動したときはそこから開くデータを取ってくる
    
    file_path = 'C:/Users/' + who_am_i + '/todo_system'
    if os.path.exists(file_path):
        f = open('C:/Users/' + who_am_i + '/todo_system/todo_system.txt','w')

        f.write(auto_up_data_name)

        f.close()
    else:
        os.makedirs(file_path)
        
        f = open('C:/Users/' + who_am_i + '/todo_system/todo_system.txt','w')

        f.write(auto_up_data_name)

        f.close()
    

# ラジオボタン判定変数作成
settei_button = tkinter.IntVar()
settei_button.set(auto_up)

def btn_settei_click():
    global auto_up
    global users
    global all_users
    global auto_up_data

    root = tkinter.Toplevel()
    root.geometry("300x150")

    # Canvas Widget を生成
    canvas = tkinter.Canvas(root)

    # Top Widget上に Scrollbar を生成して配置
    bar = tkinter.Scrollbar(root, orient=tkinter.VERTICAL)
    bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    bar.config(command=canvas.yview) # ScrollbarでCanvasを制御

    # Canvas Widget をTopWidget上に配置
    canvas.config(yscrollcommand=bar.set) # Canvasのサイズ変更をScrollbarに通知
    canvas.config(scrollregion=(0,0,300,250)) #スクロール範囲
    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    # Frame Widgetを 生成
    frame = tkinter.Frame(canvas)

    # Frame Widgetを Canvas Widget上に配置（）
    canvas.create_window((0,0), window=frame, anchor=tkinter.NW, width=500, height=500)

    # ラジオボタン判定変数作成
    settei_button.set(auto_up)

    # auto up 案内
    auto_up_ravel = tkinter.Label(frame,text='PCを立ち上げたときと同時にこのアプリも起動する')
    auto_up_ravel.place(x=25, y=25)

    # ONOFFラジオボタン
    auto_on = tkinter.Radiobutton(frame, value=0, variable=settei_button, text='ON')
    auto_on.place(x=25, y=55)
    auto_off = tkinter.Radiobutton(frame, value=1, variable=settei_button, text='OFF')
    auto_off.place(x=25, y=85)

    # 立ち上げ時に読み込むセーブデータ
    auto_up_data_lbl = tkinter.Label(frame,text='立ち上げ時に読み込むセーブデータのパス')
    auto_up_data_lbl.place(x=25, y=145)

    auto_up_data = tkinter.Entry(frame,width=40)
    auto_up_data.place(x=25,y=175)

    # 確定ボタン
    btn_kakutei = tkinter.Button(frame, text='確定' , command=btn_kakutei_click)
    btn_kakutei.place(x=100, y=205)

    root.mainloop()

#自動オープン
who_am_i = os.environ['USERNAME']

if os.path.exists('C:/Users/' + who_am_i + '/todo_system/todo_system.txt'):

    with open('C:/Users/' + who_am_i + '/todo_system/todo_system.txt','r') as f:
        yomikomi_name = f.read()
        with open(yomikomi_name) as f:
            yomikomi = [s.strip() for s in f.readlines()]
            todo = yomikomi[0:10]
            todo_kigen = yomikomi[10:20]
            todo_shousai = yomikomi[20:30]
            for i in range (0,len(todo_shousai)):
                todo_shousai[i] = todo_shousai[i].replace('\\n','\n')
            for i in range (0,len(todo_kigen)):
                todo_kigen[i] = datetime.datetime.strptime(todo_kigen[i], '%Y-%m-%d %H:%M:%S')
            uwa = 1
            refresh()

        
# DONEボタン
btn_done = ['']*10
for i in range(2):
    for j in range(5):
        btn_done[i*5+j] =tkinter.Button(tki, text='DONE', command=btn_n_click[i*5+j])
        btn_done[i*5+j].place(x=i*400+380, y=j*30+70)

# 詳細ボタン
btn_shousai = ['']*10
for i in range(2):
    for j in range(5):
        btn_shousai[i*5+j] =tkinter.Button(tki, text='詳細', command=btn_n_shousai_click[i*5+j])
        btn_shousai[i*5+j].place(x=i*400+330, y=j*30+70)

# テキストボックス
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=70, y=250)

# 期限テキストボックス・案内
lbl_kigen = tkinter.Label(text='期限:                  年           月　　    日')
lbl_kigen.place(x=205, y=250)

txt_kigen_year = tkinter.Entry(width=7)
txt_kigen_year.place(x=240, y=250)

txt_kigen_month = tkinter.Entry(width=4)
txt_kigen_month.place(x=305, y=250)

txt_kigen_day = tkinter.Entry(width=4)
txt_kigen_day.place(x=350, y=250)

# 追加ボタン
btn_add = tkinter.Button(tki, text='追加', command=btn_add_click)
btn_add.place(x=400, y=250)

# today
tdatetime = datetime.datetime.now()
tstr = tdatetime.strftime('%Y/%m/%d')
lbl_today =tkinter.Label(text='今日は'+tstr)
lbl_today.place(x=300, y=270)

# セーブ+ボタン
btn_save = tkinter.Button(tki, text='SAVE', command=lambda:btn_save_click(uwa))
btn_save.place(x=500, y=250)

# ロード+ボタン
btn_load = tkinter.Button(tki, text='LOAD', command=btn_load_click)
btn_load.place(x=540, y=250)

# 詳細
lbl_shousai = tkinter.Label(text='詳細')
lbl_shousai.place(x=70,y=300)
txt_shousai = tkinter.scrolledtext.ScrolledText(tki, font=("", 11), height=5, width=40)
txt_shousai.place(x=100,y=300)

# 設定
btn_settei = tkinter.Button(tki, text='設定', command=btn_settei_click)
btn_settei.place(x=850, y=10)

tki.mainloop()

# ver2.1
# 
