import PySimpleGUI as sg
import os.path
from glob import glob


class Mainv2:
    def __init__(self):
        # 2개의 컬럼으로 구성된 윈도우
        left_col = [
            [
                sg.Text("이미지가 들어있는 폴더를 선택해주세요."),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(button_text="열기"),
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
                )
            ],
        ]

        # 선택된 파일명만 보여준다
        image_col = [
            [sg.Text("선택한 폴더의 이미지 리스트")],
            [sg.Text(size=(40, 1), key="-TOUT-")],  # TOUT => Text Out
            [sg.Image(key="-IMAGE-")],
        ]

        layout = [
            [sg.Menu([["메뉴"], ["파일"]])],
            [sg.Column(left_col), sg.VSeperator(), sg.Column(image_col)],
        ]

        window = sg.Window("이미지 뷰어", layout)
        # window.finalize()
        # window.maximize()

        while True:
            event, values = window.read()
            if event in (None, "Exit"):
                break
            if event == "-FOLDER-":  # 폴더명이 채워지면 폴더에 파일 리스트를 생성
                folder = values["-FOLDER-"]
                try:
                    file_list = os.listdir(folder)  # 폴더 내 파일들 리스트 가져옴
                except Exception as e:
                    print(e)
                    file_list = []

                fnames = [  # list comprehension
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                    and f.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp"))
                ]

                # glob
                # fnames = glob(
                #     r"C:\Users\USER\Desktop\workplace01\gui/**/*.png", recursive=True
                # )
                print(fnames)

                window["-FILE LIST-"].update(fnames)

            elif event == "-FILE LIST-":  # 리스트박스에서 파일 1개가 선택됨
                try:
                    filename = os.path.join(
                        values["-FOLDER-"], values["-FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except Exception as e:
                    print(e)

        window.close()
