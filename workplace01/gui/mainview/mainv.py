import PySimpleGUI as sg


class Mainv:
    def __init__(self, title):
        # 윈도우 내 모든 요소들
        layout = [
            [sg.Text("Some text on Row 1")],
            [sg.Text("제목 넣는 컴포넌트"), sg.Text("제목 넣는 컴포넌트")],
            [sg.Input()],
            [sg.Button("Button1")],
            [sg.Text("Enter something on Row 2"), sg.InputText()],
            [sg.Button("Ok"), sg.Button("Cancel")],
        ]

        # 윈도우 생성
        window = sg.Window(title, layout)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if (
                event == sg.WIN_CLOSED or event == "Cancel"
            ):  # if user closes window or clicks cancel
                break
            if event == "Button1":
                print("버튼1이 눌러짐")
            print("You entered ", values[0])

        window.close()
