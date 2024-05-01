import streamlit as st
import numpy as np

def gauss(a,n):
    x = np.zeros(n)
    for i in range(n):
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x

st.title("Multiple Regression")
n = int(st.number_input("Enter the number of independent variables"))
sy = st.text_input("Enter the y values")
sx = []
nx = []
ny = sy.split(",")
flag=0
for i in range(n):
    sx.append(st.text_input(f"Enter the x{i+1} values"))
a = st.button("Analyze")
if a:
    for i in range(n):
        nx.append((sx[i].split(",")))
    m = len(nx[i])
    x = np.zeros((m,n+1))
    b = np.zeros(m)
    for i in range(m):
        b[i] = float(ny[i])
        for j in range(n+1):
            if j == 0:
                x[i][j] = 1
            else:
                x[i][j] = float(nx[j-1][i])
    t = np.zeros((n+1,m))
    aug = np.zeros((n+1,n+2))
    for i in range(n + 1):
        for j in range(m):
            t[i][j] = x[j][i]
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(m):
                aug[i][j] = aug[i][j] + t[i][k] * x[k][j]
    for i in range(n + 1):
        for j in range(m):
            aug[i][n + 1] = aug[i][n + 1] + t[i][j] * b[j]

    c = gauss(aug,n+1)
    c[np.isnan(c)] = 0
    for i in range(n+1):
        if c[i]!=0:
            flag=1
            break
    newstr = " y= "
    if c[0]!=0:
        newstr += f" {round(c[0],3)} "
    for i in range(1,n+1):
        if c[i]>0 and newstr != " y= ":
            newstr += f" + {round(c[i],3)}x{i} "
        elif c[i]<0 or newstr == " y= ":
            newstr += f" {round(c[i],3)}x{i} "
    if flag==1:
        st.subheader("The equation is ")
        st.subheader(f"$$ {newstr} $$")
    else:
        st.subheader("The normal equations have infinitely many solutions")
