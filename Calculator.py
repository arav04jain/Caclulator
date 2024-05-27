import tkinter as t
import turtle
import math
import decimal

window = t.Tk()

window.title("Calculator")
window.geometry("625x350")
window.configure(background="black")

label = t.Label(window, font=('aria', 30, 'bold'), text="Calculator", fg="white", bd=10, anchor='w')
label.grid(row=0, column=1)
label.configure(background="black")


def final(n):
    def western(n):
        return str(("{:,}".format(n)))

    def indian(n):
        d = decimal.Decimal(str(n))
        if d.as_tuple().exponent < -2:
            s = str(n)
        else:
            s = '{0:.2f}'.format(n)
        l = len(s)
        i = l - 1;
        res = ''
        flag = 0
        k = 0
        while i >= 0:
            if flag == 0:
                res = res + s[i]
                if s[i] == '.':
                    flag = 1
            elif flag == 1:
                k = k + 1
                res = res + s[i]
                if k == 3 and i - 1 >= 0:
                    res = res + ','
                    flag = 2
                    k = 0
            else:
                k = k + 1
                res = res + s[i]
                if k == 2 and i - 1 >= 0:
                    res = res + ','
                    flag = 2
                    k = 0
            i = i - 1

        return res[::-1]

    n = float(n)
    return (str(("Indian Numeral System: "+indian(n) + "\n" + "International Numeral System: "+ western(n))))


def bc():
    # window1 Basic Calculater
    def add(v1, v2):
        # print(v1, v2)
        # global sum
        sum = final(float(v1) + float(v2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def sub(v1, v2):
        # print(v1, v2)
        # global sum
        sum = final(float(v1) - float(v2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def mul(v1, v2):
        # print(v1, v2)
        # global sum
        sum = final(float(v1) * float(v2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def div(v1, v2):
        # print(v1, v2)
        # global sum
        sum = final(float(v1) / float(v2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def p(v1, v2):
        # print(v1, v2)
        # global sum
        v2 = int(v2)
        v1 = int(v1)

        sum = final(math.pow(v1, v2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def divr(v1, v2):
        # print(v1, v2)
        # global sum
        v1 = int(v1)
        v2 = int(v2)
        # sum = "Q:" + str(  v1 - (math.remainder(v1, v2)) / v2 ) + "R:"+ str (math.remainder(v1, v2))
        sum = "Q:" + str(final((v1 // v2))) + "\n" + "R:" + str(final((v1 % v2)))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def hl(v1, v2):
        # print(v1, v2)
        # global sum
        n = v1
        nv1 = v2
        if v1 > v2:
            while (int(v1) % int(v2)) != 0:
                c = int(v1) % int(v2)
                v1 = v2
                v2 = c
            hcf = v2
        else:
            while (int(v2) % int(v1)) != 0:
                c = int(v2) % int(v1)
                v2 = v1
                v1 = c
            hcf = v1
        sum = "HCF:" + str(final((hcf))) + "\n" + "LCM:" + str(final((int(n) * int(nv1) / int(hcf))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    window1 = t.Tk()
    window1.geometry("800x300")
    window1.configure(background="black")
    window1.title("Basic Calculator")

    entry1_label = t.Label(window1, font=('aria', 16, 'bold'), text="Enter First Number", fg="white", bd=10, anchor='w',
                           background="black")
    entry1_label.grid(row=0, column=0)
    entry1 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry1.grid(row=0, column=1)
    entry2_label = t.Label(window1, font=('aria', 16, 'bold'), text="Enter Second Number", fg="white", bd=10,
                           anchor='w', background="black")
    entry2_label.grid(row=1, column=0)
    entry2 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry2.grid(row=1, column=1)

    btn1 = t.Button(window1, text="Add", width=15, command=lambda: add(entry1.get(), entry2.get()))
    btn1.grid(row=2, column=0)
    btn1 = t.Button(window1, text="Subtract", width=15, command=lambda: sub(entry1.get(), entry2.get()))
    btn1.grid(row=2, column=1)
    btn1 = t.Button(window1, text="Multiply", width=15, command=lambda: mul(entry1.get(), entry2.get()))
    btn1.grid(row=3, column=0)
    btn1 = t.Button(window1, text="Divide", width=15, command=lambda: div(entry1.get(), entry2.get()))
    btn1.grid(row=3, column=1)
    btn1 = t.Button(window1, text="Divide(Remainder)", width=15, command=lambda: divr(entry1.get(), entry2.get()))
    btn1.grid(row=4, column=0)
    btn1 = t.Button(window1, text="HCF & LCM", width=15, command=lambda: hl(entry1.get(), entry2.get()))
    btn1.grid(row=4, column=1)
    btn1 = t.Button(window1, text="Power", width=15, command=lambda: p(entry1.get(), entry2.get()))
    btn1.grid(row=5, column=0)
    label_sum = t.Label(window1, text="", font=("Courier 18 bold"))
    label_sum.grid(row=5, column=1)


def rect():
    def area(v1, v2):
        # print(v1, v2)
        # global sum
        sum = str(final(float(v1) * float(v2)))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def perimeter(v1, v2):
        # print(v1, v2)
        # global sum
        sum = str(final((float(v1) + float(v2)) * 2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def volume(v1, v2, v3):
        # print(v1, v2)
        # global sum
        sum = str(final((float(v1) * float(v2) * float(v3))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    window2 = t.Tk()
    window2.geometry("555x300")
    window2.configure(background="black")
    window2.title("Rectangle")

    entry1_label = t.Label(window2, font=('aria', 16, 'bold'), text="Length", fg="white", bd=10, anchor='w',
                           background="black")
    entry1_label.grid(row=0, column=0)
    entry1 = t.Entry(window2, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry1.grid(row=0, column=1)
    entry2_label = t.Label(window2, font=('aria', 16, 'bold'), text="Breadth", fg="white", bd=10,
                           anchor='w', background="black")
    entry2_label.grid(row=1, column=0)
    entry2 = t.Entry(window2, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry2.grid(row=1, column=1)

    entry3_label = t.Label(window2, font=('aria', 16, 'bold'), text="Height", fg="white", bd=10,
                           anchor='w', background="black")
    entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window2, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=2, column=1)

    """entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=1, column=1)"""

    btn1 = t.Button(window2, text="Area", width=15, command=lambda: area(entry1.get(), entry2.get()))
    btn1.grid(row=3, column=0)
    btn2 = t.Button(window2, text="Perimeter", width=15, command=lambda: perimeter(entry1.get(), entry2.get()))
    btn2.grid(row=3, column=1)
    btn3 = t.Button(window2, text="Volume", width=15, command=lambda: volume(entry1.get(), entry2.get(), entry3.get()))
    btn3.grid(row=4, column=0)
    label_sum = t.Label(window2, text="", font=("Courier 16 bold"))
    label_sum.grid(row=4, column=1)


def tri():
    def area(v1, v2):
        # print(v1, v2)
        # global sum
        v1 = float(v1)
        v2 = float(v2)
        sum = final(str((v1 * v2) / 2))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def perimeter(v1, v4, v5):
        # print(v1, v2)
        # global sum
        sum = final(str((float(v1) + float(v4)) + float(v5)))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def volume(v1, v2, v3):
        # print(v1, v2)
        # global sum
        sum = final(str(((float(v1) * float(v2)) / 2) * float(v3)))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    window7 = t.Tk()
    window7.geometry("550x400")
    window7.configure(background="black")
    window7.title("Rectangle")

    entry1_label = t.Label(window7, font=('aria', 16, 'bold'), text="Base", fg="white", bd=10, anchor='w',
                           background="black")
    entry1_label.grid(row=0, column=0)
    entry1 = t.Entry(window7, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry1.grid(row=0, column=1)
    entry2_label = t.Label(window7, font=('aria', 16, 'bold'), text="Height", fg="white", bd=10,
                           anchor='w', background="black")
    entry2_label.grid(row=1, column=0)
    entry2 = t.Entry(window7, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry2.grid(row=1, column=1)

    entry3_label = t.Label(window7, font=('aria', 16, 'bold'), text="Width", fg="white", bd=10,
                           anchor='w', background="black")
    entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window7, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=2, column=1)

    entry4_label = t.Label(window7, font=('aria', 16, 'bold'), text="Side 2", fg="white", bd=10,
                           anchor='w', background="black")
    entry4_label.grid(row=3, column=0)
    entry4 = t.Entry(window7, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry4.grid(row=3, column=1)

    entry5_label = t.Label(window7, font=('aria', 16, 'bold'), text="Side 3", fg="white", bd=10,
                           anchor='w', background="black")
    entry5_label.grid(row=4, column=0)
    entry5 = t.Entry(window7, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry5.grid(row=4, column=1)

    """entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=1, column=1)"""

    btn1 = t.Button(window7, text="Area", width=15, command=lambda: area(entry1.get(), entry2.get()))
    btn1.grid(row=5, column=0)
    btn2 = t.Button(window7, text="Perimeter", width=15,
                    command=lambda: perimeter(entry1.get(), entry4.get(), entry5.get()))
    btn2.grid(row=5, column=1)
    btn3 = t.Button(window7, text="Volume(Prism)", width=15,
                    command=lambda: volume(entry1.get(), entry2.get(), entry3.get()))
    btn3.grid(row=6, column=0)
    label_sum = t.Label(window7, text="", font=("Courier 16 bold"))
    label_sum.grid(row=6, column=1)


def fra():
    def area(v1):
        # print(v1, v2)
        # global sum
        sum = final(str((float(v1) * float(v1)) * (22 / 7)))

        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def perimeter(v1):
        # print(v1, v2)
        # global sum
        sum = final(str(2 * ((22 / 7) * int(v1))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def volume(v1):
        # print(v1, v2)
        # global sum
        # v1=int(v1)
        sum = final(str((4 / 3) * (22 / 7) * (int(v1) * int(v1) * int(v1))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    window3 = t.Tk()
    window3.geometry("555x300")
    window3.configure(background="black")
    window3.title("Circle")

    entry1_label = t.Label(window3, font=('aria', 16, 'bold'), text="Radius", fg="white", bd=10, anchor='w',
                           background="black")
    entry1_label.grid(row=0, column=0)
    entry1 = t.Entry(window3, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry1.grid(row=0, column=1)

    """entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=1, column=1)"""

    btn1 = t.Button(window3, text="Area", width=15, command=lambda: area(entry1.get()))

    btn1.grid(row=3, column=0)
    btn2 = t.Button(window3, text="Perimeter", width=15, command=lambda: perimeter(entry1.get()))
    btn2.grid(row=3, column=1)
    btn3 = t.Button(window3, text="Volume", width=15, command=lambda: volume(entry1.get()))
    btn3.grid(row=4, column=0)
    label_sum = t.Label(window3, text="", font=("Courier 16 bold"))
    label_sum.grid(row=4, column=1)


def cir():
    def a(v1, v2, v3, v4, v5, v6):
        # print(v1, v2)
        # global sum
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        v4 = int(v4)
        v5 = int(v5)
        v6 = int(v6)
        a = (v3 * v1) + v2

        b = v3

        c = (v6 * v4) + v5

        d = v6

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        e = d
        e = int(e)
        a = a * d

        c = c * b

        d = d * b

        b = b * e

        an = a + c

        ad = b

        an = int(an)
        ad = int(ad)

        l = math.lcm(an, ad)
        ann = an

        an = an / ((an * ad) / l)

        l = math.lcm(ad, ann)

        ad = ad / ((ad * ann) / l)
        if an > ad:
            aw = an // ad
            an = an - (aw * ad)
            # ad=ad/((an*ad)/l)

            sum = str((str(((aw))) + "  " + str(((an))) + "/" + str((ad))))
        else:
            sum = (str((str((an)) + "/" + str((ad)))))

        # sum=str(an)+"/"+str(ad)

        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)
        label_sum.configure(font=24)

    def s(v1, v2, v3, v4, v5, v6):
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        v4 = int(v4)
        v5 = int(v5)
        v6 = int(v6)
        a = (v3 * v1) + v2

        b = v3

        c = (v6 * v4) + v5

        d = v6

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        e = d
        e = int(e)
        a = a * d

        c = c * b

        d = d * b

        b = b * e

        an = a - c

        ad = b

        an = int(an)
        ad = int(ad)

        l = math.lcm(an, ad)
        ann = an

        an = an / ((an * ad) / l)

        l = math.lcm(ad, ann)

        ad = ad / ((ad * ann) / l)
        # ad=ad/((an*ad)/l)

        if an > ad:
            aw = an // ad
            an = an - (aw * ad)
            # ad=ad/((an*ad)/l)

            sum = (str((str((aw)) + "  " + str((an)) + "/" + str((ad)))))
        else:
            sum = str((str((an)) + "/" + str((ad))))
        # sum=str(an)+"/"+str(ad)

        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)
        label_sum.configure(font=24)

    def m(v1, v2, v3, v4, v5, v6):
        # print(v1, v2)
        # global sum
        # v1=int(v1)
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        v4 = int(v4)
        v5 = int(v5)
        v6 = int(v6)
        a = (v3 * v1) + v2
        b = v3
        c = (v6 * v4) + v5
        d = v6
        an = a * c
        ad = d * b
        e = d
        e = int(e)
        a = a * d

        c = c * b

        d = d * b

        b = b * e

        l = math.lcm(an, ad)
        ann = an
        an = (an / ((an * ad) / l))
        ad = (ad / ((ann * ad) / l))
        if an > ad:
            aw = an // ad
            an = an - (aw * ad)
            # ad=ad/((an*ad)/l)

            sum = str((str((aw)) + "  " + str((an)) + "/" + str((ad))))
        else:
            sum = str((str((an)) + "/" + str((ad))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)
        label_sum.configure(font=24)

    def d(v1, v2, v3, v4, v5, v6):
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        v4 = int(v4)
        v5 = int(v5)
        v6 = int(v6)
        a = (v3 * v1) + v2
        b = v3
        c = (v6 * v4) + v5
        d = v6
        c, d = d, c
        an = a * c
        ad = d * b

        l = math.lcm(an, ad)
        ann = an
        an = (an / ((an * ad) / l))
        ad = (ad / ((ann * ad) / l))
        if an > ad:
            aw = an // ad
            an = an - (aw * ad)
            # ad=ad/((an*ad)/l)

            sum = str((str((aw)) + "  " + str((an)) + "/" + str((ad))))
        else:
            sum = str((str(final(an)) + "/" + str(final(ad))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)
        label_sum.configure(font=24)

    def c(v1, v2, v3, v4, v5, v6):
        # print(v1, v2)
        # global sum
        # v1=int(v1)
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        v4 = int(v4)
        v5 = int(v5)
        v6 = int(v6)
        a = (v3 * v1) + v2
        b = v3
        c = (v6 * v4) + v5
        d = v6
        if a > c:
            sum = (str((v1)) + " " + str((v2)) + "/" + str((v3)) + " is Greater")
        else:
            sum = str((v4)) + "  " + str((v5)) + "/" + str((v6)) + "is Greater"

        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)
        label_sum.configure(font=11)

    window4 = t.Tk()
    window4.geometry("558x425")
    window4.configure(background="black")
    window4.title("Fractions")

    entry1 = t.Entry(window4, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='left', width=4)
    entry1.grid(row=2, column=0)

    entry2 = t.Entry(window4, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='left', width=4)
    entry2.grid(row=1, column=1)

    entry3 = t.Entry(window4, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='left', width=4)
    entry3.grid(row=3, column=1)

    entry4 = t.Entry(window4, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='left', width=4)
    entry4.grid(row=2, column=4)

    entry5 = t.Entry(window4, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='left', width=4)
    entry5.grid(row=1, column=5)

    entry6 = t.Entry(window4, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='left', width=4)
    entry6.grid(row=3, column=5)

    btn1 = t.Button(window4, text="Add", width=15,
                    command=lambda: a(entry1.get(), entry2.get(), entry3.get(), entry4.get()
                                      , entry5.get(), entry6.get()))
    btn1.place(x=0, y=200)
    btn2 = t.Button(window4, text="Subtract", width=15,
                    command=lambda: s(entry1.get(), entry2.get(), entry3.get(), entry4.get()
                                      , entry5.get(), entry6.get()))
    btn2.place(x=175, y=200)
    btn3 = t.Button(window4, text="Multiply", width=15,
                    command=lambda: m(entry1.get(), entry2.get(), entry3.get(), entry4.get()
                                      , entry5.get(), entry6.get()))
    btn3.place(x=0, y=240)
    btn4 = t.Button(window4, text="Divide", width=15,
                    command=lambda: d(entry1.get(), entry2.get(), entry3.get(), entry4.get()
                                      , entry5.get(), entry6.get()))
    btn4.place(x=175, y=240)
    btn5 = t.Button(window4, text="Compare", width=15,
                    command=lambda: c(entry1.get(), entry2.get(), entry3.get(), entry4.get()
                                      , entry5.get(), entry6.get()))

    btn5.place(x=0, y=280)

    label_sum = t.Label(window4, text="", font=("Courier 16 bold"))
    label_sum.grid(row=3, column=2)
    label_sum.configure(text="Result")


def cn():
    def p(v1, v2, v3):
        # print(v1, v2)
        # global sum
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        sum = (str(final(((((v3 * v1) + v2) / v3) * 100)) + "%"))

        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def d(v1, v2, v3):
        # print(v1, v2)
        # global sum
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)

        sum = str(final((((v3 * v1) + v2) / v3)))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def l(v1, v2, v3):
        # print(v1, v2)
        # global sum
        # v1=int(v1)
        v1 = int(v1)
        v2 = int(v2)
        v3 = int(v3)
        an = (v3 * v1) + v2
        ad = v3
        l = math.lcm(an, ad)
        ann = an
        an = (an / ((an * ad) / l))
        ad = (ad / ((ann * ad) / l))
        sum = str((str((an)) + "/" + str((ad))))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    window5 = t.Tk()
    window5.geometry("450x350")
    window5.configure(background="black")
    window5.title("Convert Fractions")

    entry2 = t.Entry(window5, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right', width=4)
    entry2.grid(row=0, column=3)
    entry1 = t.Entry(window5, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right', width=4)
    entry1.grid(row=1, column=2)
    entry3 = t.Entry(window5, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right', width=4)
    entry3.grid(row=2, column=3)

    """entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=1, column=1)"""

    btn1 = t.Button(window5, text="To Percentage", width=15,
                    command=lambda: p(entry1.get(), entry2.get(), entry3.get()))

    btn1.place(x=0, y=125)
    btn2 = t.Button(window5, text="To Decimal", width=15, command=lambda: d(entry1.get(), entry2.get(), entry3.get()))
    btn2.place(x=125, y=125)

    btn3 = t.Button(window5, text="Lowest Form", width=15, command=lambda: l(entry1.get(), entry2.get(), entry3.get()))
    btn3.place(x=0, y=165)

    label_sum = t.Label(window5, text="", font=("Courier 16 bold"))
    label_sum.place(x=100, y=200)


def pon():
    def sr(v1):

        v1 = int(v1)
        sum = str(final(math.sqrt(v1)))

        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def s(v1):
        # print(v1, v2)
        # global sum
        v1 = int(v1)

        sum = str(final(v1 * v1))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def q(v1):
        # print(v1, v2)
        # global sum
        v1 = int(v1)

        sum = str(final(v1 * v1 * v1))
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    def ca(v1):
        # print(v1, v2)
        # global sum
        v1 = int(v1)
        t = turtle.Turtle()
        turtle.speed(0)
        turtle.hideturtle()
        we = turtle.Screen()
        we.bgcolor("black")
        we.screensize(50, 50)
        turtle.pensize(5)
        turtle.pencolor("white")
        turtle.forward(500)
        for xxxxxxxx in range(0, v1, 1):
            turtle.goto(0, 0)
            turtle.forward(125)
            turtle.left(1)
        turtle.forward(500)
        we.exitonclick()

    def f(v1):
        # print(v1, v2)
        # global sum
        # v1=int(v1)
        v1 = int(v1)
        a = v1
        b = 1
        arav = []

        while a != b:
            if (a) % (b) == 0:
                arav.append((b))

            b += 1
        arav.append(a)
        str1 = ""
        for jain in range(0, len(arav), 1):
            str1 = str1 + (str(arav[jain])) + "\n"

        sum = str1
        label_sum.configure(fg="white")
        label_sum.configure(background="black")
        label_sum.configure(text=sum)

    window6 = t.Tk()
    window6.geometry("550x1000")
    window6.configure(background="black")
    window6.title("Properties Of Numbers")

    entry1 = t.Entry(window6, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry1.grid(row=0, column=0)

    """entry3_label.grid(row=2, column=0)
    entry3 = t.Entry(window1, font=('ariel', 16, 'bold'), textvariable="", bd=6, insertwidth=4, bg="white",
                     justify='right')
    entry3.grid(row=1, column=1)"""

    # print(v1, v2)
    # global sum

    btn1 = t.Button(window6, text="Factors", width=15,
                    command=lambda: f(entry1.get()))

    btn1.grid(row=2, column=0)
    btn2 = t.Button(window6, text="Square Root", width=15, command=lambda: sr(entry1.get()))
    btn2.grid(row=1, column=0)

    btn3 = t.Button(window6, text="Square", width=15, command=lambda: s(entry1.get()))
    btn3.grid(row=3, column=0)

    btn4 = t.Button(window6, text="Qube", width=15, command=lambda: q(entry1.get()))
    btn4.grid(row=4, column=0)

    btn5 = t.Button(window6, text="Create Angle", width=15, command=lambda: ca(entry1.get()))
    btn5.grid(row=5, column=0)

    label_sum = t.Label(window6, text="", font=("Courier 16 bold"))
    label_sum.grid(row=6, column=0)



btn1 = t.Button(window, text="Basic Calculator", width=15, command=bc, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn1.grid(row=1, column=0)
btn2 = t.Button(window, text="Rectangle", width=15, command=rect, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn2.grid(row=2, column=0)
btn3 = t.Button(window, text="Circle", width=15, command=fra, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn3.grid(row=2, column=2)
btn4 = t.Button(window, text="Fraction", width=15, command=cir, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn4.grid(row=1, column=1)
btn5 = t.Button(window, text="Convert Fraction", width=15, command=cn, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn5.grid(row=1, column=2)
btn6 = t.Button(window, text="Properties of Numbers", width=20, command=pon, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn6.place(x=175, y=200)
btn7 = t.Button(window, text="Triangle", width=15, command=tri, height=2, font=('aria', 16, 'bold'))
# btn1.place(x=180, y=50)
btn7.grid(row=2, column=1)
label_sum = t.Label(window, text="Made By Arav Jain", font=("Georgia", 30), background="black", fg="white")
label_sum.place(x=150, y=275)
window.mainloop()
