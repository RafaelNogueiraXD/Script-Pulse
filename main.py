from telas.principal import *
from models.parselog import *
from models.controller import *
from resources.docs import *

runningType = pickArgs()

if runningType["index"] == 1:
    opcao = "3"
    print("\n\nexecucao em ssh!\n")
    while opcao != "0":
        print("\nDashboard:\n\t0 - Sair \n\t1 - executar arquivo\n\t2 - configure program\n\t3 - Escrita no docs \n\t4 - Import output \nEscolha: ",end="")
        opcao = input()
        if opcao == "1":
            btn_select_file(1)
        elif opcao == "2":
            btn_configure(1)
        elif opcao == "3":
            escreveDocs()
        elif opcao == "4":
            btn_submit_file(ssh=1,path=input("Escreva o nome do arquivo: "))
        elif opcao == "0":
            print("encerrando programa ...")
        else:
            print("opcao invalida ") 
elif runningType["index"] == 2:
    print(runningType)
    print(runningType["Conditional2"])
    
    dicionario = {
        "path": str(runningType["text"]),
        "Conditional1": str(runningType["Conditional1"]),
        "Conditional2": " " if runningType["Conditional2"] == None else runningType["conditional2"],
        "texto": None
    }

    btn_submit_file(1,dicionario)
    escreveDocs()

else: 
    telaInicial()