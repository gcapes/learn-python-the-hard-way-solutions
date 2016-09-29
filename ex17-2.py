from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Combined most of the commands into one line.
# It's not worth going this far though because it loses readability.
open(to_file, 'w').write(open(from_file).read())

# Study drills
# 1. Remove screen output.
# 2. Make script as short as possible.
# 3. Read about 'cat' command
# 4. Closing files is good housekeeping. 
    # Data might not be written to file until it is closed - a problem if your program crashes.
    # If the file remains open you might not be able to eject the disk the file is on.
    # There is a limit to the number of files you can open. Not closing files brings you
    # closer to this limit.
# 5. The 'import' statement gives access to commands from other modules.
