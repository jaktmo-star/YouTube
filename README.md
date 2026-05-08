# YouTube Downloader com Python

Aplicação simples desenvolvida em Python para realizar download de vídeos do YouTube utilizando interface gráfica com **CustomTkinter**.

---

# 📌 Tecnologias Utilizadas

- Python 3
- CustomTkinter
- pytubefix

---

# 📂 Estrutura do Projeto

```bash
youtube-downloader/
│
├── main.py
├── youtube.ico
├── requirements.txt
└── README.md
```

---

# 🚀 Funcionalidades

- Interface gráfica moderna
- Download de vídeos do YouTube
- Feedback visual de sucesso ou erro
- Ícone personalizado da aplicação

---

# 🖥️ Pré-requisitos

Antes de executar o projeto, instale:

- Python 3.10 ou superior

Download oficial:

https://www.python.org

---

# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/youtube-downloader.git
```

## 2. Acesse a pasta do projeto

```bash
cd youtube-downloader
```

## 3. Crie um ambiente virtual (Opcional, mas recomendado)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Instalação das Dependências

## Instale manualmente

```bash
pip install customtkinter pytubefix
```

## Ou utilize o requirements.txt

Crie o arquivo:

```txt
customtkinter
pytubefix
```

Depois execute:

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute o arquivo principal:

```bash
python main.py
```

---

# 🧠 Explicação do Código

## Importação das Bibliotecas

```python
import customtkinter as ctk
from pytubefix import YouTube
```

- `customtkinter` → cria a interface gráfica moderna
- `pytubefix` → realiza o download do vídeo

---

## Configuração Visual

```python
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
```

Define:

- Tema escuro
- Cor azul padrão

---

## Função de Download

```python
def baixar():
```

Responsável por:

1. Capturar o link digitado
2. Criar objeto do YouTube
3. Fazer o download
4. Mostrar mensagem de sucesso ou erro

---

## Capturando o Link

```python
url = entrada.get()
```

Obtém o texto digitado pelo usuário.

---

## Download do Vídeo

```python
yt = YouTube(url)
yt.streams.first().download()
```

- Cria o objeto do vídeo
- Baixa a primeira stream disponível

---

## Mensagem de Status

### Sucesso

```python
status.configure(text="Sucesso!", text_color="green")
```

### Erro

```python
status.configure(text="Erro no link", text_color="red")
```

---

# 💡 Melhorias Futuras

- Escolha de resolução
- Barra de progresso
- Escolha da pasta de download
- Download apenas de áudio
- Histórico de downloads
- Tema claro/escuro dinâmico

---

# ✅ Boas Práticas Aplicadas

- Organização simples do projeto
- Interface amigável
- Tratamento básico de exceções
- Separação da lógica em função

---

# ⚠️ Melhorias Recomendadas no Código

Atualmente o código utiliza:

```python
except:
```

O ideal é utilizar exceções específicas:

```python
except Exception as erro:
    status.configure(text=f"Erro: {erro}", text_color="red")
```

Isso facilita:

- Depuração
- Manutenção
- Identificação de problemas

---

# 🔒 Observações

- Alguns vídeos podem possuir restrições de download.
- O funcionamento depende das alterações da plataforma YouTube.
- Utilize apenas para fins educacionais e pessoais.

---

# 📸 Interface da Aplicação

Exemplo da interface:

<img width="751" height="537" alt="image" src="https://github.com/user-attachments/assets/a8e9babe-3bfb-404a-91d1-a0e780f80696" />

```

---

# 👨‍💻 Autor

Projeto desenvolvido para estudos de:

- Python
- Interface gráfica
- Consumo de bibliotecas externas
- Automação de downloads

---

# ⭐ Contribuição

Contribuições são bem-vindas.

Faça um fork do projeto e envie um pull request.

---

# 📄 Licença

Este projeto está sob a licença MIT.
