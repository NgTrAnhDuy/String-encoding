print("---***---***---***---***---***---***---***---***---")
print("Chào mừng đến với bộ công cụ mã hoá bởi NgTrAnhDuy!")
print("---***---***---***---***---***---***---***---***---")
print("\n")
nn = int(input("Mã hoá (0) - Giải mã (1): "))
print("\n")
if nn == 0:
    ni = str(input("Nhập vào chuỗi (Không có số): "))
    n = ni.lower()
    print("\n")
    kt = ''
    s = ''
    for i in str(n):
        a = ord(i) - ord('a') + 1
        if a >= 10:
            kt += (str(a)+'0')
        else:
            kt += str(a)
    for i in kt:
        a = ord(i)
        s += str(a)
    print('Xâu nhập vào:', ni)
    print('Mã hoá ký tự:', kt)
    print('Mã hoá số:', s)
    print("\n")
    print("-------Complete-------")
    print("Kết thúc chương trình!")
    print("-------Complete-------")
elif nn == 1:
    n = int(input("Nhập vào dãy đã được mã hoá (Không có chữ cái): "))
    print("\n")
    ln = list(str(n))
    m,gm = [],[]
    for i in range(0,len(ln),2):
        m.append(ln[i])
        m.append(ln[i+1])
        j = ''.join(m)
        b = chr(int(j))
        gm.append(b)
        m = []
    c = ''.join(gm)
    s = c
    m, a, i = [], [], 0
    def tim(s):
        bcc = 'abcdefghijklmnopqrstuvwxyz'
        si = int(s)
        if si>13:
            for i in bcc[::-1]:
                if (si-1) == bcc.index(i):
                    return i
        else:
            for i in bcc:
                if (int(s)-1) == bcc.index(i):
                    return i
    while i < len(s):
        if i == len(s) - 1:
            a.append(s[i])
            ja = ''.join(a)
            m.append(tim(ja))
            break
        else:
            if i+2 <= len(s) -1 and s[i+2] == '0':
                if (len(s)-1) - i >= 3:
                    if s[i+3] == '0':
                        a.append(s[i])
                        ja = ''.join(a)
                        m.append(tim(ja))
                        a = []
                        i += 1
                    elif s[i+3] != '0':
                        a.append(s[i])
                        a.append(s[i+1])
                        ja = ''.join(a)
                        if int(ja)>26:
                            m.append(tim(ja[0]))
                            a = []
                            i += 1
                        elif int(ja)<26:
                            m.append(tim(ja))
                            a = []
                            i += 3
                else :
                    a.append(s[i])
                    a.append(s[i+1])
                    ja = ''.join(a)
                    if int(ja)>26:
                        m.append(tim(ja[0]))
                        a = []
                        i += 1
                    elif int(ja)<26:
                        m.append(tim(ja))
                        a = []
                        i += 3
            else:
                a.append(s[i])
                ja = ''.join(a)
                m.append(tim(ja))
                a = []
                i += 1
    tim = ''.join(m)
    print('Dãy nhập vào:',n)
    print('Dãy giải mã số:',c)
    print('Dãy giải mã xâu:',tim)
    print("\n")
    print("-------Complete-------")
    print("Kết thúc chương trình!")
    print("-------Complete-------")
else:
    print("\n")
    print("------------Error------------")
    print("Vui lòng restart chương trình")
    print("------------Error------------")