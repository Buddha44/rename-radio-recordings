#
#
"""
@author JAC
@date AT44-C05
@date 2017-09-07

"""
import re
import os
import subprocess


def main():
    rename_files()


def dir4():
    """List the files in the folder/directory """
    subprocess.call("ls", shell=True)


def rename_files():
    """This function renames files in the directory """
    cwd = os.getcwd()
    print("I am now in this directory: ", cwd)
    dir4()

    re_strings_len = len(re_strings())
    print("re_strings() length is", re_strings_len, "\n")

    for n in os.listdir(cwd):
        print(n)

        # The substituted name of the file: n_sub
        n_sub = n
        for i in range(0, re_strings_len):
            n_sub = re.sub(re_strings()[i][0], re_strings()[i][1], n_sub)
        print("I am renaming to→\n", n_sub, "\n", sep="")
        try:
            os.rename(n, n_sub)
        except Exception:
            print("There is something wrong…")

    print("\n\n", "Here is the result of the 'rename' operation: ")
    dir4()


def re_strings():
    """This function contains the set of strings to be processed
    ("find-this-string", "replace-with-this")
    """
    s1 = ("vlc-record-", "")
    s2 = ("-http___", " ")
    s3 = ("mainstream.radioagora.pl_80_tuba10-1.mp3-", "TokFM")
    s4 = ("bialystok.radio.pionier.net.pl_8000_pl_tuba10-1.mp3-", "TokFM")
    s5 = ("s3.deb1.scdn.smcloud.net_t051-1.mp3-", "Radio Plus")
    s6 = ("195.0.0.6_8000_stream-", "Radio6")

    return s1, s2, s3, s4, s5, s6


if __name__ == '__main__':
    main()
