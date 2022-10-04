
def main():
    with open("morse.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("{")
        for index, line in enumerate(lines):
            args = line.split("\t") 
            print('"' + args[0] + '": "' + args[1].replace(" ", "").replace("/", "") + '"', ", " if (index + 1 < len(lines)) else "")
        print("}")


if __name__ == "__main__":
    main()