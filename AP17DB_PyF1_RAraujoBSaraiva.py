# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 02:28:52 2017

@author: Rodrigo
"""

import heapq
import datetime
import numpy as np
import matplotlib.pyplot as plt
curso="Informática de Gestão"
disciplinas=["AP","NFC","IE","MAT1","IG"]
docentes=["Helena Curto","Rui Neves","Patricia Ferreira","Vera Pedragosa","Ana Quaresma","João Vela Bastos","Paulo Enes da Silveira","Marco Costa","Arlindo Donário","Ricardo Borges"]
r=input("Escolha o que deseja observar [NFC/AP/IE/IG/MAT1/ALL]: ")
if r=="AP":
    s1=input("Conhece a nota do primeiro teste (AP) [S/N]: ")
    if s1=="S":
        t1=float(input("Nota do primeiro teste (AP): "))
        while t1>20 or t1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            t1=float(input("Nota do primeiro teste (AP): "))
    else:
        t1=" "
    while s1!="S" and s1!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s1=input("Conhece a nota do primeiro teste (AP) [S/N]: ")
        if s1=="S":
            t1=float(input("Nota do primeiro teste (AP): "))
            while t1>20 or t1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t1=float(input("Nota do primeiro teste (AP): "))
        else:
            t1=" "
    s2=input("Conhece a nota do trabalho (AP) [S/N]: ")
    if s2=="S":
        t2=float(input("Nota do trabalho (AP): "))
        while t2>20 or t2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            t2=float(input("Nota do trabalho (AP): "))
    else:
        t2=" "
    while s2!="S" and s2!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s2=input("Conhece a nota do trabalho (AP) [S/N]: ")
        if s2=="S":
            t2=float(input("Nota do trabalho (AP): "))
            while t2>20 or t2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t2=float(input("Nota do trabalho (AP): "))
        else:
            t2=" "
    s3=input("Conhece a nota do segundo teste (AP) [S/N]: ")
    if s3=="S":
        t3=float(input("Nota do segundo teste (AP): "))
        while t3>20 or t3<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            t3=float(input("Nota do segundo teste (AP): "))
    else:
        t3=" "
    while s3!="S" and s3!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s3=input("Conhece a nota do segundo teste (AP) [S/N]: ")
        if s3=="S":
            t3=float(input("Nota do segundo teste (AP): "))
            while t3>20 or t3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t3=float(input("Nota do segundo teste (AP): "))
        else:
            t3=" "
    s4=input("Conhece a nota correspondente à participação em aula (AP) [S/N]: ")
    if s4=="S":
        p=float(input("Participação (AP): "))
        while p>20 or p<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            p=float(input("Participação (AP): "))
    else:
        p=" "
    while s4!="S" and s4!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s4=input("Conhece a nota correspondente à participação em aula (AP) [S/N]: ")
        if s4=="S":
            p=float(input("Participação (AP): "))
            while p>20 or p<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                p=float(input("Participação (AP): "))
        else:
            p=" "
    d1=datetime.date(2017,11,28)
    d2=datetime.date(2018,1,5)
    d3=datetime.date(2018,1,16)
    if t1==" " or t2==" " or t3==" " or p==" ":
        AP=[["Teste1","Trabalho","Teste2","Participação","Final"],["30%","35%","30%","5%"," "],[d1,d2,d3," "," "],[t1,t2,t3,p," "]]
        print()
        for z in AP:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[0],docentes[6],docentes[7]))
        print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
    else:
        def f (t1,t2,t3,p):
            f=(t1*0.30)+(t2*0.35)+(t3*0.30)+(p*0.05)
            return f
        AP=[["Teste1","Trabalho","Teste2","Participação","Final"],["30%","35%","30%","5%"," "],[d1,d2,d3," "," "],[t1,t2,t3,p,round(f(t1,t2,t3,p),2)]]
        print()
        for z in AP:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[0],docentes[6],docentes[7]))
        x=["Teste1","Trabalho","Teste2","Participação","Final"]
        y=[t1,t2,t3,p,round(f(t1,t2,t3,p),2)]
        def plotgraph (x,y):
            plt.xlabel("Elementos de avaliação")
            plt.ylabel("Notas obtidas")  
            plt.title("Classificações obtidas em AP")
            plt.bar(x,y)
            plt.ylim(0,20)
            plt.yticks(np.arange(0,20+1,2.0))
            plt.show()
        plotgraph(x,y)
if r=="NFC":
    s1=input("Conhece a nota do primeiro teste (NFC) [S/N]: ")
    if s1=="S":
        n1=float(input("Nota do primeiro teste (NFC): "))
        while n1>20 or n1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            n1=float(input("Nota do primeiro teste (NFC): "))
    else:
        n1=" "
    while s1!="S" and s1!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s1=input("Conhece a nota do primeiro teste (NFC) [S/N]: ")
        if s1=="S":
            n1=float(input("Nota do primeiro teste (NFC): "))
            while n1>20 or n1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n1=float(input("Nota do primeiro teste (NFC): "))
        else:
            n1=" "
    s2=input("Conhece a nota do segundo teste (NFC) [S/N]: ")
    if s2=="S":
        n2=float(input("Nota do segundo teste (NFC): "))
        while n2>20 or n2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            n2=float(input("Nota do segundo teste (NFC): "))
    else:
        n2=" "
    while s2!="S" and s2!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s2=input("Conhece a nota do segundo teste (NFC) [S/N]: ")
        if s2=="S":
            n2=float(input("Nota do segundo teste (NFC): "))
            while n2>20 or n2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n2=float(input("Nota do segundo teste (NFC): "))
        else:
            n2=" "
    s3=input("Conhece a nota correspondente à participação em aula (NFC) [S/N]: ")
    if s3=="S":
        q=float(input("Participação (NFC): "))
        while q>20 or q<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            q=float(input("Participação (NFC): "))
    else:
        q=" "
    while s3!="S" and s3!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s3=input("Conhece a nota correspondente à participação em aula (NFC) [S/N]: ")
        if s3=="S":
            q=float(input("Participação (NFC): "))
            while q>20 or q<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                q=float(input("Participação (NFC): "))
        else:
            q=" "
    c1=datetime.date(2017,11,24)
    c2=datetime.date(2018,1,19)
    if n1==" " or n2==" " or q==" ":
        NFC=[["Teste1","Teste2","Participação","Final"],["40%","40%","20%"," "],[c1,c2," "," "],[n1,n2,q," "]]
        print()
        for z in NFC:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1}".format(disciplinas[1],docentes[0]))
        print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
    else:
        def i (n1,n2,q):
            i=(n1*0.40)+(n2*0.40)+(q*0.20)
            return i
        NFC=[["Teste1","Teste2","Participação","Final"],["40%","40%","20%"," "],[c1,c2," "," "],[n1,n2,q,round(i(n1,n2,q))]]
        print()
        for z in NFC:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1}".format(disciplinas[1],docentes[0]))
        x=["Teste1","Teste2","Participação","Final"]
        y=[n1,n2,q,round(i(n1,n2,q),2)]
        def plotgraph (x,y):
            plt.xlabel("Elementos de avaliação")
            plt.ylabel("Notas obtidas")  
            plt.title("Classificações obtidas em NFC")
            plt.bar(x,y)
            plt.ylim(0,20)
            plt.yticks(np.arange(0,20+1,2.0))
            plt.show()
        plotgraph(x,y)
if r=="IG":
    s1=input("Conhece a nota do trabalho (IG) [S/N]: ")
    if s1=="S":
        g1=float(input("Nota do trabalho (IG): "))
        while g1>20 or g1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            g1=float(input("Nota do trabalho (IG): "))
    else:
        g1=" "
    while s1!="S" and s1!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s1=input("Conhece a nota do trabalho (IG) [S/N]: ")
        if s1=="S":
            g1=float(input("Nota do trabalho (IG): "))
            while g1>20 or g1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g1=float(input("Nota do trabalho (IG): "))
        else:
            g1=" "
    s2=input("Conhece a nota do primeiro teste (IG) [S/N]: ")
    if s2=="S":
        g2=float(input("Nota do primeiro teste (IG): "))
        while g2>20 or g2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            g2=float(input("Nota do primeiro teste (IG): "))
    else:
        g2=" "
    while s2!="S" and s2!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s2=input("Conhece a nota do primeiro teste (IG) [S/N]: ")
        if s2=="S":
            g2=float(input("Nota do primeiro teste (IG): "))
            while g2>20 or g2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g2=float(input("Nota do primeiro teste (IG): "))
        else:
            g2=" "
    s3=input("Conhece a nota correspondente à participação em aula (IG) [S/N]: ")
    if s3=="S":
        u=float(input("Participação (IG): "))
        while u>20 or u<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            u=float(input("Participação (NFC): "))
    else:
        u=" "
    while s3!="S" and s3!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s3=input("Conhece a nota correspondente à participação em aula (IG) [S/N]: ")
        if s3=="S":
            u=float(input("Participação (IG): "))
            while u>20 or u<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                u=float(input("Participação (IG): "))
        else:
            u=" "
    b1=datetime.date(2017,12,10)
    b2=datetime.date(2018,1,13)
    if g1==" " or g2==" " or u==" ":
        IG=[["Trabalho","Teste1","Participação","Final"],["60%","30%","10%"," "],[b1,b2," "," "],[g1,g2,u," "]]
        print()
        for z in IG:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[4],docentes[3],docentes[4]))
        print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
    else:
        def j (g1,g2,u):
            j=(g1*0.30)+(g2*0.60)+(u*0.10)
            return j
        IG=[["Trabalho","Teste1","Participação","Final"],["60%","30%","10%"," "],[b1,b2," "," "],[g1,g2,u,round(j(g1,g2,u))]]
        print()
        for z in IG:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[4],docentes[3],docentes[4]))
        x=["Trabalho","Teste1","Participação","Final"]
        y=[g1,g2,u,round(j(g1,g2,u),2)]
        def plotgraph (x,y):
            plt.xlabel("Elementos de avaliação")
            plt.ylabel("Notas obtidas")  
            plt.title("Classificações obtidas em IG")
            plt.bar(x,y)
            plt.ylim(0,20)
            plt.yticks(np.arange(0,20+1,2.0))
            plt.show()
        plotgraph(x,y)
if r=="IE":
    s1=input("Conhece a nota do primeiro teste (IE) [S/N]: ")
    if s1=="S":
        e1=float(input("Nota do primeiro teste (IE): "))
        while e1>20 or e1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            e1=float(input("Nota do primeiro teste (IE): "))
    else:
        e1=" "
    while s1!="S" and s1!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s1=input("Conhece a nota do primeiro teste (IE) [S/N]: ")
        if s1=="S":
            e1=float(input("Nota do primeiro teste (IE): "))
            while e1>20 or e1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e1=float(input("Nota do primeiro teste (IE): "))
        else:
            e1=" "
    s2=input("Conhece a nota do segundo teste (IE) [S/N]: ")
    if s2=="S":
        e2=float(input("Nota do segundo teste (IE): "))
        while e2>20 or e2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            e2=float(input("Nota do segundo teste (IE): "))
    else:
        e2=" "
    while s2!="S" and s2!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s2=input("Conhece a nota do segundo teste (IE) [S/N]: ")
        if s2=="S":
            e2=float(input("Nota do segundo teste (IE): "))
            while e2>20 or e2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e2=float(input("Nota do segundo teste (IE): "))
        else:
            e2=" "
    s3=input("Conhece a nota do terceiro teste (IE) [S/N]: ")
    if s3=="S":
        e3=float(input("Nota do terceiro teste (IE): "))
        while e3>20 or e3<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            e3=float(input("Nota do terceiro teste (IE): "))
    else:
        e3=" "
    while s3!="S" and s3!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s3=input("Conhece a nota do terceiro teste (IE) [S/N]: ")
        if s3=="S":
            e3=float(input("Nota do terceiro teste (IE): "))
            while e3>20 or e3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e3=float(input("Nota do terceiro teste (IE): "))
        else:
            e3=" "
    s4=input("Conhece a nota correspondente à participação em aula (IE) [S/N]: ")
    if s4=="S":
        h=float(input("Participação (IE): "))
        while h>20 or h<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            h=float(input("Participação (IE): "))
    else:
        h=" "
    while s4!="S" and s4!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s4=input("Conhece a nota correspondente à participação em aula (IE) [S/N]: ")
        if s4=="S":
            h=float(input("Participação (IE): "))
            while h>20 or h<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                h=float(input("Participação (IE): "))
        else:
            h=" "
    w1=datetime.date(2017,11,9)
    w2=datetime.date(2017,12,7)
    w3=datetime.date(2018,1,25)
    if e1==" " or e2==" " or e3==" " or h==" ":
        IE=[["Teste1","Teste2","Teste3","Participação","Final"],["18%","30%","35%","17%"," "],[w1,w2,w3," "," "],[e1,e2,e3,h," "]]
        print()
        for z in IE:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[2],docentes[8],docentes[9]))
        print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
    else:
        def k (e1,e2,e3,h):
            k=(e1*0.18)+(e2*0.30)+(e3*0.35)+(h*0.17)
            return k
        IE=[["Teste1","Teste2","Teste3","Participação","Final"],["18%","30%","35%","17%"," "],[w1,w2,w3," "," "],[e1,e2,e3,h,round(k(e1,e2,e3,h))]]
        print()
        for z in IE:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[2],docentes[8],docentes[9]))
        x=["Teste1","Teste2","Teste3","Participação","Final"]
        y=[e1,e2,e3,h,round(k(e1,e2,e3,h),2)]
        def plotgraph (x,y):
            plt.xlabel("Elementos de avaliação")
            plt.ylabel("Notas obtidas")  
            plt.title("Classificações obtidas em IE")
            plt.bar(x,y)
            plt.ylim(0,20)
            plt.yticks(np.arange(0,20+1,2.0))
            plt.show()
        plotgraph(x,y)
if r=="MAT1":
    s1=input("Conhece a nota do primeiro mini-teste (MAT1) [S/N]: ")
    if s1=="S":
        m1=float(input("Nota do primeiro mini-teste (MAT1): "))
        while m1>20 or m1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            m1=float(input("Nota do primeiro mini-teste (MAT1): "))
    else:
        m1=" "
    while s1!="S" and s1!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s1=input("Conhece a nota do primeiro mini-teste (MAT1) [S/N]: ")
        if s1=="S":
            m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            while m1>20 or m1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m1=float(input("Nota do primeiro mini-teste (MAT1): "))
        else:
            m1=" "
    s2=input("Conhece a nota do segundo mini-teste (MAT1) [S/N]: ")
    if s2=="S":
        m2=float(input("Nota do segundo mini-teste (MAT1): "))
        while m2>20 or m2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            m2=float(input("Nota do segundo mini-teste (MAT1): "))
    else:
        m2=" "
    while s2!="S" and s2!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s2=input("Conhece a nota do segundo mini-teste (MAT1) [S/N]: ")
        if s2=="S":
            m2=float(input("Nota do segundo mini-teste (MAT1): "))
            while m2>20 or m2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m2=float(input("Nota do segundo mini-teste (MAT1): "))
        else:
            m2=" "
    s3=input("Conhece a nota do terceiro mini-teste (MAT1) [S/N]: ")
    if s3=="S":
        m3=float(input("Nota do terceiro mini-teste (MAT1): "))
        while m3>20 or m3<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            m3=float(input("Nota do terceiro mini-teste (MAT1): "))
    else:
        m3=" "
    while s3!="S" and s3!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s3=input("Conhece a nota do terceiro mini-teste (MAT1) [S/N]: ")
        if s3=="S":
            m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            while m3>20 or m3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m3=float(input("Nota do terceiro mini-teste (MAT1): "))
        else:
            m3=" "
    s4=input("Conhece a nota do teste intermédio (MAT1) [S/N]: ")
    if s4=="S":
        TI=float(input("Nota do teste intermédio (MAT1): "))
        while TI>20 or TI<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            TI=float(input("Nota do teste intermédio (MAT1): "))
    else:
        TI=" "
    while s4!="S" and s4!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s4=input("Conhece a nota do teste intermédio (MAT1) [S/N]: ")
        if s4=="S":
            TI=float(input("Nota do teste intermédio (MAT1): "))
            while TI>20 or TI<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TI=float(input("Nota do teste intermédio (MAT1): "))
        else:
            TI=" "
    s5=input("Conhece a nota do teste final (MAT1) [S/N]: ")
    if s5=="S":
        TF=float(input("Nota do teste final (MAT1): "))
        while TF>20 or TF<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            TF=float(input("Nota do teste final (MAT1): "))
    else:
        TF=" "
    while s5!="S" and s5!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s5=input("Conhece a nota do teste final (MAT1) [S/N]: ")
        if s5=="S":
            TF=float(input("Nota do teste final (MAT1): "))
            while TF>20 or TF<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TF=float(input("Nota do teste final (MAT1): "))
        else:
            TF=" "
    s6=input("Conhece a nota correspondente à participação em aula (MAT1) [S/N]: ")
    if s6=="S":
        v=float(input("Participação (MAT1): "))
        while v>20 or v<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            v=float(input("Participação (MAT1): "))
    else:
        v=" "
    while s6!="S" and s6!="N":
        print("\nPor favor responda sim(S) ou não(N)")
        s6=input("Conhece a nota correspondente à participação em aula (MAT1) [S/N]: ")
        if s6=="S":
            v=float(input("Participação (MAT1): "))
            while v>20 or v<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                v=float(input("Participação (MAT1): "))
        else:
            v=" "
    l1=datetime.date(2017,11,29)
    l2=datetime.date(2017,1,17)
    if m1==" " or m2==" " or m3==" " or v==" " or TI==" " or TF==" ":
        MAT1=[["Média mini","TI","TF","Participação","Final"],["15%","40%","40%","5%"," "],["Datas mini",l1,l2," "," "],[" ",TI,TF,v," "]]
        print()
        for z in MAT1:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1}, {2} e {3}".format(disciplinas[3],docentes[1],docentes[2],docentes[5]))
        print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
    else:
        tm=[m1,m2,m3]
        TM=heapq.nlargest(2,tm)
        MT=(TM[0]+TM[1])/2
        def a (MT,TI,TF,v):
            a=(MT*0.15)+(TI*0.40)+(TF*0.40)+(v*0.05)
            return a
        MAT1=[["Média mini","TI","TF","Participação","Final"],["15%","40%","40%","5%"," "],["Datas mini",l1,l2," "," "],[MT,TI,TF,v,round(a(MT,TI,TF,v))]]
        print()
        for z in MAT1:
            print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
        print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2} e {3}".format(disciplinas[3],docentes[1],docentes[2],docentes[5]))
        x=["m1","m2","m3","MT","TI","TF","Partipação","Final"]
        y=[m1,m2,m3,MT,TI,TF,v,round(k(MT,TI,TF,v),2)]
        def plotgraph (x,y):
            plt.xlabel("Elementos de avaliação")
            plt.ylabel("Notas obtidas")  
            plt.title("Classificações obtidas em MAT1")
            plt.bar(x,y)
            plt.ylim(0,20)
            plt.yticks(np.arange(0,20+1,2.0))
            plt.show()
        plotgraph(x,y)
if r=="ALL":
    s1=input("ATENÇÃO use apenas quando conhecer todas as notas de todas as disciplinas, deseja continuar [S/N]: ")
    if s1=="S":
        t1=float(input("Nota do primeiro teste (AP): "))
        while t1>20 or t1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            t1=float(input("Nota do primeiro teste (AP): "))
        t2=float(input("Nota do trabalho (AP): "))
        while t2>20 or t2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            t2=float(input("Nota do trabalho (AP): "))
        t3=float(input("Nota do segundo teste (AP): "))
        while t3>20 or t3<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            t3=float(input("Nota do segundo teste (AP): "))
        p=float(input("Participação (AP): "))
        while p>20 or p<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            p=float(input("Participação (AP): "))
        def f (t1,t2,t3,p):
            f=(t1*0.30)+(t2*0.35)+(t3*0.30)+(p*0.05)
            return f
        n1=float(input("Nota do primeiro teste (NFC): "))
        while n1>20 or n1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            n1=float(input("Nota do primeiro teste (NFC): "))
        n2=float(input("Nota do segundo teste (NFC): "))
        while n2>20 or n2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            n2=float(input("Nota do segundo teste (NFC): "))
        q=float(input("Participação (NFC): "))
        while q>20 or q<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            q=float(input("Participação (NFC): "))
        def i (n1,n2,q):
            i=(n1*0.40)+(n2*0.40)+(q*0.20)
            return i
        g1=float(input("Nota do trabalho (IG): "))
        while g1>20 or g1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            g1=float(input("Nota do trabalho (IG): "))
        g2=float(input("Nota do primeiro teste (IG): "))
        while g2>20 or g2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            g2=float(input("Nota do primeiro teste (IG): "))
        u=float(input("Participação (IG): "))
        while u>20 or u<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            u=float(input("Participação (NFC): "))
        def j (g1,g2,u):
            j=(g1*0.30)+(g2*0.60)+(u*0.10)
            return j
        e1=float(input("Nota do primeiro teste (IE): "))
        while e1>20 or e1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            e1=float(input("Nota do primeiro teste (IE): "))
        e2=float(input("Nota do segundo teste (IE): "))
        while e2>20 or e2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            e2=float(input("Nota do segundo teste (IE): "))
        e3=float(input("Nota do terceiro teste (IE): "))
        while e3>20 or e3<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            e3=float(input("Nota do terceiro teste (IE): "))
        h=float(input("Participação (IE): "))
        while h>20 or h<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            h=float(input("Participação (IE): "))
        def k (e1,e2,e3,h):
            k=(e1*0.18)+(e2*0.30)+(e3*0.35)+(h*0.17)
            return k
        m1=float(input("Nota do primeiro mini-teste (MAT1): "))
        while m1>20 or m1<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            m1=float(input("Nota do primeiro mini-teste (MAT1): "))
        m2=float(input("Nota do segundo mini-teste (MAT1): "))
        while m2>20 or m2<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            m2=float(input("Nota do segundo mini-teste (MAT1): "))
        m3=float(input("Nota do terceiro mini-teste (MAT1): "))
        while m3>20 or m3<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            m3=float(input("Nota do terceiro mini-teste (MAT1): "))
        TI=float(input("Nota do teste intermédio (MAT1): "))
        while TI>20 or TI<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            TI=float(input("Nota do teste intermédio (MAT1): "))
        TF=float(input("Nota do teste final (MAT1): "))
        while TF>20 or TF<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            TF=float(input("Nota do teste final (MAT1): "))
        v=float(input("Participação (MAT1): "))
        while v>20 or v<0:
            print("\nPor favor introduza valores compreendidos entre 0 e 20")
            v=float(input("Participação (MAT1): "))
        tm=[m1,m2,m3]
        TM=heapq.nlargest(2,tm)
        MT=(TM[0]+TM[1])/2
        def a (MT,TI,TF,v):
            a=(MT*0.15)+(TI*0.40)+(TF*0.40)+(v*0.05)
            return a
        x=[round(i(n1,n2,q),2),round(k(e1,e2,e3,h),2),round(a(MT,TI,TF,v),2),round(f(t1,t2,t3,p),2),round(j(g1,g2,u),2)]
        y=["NFC","IE","MAT1","AP","IG"]
        def plotgraph (y,x):
            plt.xlabel("Notas finais")
            plt.ylabel("Disciplinas")  
            plt.title("Classificações finais de todas as disciplinas")
            plt.barh(y,x)
            plt.xlim(0,20)
            plt.xticks(np.arange(0,20+1,2.0))
            plt.show()
        plotgraph(y,x)
    else:
        print()
    while s1!="S" and s1!="N":
        print("Por favor responda sim(S) ou não(N)")
        s1=input("ATENÇÃO use apenas quando conhecer todas as notas de todas as disciplinas, deseja continuar [S/N]: ")
        if s1=="S":
            t1=float(input("Nota do primeiro teste (AP): "))
            while t1>20 or t1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t1=float(input("Nota do primeiro teste (AP): "))
            t2=float(input("Nota do trabalho (AP): "))
            while t2>20 or t2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t2=float(input("Nota do trabalho (AP): "))
            t3=float(input("Nota do segundo teste (AP): "))
            while t3>20 or t3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t3=float(input("Nota do segundo teste (AP): "))
            p=float(input("Participação (AP): "))
            while p>20 or p<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                p=float(input("Participação (AP): "))
            def f (t1,t2,t3,p):
                f=(t1*0.30)+(t2*0.35)+(t3*0.30)+(p*0.05)
                return f
            n1=float(input("Nota do primeiro teste (NFC): "))
            while n1>20 or n1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n1=float(input("Nota do primeiro teste (NFC): "))
            n2=float(input("Nota do segundo teste (NFC): "))
            while n2>20 or n2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n2=float(input("Nota do segundo teste (NFC): "))
            q=float(input("Participação (NFC): "))
            while q>20 or q<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                q=float(input("Participação (NFC): "))
            def i (n1,n2,q):
                i=(n1*0.40)+(n2*0.40)+(q*0.20)
                return i
            g1=float(input("Nota do trabalho (IG): "))
            while g1>20 or g1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g1=float(input("Nota do trabalho (IG): "))
            g2=float(input("Nota do primeiro teste (IG): "))
            while g2>20 or g2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g2=float(input("Nota do primeiro teste (IG): "))
            u=float(input("Participação (IG): "))
            while u>20 or u<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                u=float(input("Participação (NFC): "))
            def j (g1,g2,u):
                j=(g1*0.30)+(g2*0.60)+(u*0.10)
                return j
            e1=float(input("Nota do primeiro teste (IE): "))
            while e1>20 or e1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e1=float(input("Nota do primeiro teste (IE): "))
            e2=float(input("Nota do segundo teste (IE): "))
            while e2>20 or e2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e2=float(input("Nota do segundo teste (IE): "))
            e3=float(input("Nota do terceiro teste (IE): "))
            while e3>20 or e3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e3=float(input("Nota do terceiro teste (IE): "))
            h=float(input("Participação (IE): "))
            while h>20 or h<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                h=float(input("Participação (IE): "))
            def k (e1,e2,e3,h):
                k=(e1*0.18)+(e2*0.30)+(e3*0.35)+(h*0.17)
                return k
            m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            while m1>20 or m1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            m2=float(input("Nota do segundo mini-teste (MAT1): "))
            while m2>20 or m2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m2=float(input("Nota do segundo mini-teste (MAT1): "))
            m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            while m3>20 or m3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            TI=float(input("Nota do teste intermédio (MAT1): "))
            while TI>20 or TI<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TI=float(input("Nota do teste intermédio (MAT1): "))
            TF=float(input("Nota do teste final (MAT1): "))
            while TF>20 or TF<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TF=float(input("Nota do teste final (MAT1): "))
            v=float(input("Participação (MAT1): "))
            while v>20 or v<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                v=float(input("Participação (MAT1): "))
            tm=[m1,m2,m3]
            TM=heapq.nlargest(2,tm)
            MT=(TM[0]+TM[1])/2
            def a (MT,TI,TF,v):
                a=(MT*0.15)+(TI*0.40)+(TF*0.40)+(v*0.05)
                return a
            x=[round(i(n1,n2,q),2),round(k(e1,e2,e3,h),2),round(a(MT,TI,TF,v),2),round(f(t1,t2,t3,p),2),round(j(g1,g2,u),2)]
            y=["NFC","IE","MAT1","AP","IG"]
            def plotgraph (y,x):
                plt.xlabel("Notas finais")
                plt.ylabel("Disciplinas")  
                plt.title("Classificações finais de todas as disciplinas")
                plt.barh(y,x)
                plt.xlim(0,20)
                plt.xticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(y,x)
        else:
            print()
while r!="NFC" and r!="MAT1" and r!="AP" and r!="IE" and r!="IG" and r!="ALL":
    print("\nPor favor escolha uma das disciplinas referidas ou a opção ALL")
    r=input("Escolha o que deseja observar [NFC/AP/IE/IG/MAT1/ALL]: ")
    if r=="AP":
        s1=input("Conhece a nota do primeiro teste (AP) [S/N]: ")
        if s1=="S":
            t1=float(input("Nota do primeiro teste (AP): "))
            while t1>20 or t1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t1=float(input("Nota do primeiro teste (AP): "))
        else:
            t1=" "
        while s1!="S" and s1!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s1=input("Conhece a nota do primeiro teste (AP) [S/N]: ")
            if s1=="S":
                t1=float(input("Nota do primeiro teste (AP): "))
                while t1>20 or t1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    t1=float(input("Nota do primeiro teste (AP): "))
            else:
                t1=" "
        s2=input("Conhece a nota do trabalho (AP) [S/N]: ")
        if s2=="S":
            t2=float(input("Nota do trabalho (AP): "))
            while t2>20 or t2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t2=float(input("Nota do trabalho (AP): "))
        else:
            t2=" "
        while s2!="S" and s2!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s2=input("Conhece a nota do trabalho (AP) [S/N]: ")
            if s2=="S":
                t2=float(input("Nota do trabalho (AP): "))
                while t2>20 or t2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    t2=float(input("Nota do trabalho (AP): "))
            else:
                t2=" "
        s3=input("Conhece a nota do segundo teste (AP) [S/N]: ")
        if s3=="S":
            t3=float(input("Nota do segundo teste (AP): "))
            while t3>20 or t3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t3=float(input("Nota do segundo teste (AP): "))
        else:
            t3=" "
        while s3!="S" and s3!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s3=input("Conhece a nota do segundo teste (AP) [S/N]: ")
            if s3=="S":
                t3=float(input("Nota do segundo teste (AP): "))
                while t3>20 or t3<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    t3=float(input("Nota do segundo teste (AP): "))
            else:
                t3=" "
        s4=input("Conhece a nota correspondente à participação em aula (AP) [S/N]: ")
        if s4=="S":
            p=float(input("Participação (AP): "))
            while p>20 or p<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                p=float(input("Participação (AP): "))
        else:
            p=" "
        while s4!="S" and s4!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s4=input("Conhece a nota correspondente à participação em aula (AP) [S/N]: ")
            if s4=="S":
                p=float(input("Participação (AP): "))
                while p>20 or p<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    p=float(input("Participação (AP): "))
            else:
                p=" "
        d1=datetime.date(2017,11,28)
        d2=datetime.date(2018,1,5)
        d3=datetime.date(2018,1,16)
        if t1==" " or t2==" " or t3==" " or p==" ":
            AP=[["Teste1","Trabalho","Teste2","Participação","Final"],["30%","35%","30%","5%"," "],[d1,d2,d3," "," "],[t1,t2,t3,p," "]]
            print()
            for z in AP:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[0],docentes[6],docentes[7]))
            print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
        else:
            def f (t1,t2,t3,p):
                f=(t1*0.30)+(t2*0.35)+(t3*0.30)+(p*0.05)
                return f
            AP=[["Teste1","Trabalho","Teste2","Participação","Final"],["30%","35%","30%","5%"," "],[d1,d2,d3," "," "],[t1,t2,t3,p,round(f(t1,t2,t3,p),2)]]
            print()
            for z in AP:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[0],docentes[6],docentes[7]))
            x=["Teste1","Trabalho","Teste2","Participação","Final"]
            y=[t1,t2,t3,p,round(f(t1,t2,t3,p),2)]
            def plotgraph (x,y):
                plt.xlabel("Elementos de avaliação")
                plt.ylabel("Notas obtidas")  
                plt.title("Classificações obtidas em AP")
                plt.bar(x,y)
                plt.ylim(0,20)
                plt.yticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(x,y)
    if r=="NFC":
        s1=input("Conhece a nota do primeiro teste (NFC) [S/N]: ")
        if s1=="S":
            n1=float(input("Nota do primeiro teste (NFC): "))
            while n1>20 or n1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n1=float(input("Nota do primeiro teste (NFC): "))
        else:
            n1=" "
        while s1!="S" and s1!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s1=input("Conhece a nota do primeiro teste (NFC) [S/N]: ")
            if s1=="S":
                n1=float(input("Nota do primeiro teste (NFC): "))
                while n1>20 or n1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    n1=float(input("Nota do primeiro teste (NFC): "))
            else:
                n1=" "
        s2=input("Conhece a nota do segundo teste (NFC) [S/N]: ")
        if s2=="S":
            n2=float(input("Nota do segundo teste (NFC): "))
            while n2>20 or n2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n2=float(input("Nota do segundo teste (NFC): "))
        else:
            n2=" "
        while s2!="S" and s2!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s2=input("Conhece a nota do segundo teste (NFC) [S/N]: ")
            if s2=="S":
                n2=float(input("Nota do segundo teste (NFC): "))
                while n2>20 or n2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    n2=float(input("Nota do segundo teste (NFC): "))
            else:
                n2=" "
        s3=input("Conhece a nota correspondente à participação em aula (NFC) [S/N]: ")
        if s3=="S":
            q=float(input("Participação (NFC): "))
            while q>20 or q<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                q=float(input("Participação (NFC): "))
        else:
            q=" "
        while s3!="S" and s3!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s3=input("Conhece a nota correspondente à participação em aula (NFC) [S/N]: ")
            if s3=="S":
                q=float(input("Participação (NFC): "))
                while q>20 or q<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    q=float(input("Participação (NFC): "))
            else:
                q=" "
        c1=datetime.date(2017,11,24)
        c2=datetime.date(2018,1,19)
        if n1==" " or n2==" " or q==" ":
            NFC=[["Teste1","Teste2","Participação","Final"],["40%","40%","20%"," "],[c1,c2," "," "],[n1,n2,q," "]]
            print()
            for z in NFC:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1}".format(disciplinas[1],docentes[0]))
            print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
        else:
            def i (n1,n2,q):
                i=(n1*0.40)+(n2*0.40)+(q*0.20)
                return i
            NFC=[["Teste1","Teste2","Participação","Final"],["40%","40%","20%"," "],[c1,c2," "," "],[n1,n2,q,round(i(n1,n2,q))]]
            print()
            for z in NFC:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1}".format(disciplinas[1],docentes[0]))
            x=["Teste1","Teste2","Participação","Final"]
            y=[n1,n2,q,round(i(n1,n2,q),2)]
            def plotgraph (x,y):
                plt.xlabel("Elementos de avaliação")
                plt.ylabel("Notas obtidas")  
                plt.title("Classificações obtidas em NFC")
                plt.bar(x,y)
                plt.ylim(0,20)
                plt.yticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(x,y)
    if r=="IG":
        s1=input("Conhece a nota do trabalho (IG) [S/N]: ")
        if s1=="S":
            g1=float(input("Nota do trabalho (IG): "))
            while g1>20 or g1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g1=float(input("Nota do trabalho (IG): "))
        else:
            g1=" "
        while s1!="S" and s1!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s1=input("Conhece a nota do trabalho (IG) [S/N]: ")
            if s1=="S":
                g1=float(input("Nota do trabalho (IG): "))
                while g1>20 or g1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    g1=float(input("Nota do trabalho (IG): "))
            else:
                g1=" "
        s2=input("Conhece a nota do primeiro teste (IG) [S/N]: ")
        if s2=="S":
            g2=float(input("Nota do primeiro teste (IG): "))
            while g2>20 or g2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g2=float(input("Nota do primeiro teste (IG): "))
        else:
            g2=" "
        while s2!="S" and s2!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s2=input("Conhece a nota do primeiro teste (IG) [S/N]: ")
            if s2=="S":
                g2=float(input("Nota do primeiro teste (IG): "))
                while g2>20 or g2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    g2=float(input("Nota do primeiro teste (IG): "))
            else:
                g2=" "
        s3=input("Conhece a nota correspondente à participação em aula (IG) [S/N]: ")
        if s3=="S":
            u=float(input("Participação (IG): "))
            while u>20 or u<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                u=float(input("Participação (NFC): "))
        else:
            u=" "
        while s3!="S" and s3!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s3=input("Conhece a nota correspondente à participação em aula (IG) [S/N]: ")
            if s3=="S":
                u=float(input("Participação (IG): "))
                while u>20 or u<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    u=float(input("Participação (IG): "))
            else:
                u=" "
        b1=datetime.date(2017,12,10)
        b2=datetime.date(2018,1,13)
        if g1==" " or g2==" " or u==" ":
            IG=[["Trabalho","Teste1","Participação","Final"],["60%","30%","10%"," "],[b1,b2," "," "],[g1,g2,u," "]]
            print()
            for z in IG:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[4],docentes[3],docentes[4]))
            print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
        else:
            def j (g1,g2,u):
                j=(g1*0.30)+(g2*0.60)+(u*0.10)
                return j
            IG=[["Trabalho","Teste1","Participação","Final"],["60%","30%","10%"," "],[b1,b2," "," "],[g1,g2,u,round(j(g1,g2,u))]]
            print()
            for z in IG:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(12-len(str(z[2]))),"|",z[3]," "*(5-len(str(z[3]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[4],docentes[3],docentes[4]))
            x=["Trabalho","Teste1","Participação","Final"]
            y=[g1,g2,u,round(j(g1,g2,u),2)]
            def plotgraph (x,y):
                plt.xlabel("Elementos de avaliação")
                plt.ylabel("Notas obtidas")  
                plt.title("Classificações obtidas em IG")
                plt.bar(x,y)
                plt.ylim(0,20)
                plt.yticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(x,y)
    if r=="IE":
        s1=input("Conhece a nota do primeiro teste (IE) [S/N]: ")
        if s1=="S":
            e1=float(input("Nota do primeiro teste (IE): "))
            while e1>20 or e1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e1=float(input("Nota do primeiro teste (IE): "))
        else:
            e1=" "
        while s1!="S" and s1!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s1=input("Conhece a nota do primeiro teste (IE) [S/N]: ")
            if s1=="S":
                e1=float(input("Nota do primeiro teste (IE): "))
                while e1>20 or e1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    e1=float(input("Nota do primeiro teste (IE): "))
            else:
                e1=" "
        s2=input("Conhece a nota do segundo teste (IE) [S/N]: ")
        if s2=="S":
            e2=float(input("Nota do segundo teste (IE): "))
            while e2>20 or e2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e2=float(input("Nota do segundo teste (IE): "))
        else:
            e2=" "
        while s2!="S" and s2!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s2=input("Conhece a nota do segundo teste (IE) [S/N]: ")
            if s2=="S":
                e2=float(input("Nota do segundo teste (IE): "))
                while e2>20 or e2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    e2=float(input("Nota do segundo teste (IE): "))
            else:
                e2=" "
        s3=input("Conhece a nota do terceiro teste (IE) [S/N]: ")
        if s3=="S":
            e3=float(input("Nota do terceiro teste (IE): "))
            while e3>20 or e3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e3=float(input("Nota do terceiro teste (IE): "))
        else:
            e3=" "
        while s3!="S" and s3!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s3=input("Conhece a nota do terceiro teste (IE) [S/N]: ")
            if s3=="S":
                e3=float(input("Nota do terceiro teste (IE): "))
                while e3>20 or e3<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    e3=float(input("Nota do terceiro teste (IE): "))
            else:
                e3=" "
        s4=input("Conhece a nota correspondente à participação em aula (IE) [S/N]: ")
        if s4=="S":
            h=float(input("Participação (IE): "))
            while h>20 or h<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                h=float(input("Participação (IE): "))
        else:
            h=" "
        while s4!="S" and s4!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s4=input("Conhece a nota correspondente à participação em aula (IE) [S/N]: ")
            if s4=="S":
                h=float(input("Participação (IE): "))
                while h>20 or h<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    h=float(input("Participação (IE): "))
            else:
                h=" "
        w1=datetime.date(2017,11,9)
        w2=datetime.date(2017,12,7)
        w3=datetime.date(2018,1,25)
        if e1==" " or e2==" " or e3==" " or h==" ":
            IE=[["Teste1","Teste2","Teste3","Participação","Final"],["18%","30%","35%","17%"," "],[w1,w2,w3," "," "],[e1,e2,e3,h," "]]
            print()
            for z in IE:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[2],docentes[8],docentes[9]))
            print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
        else:
            def k (e1,e2,e3,h):
                k=(e1*0.18)+(e2*0.30)+(e3*0.35)+(h*0.17)
                return k
            IE=[["Teste1","Teste2","Teste3","Participação","Final"],["18%","30%","35%","17%"," "],[w1,w2,w3," "," "],[e1,e2,e3,h,round(k(e1,e2,e3,h))]]
            print()
            for z in IE:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2}".format(disciplinas[2],docentes[8],docentes[9]))
            x=["Teste1","Teste2","Teste3","Participação","Final"]
            y=[e1,e2,e3,h,round(k(e1,e2,e3,h),2)]
            def plotgraph (x,y):
                plt.xlabel("Elementos de avaliação")
                plt.ylabel("Notas obtidas")  
                plt.title("Classificações obtidas em IE")
                plt.bar(x,y)
                plt.ylim(0,20)
                plt.yticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(x,y)
    if r=="MAT1":
        s1=input("Conhece a nota do primeiro mini-teste (MAT1) [S/N]: ")
        if s1=="S":
            m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            while m1>20 or m1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m1=float(input("Nota do primeiro mini-teste (MAT1): "))
        else:
            m1=" "
        while s1!="S" and s1!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s1=input("Conhece a nota do primeiro mini-teste (MAT1) [S/N]: ")
            if s1=="S":
                m1=float(input("Nota do primeiro mini-teste (MAT1): "))
                while m1>20 or m1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            else:
                m1=" "
        s2=input("Conhece a nota do segundo mini-teste (MAT1) [S/N]: ")
        if s2=="S":
            m2=float(input("Nota do segundo mini-teste (MAT1): "))
            while m2>20 or m2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m2=float(input("Nota do segundo mini-teste (MAT1): "))
        else:
            m2=" "
        while s2!="S" and s2!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s2=input("Conhece a nota do segundo mini-teste (MAT1) [S/N]: ")
            if s2=="S":
                m2=float(input("Nota do segundo mini-teste (MAT1): "))
                while m2>20 or m2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    m2=float(input("Nota do segundo mini-teste (MAT1): "))
            else:
                m2=" "
        s3=input("Conhece a nota do terceiro mini-teste (MAT1) [S/N]: ")
        if s3=="S":
            m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            while m3>20 or m3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m3=float(input("Nota do terceiro mini-teste (MAT1): "))
        else:
            m3=" "
        while s3!="S" and s3!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s3=input("Conhece a nota do terceiro mini-teste (MAT1) [S/N]: ")
            if s3=="S":
                m3=float(input("Nota do terceiro mini-teste (MAT1): "))
                while m3>20 or m3<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            else:
                m3=" "
        s4=input("Conhece a nota do teste intermédio (MAT1) [S/N]: ")
        if s4=="S":
            TI=float(input("Nota do teste intermédio (MAT1): "))
            while TI>20 or TI<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TI=float(input("Nota do teste intermédio (MAT1): "))
        else:
            TI=" "
        while s4!="S" and s4!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s4=input("Conhece a nota do teste intermédio (MAT1) [S/N]: ")
            if s4=="S":
                TI=float(input("Nota do teste intermédio (MAT1): "))
                while TI>20 or TI<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    TI=float(input("Nota do teste intermédio (MAT1): "))
            else:
                TI=" "
        s5=input("Conhece a nota do teste final (MAT1) [S/N]: ")
        if s5=="S":
            TF=float(input("Nota do teste final (MAT1): "))
            while TF>20 or TF<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TF=float(input("Nota do teste final (MAT1): "))
        else:
            TF=" "
        while s5!="S" and s5!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s5=input("Conhece a nota do teste final (MAT1) [S/N]: ")
            if s5=="S":
                TF=float(input("Nota do teste final (MAT1): "))
                while TF>20 or TF<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    TF=float(input("Nota do teste final (MAT1): "))
            else:
                TF=" "
        s6=input("Conhece a nota correspondente à participação em aula (MAT1) [S/N]: ")
        if s6=="S":
            v=float(input("Participação (MAT1): "))
            while v>20 or v<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                v=float(input("Participação (MAT1): "))
        else:
            v=" "
        while s6!="S" and s6!="N":
            print("\nPor favor responda sim(S) ou não(N)")
            s6=input("Conhece a nota correspondente à participação em aula (MAT1) [S/N]: ")
            if s6=="S":
                v=float(input("Participação (MAT1): "))
                while v>20 or v<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    v=float(input("Participação (MAT1): "))
            else:
                v=" "
        l1=datetime.date(2017,11,29)
        l2=datetime.date(2017,1,17)
        if m1==" " or m2==" " or m3==" " or v==" " or TI==" " or TF==" ":
            MAT1=[["Média mini","TI","TF","Participação","Final"],["15%","40%","40%","5%"," "],["Datas mini",l1,l2," "," "],[" ",TI,TF,v," "]]
            print()
            for z in MAT1:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1}, {2} e {3}".format(disciplinas[3],docentes[1],docentes[2],docentes[5]))
            print("\nNOTA: Dados insuficientes para ilustrar o gráfico")
        else:
            tm=[m1,m2,m3]
            TM=heapq.nlargest(2,tm)
            MT=(TM[0]+TM[1])/2
            def a (MT,TI,TF,v):
                a=(MT*0.15)+(TI*0.40)+(TF*0.40)+(v*0.05)
                return a
            MAT1=[["Média mini","TI","TF","Participação","Final"],["15%","40%","40%","5%"," "],["Datas mini",l1,l2," "," "],[MT,TI,TF,v,round(a(MT,TI,TF,v))]]
            print()
            for z in MAT1:
                print("|",z[0]," "*(10-len(str(z[0]))),"|",z[1]," "*(10-len(str(z[1]))),"|",z[2]," "*(10-len(str(z[2]))),"|",z[3]," "*(12-len(str(z[3]))),"|",z[4]," "*(5-len(str(z[4]))),"|")
            print("\nCorpo docente do curso de",curso,"referente à disciplina de {0}: {1} e {2} e {3}".format(disciplinas[3],docentes[1],docentes[2],docentes[5]))
            x=["m1","m2","m3","MT","TI","TF","Partipação","Final"]
            y=[m1,m2,m3,MT,TI,TF,v,round(k(MT,TI,TF,v),2)]
            def plotgraph (x,y):
                plt.xlabel("Elementos de avaliação")
                plt.ylabel("Notas obtidas")  
                plt.title("Classificações obtidas em MAT1")
                plt.bar(x,y)
                plt.ylim(0,20)
                plt.yticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(x,y)
    if r=="ALL":
        s1=input("ATENÇÃO use apenas quando conhecer todas as notas de todas as disciplinas, deseja continuar [S/N]: ")
        if s1=="S":
            t1=float(input("Nota do primeiro teste (AP): "))
            while t1>20 or t1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t1=float(input("Nota do primeiro teste (AP): "))
            t2=float(input("Nota do trabalho (AP): "))
            while t2>20 or t2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t2=float(input("Nota do trabalho (AP): "))
            t3=float(input("Nota do segundo teste (AP): "))
            while t3>20 or t3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                t3=float(input("Nota do segundo teste (AP): "))
            p=float(input("Participação (AP): "))
            while p>20 or p<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                p=float(input("Participação (AP): "))
            def f (t1,t2,t3,p):
                f=(t1*0.30)+(t2*0.35)+(t3*0.30)+(p*0.05)
                return f
            n1=float(input("Nota do primeiro teste (NFC): "))
            while n1>20 or n1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n1=float(input("Nota do primeiro teste (NFC): "))
            n2=float(input("Nota do segundo teste (NFC): "))
            while n2>20 or n2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                n2=float(input("Nota do segundo teste (NFC): "))
            q=float(input("Participação (NFC): "))
            while q>20 or q<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                q=float(input("Participação (NFC): "))
            def i (n1,n2,q):
                i=(n1*0.40)+(n2*0.40)+(q*0.20)
                return i
            g1=float(input("Nota do trabalho (IG): "))
            while g1>20 or g1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g1=float(input("Nota do trabalho (IG): "))
            g2=float(input("Nota do primeiro teste (IG): "))
            while g2>20 or g2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                g2=float(input("Nota do primeiro teste (IG): "))
            u=float(input("Participação (IG): "))
            while u>20 or u<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                u=float(input("Participação (NFC): "))
            def j (g1,g2,u):
                j=(g1*0.30)+(g2*0.60)+(u*0.10)
                return j
            e1=float(input("Nota do primeiro teste (IE): "))
            while e1>20 or e1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e1=float(input("Nota do primeiro teste (IE): "))
            e2=float(input("Nota do segundo teste (IE): "))
            while e2>20 or e2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e2=float(input("Nota do segundo teste (IE): "))
            e3=float(input("Nota do terceiro teste (IE): "))
            while e3>20 or e3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                e3=float(input("Nota do terceiro teste (IE): "))
            h=float(input("Participação (IE): "))
            while h>20 or h<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                h=float(input("Participação (IE): "))
            def k (e1,e2,e3,h):
                k=(e1*0.18)+(e2*0.30)+(e3*0.35)+(h*0.17)
                return k
            m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            while m1>20 or m1<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m1=float(input("Nota do primeiro mini-teste (MAT1): "))
            m2=float(input("Nota do segundo mini-teste (MAT1): "))
            while m2>20 or m2<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m2=float(input("Nota do segundo mini-teste (MAT1): "))
            m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            while m3>20 or m3<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                m3=float(input("Nota do terceiro mini-teste (MAT1): "))
            TI=float(input("Nota do teste intermédio (MAT1): "))
            while TI>20 or TI<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TI=float(input("Nota do teste intermédio (MAT1): "))
            TF=float(input("Nota do teste final (MAT1): "))
            while TF>20 or TF<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                TF=float(input("Nota do teste final (MAT1): "))
            v=float(input("Participação (MAT1): "))
            while v>20 or v<0:
                print("\nPor favor introduza valores compreendidos entre 0 e 20")
                v=float(input("Participação (MAT1): "))
            tm=[m1,m2,m3]
            TM=heapq.nlargest(2,tm)
            MT=(TM[0]+TM[1])/2
            def a (MT,TI,TF,v):
                a=(MT*0.15)+(TI*0.40)+(TF*0.40)+(v*0.05)
                return a
            x=[round(i(n1,n2,q),2),round(k(e1,e2,e3,h),2),round(a(MT,TI,TF,v),2),round(f(t1,t2,t3,p),2),round(j(g1,g2,u),2)]
            y=["NFC","IE","MAT1","AP","IG"]
            def plotgraph (y,x):
                plt.xlabel("Notas finais")
                plt.ylabel("Disciplinas")  
                plt.title("Classificações finais de todas as disciplinas")
                plt.barh(y,x)
                plt.xlim(0,20)
                plt.xticks(np.arange(0,20+1,2.0))
                plt.show()
            plotgraph(y,x)
        else:
            print()
        while s1!="S" and s1!="N":
            print("Por favor responda sim(S) ou não(N)")
            s1=input("ATENÇÃO use apenas quando conhecer todas as notas de todas as disciplinas, deseja continuar [S/N]: ")
            if s1=="S":
                t1=float(input("Nota do primeiro teste (AP): "))
                while t1>20 or t1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    t1=float(input("Nota do primeiro teste (AP): "))
                t2=float(input("Nota do trabalho (AP): "))
                while t2>20 or t2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    t2=float(input("Nota do trabalho (AP): "))
                t3=float(input("Nota do segundo teste (AP): "))
                while t3>20 or t3<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    t3=float(input("Nota do segundo teste (AP): "))
                p=float(input("Participação (AP): "))
                while p>20 or p<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    p=float(input("Participação (AP): "))
                def f (t1,t2,t3,p):
                    f=(t1*0.30)+(t2*0.35)+(t3*0.30)+(p*0.05)
                    return f
                n1=float(input("Nota do primeiro teste (NFC): "))
                while n1>20 or n1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    n1=float(input("Nota do primeiro teste (NFC): "))
                n2=float(input("Nota do segundo teste (NFC): "))
                while n2>20 or n2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    n2=float(input("Nota do segundo teste (NFC): "))
                q=float(input("Participação (NFC): "))
                while q>20 or q<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    q=float(input("Participação (NFC): "))
                def i (n1,n2,q):
                    i=(n1*0.40)+(n2*0.40)+(q*0.20)
                    return i
                g1=float(input("Nota do trabalho (IG): "))
                while g1>20 or g1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    g1=float(input("Nota do trabalho (IG): "))
                g2=float(input("Nota do primeiro teste (IG): "))
                while g2>20 or g2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    g2=float(input("Nota do primeiro teste (IG): "))
                u=float(input("Participação (IG): "))
                while u>20 or u<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    u=float(input("Participação (NFC): "))
                def j (g1,g2,u):
                    j=(g1*0.30)+(g2*0.60)+(u*0.10)
                    return j
                e1=float(input("Nota do primeiro teste (IE): "))
                while e1>20 or e1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    e1=float(input("Nota do primeiro teste (IE): "))
                e2=float(input("Nota do segundo teste (IE): "))
                while e2>20 or e2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    e2=float(input("Nota do segundo teste (IE): "))
                e3=float(input("Nota do terceiro teste (IE): "))
                while e3>20 or e3<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    e3=float(input("Nota do terceiro teste (IE): "))
                h=float(input("Participação (IE): "))
                while h>20 or h<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    h=float(input("Participação (IE): "))
                def k (e1,e2,e3,h):
                    k=(e1*0.18)+(e2*0.30)+(e3*0.35)+(h*0.17)
                    return k
                m1=float(input("Nota do primeiro mini-teste (MAT1): "))
                while m1>20 or m1<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    m1=float(input("Nota do primeiro mini-teste (MAT1): "))
                m2=float(input("Nota do segundo mini-teste (MAT1): "))
                while m2>20 or m2<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    m2=float(input("Nota do segundo mini-teste (MAT1): "))
                m3=float(input("Nota do terceiro mini-teste (MAT1): "))
                while m3>20 or m3<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    m3=float(input("Nota do terceiro mini-teste (MAT1): "))
                TI=float(input("Nota do teste intermédio (MAT1): "))
                while TI>20 or TI<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    TI=float(input("Nota do teste intermédio (MAT1): "))
                TF=float(input("Nota do teste final (MAT1): "))
                while TF>20 or TF<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    TF=float(input("Nota do teste final (MAT1): "))
                v=float(input("Participação (MAT1): "))
                while v>20 or v<0:
                    print("\nPor favor introduza valores compreendidos entre 0 e 20")
                    v=float(input("Participação (MAT1): "))
                tm=[m1,m2,m3]
                TM=heapq.nlargest(2,tm)
                MT=(TM[0]+TM[1])/2
                def a (MT,TI,TF,v):
                    a=(MT*0.15)+(TI*0.40)+(TF*0.40)+(v*0.05)
                    return a
                x=[round(i(n1,n2,q),2),round(k(e1,e2,e3,h),2),round(a(MT,TI,TF,v),2),round(f(t1,t2,t3,p),2),round(j(g1,g2,u),2)]
                y=["NFC","IE","MAT1","AP","IG"]
                def plotgraph (y,x):
                    plt.xlabel("Notas finais")
                    plt.ylabel("Disciplinas")  
                    plt.title("Classificações finais de todas as disciplinas")
                    plt.barh(y,x)
                    plt.xlim(0,20)
                    plt.xticks(np.arange(0,20+1,2.0))
                    plt.show()
                plotgraph(y,x)
            else:
                print()