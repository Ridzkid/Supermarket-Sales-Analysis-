
from sympy import im
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd


st.set_page_config(
    page_title="Milestone 1",
    page_icon="👽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/',
        'Report a bug': "https://github.com/Ridzkid",
        'About': "Practice Streamlit"
    }
)

st.sidebar.title('Site Navigation')
selection = st.sidebar.selectbox("Please select a page to view", ["Home","Data Visualization", "Hypothesis Testing"])

if selection == "Home":
    st.title('Home Page')
    st.markdown(f""" 
                                    Hello Semua Apakabar semuanya? baik\
                                    Jika ada kendala atau masalah bisa hubungi aku ya di [Github](https://github.com/Ridzkid) """)


                
elif selection == "Data Visualization":
    st.title('Data Visualization')
    


    def get_data():
        return pd.read_csv('supermarket_sales.csv')

    df= get_data()

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.header('Dataframe')
    with st.expander ('More Data '):
        st.markdown(f""" ### Akan Menampilkan sebuah Data Frame, Jika tidak ingin maka tidak perlu mencetangnya""")
    #checkbox
        show_df= st.checkbox('Melihatkan DataFrame')

        if show_df:
            st.write(df)
###########################################################################
    st.header(' Perubahan Gross Income berdasarkan tanggal ')
    st.markdown('Disni kita akan melihat perubahan gross income berdasarkan kota berikut simulasinya')
    with st.expander ('More Data'):     #Melakukan Expander
        x= df.sort_values(by=["Date"], ascending=True)
        st.write(px.bar(x,x='City',y='gross income',color='City',animation_frame='Date',    #Melakukan simulasi dengan barchart dengan melihat kenaikan gross income per harinya
                    title='Perubahan Gross Income per kota berdasarkan tanggal',
                    animation_group="Branch", range_y=[0,100]))
    st.markdown('Setelah melihat perubahannya sekarang akan melihat bagaimana perbandingan rata-rata dari gross income setiap kotanya')
################################################################################
    st.header('Menampilkan rata rata Gross Income') 
    with st.expander ('More Data '):    #Melakukan Expander
        df_city= df.groupby(['City'])['gross income'].mean() #Melakukan Data query dengan grouping
        city = st.radio('City', df.City.unique())
        st.write(f'Avg Gross income of {city}: {df.query("City==@city")["gross income"].mean():.2f}') #Menggunakan Radio button


        #Visualisasi menggunakan Plotly
        fig1= px.bar(x=df_city, y=df_city.index, color= df_city.index, orientation='h', #Visualisasi Grafik berdasarkan Bar chart
        labels= {'y': 'City', 'x': 'Avg Gross Income'}, 
        title='Avg Gross Income by City')
        st.plotly_chart(fig1)
        
        st.write(f"""Dari sini bisa dilihat bahwa nilai rata-rata Gross Income Kota Yangon adalah yang paling rendah dengan nilai `14.87` """)

   
    #####################################################################
    st.header('Perbandingan Avg Gross Income Kota Yangoon Berdasarkan Gender')
    with st.expander('More Data'):
    
        YG = df[df.City=='Yangon'] 
        df_yangon= YG.groupby(['Gender'])['gross income'].mean() #Melakukan Data query dengan grouping
        city = st.radio('Gender', YG.Gender.unique())
        st.write(f'Avg Gross income of {city}: {YG.query("Gender==@city")["gross income"].mean():.2f}')
        
       
        
        
        fig2= px.bar(x=df_yangon.index, y=df_yangon, color= df_yangon.index, #Visualisasi Grafik berdasarkan Bar chart
        labels= {'y': 'Avg Gross Income', 'x': 'Gender'}, 
        title='Avg Gross Income by Gender')
        st.plotly_chart(fig2)
        
        st.markdown(f"""
        Dari sini bisa dilihat bahwa:
        > Avg Gross Income Female > Avg Gross Income Male
        
        Setelah itu kita akan melihat Product line apa saja yang diminati berdasarkan gender di kota yangoon? berikut simulasinya
        """)

    st.header('Barang yang diminati berdasarkan Gender di Kota Yangon')
    with st.expander('More Data'):
        fig3 = px.bar(YG,x='Product line',y='Unit price',color='Gender',barmode='group',title='Tipe Barang yang dibeli berdasarkan Jenis Kelamin')
        fig3.update_layout(uniformtext_minsize=8 , xaxis_tickangle=-45)
        st.write(fig3)
        st.markdown(f"""
        Dari sini bisa dilihat bahwa paling tinggi Peminatan Female terhadap Product Home dan Lifestyle, sedangkan Male peminatan tertingginya pada Food and Beverage """)
else:
    st.title('Hypotesis Testing')
    st.markdown(f"""
       ##  Dari data diatas bisa disimpulkan bahwa rata rata gross income dikota Yangoon dari kedua gender tersebut adalah:
        - Female memiliki rata-rata Gross Income sebesar `15.75`
        - Male memiliki rata-rata Gross Income sebesar `14.081`
        Secara kasat mata rata-rata gross income pada Female dan Male bereda dengan Rata-rata Female > Rata-rata Male
        tapi apakah berbeda signifikan? apakah tidak? Mari buktikan dengan Hipotesa:
    
       - H0: μ Rata Rata Gross Income Female Yangon == μ Rata Rata Gross Income Male Yangon Maksudnya adalah jika nilai Rata rata sample Female == Rata-rata sample Male

       - H1: μ Rata Rata Gross Income Female Yangon != μ Rata Rata Gross Income Male Yangon Maksudnya adalah jika nilai Rata rata sample Female != Rata-rata sample Male
       
        Dengan menggunakan metode Dependent Two Tail, Untuk melihat apakah Berbeda signifikan atau tidak

       > 
       """)
    st.markdown(f""" 
        ### Hasil Analisis 
        -  Didapati Untuk P-valuenya yaitu : 0.16261180081238572
        -  Didapati Untuk T-Value yaitu : 1.3993944019116016
        Dari sini bisa disimpulkan bahwa H0 diterima , akan tetapi saya akan mencoba membuktikannya lagi berdasarkan grafik, berikut simulasinya:
        """)
    img=plt.imread('output.png')
    st.image(img, caption='Uji Hipotesis')
    
    st.markdown('Itu menandakan bahwa Rata-rata gross income antara Gender Laki-laki dengan Gender Female memiliki kesamaan, teteapi kalau dilihat dari nilai Mean yang dimiliki keduanya, tetap Gender Female yang lebih besar dibanding Gender Male (F> M) ')
    st.markdown(f""" 
        Dari hal tersebut dikarekan tidak memiliki perbedaan secara signifikan, maka saya akan menyarankan untuk meningkatkan gross income dengan memfokuskan menjual sesuai dengan Product yang paling diminati, yaitu:
        -    Untuk Female Product yang paling diminati yaitu Home And Lifestyle dengan cara memperbanyak variasi pada Product tersebut
        -    Untuk Male Product yang paling diminati yaitu Food and Beverage dengan cara memperbanyak variasi pada Product tersebut """)

