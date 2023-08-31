import argparse
import logging

def parse_arguments():
    parser = argparse.ArgumentParser()
    # adiciona argumentos

    parser.add_argument("-gpt",type=str , help="Usar o auxilio da IA")
    parser.add_argument("-ssh",type=str , help="Usar para ssh")
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
    if args.ssh:
        return 1
    else:
        return 0
def pickArgs():
    args = parse_arguments()
    configure_logging(args.verbose)
    return typeRun(args)
    # calculate_square(args)

if __name__ == "__main__":
    pickArgs()
