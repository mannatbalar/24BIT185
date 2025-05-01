def copyupper():
    f1 = open("C:\\Self\\college\\sem2\\10\\input.txt", "r+")
    f2 = open("output.txt", "w+")
    for line in f1:
        f2.write(line.upper())
    f1.close()
    f2.close()

copyupper()
