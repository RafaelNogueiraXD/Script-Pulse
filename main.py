from telas.principal import *
from models.parselog import *
from models.controller import *
from resources.docs import *

runningType = pickArgs()

if runningType == 1:
    opcao = "3"
    print("\n\nexecucao em ssh!\n")
    while opcao != "0":
        print("\nDashboard:\n\t0 - Sair \n\t1 - executar arquivo\n\t2 - configure program\nEscolha: ",end="")
        opcao = input()
        if opcao == "1":
            btn_select_file(1)
        elif opcao == "2":
            btn_configure(1)
        elif opcao == "3":
            escreveDocs()
        elif opcao == "0":
            print("encerrando programa ...")
        else:
            print("opcao invalida ") 
    
else: 
    telaInicial()