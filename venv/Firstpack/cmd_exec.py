import PySimpleGUI as pg1


def Add_exec(N1,N2):
   N3 = N1 + N2
   pg1.Print("the result of your operation is :", N3)
   return
def Sub_exec(N1,N2):
   N3 = N1 - N2
   pg1.Print("the result of your operation is :", N3)
   return
def Mul_exec(N1,N2):
   N3 = N1 * N2
   pg1.Print("the result of your operation is :", N3)
   return
def Div_exec(N1,N2):
   N3 = N1 / N2
   pg1.Print("the result of your operation is :", N3)
   return