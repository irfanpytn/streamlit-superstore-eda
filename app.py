import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("📊 EDA Superstore Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("📂 Upload Superstore Dataset (.csv)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Tampilkan tabel
    st.subheader("Preview Dataset")
    st.dataframe(df.head())

    # Checkbox untuk shape dan info
    if st.checkbox("Show dataset shape"):
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Selectbox: pilih kolom numerik
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    selected_col = st.selectbox("Select a numeric column to analyze", numeric_cols)

    # Histogram
    st.subheader(f"Histogram of {selected_col}")
    bins = st.slider("Bins", 5, 50, 20)
    fig, ax = plt.subplots()
    ax.hist(df[selected_col], bins=bins, color="skyblue")
    st.pyplot(fig)

    # Pie chart kategori
    if "Category" in df.columns:
        st.subheader("📎 Product Category Distribution")
        cat_counts = df["Category"].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)

    # Barplot per segmen
    if "Segment" in df.columns and "Sales" in df.columns:
        st.subheader("💼 Sales by Segment")
        fig3, ax3 = plt.subplots()
        sns.barplot(x="Segment", y="Sales", data=df, ci=None, estimator=sum, ax=ax3)
        st.pyplot(fig3)
