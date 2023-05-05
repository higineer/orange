import logging
import mylib


def main():
    # logging.basicConfig(filename='debug.log', filemode="w", level=logging.DEBUG)
    logging.basicConfig(filename='info.log', encoding='utf-8', filemode="w", level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.debug('core')
    logging.info('Finished')


if __name__ == '__main__':
    main()
    print('good')
