import sys

argv = sys.argv
argc = len(argv)

class CmdLineParser:
    def __init__(self, folder_to_free="~/Downloads/", staging="~/Desktop/to-delete"):
        self.folder_to_free = folder_to_free
        self.staging = staging

    def flags(self):
        print("Flags:")
        print("     --to-free [directory_name] (REQUIRED): directory you want to free space from")
        print("     --stager [directory_name]: directory you want to put files to-be-deleted into; default is '~/Desktop/to-delete'")

    def usage(self):
        print("Usage: python3 stager.py --to-free [directory_name] --stager [directory_name]")
        self.flags()
        exit(4)

    def flagParse(self, flag):
        arg = ""
        try:
            flag_index = argv.index(flag)
        except ValueError:
            pass
        else:
            arg_index = flag_index + 1
            if arg_index < argc:
                arg = argv[arg_index]
            else:
                self.usage()

        return arg

    def parse(self):
        if argc < 3:
            self.usage()
        else:
            if argc in range(3, 6):
                folder_to_free = self.flagParse("--to-free")
                if folder_to_free != "":
                    self.folder_to_free = folder_to_free
                else:
                    self.usage()
                staging = self.flagParse("--stager")
                if staging != "":
                    self.staging = staging
            return self.folder_to_free, self.staging

        return None