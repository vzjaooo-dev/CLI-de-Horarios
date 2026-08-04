ligado = True

class Disciplinas():
    def __init__(self, nome, prof, dia, hora):
        self.nome = nome
        self.prof = prof
        self.dia = dia
        self.hora = hora

    def retornarResumo(self):
        return f"Disciplina: {self.nome} | Prof: {self.prof} | Dia: {self.dia} | Horário: {self.hora}\n"

    def verificaConflito(self, dia, hora):
        if dia == self.dia and hora == self.hora:
            return True
        else:
            return False

quadroHorarios = []
ligado = True

while ligado:
    print("---Quadro de Horários---\n")
    print("1.Cadastrar Disciplina\n2.Visualizar Horários\n3.Buscar Disciplina (dia da semana)\n4.Sair\n")

    decisao = int(input("\nDigite a opção desejada: \n"))

    if decisao == 1:
        disciplinaNome = input("\nInforme o nome da disciplina: \n")
        disciplinaProf = input("Infome o professor da disciplina: \n")
        disciplinaDia = input("Informe o dia da disciplina: \n").strip().lower()
        disciplinaHora = input("Informe o horário da disciplina: \n").strip().lower()

        temConflito = False

        for disciplina in quadroHorarios:
            if disciplina.verificaConflito(disciplinaDia, disciplinaHora) == True:
                temConflito = True
                print("Conflitos de horários, você já tem uma aula nesse dia e horário.")
                break
        if not temConflito:        
            disciplinaNova = Disciplinas(disciplinaNome, disciplinaProf, disciplinaDia, disciplinaHora)
            quadroHorarios.append(disciplinaNova)
    elif decisao == 2:
        if len(quadroHorarios) == 0:
            print("\nNenhuma disciplina cadastrada até o momento.\n")
        else:
            for disciplina in quadroHorarios:
                print(disciplina.retornarResumo())
    elif decisao == 3:
        buscarDia = input("\nInforme o dia que quer consultar: \n").strip().lower()
        encontrou = False

        for disciplina in quadroHorarios:
            if disciplina.dia == buscarDia:
                print(disciplina.retornarResumo())
                encontrou = True
        if not encontrou:
            print("\nNenhuma aula cadastrada nesse dia.\n")
    elif decisao == 4:
        ligado = False
        print("Saindo do sistema... Até logo!")
    else:
        print("\nOpção inválida.\n")