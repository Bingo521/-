import wx
from math import *
from math import sqrt
class IsPrimeFrame(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent=superion,title=u"Python科学计算器",size=(400,400))
        self.exp=""
        self.ans="0.0"
        #面板-----------------------------------
        panel=wx.Panel(self)
        panel.SetBackgroundColour("blue")
        panel.Bind(wx.EVT_SIZE, self.OnSize)
        #添加控件--------------------------------
        #文本框
        self.textExp = wx.TextCtrl(parent=panel, style=wx.TE_READONLY, pos=(0, 0))
        self.textAns = wx.TextCtrl(parent=panel, style=wx.TE_READONLY)
        #self.textAns.SetBackgroundColour("blue")
        self.textAns.SetBackgroundColour("white")
        self.textAns.SetValue("请输入表达式！")
        #按钮
        self.btnx2 = wx.Button(parent=panel, label="x^2")
        self.btnxy = wx.Button(parent=panel, label="x^y")
        self.btnsin = wx.Button(parent=panel, label="sin")
        self.btncos = wx.Button(parent=panel, label="cos")
        self.btntan = wx.Button(parent=panel, label="tan")
        self.btnsqrt = wx.Button(parent=panel, label="sqrt")
        self.btnlog = wx.Button(parent=panel, label="log")
        self.btnmod = wx.Button(parent=panel, label="mod")
        self.btnC = wx.Button(parent=panel, label="C")
        self.btnback = wx.Button(parent=panel, label="back")
        self.btnPi = wx.Button(parent=panel, label="Pi")
        self.btn7 = wx.Button(parent=panel, label="7")
        self.btn8 = wx.Button(parent=panel, label="8")
        self.btn9 = wx.Button(parent=panel, label="9")
        self.btndiv = wx.Button(parent=panel, label="/")
        self.btnn = wx.Button(parent=panel, label="n!")
        self.btn4 = wx.Button(parent=panel, label="4")
        self.btn5 = wx.Button(parent=panel, label="5")
        self.btn6 = wx.Button(parent=panel, label="6")
        self.btnx = wx.Button(parent=panel, label="x")
        self.btnleft = wx.Button(parent=panel, label="(")
        self.btn1 = wx.Button(parent=panel, label="1")
        self.btn2 = wx.Button(parent=panel, label="2")
        self.btn3 = wx.Button(parent=panel, label="3")
        self.btnadd = wx.Button(parent=panel, label="+")
        self.btnright = wx.Button(parent=panel, label=")")
        self.btndot = wx.Button(parent=panel, label=".")
        self.btn0 = wx.Button(parent=panel, label="0")
        self.btnans = wx.Button(parent=panel, label="=")
        self.btnsub = wx.Button(parent=panel, label="-")
        self.btnlist=[]
        self.btnlist.append( self.btnx2)
        self.btnlist.append(self.btnxy)
        self.btnlist.append(self.btnsin)
        self.btnlist.append(self.btncos)
        self.btnlist.append(self.btntan)
        self.btnlist.append(self.btnsqrt)
        self.btnlist.append(self.btnlog)
        self.btnlist.append(self.btnmod)
        self.btnlist.append(self.btnC)
        self.btnlist.append(self.btnback)
        self.btnlist.append(self.btnPi)
        self.btnlist.append(self.btn7)
        self.btnlist.append(self.btn8)
        self.btnlist.append(self.btn9)
        self.btnlist.append(self.btndiv)
        self.btnlist.append(self.btnn)
        self.btnlist.append(self.btn4)
        self.btnlist.append(self.btn5)
        self.btnlist.append(self.btn6)
        self.btnlist.append(self.btnx)
        self.btnlist.append(self.btnleft)
        self.btnlist.append(self.btn1)
        self.btnlist.append(self.btn2)
        self.btnlist.append(self.btn3)
        self.btnlist.append(self.btnadd)
        self.btnlist.append(self.btnright)
        self.btnlist.append(self.btndot)
        self.btnlist.append(self.btn0)
        self.btnlist.append(self.btnans)
        self.btnlist.append(self.btnsub)
        #绑定事件--------------------------------------------
        for item in self.btnlist:
            self.Bind(wx.EVT_BUTTON,self.fproc,item)
    def Lay(self,size):#布局---------------------------------
        dy=int(size[1]*0.4)
        x=size[0]
        y=size[1]-dy
        sx=0
        sy=dy
        width=x//5
        height=y//6
        t1height=y//8
        t2y=t1height
        t2height=dy-t1height
        self.textExp.SetSize((x,t1height))
        self.textAns.SetPosition((0,t2y))
        self.textAns.SetSize((x,t2height-3))
        #f = wx.Font(t1height, wx.ROMAN, wx.ITALIC, wx.BOLD, True)

        for item in range(0,len(self.btnlist)):
            yy=item//5
            xx=item%5
            #print("(%d,%d)"%(width*xx,dy+height*yy))
            self.btnlist[item].SetPosition((width*xx+3,dy+height*yy))
            self.btnlist[item].SetSize((width-2,height-2))

    def OnSize(self,event):
        size=event.GetSize()
        self.Lay(size)
    def fproc(self,event):
        obj=event.GetEventObject()
        if obj==self.btnlist[0]:
            self.exp="pow("+self.exp+",2)"
        elif obj==self.btnlist[1]:
            self.exp="pow("+self.exp+","
        elif obj==self.btnlist[2]:
            self.exp+="sin"
        elif obj==self.btnlist[3]:
            self.exp += "cos"
        elif obj==self.btnlist[4]:
            self.exp += "tan"
        elif obj==self.btnlist[5]:
            self.exp += "sqrt"
        elif obj==self.btnlist[6]:
            self.exp += "log"
        elif obj==self.btnlist[7]:
            self.exp += "%"
        elif obj==self.btnlist[8]:
            self.exp = ""
        elif obj==self.btnlist[9]:
            if len(self.exp)>0:
                self.exp = self.exp[0:len(self.exp)-1]
        elif obj==self.btnlist[10]:
            self.exp += "pi"
        elif obj==self.btnlist[11]:
            self.exp += "7"
        elif obj==self.btnlist[12]:
            self.exp += "8"
        elif obj==self.btnlist[13]:
            self.exp += "9"
        elif obj==self.btnlist[14]:
            self.exp += "/"
        elif obj==self.btnlist[15]:
            self.exp += "!"
        elif obj==self.btnlist[16]:
            self.exp += "4"
        elif obj==self.btnlist[17]:
            self.exp += "5"
        elif obj==self.btnlist[18]:
            self.exp += "6"
        elif obj==self.btnlist[19]:
            self.exp += "*"
        elif obj==self.btnlist[20]:
            self.exp += "("
        elif obj==self.btnlist[21]:
            self.exp += "1"
        elif obj==self.btnlist[22]:
            self.exp += "2"
        elif obj==self.btnlist[23]:
            self.exp += "3"
        elif obj==self.btnlist[24]:
            self.exp += "+"
        elif obj==self.btnlist[25]:
            self.exp += ")"
        elif obj==self.btnlist[26]:
            self.exp += "."
        elif obj==self.btnlist[27]:
            self.exp += "0"
        elif obj==self.btnlist[28]:
            #self.exp += "="
            try:
                self.ans=str(eval(self.exp))
                self.exp=self.ans
            except:
                self.ans="error"
            print("%s=%s"%(self.exp,self.ans))
        elif obj==self.btnlist[29]:
            self.exp += "-"
        self.textExp.SetValue(self.exp)
        #动态计算答案-------------------------------------------------------
        try:
            if len(self.exp)>0:
                self.ans=str(eval(self.exp))
                self.textAns.SetValue("="+self.ans)
            else:
                self.textAns.SetValue("请输入表达式！")
        except:
            self.textAns.SetValue("Error Expression!")
        #将焦点放在文本框1上------------------------------------------------
        self.textExp.SetInsertionPoint(len(self.exp))
        #self.textExp.FindFocus()
        #print(self.exp)
app=wx.App()
frame=IsPrimeFrame(None)
frame.Show(True)
app.MainLoop()
