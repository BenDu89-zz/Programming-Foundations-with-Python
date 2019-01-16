import os

def rename_files():
    list = os.listdir("/Users/benjamindunisch/Downloads/prank")
    for val in list:
        os.chdir("/Users/benjamindunisch/Downloads/prank")
        print val
        os.rename(val, val.strip("0123456789"))
rename_files()
