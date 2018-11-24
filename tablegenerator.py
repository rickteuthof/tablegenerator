import sys
newfile = "\\hline\n"
len_ = 0
for line in sys.stdin:
    split = line.split()
    if len_ == 0:
        len_ = len(split)
    else:
        if len_ != len(split):
            raise Exception("Invalid line lengths.")
    newfile += "  "
    for item in split:
        newfile += item + " & "
    newfile = newfile[:-2]
    newfile += "\\\\ \\hline\n"
l = "|l" * len_ + "|"
newfile = "\\begin{table}[H]\n\\begin{tabular}{" + l + "}\n" + newfile
newfile += "\\end{tabular}\n\\end{table}"
print(newfile.strip())
