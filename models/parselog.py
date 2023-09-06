import argparse
import logging

def parse_arguments():
    parser = argparse.ArgumentParser()
    # adiciona argumentos

    parser.add_argument("-gpt",type=str , help="Usar o auxilio da IA")
    parser.add_argument("-ssh",type=str , help="Usar para ssh")
   
    parser.add_argument("-output",type=str , help="Importar o output de um arquivo")
    parser.add_argument("word1",type=str,nargs="?",default=None, help="Palavra para filtrar")
    parser.add_argument("word2",type=str,nargs="?",default=None, help="Palavra para filtrar")
   
    parser.add_argument("-v", "--verbose",action="store_true")
    help_msg = "Logging level (INFO=%d DEBUG=%d)" % (logging.INFO, logging.DEBUG)
    args = parser.parse_args()
    return args

def configure_logging(verbose):
    if verbose == logging.DEBUG:
        # Mostra mais detalhes
        logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                            level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(message)s', level=verbose)

def typeRun(args): 
    data = {
        "index": 0,
        "text": None,
        "Conditional1": args.word1,
        "Conditional2":  args.word2
    }
    if args.ssh:
        data["index"] = 1
        return data
    elif args.output:
        data["index"] = 2
        data["text"] = args.output
        return data
    else:
        return data
def pickArgs():
    args = parse_arguments()
    configure_logging(args.verbose)
    return typeRun(args)
    # calculate_square(args)

if __name__ == "__main__":
    pickArgs()
