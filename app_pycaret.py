# Imports
import pandas as pd
import streamlit as st
from io import BytesIO
from pycaret.classification import load_model, save_model, create_model, predict_model, setup
import joblib

# Configuração inicial da página da aplicação
st.set_page_config(page_title='PyCaret',
                   layout="wide",
                   initial_sidebar_state='expanded')

# Função para converter o df para excel
@st.cache_data
def to_excel(df: pd.DataFrame):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

# Função principal da aplicação
def main():
    # Título principal da aplicação
    st.write("""## Escorando o modelo gerado no pycaret """)
    st.markdown("---")
    
    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank Credit Dataset", type=['csv', 'ftr'])

    # Verifica se há conteúdo carregado na aplicação
    if data_file_1 is not None:
        df_credit = pd.read_feather(data_file_1)
        df_credit = df_credit.sample(10000)
        st.write(df_credit)

        # Exibe as colunas do DataFrame para referência
        st.write("Colunas disponíveis:", df_credit.columns.tolist())

        # Criar e treinar o modelo se ele não existir
        try:
            model_saved = load_model(r"C:\Users\-__-\Desktop\pycaret\Projeto-Credit-Score\modelo_salvo")
        except FileNotFoundError:
            target_column = 'nome_da_coluna_alvo'  # Substitua pelo nome real da coluna alvo

            # Certifique-se de que a coluna alvo existe
            if target_column not in df_credit.columns:
                st.error(f"A coluna '{target_column}' não foi encontrada no DataFrame.")
                return
            
            # Criar e salvar o modelo
            exp = setup(data=df_credit, target=target_column)
            modelo_treinado = create_model('dt')  # Exemplo: criando um modelo de árvore de decisão
            save_model(modelo_treinado, r"C:\Users\-__-\Desktop\pycaret\Projeto-Credit-Score\modelo_salvo")
            model_saved = modelo_treinado

        predict = predict_model(model_saved, data=df_credit)

        # Converter as previsões para Excel
        df_xlsx = to_excel(predict)
        st.download_button(label='📥 Download das Previsões',
                           data=df_xlsx,
                           file_name='predict.xlsx')

        # Salvar o modelo para download
        model_download_path = r"C:\Users\-__-\Desktop\pycaret\Projeto-Credit-Score\modelo_salvo.pkl"
        joblib.dump(model_saved, model_download_path)

        # Botão de download do modelo
        with open(model_download_path, "rb") as f:
            st.download_button(label='📥 Download do Modelo',
                               data=f,
                               file_name='modelo_salvo.pkl')

if __name__ == '__main__':
    main()
