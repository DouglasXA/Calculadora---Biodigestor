import streamlit as st

# Personalização de layout com CSS
st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction: row;}</style>', unsafe_allow_html=True)
st.write('<style>div.Widget.row-widget.stMulti > div{flex-direction: row;}</style>', unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título do aplicativo
st.title("Calculadora de Biodigestor - I Feira Integrada de Ciências do IFG")

# Imagem de logotipo com dimensões em centímetros
largura_cm = 40
st.image("logo.webp", width=int(15 * largura_cm))  # Ajuste o valor de largura_cm conforme desejado

# Seção explicativa
st.header("O que é um Biodigestor")
st.write("Um biodigestor é um dispositivo que converte resíduos orgânicos em biogás, uma fonte de energia renovável. Este aplicativo ajuda a calcular o ganho econômico e a quantidade de gás produzida com base nos resíduos de um restaurante universitário.")

# Entrada do usuário: valor do botijão de gás na região
valor_botijao_gas = st.number_input("Valor de um Botijão de Gás de 13 kg na sua região (R$):", min_value=0.0)

# Insumos adicionados
insumos = {
    "Palha de Trigo": (0.2116, 0.0847),
    "Milho - resíduos da colheira": (0.1158, 0.0463),
    "Resíduos da limpeza de grãos": (0.3818, 0.1527),
    "Batata - resíduos da colheita": (0.1101, 0.0440),
    "Bananeiras c/ bananas": (0.0114, 0.0046),
    "Beterraba, folhas da colheita": (0.0358, 0.0143),
    "Abacaxi, indústria de conserva": (0.0744, 0.0297),
    "Polpa de café": (0.0644, 0.0257),
    "Polpa de laranja": (0.0343, 0.0137),
    "Resíduos Cervejaria": (0.0023, 0.0009),
    "Fábrica de Laticínios": (0.0016, 0.0006),
    "Matadouro": (0.0026, 0.0010),
    "Beterraba, sacarina": (0.1300, 0.0520),
    "Resíduos de Hortaliças": (0.0386, 0.0154),
    "Hortaliças (refugo)": (0.0586, 0.0235),
    "Cereal (resíduos)": (0.3704, 0.1481),
    "Bagaço do malte": (0.0887, 0.0355),
    "Bagaço de frutas (fresco)": (0.0729, 0.0292),
    "Casca de batata": (0.0972, 0.0389),
    "Melaço": (0.3532, 0.1413),
    "Bagalo de maçã": (0.1444, 0.0578),
    "Bagaço de uva": (0.2603, 0.1041)
}

# Caixa de seleção para os insumos
selecionados = st.multiselect("Selecione os Insumos:", list(insumos.keys()))

# Dicionário para armazenar quantidades dos insumos
quantidades_insumos = {}
for insumo in selecionados:
    quantidades_insumos[insumo] = st.number_input(f"Quantidade de {insumo} (em kg):", min_value=0.0)

# Cálculos para os insumos selecionados
producao_gas_insumos = sum(quantidades_insumos[insumo] * insumos[insumo][0] for insumo in quantidades_insumos)
quantidade_glp_insumos = sum(quantidades_insumos[insumo] * insumos[insumo][1] for insumo in quantidades_insumos)

# Cálculo do valor gerado com base no preço do botijão de gás na região
valor_gerado = (quantidade_glp_insumos * valor_botijao_gas/13)

# Resultados para os insumos selecionados
st.header("Resultados para Insumos Selecionados")
st.write(f"Produção de Biogás a partir dos Insumos (m³): {producao_gas_insumos:.4f}")
st.write(f"Quantidade de GLP a partir dos Insumos (kg): {quantidade_glp_insumos:.4f}")

# Resultado do valor gerado
st.header("Resultado do Valor Gerado")
st.write(f"Valor Gerado com a Produção de Biogás na sua Região (R$): {valor_gerado:.2f}")

# Botão "Sobre os Autores" que exibe informações dos autores
if st.button("Sobre os Autores"):
    st.write("Os Autores do Trabalho são do Instituto Federal de Goiás - Campus Aparecida de Goiânia:")
    st.write("Sinara Silva de Matos (Discente)")
    st.write("Rérald de Matos Gomes (Discente)")
    st.write("Hellen Rakel de Matos Pereira (Discente)")
    st.write("Renata Santos Ribeiro (Orientadora)")
    st.write("Douglas Xavier de Andrade (Co-orientador)")
