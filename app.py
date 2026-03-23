import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora Gráfica", page_icon="🖨️")

st.title("🖨️ Orçamento de Adesivos")
st.markdown("Preencha os dados abaixo para calcular o valor do serviço.")

# Sidebar para configurações de preço
st.sidebar.header("Configurações de Custo")
preco_m2 = st.sidebar.number_input("Preço do m² (R$)", min_value=0.0, value=80.0, step=5.0)

# Layout em colunas para os inputs
col1, col2 = st.columns(2)

with col1:
    unidade = st.selectbox("Unidade de medida", ["Milímetros (mm)", "Centímetros (cm)", "Metros (m)"])
    quantidade = st.number_input("Quantidade de adesivos", min_value=1, value=10, step=1)

with col2:
    largura = st.number_input(f"Largura ({unidade.split()[-1]})", min_value=0.01, value=10.0)
    altura = st.number_input(f"Altura ({unidade.split()[-1]})", min_value=0.01, value=10.0)

# Lógica de conversão
fator = 1
if "mm" in unidade:
    fator = 1000
elif "cm" in unidade:
    fator = 100

larg_m = largura / fator
alt_m = altura / fator

# Cálculos
area_unidade_m2 = larg_m * alt_m
area_total_m2 = area_unidade_m2 * quantidade
valor_total = area_total_m2 * preco_m2

# Exibição dos Resultados (Ajustado: agora com apenas 2 colunas)
st.divider()
c1, c2 = st.columns(2)

# Removemos a métrica da Área Unitária e mantivemos as outras duas
c1.metric("Área Total do Pedido", f"{area_total_m2:.2f} m²")
c2.metric("Valor Total", f"R$ {valor_total:.2f}")

if st.button("Gerar Resumo para Copiar"):
    # Também removi a linha da área total do resumo de texto para ficar enxuto
    texto_resumo = f"""
    📌 *ORÇAMENTO GRÁFICA*
    - Produto: Adesivo ({largura}x{altura} {unidade.split()[-1]})
    - Quantidade: {quantidade} un
    - *VALOR TOTAL: R$ {valor_total:.2f}*
    """
    st.code(texto_resumo, language="markdown")