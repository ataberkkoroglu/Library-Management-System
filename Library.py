from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QTableWidget,QHeaderView,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QTableWidgetItem,QErrorMessage,QDesktopWidget,QMainWindow,qApp
from PyQt5.QtGui import QFont,QPixmap,QKeySequence,QIcon
from PyQt5.QtCore import Qt
from datetime import datetime
import sys

class Library(QMainWindow):

    def __init__(self):
     super().__init__()
     self.file=open("books.txt","a+",encoding="utf-8")
     
     self.Menu()

    def Menu(self):
       
       self.Window=QWidget()
       self.Window.setStyleSheet("background : black")
       self.Window.setWindowTitle("Library Management")
      
       self.time=QLabel()
       self.time.setFont(QFont('Arial',20,2,True))
       self.time.setStyleSheet("color : White")
     

       self.date=QLabel(str(datetime.strftime(datetime.now(),"%H : %M : %S  %d / %m / %Y ")))
       self.date.setFont(QFont('Arial',20,2,True))
       self.date.setStyleSheet("color : White")
       
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

       v_box.addWidget(self.date)
       
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
      
       v_box.addSpacing(50)
       v_box.addLayout(h_box)
       v_box.addSpacing(50)
       v_box.addLayout(h_box2)
       v_box.addSpacing(50)
       v_box.addLayout(h_box3)
      
       v_box.addStretch()
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

       self.time=QLabel()
       self.time.setStyleSheet("color : red")

       self.file.seek(0)
       self.content=self.file.readlines()
       print(self.content)
        
       self.back=QPushButton("<")
       self.back.setFont(QFont('Arial',14,3))
       self.back.setStyleSheet('background : lightblue')
       
       self.quit=QPushButton("Quit")
       self.quit.setFont(QFont('Arial',14,3))
       self.quit.setStyleSheet("background : red")
       self.quit.setShortcut(QKeySequence('q' or 'Q'))

       self.table=QTableWidget()
       self.table.setFont(QFont('Arial',11,3))
       
       self.table.setStyleSheet("color : red")
       
       self.table.setColumnCount(4)
       self.table.setHorizontalHeaderLabels(["Title","Author","Release Year","Pages"])
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
          
          header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(1,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(2,QHeaderView.ResizeToContents)
          header.setSectionResizeMode(3,QHeaderView.ResizeToContents)
          
          
       else:
         for i in range(0,3):
          self.table.setItem(i,0,QTableWidgetItem(""))
          self.table.setItem(i,1,QTableWidgetItem(""))
          self.table.setItem(i,2,QTableWidgetItem(""))
          self.table.setItem(i,3,QTableWidgetItem(""))
          
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
       
       h_box2.addWidget(self.back)
       h_box2.addSpacing(50)
       h_box2.addWidget(self.quit)
       v_box.addLayout(h_box)
       v_box.addSpacing(50)
       v_box.addWidget(self.table)
       v_box.addSpacing(50)
       v_box.addLayout(h_box2)
       self.Window.setLayout(v_box)
       self.back.clicked.connect(self.Menu)
       self.quit.clicked.connect(self.Quit)
       self.Window.show()
       
   
    def Add(self):
       self.Window=QWidget()
       self.Window.show()
   
    def Remove(self):
       self.Window=QWidget()
       self.Window.show()
      
    def Quit(self):
       qApp.quit()

    def __del__(self):
       
       #self.Window.close()
       self.file.close()

app=QApplication(sys.argv)
app.setWindowIcon(QIcon("Library_Icon.jpg"))
library=Library()
sys.exit(app.exec())