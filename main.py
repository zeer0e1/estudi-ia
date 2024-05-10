import PySimpleGUI as sg
import google.generativeai as gemini
import os
from datetime import datetime


def configura_gemini(API):

    gemini.configure(api_key=API)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = gemini.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    return model


class Exercicio:
    def __init__(self):
        self.materia = ""
        self.qtd_exercicios = ""
        self.nivel = ""


chat = ""
exercicio = Exercicio()
caminho = ""
exercicios = []
caminho_materia = ""
response = ""
numero_exercicio = ""


def open_new_window(caminho: str):
    caminho_materia = ""
    caminho_do_exercicio_escolhido = ""
    layout = [
        [sg.Text("Matérias disponiveis para a correção: ")],
        [sg.Output(size=(30, 5), key="-OUTPUT2-")],
        [sg.Text("Qual matéria você deseja corrigir ? ")],
        [sg.Input(size=(30, 5), key="-IN1-")],
        [sg.Button("Confirmar", key="-CONFIRMAR1-")],
        [sg.Text("Exercicios disponiveis")],
        [sg.Output(size=(30, 5), key="-OUTPUT3-")],
        [sg.Text("Qual exercicio você deseja corrigir? (Digite o número)")],
        [sg.Input(size=(30, 5), key="-IN2-")],
        [sg.Button("Confirmar", key="-CONFIRMAR2-")],
        [sg.Output(size=(60, 10), key="-OUTPUT4-")],
        [sg.Button("Salvar", key="-SALVAR-")],
        [sg.Button("Fechar")],
        [sg.Text("", key='-OUTPUT9-')]
    ]

    window = sg.Window("Nova Janela", layout, finalize=True)

    with os.scandir(caminho) as pastas:
        for pasta in pastas:
            window["-OUTPUT2-"].print(pasta.name)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            break
        elif event == "-CONFIRMAR1-":
            try:
                window["-OUTPUT3-"].update('')
                caminho_materia = caminho + "//" + window["-IN1-"].get()
                with os.scandir(caminho_materia) as arquivos:
                    for arquivo in arquivos:
                        window["-OUTPUT3-"].print(arquivo.name)
            except:
                 window["-OUTPUT3-"].update('Materia enexistente')

        elif event == "-CONFIRMAR2-":
            try:
                def exercicio_para_string(exercicio):
                    with open(exercicio, "r", encoding="utf-8") as exercicio:
                        conteudo = exercicio.read()
                    return conteudo

                exercicio_para_corrigir = ""
                numero_exercicio = values["-IN2-"]
                with os.scandir(caminho_materia) as arquivos:
                    for arquivo in arquivos:
                        if arquivo.name.startswith(numero_exercicio):
                            caminho_do_exercicio_escolhido = (
                                caminho_materia + "/" + arquivo.name
                            )
                            exercicio_para_corrigir = exercicio_para_string(
                                caminho_do_exercicio_escolhido
                            )

                response = chat.send_message(
                    f"Corrija se a resposta meu exericio {exercicio_para_corrigir} está correta, caso esteja errado me informe o que eu errei"
                )
                window["-OUTPUT4-"].update("")
                window["-OUTPUT4-"].print(response.text)
            except:
                window['-OUTPUT3-'].update('Erro ao procurar exercicio')

        elif event == "-SALVAR-":
            nome_arquivo = f"resposta-exercicio{numero_exercicio}.txt"
            caminho_arquivo = os.path.join(caminho_materia, nome_arquivo)

            with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write(f"{response.text}\n\n")
            
            window['-OUTPUT9-'].update('Resposta salva')

    window.read()
    window.close()


layout = [
    [sg.Text("API KEY"), sg.Input(key="-IN5-", password_char="*")],
    [sg.Text("Caminho dos exercicios:"), sg.Input(key="-IN1-")],
    [sg.Text("Qual materia você deseja estudar ?"), sg.Input(key="-IN2-")],
    [sg.Text("Quantos exercicios você deseja fazer ?"), sg.Input(key="-IN3-")],
    [sg.Text("Qual o nível de dificuldade?"), sg.Input(key="-IN4-")],
    [sg.Button("Enviar"), sg.Button("Sair"), sg.Button("Corrigir")],
    [sg.Text("", key='-OUTPUT8-')]
]

window = sg.Window("App", layout, return_keyboard_events=True, size=(400, 200))


while True:
    chat = configura_gemini(window["-IN5-"].get()).start_chat(history=[])
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break

    if event == "Corrigir":
        caminho = window["-IN1-"].get()
        caminho_valido = os.path.normpath(caminho)
        open_new_window(caminho_valido)

    if event == "Enviar":
        window['-OUTPUT8-'].update('Carregando')
        caminho = window["-IN1-"].get()
        exercicio.materia = window["-IN2-"].get()
        exercicio.qtd_exercicios = window["-IN3-"].get()
        exercicio.nivel = window["-IN4-"].get()
        response = chat.send_message(
            f'Gere um text com {exercicio.qtd_exercicios} exercicios de nivel fácil sobre {exercicio.materia} com um nivel de dificudade {exercicio.nivel} sem mostrar a resposta, somente o enunciado, nesse formato: "Pergunta": exercicio e "Respota": onde eu vou colocar a resposta'
        )
        exercicios.append(response.text)

        caminho_materia = f"{caminho}//{exercicio.materia.upper()}"

        if not os.path.exists(caminho_materia):
            os.mkdir(caminho_materia)

        data_atual = datetime.now()

        def nome_arquivo(caminho_pasta):
            with os.scandir(caminho_pasta) as entradas:
                qtd_arquivos = sum(1 for entrada in entradas if entrada.is_file())
            return qtd_arquivos

        qtd_arquivos = nome_arquivo(caminho_materia) + 1

        nome_arquivo = (
            f'{qtd_arquivos}-{data_atual.strftime("%d/%m/%Y %H:%M")}.txt'.upper()
            .replace(":", "-")
            .replace("/", "-")
            .strip()
        )

        def criar_arquivo_exercicios(caminho_pasta, nome_arquivo, exercicios):

            if not os.path.exists(caminho):
                os.mkdir(caminho)

            nome_arquivo_completo = os.path.join(caminho_pasta, nome_arquivo)

            with open(nome_arquivo_completo, "w", encoding="utf-8") as arquivo:
                for i, exercicio in enumerate(exercicios):
                    arquivo.write(f"{exercicio}\n\n")

        criar_arquivo_exercicios(caminho_materia, nome_arquivo, exercicios)
        window['-OUTPUT8-'].update('Exercicio criado')



window.close()
