import PySimpleGUI as pg
import cmd_exec

pg.theme('SandyBeach')

layout = [
    [pg.Text('Simple Calculator')],
    [pg.Text('Enter the Number1'), pg.InputText()],
    [pg.Text('Enter the Number2'), pg.InputText()],
    [pg.Button('Add'), pg.Button('Divide')],
    [pg.Button('Subtract'), pg.Button('Multiply')],
    [pg.Button('Exit')]
         ]

window = pg.Window('Simple Calculator', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    elif event == 'Add':
        N1 = int(values[0])
        N2 = int(values[1])
        print(N1)
        cmd_exec.Add_exec(N1,N2)
    elif event == 'Multiply':
        N1 = int(values[0])
        N2 = int(values[1])
        print(N1)
        cmd_exec.Mul_exec(N1, N2)
    elif event == 'Divide':
        N1 = int(values[0])
        N2 = int(values[1])
        print(N1)
        cmd_exec.Div_exec(N1, N2)
    elif event == 'Subtract':
        N1 = int(values[0])
        N2 = int(values[1])
        print(N1)
        cmd_exec.Sub_exec(N1, N2)
window.Close()