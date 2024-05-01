import streamlit as st

st.title("Interpolation and Regression")
st.write()
st.subheader("1.Polynomial Interpolation")
st.write("    Polynomial Interpolation is the interpolation of a given "
             "   data set by the polynomial of lowest possible"
             "   degree that passes through the points of the dataset."
             "  The given data set is represented as a Vandermonde system"
             "  and it's solution is obtained using the Gauss Elimination method."
             "  This solution is used to construct the polynomial")
st.write()
st.subheader("2.Regression Analysis")
st.write("Regression analysis is a statistical method that shows the "
         "relationship between two or more variables."
         " Usually expressed in a graph, the method tests the relationship "
         "between a dependent variable against independent variables."
         " The given data set for n independent variables is represented as a"
         " matrix system and the n normal equations are derived from the Least Square method."
         " The solution of the system is obtained using the Gauss Elimination method."
         " This solution is used to form the regression equation")