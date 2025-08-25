import streamlit as st
import numpy as np
from scipy.linalg import solve

st.set_page_config(page_title="Algebraic equation solver", layout = "wide")

st. title("Algebraic Equation Solver")

st.markdown ("Solves linear, quadratic, cubic and system of equation")

linear = "linear (ax+b =0)"
qua = "Quadratic (ax + bx + c = 0)"
cub = "Cubic (ax + bx + cx + d = 0)"
sys2 = "system of two eqns"
sys3 = "system of three eqns"
options = st.sidebar.radio("choose a type of equation to solve:", (linear, qua, cub, sys2, sys3))
st.divider()

if options == linear:
    st.subheader ("Linear equation")
    a = st.number_input("Enter a coefficient", value = 0)
    b = st. number_input("Enter a constant:" ,value = 0)
    #st. latex(fr"{a}x + {b} = 0")
    if (b >= 0):
        st.latex(fr" {a}x + {b} = 0")
    elif (b < 0):
        st.latex(fr" {a}x {b} = 0")

    if st.button("Solve"):
        if a != 0:
            result = -b / a
            st.success(f"The root is: {result}")
        else:
            st.error("Invalid equation")

elif options == qua:
    st.subheader ("Quadratic equation")
    a = st.number_input("Enter a coefficient (a)", value = 0)
    b = st.number_input("Enter a coefficient (b)", value=0)
    c = st. number_input("Enter a constant:" ,value = 0)

    if (b >= 0 and c >= 0):
        st.latex(fr" {a}x^2 + {b}x + {c} = 0")
    elif (b < 0):
        st.latex(fr" {a}x^2 {b}x + {c} = 0")
    elif (c < 0):
        st.latex(fr" {a}x^2+{b}x {c} = 0")
    elif (b < 0 and c < 0):
            st.latex(fr" {a}x^2 - {b}x - {c} = 0")

    if st.button("Solve:"):
            coeff = [a, b, c]
            result = np.roots(coeff)
            st.success(f"The roots are : {result[0]} and {result[1]}")

elif options == cub:
    st.subheader ("Cubic equation")
    a = st.number_input("Enter a coefficient (a)", value = 0)
    b = st.number_input("Enter a coefficient (b)", value=0)
    c = st.number_input("Enter a coefficient (c)", value=0)
    d = st. number_input("Enter a constant:" ,value = 0)

    if (b >= 0 and c >= 0 and d>=0):
        st.latex(fr" {a}x^3 + {b}x^2 + {c}x + {d} = 0")
    elif (b < 0):
        st.latex(fr" {a}x^3 {b}x^2 + {c}x + {d} = 0")
    elif (b < 0 and c < 0):
        st.latex(fr" {a}x^3 {b}x^2 {c}x + {d} = 0")
    elif (b < 0 and d < 0):
        st.latex(fr" {a}x^3 {b}x^2 + {c}x {d} = 0")
    elif (c < 0):
         st.latex(fr" {a}x^3 {b}x^2 {c}x + {d} = 0")
    elif (d < 0 and c < 0):
        st.latex(fr" {a}x^3 + {b}x^2 {c}x {d} = 0")
    elif (d < 0):
        st.latex(fr" {a}x^3 + {b}x^2 {c}x + {d} = 0")
    elif (b < 0 and c >= 0 and d>=0):
        st.latex(fr" {a}x^3 {b}x^2 {c}x {d} = 0")

    if st.button("Solve:"):
            coeff = [a, b, c]
            result = np.roots(coeff)
            st.success(f"The roots are : {result[0]} and {result[1]}")

elif options == sys2:
    st.subheader("System of 2 equations")
    coe = st.text_input("enter coefficente values: ").split()
    for index, value in enumerate(coe):
        coe[index] = int(value)
    coe = np.array(coe)
    n = int(np.sqrt(coe.size))  # number of variables
    if n * n == coe.size:  # check it's a perfect square
        coe = coe.reshape(n, n)  # square matrix
    else:
        st.write("Number of coefficients must form a square matrix (like 4 for 2x2, 9 for 3x3)")
    cons = st.text_input("Enter Constant values: ").split()
    for index, value in enumerate(cons):
            cons[index] = int(value)
    cons = np.array(cons)

    if st.button("Solve:"):
            result = solve(coe, cons)

            st.success(f"The roots are : {result[0]} and {result[1]}")

elif options == sys3:
    st.subheader("system of two eqns")
    x1 = st.number_input("Enter the coeff of x(eqn1):", value=1)
    y1 = st.number_input("Enter the coeff of y(eqn1):", value=1)
    z1 = st.number_input("Enter the coeff of z(eqn1):", value=1)
    x2 = st.number_input("Enter the coeff of x(eqn2):", value=1)
    y2 = st.number_input("Enter the coeff of y(eqn2):", value=1)
    z2 = st.number_input("Enter the coeff of z(eqn2):", value=1)
    x3 = st.number_input("Enter the coeff of x(eqn3):", value=1)
    y3 = st.number_input("Enter the coeff of y(eqn3):", value=1)
    z3 = st.number_input("Enter the coeff of z(eqn3):", value=1)
    c1 = st.number_input("Enter a constant of c(eqn1):", value=1)
    c2 = st.number_input("Enter a constant of c(eqn2):", value=1)
    c3 = st.number_input("Enter a constant of c(eqn3):", value=1)

    st.latex(fr"({x1})x + ({y1})y + ({z2})z= {c1}")
    st.latex(fr"({x2})x + ({y2})y +({z2})= {c2}")
    st.latex(fr"({x3})x + ({y3})y +({z3})= {c3}")

    if st.button("Solve"):
        coeff = np.array([
            [x1, y1, z1],
            [x2, y2, z2],
            [x3, y3, z3]
        ])
        const = np.array([c1, c2, c3])
        result = solve(coeff, const)
        st.success(f"Values of the unknowns are : {result[0]}, {result[1]} and {result[2]}")
