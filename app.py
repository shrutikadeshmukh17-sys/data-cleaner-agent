
import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Data Cleaner Agent")
st.write("Upload your dataset and clean it automatically.")

file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)

if file is not None:
    try:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.subheader("Original Dataset")
        st.dataframe(df.head(10))

        st.write("Total rows:", len(df))
        st.write("Missing values:", int(df.isnull().sum().sum()))
        st.write("Duplicate rows:", int(df.duplicated().sum()))

        if st.button("Clean Dataset"):
            df = df.copy()

            for col in df.select_dtypes(include="number").columns:
                if df[col].isnull().any():
                    df[col] = df[col].fillna(df[col].median())

            for col in df.select_dtypes(include="object").columns:
                if df[col].isnull().any():
                    mode = df[col].mode()
                    if not mode.empty:
                        df[col] = df[col].fillna(mode[0])

            df = df.drop_duplicates()

            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)

            st.success("Dataset cleaned successfully!")
            st.dataframe(df.head(10))

            st.download_button(
                "Download Cleaned Excel",
                data=output.getvalue(),
                file_name="Cleaned_Data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"Unable to process the file: {e}")
