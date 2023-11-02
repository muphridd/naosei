class Disciplina:
    def _init_(self, nome):
        self.nome = nome
        self.atividades = []

    def adicionar_atividade(self, atividade, data):
        for a in self.atividades:
            if a['data'] == data:
                return False  # Não é possível adicionar duas atividades na mesma data
        self.atividades.append({'atividade': atividade, 'data': data, 'concluida': False})
        return True

    def listar_atividades(self, concluidas=False):
        atividades_filtradas = [a for a in self.atividades if a['concluida'] == concluidas]
        if atividades_filtradas:
            for a in atividades_filtradas:
                print(f"Atividade: {a['atividade']} - Data: {a['data']}")
        else:
            print("Nenhuma atividade encontrada.")

    def marcar_concluida(self, atividade):
        for a in self.atividades:
            if a['atividade'] == atividade:
                a['concluida'] = True
                return True
        return False  # Atividade não encontrada

class Agenda:
    def _init_(self):
        self.disciplinas = []

    def adicionar_disciplina(self, nome):
        self.disciplinas.append(Disciplina(nome))

    def encontrar_disciplina(self, nome):
        for disciplina in self.disciplinas:
            if disciplina.nome == nome:
                return disciplina
        return None        

    def adicionar_atividade(self, nome_disciplina, atividade, data):
        disciplina = self.encontrar_disciplina(nome_disciplina)
        if disciplina:
            return disciplina.adicionar_atividade(atividade, data)
        return False  # Disciplina não encontrada

    def listar_atividades(self, concluidas=False):
        for disciplina in self.disciplinas:
            print(f"Disciplina: {disciplina.nome}")
            disciplina.listar_atividades(concluidas)

    def marcar_concluida(self, nome_disciplina, atividade):
        disciplina = self.encontrar_disciplina(nome_disciplina)
        if disciplina:
            return disciplina.marcar_concluida(atividade)
        return False  # Disciplina não encontrada
