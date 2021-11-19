import speech_recognition as sr
import sys
from PySimpleGUI import PySimpleGUI as sg

#Caminho do conversor
sys.path.append(r'F:\2 2021 FIP\Processamento Digital de Sinais\Legendas\ffmpeg\bin')

#pip install pyttsx3
#pip install SpeechRecognition
#pipwin
    #PyAudio
    #pocketsphinx
    #pipwin install pocketsphinx no cmd como admin
    #pipwin install PyAudio      no cmd como admin
#https://www.youtube.com/watch?v=4gMkX0LcyJw&ab_channel=ProgramandoComRoger
#https://www.youtube.com/watch?v=vjXsa0I_dtc&ab_channel=WesleyPinheiro
#https://www.youtube.com/watch?v=G14l6CGMAWc&ab_channel=C%C3%B3digoLogo
#https://www.youtube.com/watch?v=wtlnvpVpAf4&ab_channel=Ot%C3%A1vioMiranda
#https://www.youtube.com/watch?v=vjXsa0I_dtc&ab_channel=WesleyPinheiro
#https://pt.stackoverflow.com/questions/303530/como-compilar-um-script-python-em-um-executavel

def TransmissaoVoz():
    print("Começou")
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pode Falar")
        audio = microfone.listen(source)
        print("Audio Capturado")
        try:
            text = microfone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            file = open('Arquivo_Transmissao.txt', 'w+')
            file.write(text)
            file.close()
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


def FileVoz(Arquivo_selecionado):
    print("Começou")
    microfone = sr.Recognizer()
    arquivoAudio = Arquivo_selecionado
    with sr.AudioFile(arquivoAudio) as source:
        audio = microfone.listen(source)
        print("Audio Capturado")
        try:
            text = microfone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            file = open('Arquivo.txt', 'w+')
            file.write(text)
            file.close()
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    
    
#Layout
sg.theme('Reddit')
Layout = [
    [sg.Text("         "), sg.Radio('Por Transmissão', "RADIO1", default=False, key="-IN2-")],
    [sg.Text("         "), sg.Radio('Por Arquivo', "RADIO1", default=True)],
    [sg.Input(), sg.FileBrowse('FileBrowse')],
    [sg.Button('Iniciar')]
]

#Janela
janela = sg.Window('Speech Text', Layout)
#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'Iniciar' and valores['-IN2-'] == True:
        TransmissaoVoz()
    else:
        FileVoz(valores['FileBrowse'])
    
