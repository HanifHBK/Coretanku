arr_vokal = ["a", "i", "u", "e", "o"]
s = input()
s += "    "
p = len(s)
for i in range(p-4):
    if (s[i] in arr_vokal):
        if (i >= 1) and (s[i-1] not in arr_vokal) and (s[i-1] != " "):
            if (i >= 2) and (s[i-2] not in arr_vokal) and (s[i-2] != " "):
                if (i >= 3) and (s[i-3] not in arr_vokal) and (s[i-3] != " "):
                    if (i >= 4) and (s[i-4] not in arr_vokal) and (s[i-4] != " "):
                        print(s[i-2] + s[i-1], end="")
                    else:
                        print(s[i-1], end="")
                else :
                    if(s[i-2] == "n"):
                        if(s[i-1] == "y"):
                            print("ny", end="")
                        elif(s[i-1] == "g"):
                            print("ng", end="")
                        else:
                            print(s[i-1], end="")
                    else:
                        print(s[i-1], end="")
            else:
                print(s[i-1], end="")
        print(s[i], end="")
        count = 1
        if (i <= (p-2)) and (s[i+1] not in arr_vokal) and (s[i+1] != " "):
            count = 2
            if (i <= (p-3)) and (s[i+2] not in arr_vokal) and (s[i+2] != " "):
                count = 3
                if (i <= (p-4)) and (s[i+3] not in arr_vokal) and (s[i+3] != " "):
                    count = 4
                    print(s[i+1] + s[i+2], end="")
                else :
                    if(s[i+1] == "n"):
                        if (s[i+2] != "y") and (s[i+2] != "g"):
                            print(s[i+1], end="")
                    else :
                        print(s[i+1], end="")
            elif (s[i+2] == " "):
                print(s[i+1], end="")
        if(s[i+count] != " "):
            print("-", end="")
    if s[i] == " ":
        print(" ", end="")
