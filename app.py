import io
import pandas as pd
import streamlit as st

def main():
    st.title('File Converte')
    option = st.selectbox("Choose the convertion", ['CSV 2 Parquet', 'Parquet 2 CSV'])
    file_uploaded = st.file_uploader(f'Upload your file {option.split()[0].lower()}', type=[option.split()[0]])

    if file_uploaded:
        try:
            if option == 'Parquet 2 CSV':
                label = 'csv'
                df = pd.read_parquet(io.BytesIO(file_uploaded.getvalue()))
                data = df.to_csv(index=False).encode('utf-8')
                mime='text/csv'
            else:
                label = 'parquet'
                df = pd.read_csv(file_uploaded)

                parquet = io.BytesIO()
                file_converted = df.to_parquet(parquet, index=False)
                data = parquet.getvalue()
                mime='application/octet-stream'

            st.write('Visualize your data')
            st.dataframe(df.head())

            st.download_button(label=f'Baixar arquivo {label.title()}',
                                data=data,
                                file_name=f'file_converted.{label}',
                                mime=mime)

        except Exception as ex:
            st.error(f'Error to processing the file: {ex}')


if __name__ == '__main__':
    main()