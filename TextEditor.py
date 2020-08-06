# TextEditor_test03.py
#? 파일 트리 단축키나 메뉴를 통해서 창을 활성화 했을 때, 상태표시줄 닫기를 누를 경우 toplevel이 사라짐
#? 자동실행 기능은 넣기 힘들듯...
#? openfile_ > messagebox > yes > saveFile() > 다른이름저장 창에서 닫기 > 현재 내용 저장 x > 다음 다른 열림

## txt파일만 보여주기
## 디렉토리 트리뷰에서 더블클릭 이벤트 발생시 txt파일 열기 실행
# 클래스로 만들기
# 새 창 기능 추가하기
# 디버거 사용하기
# 꾸미기


import os
import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog, Toplevel, Label, PhotoImage, ttk







# 윈도우 창을 생성하는 곳, 윈도우 창의 이름을 TextEditor라고 문자열을 넣어준다
win = Tk(className=" Python - Windows 메모장 ")
#win.title(" Python - Windows 메모장 ")

# 스크롤텍스트를 생성하고, 창의 넓이와 높이, ctrl + z, ctrl + shift + z 설정
textArea = scrolledtext.ScrolledText(win, wrap="none", width=100, height=40, undo=True, maxundo=5, autoseparators=False)

# toplevel 생성 후, 트리 뷰 생성 & 설정
treeWin = Toplevel(win)
treeWin.title("파일 트리")
treeWin.geometry("250x600")    
treeWin.resizable(False, False)

treeview=ttk.Treeview(treeWin)
treeview.column("#0", width=150)
treeview.heading("#0", text="파 일")
treeview.pack(expand=True, fill="both")

# 아이콘 이미지 파일

dir_icon = PhotoImage(file="C:/Users/94050/Desktop/git/notepad/dir_image.png")
file_icon = PhotoImage(file="C:/Users/94050/Desktop/git/notepad/txt_image.png")


# ROOT 디렉토리 설정
root_dir = "C:/Users/94050/Desktop/git/notepad"


###############################################################################
########################### 기능 ###############################################


# 새 파일을 만드는 함수를 정의한다
def newFile():
    # textArea에 작성된 내용이 있나요?
    if len(textArea.get('1.0', END+'-1c')) > 0:
        # 메세지 박스를 만들고 yes no 단추를 선택한다
        if messagebox.askyesno("저장?", "저장하시겠습니까?"):
            # yes 선택 파일 저장
            saveFile()
        else:
            # 작성한 내용이 없거나 no 선택시 텍스트 내용을 모두 지운다
            textArea.delete('1.0', END)

# 파일 열기 함수를 정의한다
def openFile():
    # 텍스트 내용을 모두 지운다
    textArea.delete('1.0', END)
    # 대화상자를 띄우고 text file과 모든파일의 파일 타입과 파일을 선택한다
    file = filedialog.askopenfile(initialdir= "path", title=" 열기 ", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

    # 선택한 파일이 존재한다면
    if file != None:
        # 선택된 파일에 모든 문자열을 읽어 저장한다
        print(file)
        print("1")
        contents = file.read()
        # '1.0' 위치부터 문자열을 삽입한다
        textArea.insert('1.0', contents)
        # 파일을 닫는다
        file.close()

# 단축키로 호출, 파일 열기 함수를 정의한다
def q_openFile(event):
    # 텍스트 내용을 모두 지운다
    textArea.delete('1.0', END)
    # 대화상자를 띄우고 text file과 모든파일의 파일 타입과 파일을 선택한다
    file = filedialog.askopenfile(initialdir= "path", title=" 열기 ", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

    # 선택한 파일이 존재한다면
    if file != None:
        # 선택된 파일에 모든 문자열을 읽어 저장한다
        contents = file.read()
        # '1.0' 위치부터 문자열을 삽입한다
        textArea.insert('1.0', contents)
        # 파일을 닫는다
        file.close()

# 파일 저장 함수를 정의한다
def saveFile():
    #파일을 저장 위한 대화상자를 띄우고 시작경로, 기본 파일형식, 파일 타입 설정 등을 설정한다
    file = filedialog.asksaveasfile(initialdir="C:/Users/94050/Desktop/python", defaultextension=".txt", filetypes=(("Text_file (.txt)", "*.txt"), ("All file", "*.*")))

    # file에 값이 존재하면 저장한다, 존재 하지 않다면 에러창을 띄우고 리턴한다
    if file != None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

# 단축키 ctrl + s 입력시 저장하기
def q_saveFile(event):
    #파일을 저장 위한 대화상자를 띄우고 시작경로, 기본 파일형식, 파일 타입 설정 등을 설정한다
    file = filedialog.asksaveasfile(initialdir="C:/Users/94050/Desktop/python", defaultextension=".txt", filetypes=(("Text_file (.txt)", "*.txt"), ("All file", "*.*")))

    # file에 값이 존재하면 저장한다, 존재 하지 않다면 에러창을 띄우고 리턴한다
    if file != None:
        print("In")
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

# 파일 내 문자열을 찾는 함수를 정의한다
def findFile():
    # 대화상자에 문자열을 입력받는다
    findString = simpledialog.askstring("찾기", "찾을 내용 : ")
    # 찾을 내용이 있다면
    if findString != None:
        # 스크롤 텍스트에 입력된 내용을 모두 저장한다
        textData = textArea.get('1.0', END)
        
        # 대화상자에 입력된 내용과 스크롤 텍스트에 입력된 내용이 같은 부분을 카운트한다
        occurances = textData.upper().count(findString.upper())

        # 찾는 내용이 있다면 존재 갯수를 출력하고, 찾는 내용이 없으면 찾지 못함을 출력
        if textData.upper().count(findString.upper()) > 0:
            label = messagebox.showinfo("결과", findString + "는 , " + str(occurances) + "개 존재합니다.")
        else:
            label = messagebox.showinfo("결과", "찾지 못하였습니다.")
    else:
        # 찾을 내용이 없다면
        return

# 메모장을 종료하는 함수를 정의한다
def exitWin():
    if messagebox.askyesno("메모장", "정말 메모장을 종료하시겠습니까?"):
        win.destroy()


# 단축키로 메모장을 종료하는 함수를 정의한다
def q_exitWin(event):
    if messagebox.askyesno("메모장", "정말 메모장을 종료하시겠습니까?"):
        win.destroy()



# 메모장을 설명하는 함수를 정의한다
def about():
    aboutWin = Toplevel(win)
    aboutWin.geometry("400x400")
    aboutWin.title("메모장 정보")
    aboutLb = Label(aboutWin, text="연습용 개발 메모장입니다.\n ND 제작")
    aboutLb.pack()
    


def q_treeView(event):


    t_state = treeWin.state()
    
    if t_state == "withdrawn":
        treeWin.deiconify()
    else:
        treeWin.withdraw()
        return


def openFile_(event):
    
    real_coords = (treeview.winfo_pointerx() - treeview.winfo_rootx(),
                           treeview.winfo_pointery() - treeview.winfo_rooty())
    item = treeview.identify('item', *real_coords)
    filename = treeview.item(item)['text']

    #print('real.x: %d, real.y: %d' % real_coords)
    #print('clicked on', treeview.item(item)['text'])
    
    
    for dir_path, dir_names, file_names in os.walk(root_dir):
        for name in file_names:
            if str(filename) == str(name):
                print(dir_path)
                file_path = dir_path

    
    if len(textArea.get('1.0', END+'-1c')) > 0 and messagebox.askyesno( " 저장 ", " 현재 파일을 저장하시겠습니까?") :
        svfile = filedialog.asksaveasfile(initialdir="C:/Users/94050/Desktop/python", defaultextension=".txt", filetypes=(("Text_file (.txt)", "*.txt"), ("All file", "*.*")))
        if svfile != None:
            data = textArea.get('1.0', END+'-1c')
            svfile.write(data)
            svfile.close()
            
        if svfile != None:
            textArea.delete('1.0', END)
            file = open(file_path + "/" + filename, mode='rt', encoding='cp949')

            if file != None:
                contents = file.read()
                textArea.insert('1.0', contents)
                file.close()

        else: return
            

    else:                
        textArea.delete('1.0', END)
        file = open(file_path + "/" + filename, mode='rt', encoding='cp949')

        if file != None:
            contents = file.read()
            textArea.insert('1.0', contents)
            file.close()

            

###############################################################################
################ 메뉴 설정 #######################################################


            
# 창에 메뉴바를 생성한다
menubar = Menu(win)

# 메뉴바에 상위 메뉴(File, Help, About)를 생성한다
fileMenu = Menu(menubar, tearoff=0)
editMenu = Menu(menubar, tearoff=0)
aboutMenu = Menu(menubar, tearoff=0)

# 메뉴바에 상위 메뉴(File, Help, About)를 넣는다
menubar.add_cascade(label="파일", menu=fileMenu)
menubar.add_cascade(label="편집", menu=editMenu)
menubar.add_cascade(label="도움말", menu=aboutMenu)

# 상위 메뉴"File"에 하위메뉴(New, Open, Save, Find, Print, Exit)를 넣고 -
# 각 기능을 부여한다
fileMenu.add_command(label="새로 만들기(N)", command=newFile)
fileMenu.add_command(label="열기(O)", command=openFile)
fileMenu.add_command(label="저장(S)", command=saveFile)
fileMenu.add_command(label="찾기(F)", command=findFile)
fileMenu.add_command(label="인쇄(P)")
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)", command=exitWin)

aboutMenu.add_command(label="메모장 정보", command=about)

#####################################################################################
################## 트리뷰 디렉토리 생성 ################################################

j = 0      
# ROOT 경로에 있는 디렉토리와 파일의 이름을 읽고 treelist를 만든다
for (root, dirs, files) in os.walk(root_dir):
          
        root_ = root.replace("C:/Users/94050/Desktop/python","")
          
        # 디렉토리가 존재하면
        if len(dirs) > 0 :
                

                for dir_name in dirs:      
                        
                        if j == 0:
                                
                                #print("dir: " + dir_name)
                                # 상위 디렉토리를 만든다
                                top = treeview.insert('', 'end', text=dir_name, image=dir_icon, iid= str(dir_name), tags=str(dir_name))
                                
                        if j >= 1:
                                
                                root_iid = root_.replace("\\","")
                                #print("dir: " + dir_name)
                                # 하위 디렉토리를 만든다
                                sub = treeview.insert(top, 'end', text=dir_name, image=dir_icon, iid= str(root_iid) + str(dir_name), tags=str(root_iid) + str(dir_name))
                                mov = treeview.move(str(root_iid) + str(dir_name), str(root_iid), 'end')
                                #print( str(root_iid) +str(dir_name)  +"생성//  " + str(root_iid)  + "저장 " )

                        
                        
        # 파일이 존재하면                        
        if len(files) > 0:
                # 파일 수 만큼
                for file_name in files:
                        file_extension = ".txt"
                        
                        if j == 0:
                                if file_extension in file_name:
                                        #print("file: " + file_name)
                                        # 상위 파일 만든다
                                        top = treeview.insert('', 'end', text=file_name, image=file_icon, tags=str(file_name))
                                        treeview.tag_bind(str(file_name), sequence="<Double-Button-1>", callback=openFile_)
                                
                                
                        

                        if j >= 1:
                                if file_extension in file_name:
                                        root_iid = root_.replace("\\","")
                                        #print("dir: " + dir_name)
                                        # 하위 파일을 만든다
                                        sub = treeview.insert(top, 'end', text=file_name, image=file_icon, iid= str(root_iid) + str(file_name), tags=str(root_iid) + str(file_name))
                                        treeview.tag_bind(str(root_iid) + str(file_name), sequence="<Double-Button-1>", callback=openFile_)
                                        mov = treeview.move(str(root_iid) + str(file_name), str(root_iid), 'end')
                                        #print( str(root_iid) +str(file_name)  +"생성//  " + str(root_iid)  + "저장 " )




        # tkinter에게 이미지를 쓰레기로 만들지 말라 지시하는 것
        #treeview.image = dir_icon, file_icon

        j += 1
        

a = treeWin.frame()
treeWin.withdraw()
treeWin.protocol("WM_DELETE_WINDOW", treeWin.withdraw)
treeWin.bind('<Escape>', lambda e: treeWin.withdraw())

#####################################################################################
############# 단축키 설정 ##############################################################   


win.bind("<Control-s>", q_saveFile)
win.bind("<Control-o>", q_openFile)
win.bind("<Control-w>", q_exitWin)
win.bind("<Control-t>", q_treeView)
treeWin.bind("<Control-t>", q_treeView)




# 설정한 메뉴바의 내용을 윈도우 창에 등록한다
win.config(menu=menubar)


# 스크롤 텍스트을 포장한다
textArea.pack(expand=True, fill="both")

# 윈도우 창을 활성을 유지한다
win.mainloop()
