import tkinter as tk
from tkinter import ttk, font, messagebox
import random


COLORS = {
    # Fundos
    "bg_absolute_black": "#0D0D0D",
    "bg_dark_blue": "#1A1A2E",
    "bg_deep_purple": "#10002B",
    # Títulos
    "title_neon_pink": "#FF6EC7",
    "title_electric_cyan": "#00FFF7",
    "title_golden_yellow": "#FFBF00",
    # Botões
    "btn_neon_red": "#FF3F3F",
    "btn_neon_green": "#00FF9D",
    "btn_neon_orange": "#FF9D00",
    # Textos
    "text_pure_white": "#FFFFFF",
    "text_light_pink": "#F2A2E8",
    "text_neon_blue": "#00FFFF",
    "text_strong_orange": "#FF4C00",
    # Efeitos e Destaques
    "fx_electric_purple": "#8A2BE2",
    "fx_intense_magenta": "#FF00FF",
    "fx_vibrant_green": "#00FF00",
}

# ----------------- HISTÓRIA DO JOGO -----------------
historia_textos = [
    "No coração de Arkhavel, um antigo mal desperta após séculos adormecido.\n"
    "As cidades do reino foram envoltas por uma névoa mágica, e criaturas sombrias\n"
    "vagueiam pela noite, espalhando caos. Heróis caíram, e somente os mais corajosos\n"
    "poderão restaurar a paz.",
    "Você, jovem caçador arcano, herdou o destino de salvar o reino. Sua espada,\n"
    "suas runas e sua coragem serão testadas como nunca antes.\n"
    "Prepare-se, pois sua jornada começa agora..."
]

# ----------------- TELA INICIAL (AGORA COM ESTILO!) -----------------
class TelaHistoria:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RPG Arkhavel - Caçadores Arcanos")
        self.root.geometry("850x550")
        self.root.configure(bg=COLORS["bg_absolute_black"])
        self.root.resizable(False, False)

        # Centraliza a janela. Porque um herói sempre está no centro das atenções.
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        self.setup_styles()

        self.title_font = font.Font(family="Trajan Pro", size=32, weight="bold")
        self.normal_font = font.Font(family="Segoe UI", size=14)

        self.canvas = tk.Canvas(self.root, bg=COLORS["bg_absolute_black"], highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.title_label = self.canvas.create_text(
            425, 80,
            text="Crônicas de Arkhavel",
            font=self.title_font,
            fill=COLORS["title_golden_yellow"]
        )
        self.canvas.create_text(
            425, 130,
            text="A SAGA DOS CAÇADORES ARCANOS",
            font=("Arial", 14, "bold"),
            fill=COLORS["title_electric_cyan"]
        )

        self.story_frame = ttk.Frame(self.root, style="Mystic.TFrame")
        self.story_frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=250)

        self.text_index = 0

        self.label_texto = tk.Label(self.story_frame, text=historia_textos[self.text_index],
                                      wraplength=730, font=self.normal_font,
                                      fg=COLORS["text_pure_white"], bg=COLORS["bg_deep_purple"], justify="center")
        self.label_texto.pack(expand=True, padx=15, pady=15)

        self.btn_proximo = ttk.Button(self.root, text="Próximo", state="disabled",
                                        command=self.proximo_texto, style="Neon.TButton")
        self.btn_proximo.place(relx=0.5, rely=0.85, anchor="center")

        self.countdown_label = tk.Label(self.root, text="", font=self.normal_font,
                                          fg=COLORS["text_neon_blue"], bg=COLORS["bg_absolute_black"])
        self.countdown_label.place(relx=0.5, rely=0.92, anchor="center")

        self.contagem_regressiva(5)

        self.particles = []
        self.create_particles()
        self.animate_particles()

        self.root.mainloop()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        # Frame místico da história
        style.configure("Mystic.TFrame",
                        background=COLORS["bg_deep_purple"],
                        borderwidth=2,
                        relief="ridge",
                        bordercolor=COLORS["fx_electric_purple"])
        # Botão neon pra clicar sem dó
        style.configure("Neon.TButton",
                        background=COLORS["btn_neon_green"],
                        foreground=COLORS["bg_absolute_black"],
                        font=("Segoe UI", 14, "bold"),
                        relief="raised",
                        borderwidth=0,
                        padding=10,
                        focusthickness=0)
        style.map("Neon.TButton",
                  background=[('pressed', COLORS["fx_vibrant_green"]),
                              ('active', COLORS["btn_neon_orange"]),
                              ('disabled', COLORS["bg_dark_blue"])],
                  foreground=[('disabled', "#555")])

    def create_particles(self):
        # Partículas mágicas, porque um jogo sem brilho é só um programa.
        particle_colors = [COLORS["fx_electric_purple"], COLORS["fx_intense_magenta"], COLORS["title_electric_cyan"]]
        for _ in range(50):
            x = random.randint(0, 850)
            y = random.randint(0, 550)
            size = random.randint(1, 3)
            color = random.choice(particle_colors)
            particle = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
            self.particles.append(particle)

    def animate_particles(self):
        for particle in self.particles:
            x_speed = random.uniform(-0.5, 0.5)
            y_speed = random.uniform(-0.8, 0.8)
            self.canvas.move(particle, x_speed, y_speed)
            x1, y1, _, _ = self.canvas.coords(particle)
            if x1 < -5 or x1 > 855 or y1 < -5 or y1 > 555:
                self.canvas.coords(particle, random.randint(300, 550), 555, random.randint(300, 550) + 2, 557)
        self.root.after(30, self.animate_particles)

    def contagem_regressiva(self, t):
        if t > 0:
            self.countdown_label.config(text=f"O destino aguarda... {t}")
            self.root.after(1000, lambda: self.contagem_regressiva(t - 1))
        else:
            self.countdown_label.config(text="A jornada te chama. Avance!")
            self.btn_proximo.config(state="normal")

    def proximo_texto(self):
        self.text_index += 1
        if self.text_index < len(historia_textos):
            self.label_texto.config(text=historia_textos[self.text_index])
            self.btn_proximo.config(state="disabled")
            self.contagem_regressiva(5)
        else:
            self.root.destroy()
            RPGGame()

# ----------------- JOGO PRINCIPAL (Onde a porrada come!) -----------------
class RPGGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RPG Arkhavel - Arena dos Destemidos")
        self.root.geometry("900x700")
        self.root.configure(bg=COLORS["bg_absolute_black"])
        self.root.minsize(800, 600)
        
        # Centraliza de novo, porque agora a arena é o palco principal.
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        self.vida_jo = 20
        self.vida_bot = 20
        self.rodadas = 0
        self.max_hp = 20

        self.personagens = ['Siren Valen', 'Elion Thorne', 'Kaen Rook']
        self.habilidades = {
            'Explosão Ígnea': 4,
            'Chute Demolidor': 3,
            'Investida Sombria': 5,
            'Golpe Arcano': 6
        }
        
        self.setup_styles()
        self.create_widgets()
        self.reset_game()
        self.root.mainloop()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # Barras de vida. Verde pra você, vermelho pro inimigo. Simples.
        style.configure("Player.Horizontal.TProgressbar", troughcolor=COLORS["bg_deep_purple"], background=COLORS["btn_neon_green"], thickness=20, bordercolor=COLORS["fx_vibrant_green"], relief="solid")
        style.configure("Bot.Horizontal.TProgressbar", troughcolor=COLORS["bg_deep_purple"], background=COLORS["btn_neon_red"], thickness=20, bordercolor=COLORS["text_strong_orange"], relief="solid")

        # ComboBox estiloso pra não parecer formulário de prefeitura.
        style.configure("TCombobox",
                        fieldbackground=COLORS["bg_deep_purple"],
                        background=COLORS["btn_neon_orange"],
                        foreground=COLORS["text_pure_white"],
                        arrowcolor=COLORS["bg_absolute_black"],
                        selectbackground=COLORS["bg_dark_blue"],
                        selectforeground=COLORS["text_pure_white"],
                        padding=5,
                        font=("Segoe UI", 12))
        style.map('TCombobox', fieldbackground=[('readonly', COLORS["bg_deep_purple"])])

        # Botão de Iniciar (verde = vai que é tua!)
        style.configure("Start.TButton", background=COLORS["btn_neon_green"], foreground=COLORS["bg_absolute_black"], font=("Segoe UI", 12, "bold"), padding=10)
        style.map("Start.TButton", background=[('active', COLORS["fx_vibrant_green"]), ('disabled', COLORS["bg_dark_blue"])])
        
        # Botão de Ataque (vermelho = perigo!)
        style.configure("Attack.TButton", background=COLORS["btn_neon_red"], foreground=COLORS["bg_absolute_black"], font=("Segoe UI", 12, "bold"), padding=10)
        style.map("Attack.TButton", background=[('active', COLORS["text_strong_orange"]), ('disabled', COLORS["bg_dark_blue"])])

    def create_widgets(self):
        # --- Layout Principal ---
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        # Título
        tk.Label(self.root, text="ARENA DE ARKHAVEL", font=("Trajan Pro", 24, "bold"), fg=COLORS["title_golden_yellow"], bg=COLORS["bg_absolute_black"]).grid(row=0, column=0, pady=(20, 10))

        # Frame de seleção
        frame_selecao = tk.Frame(self.root, bg=COLORS["bg_dark_blue"], padx=20, pady=20)
        frame_selecao.grid(row=1, column=0, sticky='ew', padx=20)
        frame_selecao.grid_columnconfigure((0, 1, 2, 3), weight=1)

        tk.Label(frame_selecao, text="Escolha seu Herói:", font=("Segoe UI", 14, "bold"), fg=COLORS["title_electric_cyan"], bg=COLORS["bg_dark_blue"]).grid(row=0, column=0, sticky='w', pady=5)
        self.personagem_var = tk.StringVar(value=self.personagens[0])
        self.personagem_menu = ttk.Combobox(frame_selecao, textvariable=self.personagem_var, values=self.personagens, state="readonly", width=20)
        self.personagem_menu.grid(row=1, column=0, sticky='ew', padx=(0, 20))

        tk.Label(frame_selecao, text="Escolha sua Habilidade:", font=("Segoe UI", 14, "bold"), fg=COLORS["title_electric_cyan"], bg=COLORS["bg_dark_blue"]).grid(row=0, column=1, sticky='w', pady=5)
        self.habilidade_var = tk.StringVar(value='Explosão Ígnea')
        self.habilidade_menu = ttk.Combobox(frame_selecao, textvariable=self.habilidade_var, values=list(self.habilidades.keys()), state="readonly", width=20)
        self.habilidade_menu.grid(row=1, column=1, sticky='ew')
        
        # Botões
        self.btn_start = ttk.Button(frame_selecao, text="INICIAR BATALHA", command=self.iniciar_jogo, style="Start.TButton")
        self.btn_start.grid(row=0, column=2, rowspan=2, sticky='nsew', padx=(20, 10))
        self.btn_roll = ttk.Button(frame_selecao, text="ROLAR DADOS!", command=self.rolar_dados, style="Attack.TButton")
        self.btn_roll.grid(row=0, column=3, rowspan=2, sticky='nsew', padx=(10, 0))

        # Frame de status
        status_frame = tk.Frame(self.root, bg=COLORS["bg_dark_blue"], padx=20, pady=20)
        status_frame.grid(row=2, column=0, sticky='nsew', padx=20, pady=20)
        status_frame.grid_columnconfigure(0, weight=3)
        status_frame.grid_columnconfigure(1, weight=1)
        status_frame.grid_rowconfigure(2, weight=1)

        # Barras de Vida
        vida_frame = tk.Frame(status_frame, bg=COLORS["bg_dark_blue"])
        vida_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
        vida_frame.grid_columnconfigure(1, weight=1)
        
        tk.Label(vida_frame, text="HERÓI", font=("Segoe UI", 12, "bold"), fg=COLORS["btn_neon_green"], bg=COLORS["bg_dark_blue"]).grid(row=0, column=0, sticky='w')
        self.vida_jo_bar = ttk.Progressbar(vida_frame, maximum=self.max_hp, style="Player.Horizontal.TProgressbar")
        self.vida_jo_bar.grid(row=0, column=1, sticky='ew', padx=10)
        self.vida_jo_label = tk.Label(vida_frame, font=("Courier New", 14, "bold"), fg=COLORS["text_pure_white"], bg=COLORS["bg_dark_blue"])
        self.vida_jo_label.grid(row=0, column=2)

        tk.Label(vida_frame, text="VILÃO", font=("Segoe UI", 12, "bold"), fg=COLORS["btn_neon_red"], bg=COLORS["bg_dark_blue"]).grid(row=1, column=0, sticky='w')
        self.vida_bot_bar = ttk.Progressbar(vida_frame, maximum=self.max_hp, style="Bot.Horizontal.TProgressbar")
        self.vida_bot_bar.grid(row=1, column=1, sticky='ew', padx=10)
        self.vida_bot_label = tk.Label(vida_frame, font=("Courier New", 14, "bold"), fg=COLORS["text_pure_white"], bg=COLORS["bg_dark_blue"])
        self.vida_bot_label.grid(row=1, column=2)
        
        # Rodadas
        self.rodada_label = tk.Label(status_frame, text="Rodada: 0", font=("Segoe UI", 16, "bold"), fg=COLORS["title_electric_cyan"], bg=COLORS["bg_dark_blue"])
        self.rodada_label.grid(row=1, column=0, sticky='w', pady=(20,5))
        
        # Log de Batalha
        log_frame = tk.Frame(status_frame, bg=COLORS["bg_deep_purple"], bd=2, relief="sunken")
        log_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')
        log_frame.grid_rowconfigure(0, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)
        
        self.text_status = tk.Text(log_frame, font=("Courier New", 12), state='disabled',
                                     bg=COLORS["bg_deep_purple"], fg=COLORS["text_pure_white"], wrap='word', bd=0, highlightthickness=0,
                                     padx=10, pady=10)
        self.text_status.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(log_frame, command=self.text_status.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.text_status.config(yscrollcommand=scrollbar.set)
        
        self.text_status.tag_config('dano_jo', foreground=COLORS["btn_neon_red"], font=("Courier New", 12, "bold"))
        self.text_status.tag_config('dano_bot', foreground=COLORS["btn_neon_green"], font=("Courier New", 12, "bold"))
        self.text_status.tag_config('empate', foreground=COLORS["title_golden_yellow"])
        self.text_status.tag_config('info', foreground=COLORS["text_neon_blue"])
        self.text_status.tag_config('notification', foreground=COLORS["text_light_pink"])

    def reset_game(self):
        self.vida_jo = self.max_hp
        self.vida_bot = self.max_hp
        self.rodadas = 0
        self.jogo_ativo = False
        self.update_vidas()
        self.update_rodadas()
        self.clear_text()
        self.log("Escolha seu herói e habilidade para começar a pancadaria!", "info")
        self.btn_roll.config(state='disabled')
        self.btn_start.config(state='normal')
        self.habilidade_menu.config(state="readonly")
        self.personagem_menu.config(state="readonly")

    def iniciar_jogo(self):
        self.reset_game()
        self.clear_text()
        self.jogador_personagem = self.personagem_var.get()
        
        # A habilidade inicial é lida aqui, mas será atualizada a cada rodada.
        self.jogador_habilidade_atual = self.habilidade_var.get()

        self.bot_personagem = random.choice(self.personagens)
        self.bot_habilidade = random.choice(list(self.habilidades.keys()))
        self.bot_dano = self.habilidades[self.bot_habilidade]

        self.jogo_ativo = True
        self.btn_roll.config(state='normal')
        self.btn_start.config(state='disabled')
        self.personagem_menu.config(state="disabled")
        
        # MUDANÇA 1: DEIXAR O JOGADOR TROCAR DE SKILL NO MEIO DA LUTA
        # Antes estava 'disabled', agora o jogador pode clicar e escolher outra.
        self.habilidade_menu.config(state="readonly")

        self.log(f"Você é {self.jogador_personagem} com a skill '{self.jogador_habilidade_atual}'. Boa sorte.", "info")
        self.log(f"O oponente é {self.bot_personagem} com a skill '{self.bot_habilidade}'. Cuidado.", "notification")

    def rolar_dados(self):
        if not self.jogo_ativo: return

        self.rodadas += 1
        
        # MUDANÇA 2: ATUALIZAR A HABILIDADE E DANO DO JOGADOR A CADA JOGADA
        # Agora, a cada clique, o jogo verifica qual habilidade está selecionada NO MOMENTO.
        habilidade_escolhida = self.habilidade_var.get()
        dano_jogador = self.habilidades[habilidade_escolhida]
        
        # Loga uma mensagem se o jogador mudou de tática
        if habilidade_escolhida != self.jogador_habilidade_atual:
            self.log(f"Você mudou para a habilidade '{habilidade_escolhida}'!", 'info')
            self.jogador_habilidade_atual = habilidade_escolhida

        # MUDANÇA 3: O BOT AGORA É MENOS PREVISÍVEL!
        # A cada 2 rodadas (na rodada 2, 4, 6...), o bot troca de habilidade.
        if self.rodadas > 1 and self.rodadas % 2 == 0:
            self.log("O VILÃO MUDA SUA ESTRATÉGIA!", "notification")
            self.bot_habilidade = random.choice(list(self.habilidades.keys()))
            self.bot_dano = self.habilidades[self.bot_habilidade]
            self.log(f"Nova habilidade do vilão: '{self.bot_habilidade}'", "notification")

        dado_jogador = random.randint(1, 6)
        dado_bot = random.randint(1, 6)
        self.log(f"\n--- Rodada {self.rodadas} ---", "empate")
        self.log(f"Você rolou: {dado_jogador} | Bot rolou: {dado_bot}", "info")

        if dado_jogador > dado_bot:
            self.vida_bot = max(0, self.vida_bot - dano_jogador)
            self.log(f"ACERTOU! Você usou '{habilidade_escolhida}' e causou {dano_jogador} de dano!", "dano_bot")
        elif dado_bot > dado_jogador:
            self.vida_jo = max(0, self.vida_jo - self.bot_dano)
            self.log(f"DEFENDA-SE! O bot usou '{self.bot_habilidade}' e te deu {self.bot_dano} de dano!", "dano_jo")
        else:
            self.log("EMPATE! Os dados resolveram dar uma folga. Ninguém se machucou.", "empate")

        self.update_vidas()
        self.update_rodadas()

        if self.vida_jo <= 0 or self.vida_bot <= 0:
            self.jogo_ativo = False
            self.btn_roll.config(state='disabled')
            vencedor = "VOCÊ VENCEU! Arkhavel te saúda, herói!" if self.vida_jo > 0 else "GAME OVER! O reino lamenta sua queda."
            cor_vencedor = "dano_bot" if self.vida_jo > 0 else "dano_jo"
            messagebox.showinfo("Fim de Batalha", vencedor)
            self.log(f"\n{vencedor}", cor_vencedor)
            self.btn_start.config(state='normal')
            self.personagem_menu.config(state="readonly")
            return
        
        self.log("Prepare-se para a próxima rodada...", "info")
        # A antiga mensagem mentirosa foi promovida a verdade!
        self.log("Você pode escolher uma nova habilidade para o próximo ataque!")

    def log(self, texto, tag=None):
        self.text_status.config(state='normal')
        self.text_status.insert(tk.END, texto + "\n", tag)
        self.text_status.see(tk.END)
        self.text_status.config(state='disabled')

    def clear_text(self):
        self.text_status.config(state='normal')
        self.text_status.delete('1.0', tk.END)
        self.text_status.config(state='disabled')

    def update_vidas(self):
        self.vida_jo_bar['value'] = self.vida_jo
        self.vida_bot_bar['value'] = self.vida_bot
        self.vida_jo_label.config(text=f"{self.vida_jo}/{self.max_hp} HP")
        self.vida_bot_label.config(text=f"{self.vida_bot}/{self.max_hp} HP")

    def update_rodadas(self):
        self.rodada_label.config(text=f"Rodada: {self.rodadas}")

# ----------------- INÍCIO -----------------
if __name__ == '__main__':
    # Começa com a história, que nem todo bom RPG.
    TelaHistoria()
