import streamlit as st

st.title('Find the largest among 3 numbers')

num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
num3 = st.number_input('Enter the third number')

if st.button('Find Largest'):
    largest = max(num1, num2, num3)
    st.write(f'The largest number is: {largest}')