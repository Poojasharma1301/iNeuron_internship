from logging import *
import argparse
from customlogger import SlackHandler

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('message', help='message string')
    h = '1:DEBUG 2:INFO 3:WARNING 4:ERROR 5:CRITICAL'
    arg.add_argument('-l', '--level', type=int, choices=[1,2,3,4,5], default=2, help=h)
    args = arg.parse_args()

    logger = getLogger('aaa')
    slack_handler = SlackHandler('https://hooks.slack.com/services/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')
    slack_handler.setLevel(DEBUG)

    logger.setLevel(DEBUG)
    logger.addHandler(slack_handler)

    level = [NOTSET, 'logger.debug', 'logger.info', 'logger.warning', 'logger.error', 'logger.critical']
    eval(level[args.level])(args.message)

