import tkinter as tk
import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import re
import bcrypt
import sqlite3

class Application():
    def __init__(self):
        self.janela = ctk.CTk()
        self.tema()
        self.tela()
        self.janela_login()
        self.janela.mainloop()
        
    def tema(self):
        ctk.set_appearance_mode("light")  # Changed to light mode
        ctk.set_default_color_theme("blue")  # Changed to blue theme

    def tela(self):    
        self.janela.geometry("700x400") 
        self.janela.title("Teela") 
        self.janela.resizable(False, False)
        self.janela.configure(fg_color="white")  # Set background to white
        
        
    def janela_login(self):
        lb_title = ctk.CTkLabel(master=self.janela, text="Bem Vindo(a) ao Teela\n Gerenciamento de Ordem de Serviço", 
                                font=("Century Gothic bold", 18), text_color="#000").place(x=25, y=70)

        login_frame = ctk.CTkFrame(master=self.janela, width=360, height=390)
        login_frame.pack(side="right")
        
        # Carregando a imagem com CTkImage
        img_path = "Logomarca1.jpg"  
        img = Image.open(img_path)
        img = img.resize((230, 230), Image.LANCZOS) 
        img_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(230, 230))

        # Usando CTkImage no CTkLabel
        img_label = ctk.CTkLabel(master=self.janela, image=img_ctk, text="")
        img_label.place(x=75, y=110)
        
        
        label_tt = ctk.CTkLabel(master=login_frame, text="Faça seu Login", font=("Century Gothic bold", 20)).place(x=105, y=20)

        self.email_entry = ctk.CTkEntry(master=login_frame, placeholder_text= "E-mail do Usuário", width=310, 
                                      font=("Century Gothic bold", 14))
        self.email_entry.place(x=25, y=80)
        
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo e-mail é de caráter obrigatório.", text_color="black", 
                                    font=("Century Gothic bold", 11)).place(x=25, y=110)

        self.password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do Usuário", show="*", width=310, 
                                    font=("Century Gothic bold", 14))
        self.password_entry.place(x=25, y=160)

        password_label = ctk.CTkLabel(master=login_frame, text="*O campo senha de usuário é de caráter obrigatório.", text_color="black", 
                                    font=("Century Gothic bold", 11)).place(x=25, y=190)

        checkbox = ctk.CTkCheckBox(master=login_frame, text= "Lembrar-me").place(x=25, y=230)
        
        login_Button = ctk.CTkButton(master=self.janela, text="Entrar", width=310, command=self.login).place(x=365, y=280)

        register_label = ctk.CTkLabel(master=login_frame, text= "Não possue conta?").place(x=25, y=320)
        
        register_button = ctk.CTkButton(master=login_frame, text= "Cadastre-se", width=150, 
                                        fg_color="green", hover_color="#2D9334", command=self.tela_register).place(x=175, y=320)

        
    def tela_register(self):
         # Remover o frame de login
        login_frame = self.janela.children.get('!ctkframe')  # Obtem o frame de login
        login_frame.pack_forget()

        # Tela de registro
       
        register_frame = ctk.CTkFrame(master=self.janela, width=350, height=396)
        register_frame.pack(side="right") 
        
        label_tt = ctk.CTkLabel(master=register_frame, text="Cadastro de Usuário", font=("Century Gothic bold", 20)).place(x=90, y=10)
        
        span = ctk.CTkLabel(master=register_frame, text="*Preencha todos os campos com dados corretos", font=("Century Gothic bold", 11)).place(x=25, y=50)
        
        self.register_username_entry = ctk.CTkEntry(master=register_frame, placeholder_text= "Nome do Usuário", width=300, 
                                      font=("Century Gothic bold", 14))
        self.register_username_entry.place(x=25, y=90)
        
        self.register_email_entry = ctk.CTkEntry(master=register_frame, placeholder_text="E-mail do Usuário", width=300, 
                                    font=("Century Gothic bold", 14))
        self.register_email_entry.place(x=25, y=130)
        
        self.register_password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Senha do Usuário", show="*", width=300, 
                                    font=("Century Gothic bold", 14))
        self.register_password_entry.place(x=25, y=170)
        
        self.register_confirme_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Confirme sua senha", show= "*", width=300, 
                                    font=("Century Gothic bold", 14))
        self.register_confirme_entry.place(x=25, y=210)

        back_Button = ctk.CTkButton(master=register_frame, text= "Voltar", width=140, fg_color="gray", 
                                    command=lambda: self.back(register_frame, login_frame)).place(x=25, y=285)
       
        save_Button = ctk.CTkButton(master=register_frame, text= "Salvar", width=140, command=self.save_user).place(x=185, y=285)
            
        checkbox = ctk.CTkCheckBox(master=register_frame, text= "Aceito todos os Termos e Política", 
                                   font=("Century Gothic bold", 10)).place(x=25, y=350)
        
        
    def back(self, register_frame, login_frame):
        # Remover o frame de Cadastro
        register_frame.pack_forget()
        # Devolvendo o frame de login
        login_frame.pack(side="right")

    def save_user(self):
        username = self.register_username_entry.get()
        email = self.register_email_entry.get()
        password = self.register_password_entry.get()
        conf_password = self.register_confirme_entry.get()

        if not username or not email or not password or not conf_password:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        if password != conf_password:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Erro", "Formato de e-mail inválido.")
            return

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Conectar ao banco de dados e inserir os dados
        conexao = sqlite3.connect("Sistema.db")
        cursor = conexao.cursor()
    
        try:
            cursor.execute("INSERT INTO users (Username, Email, Password) VALUES (?, ?, ?)", (username, email, hashed_password))
            conexao.commit() 
            messagebox.showinfo(title="Estado do Cadastro", message="Parabéns! Usuário cadastrado com sucesso.") 
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "E-mail já cadastrado.")
        finally:
            conexao.close()   # Fecha a conexão    

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Erro", "Por favor, preencha ambos os campos.")
            return

        conexao = sqlite3.connect("Sistema.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM users WHERE Email=?", (email,))
        user = cursor.fetchone()
        conexao.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3]):  # Removido o .encode('utf-8') de user[3]
            self.janela.withdraw()  # Oculta a janela de login
            self.janela_os = OrdemDeServico()  # Cria a janela da Ordem de Serviço
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")
    
class OrdemDeServico:
    def __init__(self):  
        self.janela_os = ctk.CTk() 
        self.janela_os.geometry("700x450")
        self.janela_os.title("Ordem de Serviço")

        # Label de boas-vindas
        label_os = ctk.CTkLabel(master=self.janela_os, text="Bem-vindo à Ordem de Serviço", font=("Century Gothic bold", 20))
        label_os.pack(pady=20)

        # Botão para visualizar ordens de serviços
        self.visualizar_button = ctk.CTkButton(master=self.janela_os, text="Lista de Chamados", command=self.visualizar_ordens)
        self.visualizar_button.place(x=210, y=400)
        
        # Campo de Data de Abertura
        data_atual = datetime.now().strftime("%d/%m/%Y")
        self.entry_data_atual = ctk.CTkEntry(master=self.janela_os, width=300, font=("Century Gothic bold", 12))
        self.entry_data_atual.place(x=25, y=75)
        self.entry_data_atual.insert(0, data_atual)
        
        # Campo de Local de Atendimento
        self.entry_local_atendimento = ctk.CTkEntry(master=self.janela_os, placeholder_text="Local de Atendimento", width=300, text_color="black",
                                                    font=("Century Gothic bold", 12))
        self.entry_local_atendimento.place(x=375, y=75)
        
        # Campo de Descrição do Serviço
        self.entry_descricao_servico = ctk.CTkEntry(master=self.janela_os, placeholder_text="Descrição do Serviço", width=650, text_color="black",
                                                     font=("Century Gothic bold", 12))
        self.entry_descricao_servico.place(x=25, y=120)
        
        # Campo de Setor
        label_setor = ctk.CTkLabel(master=self.janela_os, text="Setor:")
        label_setor.place(x=25, y=160)
        self.setor_var = ctk.StringVar(value="Ger.Operacional")
        self.menu_setor = ctk.CTkOptionMenu(master=self.janela_os, variable=self.setor_var,
                                             values=["Ger.Operacional", "Recepção", "Governança", "Manutenção", "A&B", "Eventos", "TI"])
        self.menu_setor.place(x=25, y=195)
        self.menu_setor.configure(fg_color="gray")
        
        # Campo de Prioridades
        label_setor = ctk.CTkLabel(master=self.janela_os, text="Prioridade:")
        label_setor.place(x=25, y=235)
        
        self.prioridade_var = ctk.StringVar(value="Urgente")
        self.menu_prioridade = ctk.CTkOptionMenu(master=self.janela_os, variable=self.prioridade_var,
                                     values=["Sem urgência", "Urgente", "Avaliação"])
        self.menu_prioridade.place(x=25, y=275)
        self.menu_prioridade.configure(fg_color="gray")
        
        # Campo de Observações
        label_observacoes = ctk.CTkLabel(master=self.janela_os, text="Observações:").place(x=210, y=160)

        self.entry_observacoes = ctk.CTkEntry(master=self.janela_os, width=465, height=170, font=("arial", 14))
        self.entry_observacoes.place(x=210, y=190)

        clean_Button = ctk.CTkButton(master=self.janela_os, text="Limpar Dados", width=140, fg_color="gray", command=self.limpar_ordem).place(x=370, y=400)
        
        service_Button = ctk.CTkButton(master=self.janela_os, text="Salvar", width=140, command=self.salvar_ordem).place(x=530, y=400)

        self.janela_os.mainloop()
        
    def salvar_ordem(self):
        
        data_atual = self.entry_data_atual.get()
        local_atendimento = self.entry_local_atendimento.get()
        descricao_servico = self.entry_descricao_servico.get()
        setor = self.setor_var.get()
        prioridade = self.prioridade_var.get()
        observacoes = self.entry_observacoes.get()

        conexao = sqlite3.connect("Sistema.db")
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO chamados (data_atual, local_atendimento, descricao_servico, status, setor, oficina, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (data_atual, local_atendimento, descricao_servico, setor, prioridade, observacoes))

        conexao.commit()
        conexao.close()

        messagebox.showinfo(title="Estado do Cadastro", message="Parabéns! Ordem de serviço gerada com sucesso.")
    
    def limpar_ordem(self):
        # Limpar todos os campos de entrada
        self.entry_local_atendimento.delete(0, tk.END)
        self.entry_descricao_servico.delete(0, tk.END)
        self.setor_var.set('Ger.Operacional')  
        self.prioridade_var.set('Urgente')
        self.entry_observacoes.delete(0, tk.END)

        messagebox.showinfo(title="Limpar Dados", message="Todos os campos foram limpos.") 

        # Criar a base de dados
        conexao = sqlite3.connect("Sistema.db")
        cursor = conexao.cursor()      

    def visualizar_ordens(self):
        self.janela_visualizar = ctk.CTkToplevel(self.janela_os)
        self.janela_visualizar.geometry("400x450")
        self.janela_visualizar.title("Lista de Chamados")

        # Título da tela
        label_titulo = ctk.CTkLabel(master=self.janela_visualizar, text="Lista de Chamados Solicitados", font=("Century Gothic bold", 18))
        label_titulo.pack(pady=10)

        # Listbox para exibir as ordens
        self.listbox_ordens = ctk.CTkTextbox(master=self.janela_visualizar, width=580, height=300)
        self.listbox_ordens.pack(padx=10, pady=10)

        # Botão para fechar a janela
        close_button = ctk.CTkButton(master=self.janela_visualizar, text="Fechar", command=self.janela_visualizar.destroy)
        close_button.pack(pady=10)

        # Carregar as ordens de serviço
        self.carregar_ordens()

    def carregar_ordens(self):
        conexao = sqlite3.connect("Sistema.db")
        cursor = conexao.cursor()
    
        cursor.execute("SELECT * FROM chamados")
        ordens = cursor.fetchall()
    
        # Limpa a listbox antes de adicionar as novas ordens
        self.listbox_ordens.delete("1.0", tk.END)
    
        for ordem in ordens:
        # Formate a ordem como uma string e adicione ao Textbox
            ordem_str = f"ID: {ordem[0]}, Data: {ordem[1]}, Local: {ordem[2]}, Descrição: {ordem[3]}, Setor: {ordem[4]}, Prioridade: {ordem[5]}, Observações: {ordem[6]}\n"
            self.listbox_ordens.insert(tk.END, ordem_str)    

        conexao.close()


# Criar a base de dados
conexao = sqlite3.connect("Sistema.db")
cursor = conexao.cursor()

# Criar tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)""")

# Criar tabela de chamados
cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data_atual TEXT NOT NULL,
    local_atendimento TEXT NOT NULL,
    descricao_servico TEXT NOT NULL,
    setor TEXT NOT NULL,
    prioridade TEXT NOT NULL,  
    observacoes TEXT NOT NULL  
)""")

try:
    cursor.execute("ALTER TABLE chamados ADD COLUMN oficina TEXT")
except sqlite3.OperationalError:
    pass  # A coluna já existe

conexao.commit()
conexao.close()

Application()

