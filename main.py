import logging
import argparse
import mylib


def main():
    # logging.basicConfig(filename='debug.log', filemode="w", level=logging.DEBUG)
    logging.basicConfig(filename='info.log', encoding='utf-8', filemode="w", level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.debug('core')
    logging.info('Finished')

def set_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decimal", dest="decimal", action="store") # extra value
    parser.add_argument("-f", "--fast", dest="fast", action="store_true") # existence/non-existence
    args = parser.parse_args()

    print(args.decimal)
    print(args.fast)

    return args


if __name__ == '__main__':
    main()
    print('set_arg test')
    args = set_arg()

    if args.decimal == '1':
        print('1')

    if args.fast:
        print('f option is used')

