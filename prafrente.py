import tkinter as tk
from tkinter import messagebox
import random

class SistemaAnticorrupcao:
    def __init__(self, root):
        self.root = root
        self.root.title("sistema anticorrupção na educação")
        self.root.geometry("800x750")

        # Relações registradas iniciais (Opções 1, 2 e 3)
        self.opcoes_registro = [
            {"id": 1, "texto": "para comprar de 40 canetas simples no valor de 2 reais cada ficando 80 reais .", "valor_real": 80, "possiveis": [80, 200, 500]},
            {"id": 2, "texto": "Para compra de computador de 3000 reais de marcar y de mercado que custa 3000 reais.", "valor_real": 3000, "possiveis": [3000, 8000, 9000]},
            {"id": 3, "texto": "comprar de 5 cadernos que no mercado custa 20 reais cada ficando 100 reais no total", "valor_real": 100, "possiveis": [100, 700, 600]}
        ]
        
        self.respostas_fixas = {} 
        self.valores_temp_grupos = {} 
        
        self.senha_governo = "123"
        self.senhas_grupos = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f"}

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.mostrar_pagina_inicial()

    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def mostrar_pagina_inicial(self):
        self.limpar_tela()
        tk.Label(self.container, text="sistema anticorrupção na educação", font=("Arial", 16, "bold")).pack(pady=10)
        
        info_principal = ("Este programa educacional anticorrupção tem como objetivo melhorar a eficiência na aplicação dos recursos financeiros. "
                          "As regras para o funcionamento desse sistema incluem a notificação, em tempo real, de quem envia e de quem recebe o dinheiro. "
                          "Além disso, ainda em tempo real, é fornecida uma explicação detalhada e específica sobre os gastos realizados, como os preços "
                          "dos objetos adquiridos, evitando, assim, um tipo de corrupção conhecido como superfaturamento.")
        tk.Message(self.container, text=info_principal, width=700, justify="center").pack(pady=5)

        info_grupos = (" a intenção de 6 dias se composto por 6 grupos de fiscalizadores ao total seria para dificulta a tentativa de concordar "
                       "com corrupção , exemplo: se o grupo 1 , 2 e 3 concordar com a corrupção ainda falta os grupos 4, 5 e 6 para denuncia")
        tk.Message(self.container, text=info_grupos, width=700, fg="blue").pack(pady=5)

        info_senhas = ("Informação do programa:” senha da universidade/governo é 123, já a senha dos grupos fiscalizados é "
                       "dia 1 é a, dia 2 é b, dia 3 é c, dia 4 d, dia 5 é e, dia 6 é f.”")
        tk.Label(self.container, text=info_senhas, font=("Arial", 10, "bold"), fg="red", wraplength=700).pack(pady=10)

        tk.Button(self.container, text="avançar como aluno", command=self.pagina_aluno, width=35).pack(pady=5)
        tk.Button(self.container, text="avançar como universidade/governo", command=self.pagina_governo, width=35).pack(pady=5)
        tk.Button(self.container, text="avançar grupo de alunos", command=self.pagina_grupos, width=35).pack(pady=5)

    def pagina_aluno(self):
        self.limpar_tela()
        tk.Label(self.container, text="Relação entre universidade x e governo", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.container, text="fiscalizadores universais( alunos) foram fiscalizar em 6 dias em que cada dia foi um grupo de 3 pessoas, ou seja, 18 pessoas diferentes devem confirmar:", wraplength=700).pack(pady=5)
        
        for op in self.opcoes_registro:
            texto_botao = f"Opção {op['id']}: {op['texto']}"
            tk.Button(self.container, text=texto_botao, wraplength=650, command=lambda o=op: self.fiscalizar_opcao(o)).pack(fill="x", padx=50, pady=5)
        
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial).pack(pady=20)

    def fiscalizar_opcao(self, opcao):
        id_op = opcao['id']
        
        if id_op not in self.respostas_fixas:
            self.respostas_fixas[id_op] = random.choice(opcao['possiveis'])
        
        valor_retornado = self.respostas_fixas[id_op]
        
        if valor_retornado == "ERRO_DIVERGENCIA":
            messagebox.showerror("ALERTA", "corrupção detectada")
            return

        resultado = "comprar sem corrupção" if valor_retornado == opcao['valor_real'] else "corrupção detectada"
        messagebox.showinfo("Análise de Fiscalização", f"Valor Retorno Simultâneo: R$ {valor_retornado}\nStatus: {resultado}")

    def pagina_governo(self):
        self.limpar_tela()
        tk.Label(self.container, text="Área da Universidade / Governo", font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Label(self.container, text="Senha:").pack()
        self.ent_senha = tk.Entry(self.container, show="*")
        self.ent_senha.pack()
        
        tk.Label(self.container, text="Comprar:").pack()
        self.ent_comprar = tk.Entry(self.container)
        self.ent_comprar.pack()
        
        tk.Label(self.container, text="Quantos produtos:").pack()
        self.ent_qtd = tk.Entry(self.container)
        self.ent_qtd.pack()
        
        tk.Label(self.container, text="Qual foi o produto comprado:").pack()
        self.ent_prod = tk.Entry(self.container)
        self.ent_prod.pack()
        
        tk.Label(self.container, text="Total em reais:").pack()
        self.ent_total = tk.Entry(self.container)
        self.ent_total.pack()
        
        tk.Button(self.container, text="Registrar Ação", command=self.salvar_nova_opcao).pack(pady=10)
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial).pack()

    def salvar_nova_opcao(self):
        if self.ent_senha.get() != self.senha_governo:
            messagebox.showerror("Erro", "Senha incorreta!")
            return
        try:
            total = float(self.ent_total.get())
            texto_corrido = f"{self.ent_comprar.get()} {self.ent_qtd.get()} {self.ent_prod.get()} {total}"
            
            nova_op = {
                "id": len(self.opcoes_registro) + 1,
                "texto": texto_corrido,
                "valor_real": total,
                "possiveis": [total, total * 1.8, total * 1.9]
            }
            self.opcoes_registro.append(nova_op)
            messagebox.showinfo("Sucesso", f"Opção {nova_op['id']} registrada!")
            self.mostrar_pagina_inicial()
        except:
            messagebox.showerror("Erro", "Preencha os valores corretamente.")

    def pagina_grupos(self):
        self.limpar_tela()
        tk.Label(self.container, text="Área Grupo de Alunos", font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Label(self.container, text="ID da Opção alvo:").pack()
        self.ent_id_alvo = tk.Entry(self.container)
        self.ent_id_alvo.pack()
        
        tk.Label(self.container, text="Dia (1 a 6):").pack()
        self.ent_dia = tk.Entry(self.container)
        self.ent_dia.pack()
        
        tk.Label(self.container, text="Senha do Grupo (oculta):").pack()
        self.ent_senha_grp = tk.Entry(self.container, show="*")
        self.ent_senha_grp.pack()
        
        tk.Label(self.container, text="Valor Numérico (R$):").pack()
        self.ent_valor = tk.Entry(self.container)
        self.ent_valor.pack()
        
        tk.Button(self.container, text="Registrar Valor do Dia", command=self.registrar_dia).pack(pady=5)
        tk.Button(self.container, text="Finalizar e Aplicar", command=self.validar_e_aplicar).pack(pady=10)
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_inicial).pack()

    def registrar_dia(self):
        dia = self.ent_dia.get()
        if self.senhas_grupos.get(dia) == self.ent_senha_grp.get():
            try:
                id_alvo = int(self.ent_id_alvo.get())
                valor = float(self.ent_valor.get())
                if id_alvo not in self.valores_temp_grupos:
                    self.valores_temp_grupos[id_alvo] = {}
                self.valores_temp_grupos[id_alvo][dia] = valor
                messagebox.showinfo("Sucesso", f"Dia {dia} registrado.")
            except:
                messagebox.showerror("Erro", "ID ou Valor inválido.")
        else:
            messagebox.showerror("Erro", "Senha incorreta.")

    def validar_e_aplicar(self):
        try:
            id_alvo = int(self.ent_id_alvo.get())
            dias_preenchidos = self.valores_temp_grupos.get(id_alvo, {})
            
            if len(dias_preenchidos) < 6:
                messagebox.showwarning("Aviso", "Preencha os 6 dias antes de aplicar.")
                return
            
            valores = list(dias_preenchidos.values())
            # Regra: se os valores forem diferentes entre si 
            if len(set(valores)) > 1:
                self.respostas_fixas[id_alvo] = "ERRO_DIVERGENCIA"
                messagebox.showwarning("Aviso", "Valores divergentes entre os grupos.")
            else:
                self.respostas_fixas[id_alvo] = valores[0]
                messagebox.showinfo("Sucesso", f"Opção {id_alvo} atualizada.")
            self.valores_temp_grupos[id_alvo] = {}
        except:
            messagebox.showerror("Erro", "ID inválido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAnticorrupcao(root)
    root.mainloop()