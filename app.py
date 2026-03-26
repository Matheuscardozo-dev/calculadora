import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora Gráfica", page_icon="🖨️")

st.title("🖨️ Orçamento de Impressão")
st.markdown("Preencha os dados abaixo para calcular o valor do serviço.")

# 1. ESCOLHA DO PRODUTO E PREÇO (No corpo principal para facilitar)
col_p1, col_p2 = st.columns([2, 1])

with col_p1:
    # Adicionamos a opção de escolher o produto
    produto = st.selectbox("Tipo de Produto", ["Adesivo", "Banner", "Lona", "Adesivo Perfurado", "Outro"])

with col_p2:
    # O preço continua sendo digitado por você, como você pediu
    preco_m2 = st.number_input("Preço do m² (R$)", min_value=0.0, value=80.0, step=5.0)

# 2. SEU LAYOUT ORIGINAL DE MEDIDAS
st.divider()
col1, col2 = st.columns(2)

with col1:
    unidade = st.selectbox("Unidade de medida", ["Milímetros (mm)", "Centímetros (cm)", "Metros (m)"])
    quantidade = st.number_input("Quantidade de adesivos", min_value=1, value=10, step=1)

with col2:
    largura = st.number_input(f"Largura ({unidade.split()[-1]})", min_value=0.01, value=10.0)
    altura = st.number_input(f"Altura ({unidade.split()[-1]})", min_value=0.01, value=10.0)

# 3. SUA LÓGICA DE CONVERSÃO ORIGINAL (Mantida 100%)
fator = 1
if "mm" in unidade:
    fator = 1000
elif "cm" in unidade:
    fator = 100

larg_m = largura / fator
alt_m = altura / fator

# 4. SEUS CÁLCULOS ORIGINAIS (Mantidos 100%)
area_unidade_m2 = larg_m * alt_m
area_total_m2 = area_unidade_m2 * quantidade
valor_total = area_total_m2 * preco_m2

# 5. EXIBIÇÃO DOS RESULTADOS (Mantida conforme sua última versão)
st.divider()
c1, c2 = st.columns(2)

c1.metric("Área Total do Pedido", f"{area_total_m2:.2f} m²")
c2.metric("Valor Total", f"R$ {valor_total:.2f}")

if st.button("Gerar Resumo para Copiar"):
    # AQUI MUDOU: Agora o nome do produto selecionado aparece no título
    texto_resumo = f"""
    📌 *ORÇAMENTO - {produto.upper()}*
    - Medida: {largura}x{altura} {unidade.split()[-1]}
    - Quantidade: {quantidade} un
    - *VALOR TOTAL: R$ {valor_total:.2f}*
    """
    st.code(texto_resumo, language="markdown")