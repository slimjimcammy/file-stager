from cmdlineparser import CmdLineParser
from io_utils import getOldFiles, moveToStaging
from crtime import get_crtimes
from datetime import datetime, timedelta

parser = CmdLineParser()
freeing_directory, staging_directory = parser.parse()
current_time = datetime.now()
files_to_delete = []
getOldFiles(freeing_directory, current_time, files_to_delete)
moveToStaging(staging_directory, files_to_delete)

