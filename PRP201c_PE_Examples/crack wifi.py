f = open("credPasswd", "x")
for i in range(0,3):
    for j in range(0,3):
        for k in range(0, 3):
            for x in range(0, 3):
                for y in range(0, 3):
                    if i==0:
                        f.write("m")
                    elif i==1:
                        f.write("n")
                    elif i==2:
                        f.write("o")

                    if j==0:
                        f.write("m")
                    elif j==1:
                        f.write("n")
                    elif j==2:
                        f.write("o")

                    if k==0:
                        f.write("m")
                    elif k==1:
                        f.write("n")
                    elif k==2:
                        f.write("o")

                    if x==0:
                        f.write("m")
                    elif x==1:
                        f.write("n")
                    elif x==2:
                        f.write("o")

                    if y==0:
                        f.write("m\n")
                    elif y==1:
                        f.write("n\n")
                    elif y==2:
                        f.write("o\n")