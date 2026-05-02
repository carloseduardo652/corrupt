import tkinter as tk
from tkinter import messagebox
import random

class SistemaAnticorrupcao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Anticorrupção na Educação")
        self.root.geometry("850x800")

        # Relações registradas iniciais (Adicionado campo qtd_real para comparação)
        self.opcoes_registro = [
            {"id": 1, "texto": "Compra de 40 canetas simples no valor de R$ 2,00 cada (Total: R$ 80,00).", "valor_real": 80, "qtd_real": 40, "possiveis": [80, 200, 500]},
            {"id": 2, "texto": "Compra de computador de R$ 3.000,00 de marca Y (Preço de mercado: R$ 3.000,00).", "valor_real": 3000, "qtd_real": 1, "possiveis": [3000, 8000, 9000]},
            {"id": 3, "texto": "Compra de 5 cadernos (Preço de mercado: R$ 20,00 cada; Total: R$ 100,00).", "valor_real": 100, "qtd_real": 5, "possiveis": [100, 700, 600]}
        ]
        
        self.respostas_fixas = {} 
        self.valores_temp_grupos = {} 
        
        self.senha_governo = "123"
        self.senhas_grupos = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f"}

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)
        self.mostrar_pagina_inicial()

    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def mostrar_pagina_inicial(self):
        self.limpar_tela()
        
        tk.Label(self.container, text="SISTEMA ANTICORRUPÇÃO NA EDUCAÇÃO", 
                 font=("Arial", 18, "bold"), fg="#2c3e50").pack(pady=(0, 20))
        
        texto_principal = (
            "Este programa educacional anticorrupção tem como objetivo melhorar a eficiência na aplicação dos recursos financeiros. "
            "As regras para o funcionamento desse sistema incluem a notificação, em tempo real, de quem envia e de quem recebe o dinheiro. "
            "Além disso, ainda em tempo real, é fornecida uma explicação detalhada e específica sobre os gastos realizados, como os preços "
            "dos objetos adquiridos, posteriormente ocorre o processo de fiscalizadores universais que consiste na atuação de qualquer aluno "
            "que deseja atuar de forma própria no processo de camadas (grupos) relacionadas com outras camadas (grupos) de fiscalização, "
            "evitando, assim, um tipo de corrupção conhecido como superfaturamento. Esse programa pode ser ampliado para outras áreas e formas."
        )
        
        tk.Message(self.container, text=texto_principal, width=750, justify="left", 
                   font=("Arial", 11), aspect=200).pack(pady=10)

        texto_grupos = (
            "Os fiscalizadores universais: a intenção de 6 dias ser composto por 6 grupos de fiscalizadores no total seria para "
            "dificultar a tentativa de concordar com a corrupção. Exemplo: se os grupos 1, 2 e 3 concordarem com a corrupção, "
            "ainda faltam os grupos 4, 5 e 6 para denunciar."
        )
        
        tk.Message(self.container, text=texto_grupos, width=750, fg="#2980b9", 
                   font=("Arial", 11, "italic")).pack(pady=10)

        info_senhas = (
            "Informação do programa: a senha da universidade/governo é 123. "
            "Já a senha dos grupos fiscalizados é: Dia 1 é 'a', Dia 2 é 'b', Dia 3 é 'c', Dia 4 é 'd', Dia 5 é 'e' e Dia 6 é 'f'."
        )
        tk.Label(self.container, text=info_senhas, font=("Arial", 10, "bold"), 
                 fg="#c0392b", wraplength=750).pack(pady=20)

        btn_frame = tk.Frame(self.container)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Avançar como Aluno (Visualizar)", command=self.pagina_aluno, 
                  width=40, bg="#ecf0f1").pack(pady=5)
        tk.Button(btn_frame, text="Avançar como Universidade/Governo", command=self.pagina_governo, 
                  width=40, bg="#ecf0f1").pack(pady=5)
        tk.Button(btn_frame, text="Avançar como Grupo de Fiscalização", command=self.pagina_grupos, 
                  width=40, bg="#ecf0f1").pack(pady=5)

    def pagina_aluno(self):
        self.limpar_tela()
        tk.Label(self.container, text="Relação entre Universidade X e Governo", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.container, text="Fiscalizadores universais (alunos) fiscalizam durante 6 dias. \nCada dia um grupo diferente deve confirmar os valores:", 
                 wraplength=700).pack(pady=10)
        
        for op in self.opcoes_registro:
            texto_botao = f"Opção {op['id']}: {op['texto']}"
            tk.Button(self.container, text=texto_botao, wraplength=650, 
                      command=lambda o=op: self.fiscalizar_opcao(o), bg="white", relief="groove").pack(fill="x", padx=50, pady=5)
        
        tk.Button(self.container, text="Voltar ao Início", command=self.mostrar_pagina_inicial, bg="#bdc3c7").pack(pady=30)

    def fiscalizar_opcao(self, opcao):
        id_op = opcao['id']
        if id_op not in self.respostas_fixas:
            # Simulação: se não auditado, escolhe valor e mantém a quantidade real para o teste
            self.respostas_fixas[id_op] = {"valor": random.choice(opcao['possiveis']), "qtd": opcao['qtd_real']}
        
        resultado = self.respostas_fixas[id_op]
        
        if resultado == "ERRO_DIVERGENCIA":
            messagebox.showerror("ALERTA DE SEGURANÇA", "CORRUPÇÃO DETECTADA: Houve divergência entre os grupos fiscalizadores!")
            return

        # Alteração: agora checa se valor E quantidade são idênticos ao real
        if resultado['valor'] == opcao['valor_real'] and resultado['qtd'] == opcao['qtd_real']:
            status = "COMPRA SEM CORRUPÇÃO"
        else:
            status = "CORRUPÇÃO DETECTADA (Superfaturamento ou divergência de quantidade)"
            
        messagebox.showinfo("Resultado da Fiscalização", f"Valor Auditado: R$ {resultado['valor']:.2f}\nQuantidade Auditada: {resultado['qtd']}\nStatus: {status}")

    def pagina_governo(self):
        self.limpar_tela()
        tk.Label(self.container, text="Área de Registro: Universidade / Governo", font=("Arial", 14, "bold")).pack(pady=10)
        
        fields = [("Senha de Acesso:", "senha"), ("Ação (Ex: Comprar):", "acao"), 
                  ("Quantidade:", "qtd"), ("Produto:", "prod"), ("Valor Total (R$):", "total")]
        
        self.entries = {}
        for label, key in fields:
            tk.Label(self.container, text=label).pack()
            show = "*" if key == "senha" else ""
            ent = tk.Entry(self.container, show=show, width=40)
            ent.pack(pady=2)
            self.entries[key] = ent
        
        tk.Button(self.container, text="Registrar Gasto no Sistema", command=self.salvar_nova_opcao, 
                  bg="#27ae60", fg="white", font=("Arial", 10, "bold")).pack(pady=20)
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial).pack()

    def salvar_nova_opcao(self):
        if self.entries["senha"].get() != self.senha_governo:
            messagebox.showerror("Erro", "Senha do governo incorreta!")
            return
        try:
            total = float(self.entries["total"].get())
            qtd = int(self.entries["qtd"].get())
            texto_corrido = f"{self.entries['acao'].get()} de {qtd} {self.entries['prod'].get()} no valor total de R$ {total:.2f}"
            
            nova_op = {
                "id": len(self.opcoes_registro) + 1,
                "texto": texto_corrido,
                "valor_real": total,
                "qtd_real": qtd,
                "possiveis": [total, total * 1.5, total * 2.0]
            }
            self.opcoes_registro.append(nova_op)
            messagebox.showinfo("Sucesso", f"Gasto ID {nova_op['id']} registrado!")
            self.mostrar_pagina_inicial()
        except ValueError:
            messagebox.showerror("Erro", "O valor total e quantidade devem ser numéricos.")

    def pagina_grupos(self):
        self.limpar_tela()
        tk.Label(self.container, text="Painel do Grupo de Fiscalizadores", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self.container, text="ID da Opção a ser fiscalizada:").pack()
        self.ent_id_alvo = tk.Entry(self.container)
        self.ent_id_alvo.pack(pady=2)
        
        tk.Label(self.container, text="Dia da Fiscalização (1 a 6):").pack()
        self.ent_dia = tk.Entry(self.container)
        self.ent_dia.pack(pady=2)
        
        tk.Label(self.container, text="Senha do Grupo:").pack()
        self.ent_senha_grp = tk.Entry(self.container, show="*")
        self.ent_senha_grp.pack(pady=2)

        # Alteração: Campo Quantidade adicionado
        tk.Label(self.container, text="Quantidade Encontrada:").pack()
        self.ent_qtd_grp = tk.Entry(self.container)
        self.ent_qtd_grp.pack(pady=2)
        
        tk.Label(self.container, text="Valor encontrado em mercado (R$):").pack()
        self.ent_valor = tk.Entry(self.container)
        self.ent_valor.pack(pady=2)
        
        tk.Button(self.container, text="Registrar Relatório do Dia", command=self.registrar_dia, bg="#f39c12").pack(pady=10)
        tk.Button(self.container, text="Consolidar Fiscalização (Aplicar)", command=self.validar_e_aplicar, bg="#2980b9", fg="white").pack(pady=5)
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial).pack(pady=10)

    def registrar_dia(self):
        dia = self.ent_dia.get()
        if self.senhas_grupos.get(dia) == self.ent_senha_grp.get():
            try:
                id_alvo = int(self.ent_id_alvo.get())
                valor = float(self.ent_valor.get())
                qtd = int(self.ent_qtd_grp.get())
                if id_alvo not in self.valores_temp_grupos:
                    self.valores_temp_grupos[id_alvo] = {}
                self.valores_temp_grupos[id_alvo][dia] = {"valor": valor, "qtd": qtd}
                messagebox.showinfo("Sucesso", f"Relatório do Dia {dia} salvo com sucesso.")
            except ValueError:
                messagebox.showerror("Erro", "Verifique se ID, Valor e Quantidade são numéricos.")
        else:
            messagebox.showerror("Erro", "Senha do grupo incorreta.")

    def validar_e_aplicar(self):
        try:
            id_alvo = int(self.ent_id_alvo.get())
            dias_preenchidos = self.valores_temp_grupos.get(id_alvo, {})
            
            if len(dias_preenchidos) < 6:
                messagebox.showwarning("Aviso", f"Ainda faltam {6 - len(dias_preenchidos)} grupos.")
                return
            
            dados = list(dias_preenchidos.values())
            # Verifica se todos os 6 grupos enviaram exatamente o mesmo valor e quantidade
            if any(d != dados[0] for d in dados):
                self.respostas_fixas[id_alvo] = "ERRO_DIVERGENCIA"
                messagebox.showwarning("DIVERGÊNCIA", "Os grupos reportaram dados diferentes!")
            else:
                self.respostas_fixas[id_alvo] = dados[0]
                messagebox.showinfo("Sucesso", "Fiscalização validada por todos os grupos.")
            
            self.valores_temp_grupos[id_alvo] = {} 
        except ValueError:
            messagebox.showerror("Erro", "ID inválido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAnticorrupcao(root)
    root.mainloop()
