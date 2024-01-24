import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("laptop_prices_cleaned.csv")
    return df

df = load_data()


def show_explore_page():
    st.title("Explore Laptop Data")

    st.write(
        """
    ### Most expensive brands
    """
    )
    temp = df.groupby('brand').price.mean()
    temp2 = temp.sort_values(ascending=False)[:10]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=temp2.index, x=temp2.values, ax=ax)
    st.pyplot(fig)

    st.write(
        """
    ### Top rated brands
    """
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    temp = df.groupby('brand').rating.mean()
    temp2 = temp.sort_values(ascending=False)[:10]
    sns.barplot(y=temp2.index, x=temp2.values, palette='viridis', ax=ax)
    ax.set_xlabel('Average Rating')
    ax.set_ylabel('Brand')
    st.pyplot(fig)

    st.write(
        """
    ### Laptop Price vs RAM
    """
    )
    fig, ax = plt.subplots()
    sns.lineplot(x='ram', y='price', data=df, marker='o', color='skyblue', ax=ax)
    ax.set_xlabel('RAM (GB)')
    ax.set_ylabel('Price ($)')
    st.pyplot(fig)

    st.write(
        """
    ### Distribution of Top 5 Operating Systems
    """
    )
    os_counts = df['OS'].value_counts()
    os_counts_top5 = os_counts.head(5)

    fig, ax = plt.subplots()
    ax.pie(os_counts_top5, labels=os_counts_top5.index, autopct='%1.1f%%', startangle=45,
           colors=sns.color_palette('viridis'), wedgeprops=dict(width=0.4))
    st.pyplot(fig)



    st.write(
        """
    ### Price Distribution by Graphics Coprocessor
    """
    )
    fig, ax = plt.subplots()
    sns.barplot(x='graphics_coprocessor', y='price', data=df, palette='Set2', ax=ax)
    ax.set_xlabel('Graphics Coprocessor')
    ax.set_ylabel('Price ($)')
    st.pyplot(fig)

    st.write(
        """
    ### Price Distribution by Graphics
    """
    )
    fig, ax = plt.subplots()
    sns.barplot(x='graphics', y='price', data=df, palette='Set2', ax=ax)
    ax.set_xlabel('Graphics Coprocessor')
    ax.set_ylabel('Price ($)')
    st.pyplot(fig)

    bins = [10, 12, 14, 16, 18, 20]
    labels = ['10-12', '12-14', '14-16', '16-18', '18-20']
    df['screen_size_bin'] = pd.cut(df['screen_size'], bins=bins, labels=labels, right=False)


    st.write(
        """
    ### Laptop Price by Screen Size
    """
    )
    fig, ax = plt.subplots()
    sns.barplot(x='screen_size_bin', y='price', data=df,errorbar=None, palette='viridis', ax=ax)
    ax.set_xlabel('Screen Size (inches)')
    ax.set_ylabel('Price ($)')
    st.pyplot(fig)

    st.write(
        """
    ### Laptop Price vs CPU
    """
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='cpu', y='price', data=df.sort_values(by='price', ascending=False), palette='coolwarm', ax=ax)
    ax.set_xlabel('CPU')
    ax.set_ylabel('Price ($)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)
