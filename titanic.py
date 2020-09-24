import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import pandas as pd


st.title("Titanic  Dataset EDA")


st.set_option('deprecation.showPyplotGlobalUse', False)


@st.cache(persist=True)
def Explore_data(dataset):
    
    data = pd.read_csv(dataset)
    return data

if st.checkbox("Preview Training DataSet"):
    data = Explore_data("train.csv")
    
    if st.button("Head"):
        st.write(data.head(5))
        
    if st.button("Tail"):
        st.write(data.tail(5))
        
if st.checkbox("Preview Testing DataSet"):
    data = Explore_data("test.csv")
    
    if st.button("Head"):
        st.write(data.head(5))
        
    if st.button("Tail"):
        st.write(data.tail(5))
        
if st.checkbox("Show All DataSet"):
    data = Explore_data("train.csv")
    st.write(data)
    
    
if st.checkbox("Show Columns Name"):
    data = Explore_data("train.csv")
    st.write(data.columns)  
    
if st.checkbox("Show Dimensions"):
    data = Explore_data("train.csv")
    
    st.text("Rows And Columns")
    st.write(data.shape) 
    
if st.checkbox("Describe Train DataSet"):
    data = Explore_data("train.csv")
    
    st.write(data.describe())
    
if st.checkbox("Describe Test DataSet"):
    data = Explore_data("test.csv")
    
    st.write(data.describe())
    
if st.checkbox("Show Null Values "):
    data = Explore_data("train.csv")
    st.write(data.isnull().sum())
    st.pyplot()
    
if st.checkbox("Age Distribution Plot"):
    data = Explore_data("train.csv")
    st.write(sns.distplot(data["Age"]))
    st.pyplot()
    
if st.checkbox("Survived Based On Gender"):
    data = Explore_data("train.csv")
    st.write(sns.barplot(x="Sex", y="Survived", data=data))
    st.pyplot()
    
if st.checkbox("Survived Based On Passenger Class"):
    data = Explore_data("train.csv")
    st.write(sns.barplot(x="Pclass", y="Survived", data=data))
    st.pyplot()
    
if st.checkbox("Survived Based On Passenger Class with Gender"):
    data = Explore_data("train.csv")
    st.write(sns.barplot(x="Pclass", y="Survived", hue = "Sex", data=data))
    st.pyplot()
    
if st.checkbox("Sex vs Survival Rate "):
    data = Explore_data("train.csv")
    st.write(sns.barplot(x="Sex", y="Survived", hue = "Pclass", data=data))
    st.pyplot()
    
if st.checkbox("Survived Vs Age"):
    data = Explore_data("train.csv")
    st.write(sns.stripplot(x="Survived", y="Age", jitter=True , data=data))
    st.pyplot()
    
if st.checkbox("Pair Plot"):
    data = Explore_data("train.csv")
    st.write(sns.pairplot(data))
    st.pyplot()
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    