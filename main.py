from classes import Agenda

def main():
    agenda = Agenda()

    while True:
        print("Opções de Menu:")
        print("1. Adicionar Matéria")
        print("2. Adicionar Atividad")
        print("3. Marcar Atividade feita")
        print("4. Listar Atividades em Aberto")
        print("5. Listar Atividades feitas")
        print("6. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            nome_materia = input("Nome da materia: ")
            agenda.adicionar_disciplina(nome_materia)
        elif opcao == "2":
            nome_materia = input("Nome da materia: ") 
            exercicio = input("Nome do exercicio: ")
            data = input("Data do exercicio: ")
            if not agenda.adicionar_atividade(nome_materia, exercicio, data):
                print("Não é possível adicionar dois exercícios na mesma data.")
        elif opcao == "3":
            nome_materia= input("Nome do exercicio: ")
            exercicio = input("Nome do Exercício: ")
            if not agenda.marcar_concluida(nome_materia, exercicio):
                print("Exercício ou Matéria não encontrada.")
        elif opcao == "4":
            agenda.listar_atividades(concluidas=False)
        elif opcao == "5":
            agenda.listar_atividades(concluidas=True)
        elif opcao == "6":
            break
        else:
            print("Tente novamente")

if _name_ == "_main_":
    main()
