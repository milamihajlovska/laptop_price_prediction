import streamlit as st
import pickle
import numpy as np
import pandas as pd
from keras.models import load_model

def def_load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = def_load_model()

keras_model = load_model("my_model.keras")

label_encoder = data["label_encoder"]
scaler = data["scaler"]
df = data ["df"]
df_encoded = data ["df_encoded"]

def show_predict_page():
    st.title("Laptop Price Prediction")

    st.write("""### Fill out the following form""")

    model = (
        'Unknown', 'VectorGP6612UGS-267', 'Ideapad3',
       'StealthGS6612UGS-025', 'Inspiron', 'Chromebook', 'Latitude',
       'Ideapad', 'Latitude5000', 'Pavilion', 'Latitude5530',
       'Latitude7000', 'Latitude3000', 'XPS159520', 'Latitude9000',
       'Alienwarem18', 'Latitude5440', 'Latitude5430', 'Thinkpad',
       'XPS9520', 'Latitude7320Detachable2-in-1', 'Latitude3520',
       'XPS9510', 'Precision7770', 'Latitude7440', 'Precision3000',
       'Latitude7420', 'XPS9530', 'XPS9320', 'XPS', 'Inspiron3511',
       'AlienwareX17R2', 'Latitude5420', 'Precision7670', 'Latitude5320',
       'Alienwarem16', 'Vostro7620', 'Latitude3420', 'Latitude5520',
       'Precision7560', 'Latitude7320', 'Vostro3510', 'Precision7780'
    )

    brand = (
        'ROKC', 'HP', 'MSI', 'Dell', 'Lenovo', 'Samsung', 'Asus', 'Apple',
        'Acer', 'Alienware'
    )

    color = ('Blue', 'Silver', 'Black', 'Gray', 'Gold', 'Unknown', 'Brown',
       'White', 'Green', 'Red')

    OS = ('Windows 11', 'Windows 11 Pro', 'Chrome OS', 'Windows 10 Pro',
       'Windows 10', 'Mac OS', 'Windows 11 S', 'Unknown', 'Windows 7',
       'Windows', 'Windows 10 S', 'Windows 8')
    graphics = ('Integrated', 'Dedicated', 'Unknown', 'Integrated, Dedicated')
    graphics_coprocessor = ('Integrated', 'Unknown', 'Mid-range GPU', 'High-end GPU',
       'Low-end GPU')
    wifi_and_bluetooth = ('Yes','No')
    backlit_keyboard = ('Yes','No')
    anti_glare = ('Yes','No')
    fingerprint = ('Yes','No')
    hd_audio = ('Yes','No')

    cpu = ('Intel Core i7', 'Intel Core i5', 'Intel Core i9', 'Pentium',
       'Celeron', 'MediaTek MT8183', 'Intel Core i3', 'AMD A Series',
       'Ryzen 7', 'Unknown', 'Ryzen 3', 'Ryzen 5', 'AMD R Series', '8032')



    brand = st.selectbox("Brand", brand)
    model = st.selectbox("Model", model)
    OS = st.selectbox("Operating System", OS)
    graphics = st.selectbox("Graphics", graphics)
    graphics_coprocessor = st.selectbox("Graphics Coprocessor", graphics_coprocessor)
    harddisk = st.number_input("Insert Hard disk size (GB)")
    ram = st.number_input("Insert RAM (GB)")
    cpu = st.selectbox("CPU", cpu)
    screen_size = st.number_input("Insert screen size")
    color = st.selectbox("Color", color)
    wifi_and_bluetooth = st.selectbox("Wifi and Bluetooth", wifi_and_bluetooth)
    anti_glare = st.selectbox("Anti Glare", anti_glare)
    fingerprint = st.selectbox("Fingerprint", fingerprint)
    backlit_keyboard = st.selectbox("Backlit keyboard", backlit_keyboard)
    hd_audio = st.selectbox("HD audio", hd_audio)



    ok = st.button("Calculate Price")
    if ok:
        X = np.array([[model, brand, screen_size,color, harddisk, cpu, ram, OS, graphics, graphics_coprocessor, wifi_and_bluetooth, backlit_keyboard, anti_glare, fingerprint, hd_audio]], dtype=object)

        new_laptop_df = pd.DataFrame(X, columns=df.drop(columns = ['price','rating'], axis=1).columns)

        # Create DataFrames with all possible categories for each column
        all_graphics = df['graphics'].unique()
        all_graphics_df = pd.DataFrame({'graphics': all_graphics})

        all_colors = df['color'].unique()
        all_colors_df = pd.DataFrame({'color': all_colors})

        all_gc = df['graphics_coprocessor'].unique()
        all_gc_df = pd.DataFrame({'graphics_coprocessor': all_gc})

        # Merge the new input data with the DataFrames of all categories
        new_laptop_df = pd.merge(new_laptop_df, all_graphics_df, how='outer', on=['graphics'])
        new_laptop_df = pd.merge(new_laptop_df, all_colors_df, how='outer', on=['color'])
        new_laptop_df = pd.merge(new_laptop_df, all_gc_df, how='outer', on=['graphics_coprocessor'])
        new_laptop_df['color'].fillna('Blue', inplace=True)
        new_laptop_df['graphics'].fillna('Integrated', inplace=True)
        new_laptop_df['graphics_coprocessor'].fillna('Integrated', inplace=True)

        label_cols = ['color', 'graphics', 'graphics_coprocessor', 'wifi & bluetooth', 'backlit keyboard', 'anti-glare',
                      'fingerprint', 'hd audio']
        new_laptop_df[label_cols] = new_laptop_df[label_cols].apply(label_encoder.fit_transform)

        new_laptop_df = new_laptop_df.iloc[[0]]

        categorical_cols = ['brand', 'model', 'cpu', 'OS']
        new_laptop_encoded = pd.get_dummies(new_laptop_df, columns=categorical_cols)

        missing_cols = set(df_encoded.drop('price', axis=1).columns) - set(new_laptop_encoded.columns)
        for col in missing_cols:
            new_laptop_encoded[col] = 0

        new_laptop_encoded = new_laptop_encoded[df_encoded.drop('price', axis=1).columns]

        new_laptop_scaled = scaler.transform(new_laptop_encoded)

        new_laptop_price_pred = keras_model.predict(new_laptop_scaled)

        st.subheader(f"The estimated price is ${new_laptop_price_pred.flatten()[0]:.2f}")