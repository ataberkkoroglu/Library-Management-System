from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QTableWidget,QHeaderView,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem,QMainWindow,qApp,QFileDialog
from PyQt5.QtGui import QFont,QPixmap,QKeySequence,QIcon
from PyQt5.QtCore import Qt
from datetime import datetime
import sys,pandas as pd,os,openpyxl

class Library(QMainWindow):

    def __init__(self):
     super().__init__()
     self.file=open("books.txt","a+",encoding="utf-8")

     msg=QMessageBox() 
     msg.setWindowIcon(QIcon("Library_Icon.jpg"))
     msg=msg.information(self,"Library Management","Welcome To  The Library Management System!\n"+
                         str(datetime.strftime(datetime.now(),"%H : %M : %S  %d / %m / %Y ")))
     self.Menu()

    def Menu(self):
       
       self.Window=QWidget()
       self.Window.setStyleSheet("background : black")
       self.Window.setWindowTitle("Library Management")
       self.Window.setGeometry(500,200,640,320)
       self.time=QLabel()
       self.time.setFont(QFont('Arial',20,2,True))
       self.time.setStyleSheet("color : White")
            
       self.library=QLabel()
       self.library.setPixmap(QPixmap("Library.jpg"))

       self.text=QLabel("Menu")
       self.text.setFont(QFont('Arial',36,4))
       self.text.setStyleSheet("color : White")
       
       self.list=QPushButton("List Books")
       self.list.setFont(QFont('Arial',14,3))
       self.list.setStyleSheet("background : lightblue")

       self.add=QPushButton("Add Books")
       self.add.setFont(QFont('Arial',14,3))
       self.add.setStyleSheet("background : green")

       self.remove=QPushButton("Remove Books")
       self.remove.setFont(QFont('Arial',14,3))
       self.remove.setStyleSheet("background : orange")

       self.quit=QPushButton("Quit")
       self.quit.setFont(QFont('Arial',14,3))
       self.quit.setStyleSheet("background : red")
       self.quit.setShortcut(QKeySequence('q' or 'Q'))   # When You press Q or q key , program will be terminated.
       
       v_box=QVBoxLayout()
       
       h_box=QHBoxLayout()
       h_box.addStretch()
       h_box.addWidget(self.library)
       h_box.addStretch()

       h_box2=QHBoxLayout()
       h_box2.addStretch()
       h_box2.addWidget(self.text)
       h_box2.addStretch()

       h_box3=QHBoxLayout()
       h_box3.addWidget(self.list)
       h_box3.addSpacing(100)
       h_box3.addWidget(self.add)
       h_box3.addSpacing(100)
       h_box3.addWidget(self.remove)
       h_box3.addSpacing(100)
       h_box3.addWidget(self.quit)
      
       v_box.addSpacing(30)
       v_box.addLayout(h_box)
       v_box.addSpacing(30)
       v_box.addLayout(h_box2)
       v_box.addSpacing(50)
       v_box.addLayout(h_box3)
       v_box.addSpacing(30)

       self.Window.setLayout(v_box)
       self.list.clicked.connect(self.List)
       self.add.clicked.connect(self.Add)
       self.remove.clicked.connect(self.Remove)
       self.quit.clicked.connect(self.Quit)

       self.Window.show()
    


    def List(self):
       
       self.Window=QWidget()
       self.Window.setWindowTitle("Library Management")
       self.Window.setStyleSheet("background : black")

       self.Window.setMinimumWidth(400)
       self.Window.setMinimumHeight(400)

       self.file.seek(0)
       self.content=self.file.readlines()
        
       self.back=QPushButton("<")
       self.back.setFont(QFont('Arial',14,3))
       self.back.setStyleSheet('background : lightblue')
       
       self.quit=QPushButton("Quit")
       self.quit.setFont(QFont('Arial',14,3))
       self.quit.setStyleSheet("background : red")
       self.quit.setShortcut(QKeySequence('q' or 'Q'))

       self.save=QPushButton("Save As Excel")
       self.save.setFont(QFont('Arial',14,3))
       self.save.setStyleSheet("background : green")
       self.save.setShortcut(QKeySequence("return"))

       self.table=QTableWidget()
       self.table.setFont(QFont('Arial',11,3))
       
       self.table.setStyleSheet("color : red")
       
       self.table.setColumnCount(6)
       self.table.setHorizontalHeaderLabels(["Title","Author","Release Year","Pages","Number","Edition"])
       self.table.setRowCount(len(self.content))
       
       header=self.table.horizontalHeader()
       header2=self.table.verticalHeader()
       self.content.sort()
       if (len(self.content)!=0):
        for i in range(0,len(self.content)):
          
          self.content[i]=self.content[i].replace('\n','')
          self.Content=self.content[i][2:].split(',')
         
          
          item=QTableWidgetItem(self.Content[0])
          item.setTextAlignment(Qt.AlignHCenter)
          self.table.setItem(i,0,item)
          
          item=QTableWidgetItem(self.Content[1])
          item.setTextAlignment(Qt.AlignHCenter)
          self.table.setItem(i,1,item)

          item=QTableWidgetItem(self.Content[2])
          item.setTextAlignment(Qt.AlignHCenter)
          self.table.setItem(i,2,item)

          item=QTableWidgetItem(self.Content[3])
          item.setTextAlignment(Qt.AlignHCenter)
          self.table.setItem(i,3,item)

          item=QTableWidgetItem(self.Content[4])
          item.setTextAlignment(Qt.AlignHCenter)
          self.table.setItem(i,4,item)

          item=QTableWidgetItem(self.Content[5])
          item.setTextAlignment(Qt.AlignHCenter)
          self.table.setItem(i,5,item)
          
          header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(1,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(2,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(3,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(4,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(5,QHeaderView.ResizeToContents)

       else:
         for i in range(0,3):
          self.table.setItem(i,0,QTableWidgetItem(""))
          self.table.setItem(i,1,QTableWidgetItem(""))
          self.table.setItem(i,2,QTableWidgetItem(""))
          self.table.setItem(i,3,QTableWidgetItem(""))
          self.table.setItem(i,4,QTableWidgetItem(""))
          self.table.setItem(i,5,QTableWidgetItem(""))
          
       self.table.setEditTriggers(QTableWidget.NoEditTriggers)
       self.table.setSortingEnabled(False)
       header.setSectionResizeMode(QHeaderView.Stretch)
       header2.setSectionResizeMode(QHeaderView.Stretch)

       self.list=QLabel("List Books")
       self.list.setFont(QFont('Arial',36,4))
       self.list.setStyleSheet('color : Red')

       v_box=QVBoxLayout()

       h_box=QHBoxLayout()
       h_box.addStretch()
       h_box.addWidget(self.list)
       h_box.addStretch()
       
       h_box2=QHBoxLayout()
       h_box2.addSpacing(30)
       h_box2.addWidget(self.back)
       h_box2.addSpacing(50)
       h_box2.addWidget(self.save)
       h_box2.addSpacing(50)
       h_box2.addWidget(self.quit)
       h_box2.addSpacing(30)

       v_box.addLayout(h_box)
       v_box.addSpacing(50)
       v_box.addWidget(self.table)
       v_box.addSpacing(50)
       v_box.addLayout(h_box2)

       self.Window.setLayout(v_box)

       self.back.clicked.connect(self.Menu)
       self.quit.clicked.connect(self.Quit)
       self.save.clicked.connect(self.Excel)
       self.Window.show()

    def Excel(self):
     
     self.file.seek(0)
     self.content=self.file.readlines()

     self.title_list=list()
     self.author_list=list()
     self.Year=list()
     self.Page_list=list()
     self.Number_list=list()
     self.Edition_list=list()

     for i in range(0,len(self.content)):

      self.Content=self.content[i][3:].split(',')

      self.title_list.append(self.Content[0])
      self.author_list.append(self.Content[1])
      self.Year.append(self.Content[2])
      self.Page_list.append(self.Content[3])
      self.Number_list.append(self.Content[4])
      self.Edition_list.append(self.Content[5])

     df = pd.DataFrame({'Title':self.title_list,'Author':self.author_list, 'Year':self.Year,  
                         'Pages':self.Page_list, 'Number of Copies':self.Number_list,  
                          "Edition" : self.Edition_list})
     
     default_dir="D://Library-Management-System"
     default_filename=os.path.join(default_dir,"Books.xlsx")

     filename,_=QFileDialog().getSaveFileName(self,"Save File",default_filename,"Excel Files (*.xlsx)")

     if filename!=None:

      with pd.ExcelWriter(filename, engine='openpyxl') as writer:
         df.to_excel(writer,"Page1",index=False,header=True)
     
    def Add(self):
       
       self.Window=QWidget()
       self.Window.setWindowTitle("Library Management")
       self.Window.setStyleSheet("background : black")

       self.Window.setMinimumWidth(400)
       self.Window.setMinimumHeight(1000)

       self.back=QPushButton("<")
       self.back.setFont(QFont('Arial',14,3))
       self.back.setStyleSheet('background : gray')
       
       self.quit=QPushButton("Quit")
       self.quit.setFont(QFont('Arial',14,3))
       self.quit.setStyleSheet("background : red")
       self.quit.setShortcut(QKeySequence('q' or 'Q'))

       self.add=QPushButton("Add")
       self.add.setFont(QFont('Arial',14,3))
       self.add.setStyleSheet("background : green")
       self.add.setShortcut(QKeySequence('return'))

       self.clear=QPushButton("Clear")
       self.clear.setFont(QFont('Arial',14,3))
       self.clear.setStyleSheet("background : lightblue")

       self.list=QPushButton("List Books")
       self.list.setFont(QFont('Arial',14,3))
       self.list.setStyleSheet("background : yellow")

       self.title=QLabel("Title : ")
       self.title.setFont(QFont('Arial',18,3))
       self.title.setStyleSheet("color : white")

       self.Title=QLineEdit()
       self.Title.setFont(QFont('Arial',14,3))
       self.Title.setStyleSheet("color : white")

       self.author=QLabel("Author : ")
       self.author.setFont(QFont('Arial',18,3))
       self.author.setStyleSheet("color : white")

       self.Author=QLineEdit()
       self.Author.setFont(QFont('Arial',14,3))
       self.Author.setStyleSheet("color : white")

       self.release_year=QLabel("Release Year : ")
       self.release_year.setFont(QFont('Arial',18,3))
       self.release_year.setStyleSheet("color : White")

       self.Release_Year=QLineEdit()
       self.Release_Year.setFont(QFont('Arial',14,3))
       self.Release_Year.setStyleSheet("color : White")

       self.page=QLabel("Page : ")
       self.page.setFont(QFont('Arial',18,3))
       self.page.setStyleSheet('color : White')

       self.Page=QLineEdit()
       self.Page.setFont(QFont('Arial',14,3))
       self.Page.setStyleSheet('color : white')

       self.number=QLabel("Number : ")
       self.number.setFont(QFont('Arial',18,3))
       self.number.setStyleSheet('color : White')

       self.Number=QLineEdit()
       self.Number.setFont(QFont('Arial',14,3))
       self.Number.setStyleSheet('color : white')

       self.edition=QLabel("Edition(1,2,3...) : ")
       self.edition.setFont(QFont('Arial',18,3))
       self.edition.setStyleSheet('color : White')

       self.Edition=QLineEdit()
       self.Edition.setFont(QFont('Arial',14,3))
       self.Edition.setStyleSheet('color : white')

       self.library=QLabel()
       self.library.setPixmap(QPixmap("Library.jpg"))

       v_box=QVBoxLayout()
       
       h_box=QHBoxLayout()
       h_box.addSpacing(30)
       h_box.addWidget(self.title)
       h_box.addSpacing(270)
       h_box.addWidget(self.Title)
       h_box.addSpacing(30)

       h_box2=QHBoxLayout()
       h_box2.addSpacing(30)
       h_box2.addWidget(self.author)
       h_box2.addSpacing(241)
       h_box2.addWidget(self.Author)
       h_box2.addSpacing(30)

       h_box3=QHBoxLayout()
       h_box3.addSpacing(30)
       h_box3.addWidget(self.release_year)
       h_box3.addSpacing(157)
       h_box3.addWidget(self.Release_Year)
       h_box3.addSpacing(30)

       h_box4=QHBoxLayout()
       h_box4.addSpacing(30)
       h_box4.addWidget(self.page)
       h_box4.addSpacing(262)
       h_box4.addWidget(self.Page)
       h_box4.addSpacing(30)

       h_box5=QHBoxLayout()
       h_box5.addSpacing(30)
       h_box5.addWidget(self.number)
       h_box5.addSpacing(225)
       h_box5.addWidget(self.Number)
       h_box5.addSpacing(30)

       h_box8=QHBoxLayout()
       h_box8.addSpacing(30)
       h_box8.addWidget(self.edition)
       h_box8.addSpacing(130)
       h_box8.addWidget(self.Edition)
       h_box8.addSpacing(30)

       h_box6=QHBoxLayout()
       h_box6.addSpacing(30)
       h_box6.addWidget(self.back)
       h_box6.addSpacing(50)
       h_box6.addWidget(self.quit)
       h_box6.addSpacing(30)

       h_box7=QHBoxLayout()
       h_box7.addSpacing(30)
       h_box7.addWidget(self.clear)
       h_box7.addSpacing(50)
       h_box7.addWidget(self.list)
       h_box7.addSpacing(50)
       h_box7.addWidget(self.add)
       h_box7.addSpacing(30)
       
       v_box.addSpacing(30)
       v_box.addLayout(h_box6)
       v_box.addSpacing(30)
       v_box.addWidget(self.library)
       v_box.addSpacing(30)
       v_box.addLayout(h_box)
       v_box.addSpacing(30)
       v_box.addLayout(h_box2)
       v_box.addSpacing(30)
       v_box.addLayout(h_box3)
       v_box.addSpacing(30)
       v_box.addLayout(h_box4)
       v_box.addSpacing(30)
       v_box.addLayout(h_box5)
       v_box.addSpacing(30)
       v_box.addLayout(h_box8)
       v_box.addSpacing(30)
       v_box.addLayout(h_box7)
       v_box.addSpacing(30)
       
       self.back.clicked.connect(self.Menu)
       self.quit.clicked.connect(self.Quit)
       self.clear.clicked.connect(self.Clear)
       self.add.clicked.connect(self.Confirm_Add)
       self.list.clicked.connect(self.List)

       self.Window.setLayout(v_box)
       self.Window.show()
    
    def Clear(self):

      if(self.Title.text()!=""):
       self.Title.clear()

      if(self.Edition.text()!=""):
       self.Edition.clear()

      if(self.Number.text()!=""):
       self.Number.clear()

      try:
        self.Author.clear()
        self.Release_Year.clear()
        self.Page.clear()
        
      except:
        pass
      
    def Confirm_Add(self):

      self.file.seek(0)
      self.content=self.file.readlines()
      if('\n' not in self.content[len(self.content)-1]):
        self.file.write('\n')
        self.file.seek(0)
        self.content=self.file.readlines()
      self.content.sort()         
      
      if(self.Title.text()==''):
         QMessageBox.warning(None,"Warning","Please input the title!")

      if(self.Author.text()==''):
        self.Author.setText("Unknown")

      try:
       if(int(self.Release_Year.text())>2024 or int(self.Release_Year.text())<1800):
        QMessageBox.warning(None, "Warning", "Invalid Year.")
        self.Release_Year.clear()

      except:
        QMessageBox.warning(None, "Error", "Year should be Integer.")
        self.Release_Year.clear()

      try:
       if(int(self.Page.text())<1):
        QMessageBox.warning(None,"Warning","The number of pages should be more than zero")
        self.Page.clear()

      except:
        QMessageBox.warning(None, "Error", "Page should be Integer.")
        self.Page.clear()

      try:
       if(int(self.Number.text())<1):
        QMessageBox.warning(None,"Warning","The number of books should be more than zero")
        self.Number.clear()

      except:
        QMessageBox.warning(None,"Error","Number should be Integer.")
        self.Number.clear()
      
      if(self.Edition.text()==''):
        self.Edition.setText("1")
      if(self.Edition.text().isdigit()):
       if ('-' in self.Edition.text()):
        self.Edition.setText(self.Edition.text().replace('-',''))

       if(int(self.Edition.text())<1):
         
         QMessageBox.warning(None,"Warning","The number of books should be more than zero")
         self.Edition.clear()

       if(self.Edition.text()=='1'):
        self.Edition.setText(self.Edition.text()+'st')
       elif (self.Edition.text()=='2'):
        self.Edition.setText(self.Edition.text()+'nd')
       else:
        self.Edition.setText(self.Edition.text()+'th')
      else:
        QMessageBox.warning(None, "Error", "Edition should be Integer.")
        self.Edition.clear()
      
      self.Text=[]
      for i in range(0,len(self.Title.text().split(" "))):
        
        if('I' in self.Title.text().split(" ")[i]):
          self.Text.append(self.Title.text().split(" ")[i].capitalize().replace('i','ı'))
        
        elif ('i' in self.Title.text().split(" ")[i]):
          self.Text.append(self.Title.text().split(" ")[i].capitalize().replace('I','İ'))

        else:
          self.Text.append(self.Title.text().split(" ")[i].capitalize())
      
      self.Title.setText(" ".join(self.Text))
      self.Text.clear()
      for i in range(0,len(self.Author.text().split(" "))):
        if('I' in self.Author.text().split(" ")[i]):
          self.Text.append(self.Author.text().split(" ")[i].capitalize().replace('i','ı'))
        
        elif ('i' in self.Author.text().split(" ")[i]):
          self.Text.append(self.Author.text().split(" ")[i].capitalize().replace('I','İ'))
        else:
         self.Text.append(self.Author.text().split(" ")[i].capitalize())

      
      #self.Text=set(self.Text)
      self.Author.setText(" ".join(list(self.Text)))
      
      flag=False
      number=len(self.content)

      while 1:
        try:
          self.content.remove('\n')
        except:
          try:
            self.content.remove('')
          except:
            break

      if(self.Title.text()!='' and self.Author.text()!='' and self.Release_Year.text()!='' and self.Page.text()!='' and
         self.Number.text()!='' and self.Edition.text()!=''):
       
       if (len(self.content)!=0):

        for i in range(0,len(self.content)):
          
          
          self.Content=self.content[i][3:].split(',')
          
          if(self.Title.text()==self.Content[0] and self.Edition.text()==self.Content[5].replace('\n','')):
             
             self.content[i]=self.content[i].replace('\n','')
             text=",".join([self.Title.text(),self.Content[1],self.Content[2],self.Content[3],
                            str(int(self.Content[4])+int(self.Number.text())),self.Edition.text()])
             
             self.content.pop(i)
             self.content.insert(i,str(i+1) +') '+text+'\n')
                        
             flag=True
             break
          
        if(flag):
         self.file.truncate(0)
         self.file.writelines(self.content)

        else:
          if('\n' not in self.content[len(self.content)-1]):
            self.content[len(self.content)-1]=self.content[len(self.content)-1]+'\n'

          text=str(len(self.content)+1) +') '+",".join([self.Title.text(),self.Author.text(),self.Release_Year.text(),
                                                           self.Page.text(),self.Number.text(),self.Edition.text()])+'\n'
          self.file.write(text)

       else:
        text=str(len(self.content)+1)+") " +",".join([self.Title.text(),self.Author.text(),self.Release_Year.text(),self.Page.text(),
                                                      self.Number.text(),self.Edition.text()])+'\n'
        self.file.write(text)     

    def Remove(self):
       
       self.Window=QWidget()
       self.Window.setWindowTitle("Library Management")
       self.Window.setStyleSheet("background : black")

       self.Window.setMinimumWidth(400)
       self.Window.setMinimumHeight(1000)

       self.back=QPushButton("<")
       self.back.setFont(QFont('Arial',14,3))
       self.back.setStyleSheet('background : gray')
       
       self.quit=QPushButton("Quit")
       self.quit.setFont(QFont('Arial',14,3))
       self.quit.setStyleSheet("background : red")
       self.quit.setShortcut(QKeySequence('q' or 'Q'))

       self.remove=QPushButton("Remove")
       self.remove.setFont(QFont('Arial',14,3))
       self.remove.setStyleSheet("background : green")
       self.remove.setShortcut(QKeySequence('return'))

       self.clear=QPushButton("Clear")
       self.clear.setFont(QFont('Arial',14,3))
       self.clear.setStyleSheet("background : lightblue")

       self.list=QPushButton("List Books")
       self.list.setFont(QFont('Arial',14,3))
       self.list.setStyleSheet("background : yellow")

       self.title=QLabel("Title : ")
       self.title.setFont(QFont('Arial',18,3))
       self.title.setStyleSheet("color : white")

       self.Title=QLineEdit()
       self.Title.setFont(QFont('Arial',14,3))
       self.Title.setStyleSheet("color : white")

       self.edition=QLabel("Edition(1,2,3...) : ")
       self.edition.setFont(QFont('Arial',18,3))
       self.edition.setStyleSheet('color : White')

       self.Edition=QLineEdit()
       self.Edition.setFont(QFont('Arial',14,3))
       self.Edition.setStyleSheet('color : white')

       self.number=QLabel("Number : ")
       self.number.setFont(QFont('Arial',18,3))
       self.number.setStyleSheet('color : White')

       self.Number=QLineEdit()
       self.Number.setFont(QFont('Arial',14,3))
       self.Number.setStyleSheet('color : white')

       self.library=QLabel()
       self.library.setPixmap(QPixmap("Library.jpg"))

       v_box=QVBoxLayout()
       
       h_box=QHBoxLayout()
       h_box.addSpacing(30)
       h_box.addWidget(self.back)
       h_box.addSpacing(50)
       h_box.addWidget(self.quit)
       h_box.addSpacing(30)

       h_box2=QHBoxLayout()
       h_box2.addSpacing(30)
       h_box2.addWidget(self.title)
       h_box2.addSpacing(275)
       h_box2.addWidget(self.Title)
       h_box2.addSpacing(30)

       h_box3=QHBoxLayout()
       h_box3.addSpacing(30)
       h_box3.addWidget(self.number)
       h_box3.addSpacing(225)
       h_box3.addWidget(self.Number)
       h_box3.addSpacing(30)

       h_box4=QHBoxLayout()
       h_box4.addSpacing(30)
       h_box4.addWidget(self.edition)
       h_box4.addSpacing(130)
       h_box4.addWidget(self.Edition)
       h_box4.addSpacing(30)

       h_box5=QHBoxLayout()
       h_box5.addSpacing(30)
       h_box5.addWidget(self.clear)
       h_box5.addSpacing(50)
       h_box5.addWidget(self.list)
       h_box5.addSpacing(50)
       h_box5.addWidget(self.remove)
       h_box5.addSpacing(30)

       v_box.addSpacing(30)
       v_box.addLayout(h_box)
       v_box.addSpacing(30)
       v_box.addWidget(self.library)
       v_box.addSpacing(30)
       v_box.addLayout(h_box2)
       v_box.addSpacing(30)
       v_box.addLayout(h_box3)
       v_box.addSpacing(30)
       v_box.addLayout(h_box4)
       v_box.addSpacing(30)
       v_box.addLayout(h_box5)
       v_box.addSpacing(30)
       self.Window.setLayout(v_box)

       self.clear.clicked.connect(self.Clear)
       self.quit.clicked.connect(self.Quit)
       self.remove.clicked.connect(self.Confirm_Remove)
       self.back.clicked.connect(self.Menu)
       self.list.clicked.connect(self.List)

       self.Window.show()

    def Confirm_Remove(self):

      self.file.seek(0)
      self.content=self.file.readlines()
      if('\n' not in self.content[len(self.content)-1]):
        self.file.write('\n')
        self.file.seek(0)
        self.content=self.file.readlines()
      self.content.sort()         
      
      if(self.Title.text()==''):
         QMessageBox.warning(None,"Warning","Please input the title!")
      
      try:
       if(int(self.Number.text())<1):
        QMessageBox.warning(None,"Warning","The number of books should be more than zero")
        self.Number.clear()

      except:
        QMessageBox.warning(None,"Error","Number should be Integer.")
        self.Number.clear()
      
      if(self.Edition.text()==''):
        self.Edition.setText("1")

      if(self.Edition.text().isdigit()):
       if ('-' in self.Edition.text()):
        self.Edition.setText(self.Edition.text().replace('-',''))
       
       if(int(self.Edition.text())<1):
         QMessageBox.warning(None,"Warning","The number of books should be more than zero")
         self.Edition.clear()

       if(self.Edition.text()=='1'):
        self.Edition.setText(self.Edition.text()+'st')
       elif (self.Edition.text()=='2'):
        self.Edition.setText(self.Edition.text()+'nd')
       else:
        self.Edition.setText(self.Edition.text()+'th')
      else:
        QMessageBox.warning(None, "Error", "Edition should be Integer.")
        self.Edition.clear()
      
      self.Text=[]
      for i in range(0,len(self.Title.text().split(" "))):
        
        if('I' in self.Title.text().split(" ")[i]):
          self.Text.append(self.Title.text().split(" ")[i].capitalize().replace('i','ı'))
        
        elif ('i' in self.Title.text().split(" ")[i]):
          self.Text.append(self.Title.text().split(" ")[i].capitalize().replace('I','İ'))

        else:
          self.Text.append(self.Title.text().split(" ")[i].capitalize())
      
      self.Title.setText(" ".join(self.Text))

      self.file.seek(0)
      self.content=self.file.readlines()
      flag=False
      
      while 1:
        try:
          self.content.remove('\n')
        except:
          try:
            self.content.remove('')
          except:
            break
      
      if(self.Title.text()!='' and self.Edition.text()!='' and self.Number.text()!=''):
       
       if (len(self.content)!=0):

        for i in range(0,len(self.content)):
          
         try:

          self.content[i]=self.content[i].replace('\n','')[3:]
          self.Content=self.content[i].split(',')
          
          
          if(self.Title.text()==self.Content[0] and self.Edition.text()==self.Content[5].replace('\n','')):
             flag=True

             if(int(self.Number.text())>=int(self.Content[4])):
              self.content.pop(i)
              
              if(len(self.content)!=0):
               self.content[i]=self.content[i][3:]
               for j in range(i,len(self.content)):
                self.content[j]=self.content[j].replace('\n','')
                              
             else:
              text=",".join([self.Title.text(),self.Content[1],self.Content[2],self.Content[3],
                            str(int(self.Content[4])-int(self.Number.text())),self.Edition.text()])
              
              self.content.pop(i)
              self.content.insert(i,text)  
                    
         except:
           break
          
        if(flag):
          self.file.truncate(0)

          if(len(self.content)!=0):
            for i in range(0,len(self.content)):
              self.file.write(str(i+1)+") "+self.content[i]+'\n')
          else:
             self.file.write("")

          self.file=open("books.txt","+a",encoding="utf-8")

        else:
           QMessageBox.warning(None,"Warning","Please check the information you entered.",QMessageBox.Ok)
           self.Clear()

       else:
            QMessageBox.warning(None,"Warning","The Library Is Empty.",QMessageBox.Ok)
            self.Clear()
      
    def Quit(self):
       qApp.quit()

    def __del__(self):
      self.file.close()

app=QApplication(sys.argv)
app.setWindowIcon(QIcon("Library_Icon.jpg"))
library=Library()
sys.exit(app.exec())