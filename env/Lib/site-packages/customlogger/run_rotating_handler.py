# imports {{{
import glob
import logging
import os
import re
from datetime import datetime

# }}}


class RunRotatingHandler(logging.FileHandler):
    __rotatingFilePath = None
    __defaultBackupCount = 3

    def __init__(self, dir_path, backup_count=None):  # {{{1
        filepath = self.__getRotatingFilePath(dir_path, backup_count)
        super().__init__(filepath)

    @staticmethod  # __getRotatingFilePath {{{1
    def __getRotatingFilePath(dir_path, backup_count=None):
        # If set roting file path, return the filepath
        if RunRotatingHandler.__rotatingFilePath:
            return RunRotatingHandler.__rotatingFilePath

        # Get a pattern-matched log file names
        match_filenames = []
        # E.g. 2017-09-12_12-23-40.log
        pattern = r'\d{4}\d{2}\d{2}_\d{2}\d{2}\d{2}.log$'
        log_files = sorted(glob.glob(os.path.join(dir_path, '*')))
        for log_file in log_files:
            match = re.findall(pattern, log_file)
            if len(match):
                match_filenames.append(log_file)

        # Delete old file, then set a new filepath
        backup_count = backup_count or RunRotatingHandler.__defaultBackupCount
        if len(match_filenames) >= backup_count:
            os.remove(match_filenames[0])
        filename = datetime.today().strftime('%Y%m%d_%H%M%S')
        filepath = os.path.join(dir_path, filename + '.log')
        print('Output the run rotating log file to [{}]'.format(
            os.path.abspath(filepath)))

        RunRotatingHandler.__rotatingFilePath = filepath
        return filepath

    # }}}1
