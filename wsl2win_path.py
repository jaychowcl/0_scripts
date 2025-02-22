import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filepath',
                    help='wsl filepath to convert to windows filepath')

args = parser.parse_args()

wsl_filepath = args.filepath

win_filepath = str(wsl_filepath).replace("/", "\\")

print("Raw conversion")
print(win_filepath)

print("\nFull path in laptop::")
print(r"\\wsl.localhost\Ubuntu" + win_filepath)


