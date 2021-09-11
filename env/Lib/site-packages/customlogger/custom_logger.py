# imports {{{1
import logging
import os
from os.path import expanduser

from colorlog import ColoredFormatter

from customlogger.only_filter import OnlyFilter
from customlogger.run_rotating_handler import RunRotatingHandler

# }}}


class CustomLogger:
    # class variable {{{1
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    allLogFileName = 'all.log'
    logDirPath = './log'
    streamLevel = WARNING
    fileLevel = DEBUG
    isSaveLog = False
    isColorLog = True
    backupCount = 5
    fileLogFmt = '%(asctime)s %(levelname)s %(filename)s %(name)s ' \
        '%(lineno)s "%(message)s"'
    streamLogFmt = '%(levelname)-8s %(message)s'
    streamDebugLogFmt = '[%(levelname)s: File "%(filename)s", ' \
        'line %(lineno)s, in %(funcName)s] "%(message)s"'
    streamColorLogFmt = '%(log_color)s%(levelname)-8s%(reset)s %(message)s'
    streamColorDebugLogFmt = '[%(log_color)s%(levelname)s%(reset)s: ' \
        'File "%(filename)s", line %(lineno)s, in %(funcName)s] "%(message)s"'
    dateFmt = '%Y-%m-%d %a %H:%M:%S'

    logColors = {
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }

    # class methods {{{1
    # debugMode {{{2

    @classmethod
    def debugMode(cls):
        cls.streamLevel = CustomLogger.DEBUG

    # property {{{1
    @property
    def logger(self):
        if not self.__logger.handlers or self.__isFirstInitLogger:
            self.setLogger()

        return self.__logger

    # private functions {{{1
    def __init__(  # {{{2
            self, parent=None, logger_name=None, is_default=True):
        name = parent or self
        name = logger_name or type(name).__name__
        logger = logging.getLogger(name)
        self.__logger = logger
        self.isDefault = is_default
        self.__isFirstInitLogger = True
        if self.__logger.handlers:
            self.__isFirstInitLogger = False

    @staticmethod  # __createLogDir {{{2
    def __createLogDir(path):
        path = expanduser(path)
        if os.path.isdir(path):
            return

        os.mkdir(path)
        print('Create log directory. ({})'.format(os.path.abspath(path)))

    # public functions {{{1
    def setLogger(self):  # {{{2
        if self.isDefault:
            self.defaultLoggerSetting()

    def defaultLoggerSetting(self):  # {{{2
        self.__logger.setLevel(CustomLogger.DEBUG)
        if self.isColorLog:
            if self.streamLevel <= self.DEBUG:
                fmt = self.streamColorDebugLogFmt
            else:
                fmt = self.streamColorLogFmt

            self.addStreamColorHandler(self.streamLevel, fmt=fmt)
        else:
            if self.streamLevel <= self.DEBUG:
                fmt = self.streamDebugLogFmt
            else:
                fmt = self.streamLogFmt

            self.addStreamHandler(self.streamLevel, fmt=fmt)

        self.addStreamHandler(
            CustomLogger.INFO, is_only=True, check_level=True)
        if self.isSaveLog:
            self.__createLogDir(self.logDirPath)
            self.addFileHandler(self.fileLevel)
            self.addRunRotatingHandler(CustomLogger.DEBUG, self.backupCount)

    def addHandler(  # {{{2
            self,
            handler,
            level,
            fmt=None,
            datefmt=None,
            is_only=False,
            formatter=None,
    ):
        handler.setLevel(level)

        datefmt = datefmt or self.dateFmt
        formatter = formatter or logging.Formatter(fmt, datefmt)
        handler.setFormatter(formatter)

        # set only filter
        if is_only:
            handler.addFilter(OnlyFilter(level))

        self.__logger.addHandler(handler)

    def addStreamHandler(  # {{{2
            self, level, fmt=None, is_only=False, check_level=False):
        if check_level and self.streamLevel <= level:
            return

        handler = logging.StreamHandler()
        self.addHandler(handler, level, fmt=fmt, is_only=is_only)

    def addStreamColorHandler(  # {{{2
            self, level, fmt=None, is_only=False, check_level=False):
        if check_level and self.streamLevel <= level:
            return

        handler = logging.StreamHandler()
        formatter = ColoredFormatter(
            fmt,
            log_colors=self.logColors,
            style='%',
        )
        self.addHandler(handler, level, is_only=is_only, formatter=formatter)

    def addFileHandler(  # {{{2
            self, level, out_path=None, fmt=None, is_only=False):
        out_path = expanduser(
            out_path or os.path.join(self.logDirPath, self.allLogFileName))
        handler = logging.FileHandler(out_path)
        fmt = fmt or self.fileLogFmt
        self.addHandler(handler, level, fmt, is_only)

    def addRotatingFileHandler(  # {{{2
            self,
            level,
            out_path,
            max_bytes,
            backup_count,
            fmt=None,
            is_only=False):
        handler = logging.handlers.RotatingFileHandler(
            filename=out_path, maxBytes=max_bytes, backupCount=backup_count)
        fmt = fmt or self.fileLogFmt
        self.addHandler(handler, level, fmt, is_only)

    def addRunRotatingHandler(  # {{{2
            self,
            level,
            backup_count,
            out_path=None,
            fmt=None,
            is_only=False):
        out_path = expanduser(out_path or self.logDirPath)
        handler = RunRotatingHandler(out_path, backup_count)
        fmt = fmt or self.fileLogFmt
        self.addHandler(handler, level, fmt, is_only)


# }}}1
