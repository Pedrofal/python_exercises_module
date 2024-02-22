def break_continue():
    print("\n" "Break in 5" "\n")
    i = 1
    while i <= 10:
        print(i)
        if i == 5:
            break
        i += 1

   
    print("\n" "Continue skiping 5" "\n")
    i = 1
    while i <= 10:
        if i == 5:
            i += 1
            continue
        print(i)
        i += 1
    print("\n")


