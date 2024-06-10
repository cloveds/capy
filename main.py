import src as c
import argparse

parser = argparse.ArgumentParser(description = "The capy interpreter")

parser.add_argument("file", nargs = 1, metavar = "file", type = str, help = "the file to interpret")
args = parser.parse_args()