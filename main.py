from algoritms import vigenere, permutation, scaling, homophonic
import PySimpleGUI as sg

CRYPTO_ALGS = ['Шифр Виженера', 'Шифр перестановки', 'Гаммирование', 'Монофоническая замена']

if __name__ == "__main__":
    sg.theme('Dark Black')
    sg.set_options(text_justification='center')   
    left_col = [[sg.Text("I алгоритм шифрования")],
                [sg.Drop(values=(CRYPTO_ALGS), auto_size_text=True, key='-DROP1-', size=(32, 1))]]
    right_col = [[sg.Text("II алгоритм шифрования")],
                [sg.Drop(values=(CRYPTO_ALGS), auto_size_text=True, key='-DROP2-', size=(31, 1))]]    
    layout = [[sg.Text("Ключ: "), sg.Input(key='-KEY-', size=(64, 1))],
              [sg.Text("Сообщение: "), sg.Input(key='-MESSAGE-', size=(59, 1))],
              [sg.Column(left_col, element_justification='c'), sg.VSeperator(),sg.Column(right_col, element_justification='c')],
              [sg.Text("Для шифрования одним шифром используйте одинаковое значение в полях выбора.")],
              [sg.Text("Результат: "), sg.Input(key='-RESULT-', size=(61, 1))],
              [sg.Button("Зашифровать", key='-ENCRYPT-'), sg.Push(), sg.Button("Расшифровать", key='-DECRYPT-')]]
    window = sg.Window('Шифратор', layout, font=("Times New Roman", 12), finalize=True)
    key: str = ''
    window['-DROP1-'].update(CRYPTO_ALGS[0])
    window['-DROP2-'].update(CRYPTO_ALGS[0])
    crypt_algs: list = [vigenere.Vigenere(key), permutation.Permutation(key), scaling.Scaling(key), homophonic.Homophonic(key)]
    while True:
        event, values = window.read(timeout=7)  
        if event == sg.WIN_CLOSED:
            break
        if values['-KEY-'] != key:
            key = values['-KEY-']
            crypt_algs: list = [vigenere.Vigenere(key), permutation.Permutation(key), scaling.Scaling(key), homophonic.Homophonic(key)]        
        try:
            if event == '-ENCRYPT-':
                if values['-DROP1-'] == values['-DROP2-']:
                    window['-RESULT-'].update(crypt_algs[CRYPTO_ALGS.index(values['-DROP1-'])].encrypt(values['-MESSAGE-']))
                else:
                    window['-RESULT-'].update(crypt_algs[CRYPTO_ALGS.index(values['-DROP2-'])].encrypt(crypt_algs[CRYPTO_ALGS.index(values['-DROP1-'])].encrypt(values['-MESSAGE-'])))
            if event == '-DECRYPT-':
                if values['-DROP1-'] == values['-DROP2-']:
                    window['-RESULT-'].update(crypt_algs[CRYPTO_ALGS.index(values['-DROP1-'])].decrypt(values['-MESSAGE-']))
                else:
                    window['-RESULT-'].update(crypt_algs[CRYPTO_ALGS.index(values['-DROP1-'])].decrypt(crypt_algs[CRYPTO_ALGS.index(values['-DROP2-'])].decrypt(values['-MESSAGE-'])))
        except:
            pass
    window.close()