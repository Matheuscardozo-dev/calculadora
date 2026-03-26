import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora Gráfica", page_icon="🖨️")

st.title("🖨️ Orçamento de Impressão")
st.markdown("Preencha os dados abaixo para calcular o valor do serviço.")

# 1. ESCOLHA DO PRODUTO E PREÇO
col_p1, col_p2 = st.columns([2, 1])

with col_p1:
    produto = st.selectbox("Tipo de Produto", ["Adesivo", "Banner", "Lona", "Adesivo Perfurado", "Outro"])

with col_p2:
    preco_m2 = st.number_input("Preço do m² (R$)", min_value=0.0, value=80.0, step=5.0)

# --- NOVIDADE: LÓGICA ESPECÍFICA PARA LONA ---
custo_extra = 0.0
info_extra_resumo = ""

if produto == "Lona":
    st.info("💡 Opções extras para Lona selecionadas")
    c_extra1, c_extra2 = st.columns(2)
    
    with c_extra1:
        # Checkbox para adicionar a madeira fixa de R$ 10
        add_madeira = st.checkbox("Adicionar acabamento em madeira (R$ 10,00)")
        if add_madeira:
            custo_extra += 10.0
            info_extra_resumo += "\n    - Acabamento: Madeira (R$ 10,00)"
            
    with c_extra2:
        # Campo para quantidade de ilhós a R$ 0,50 cada
        qtd_ilhos = st.number_input("Quantidade de Ilhós (R$ 0,50 un)", min_value=0, value=0, step=1)
        if qtd_ilhos > 0:
            valor_ilhos = qtd_ilhos * 0.50
            custo_extra += valor_ilhos
            info_extra_resumo += f"\n    - Ilhós: {qtd_ilhos} un (R$ {valor_ilhos:.2f})"

# 2. SEU LAYOUT ORIGINAL DE MEDIDAS
st.divider()
col1, col2 = st.columns(2)

with col1:
    unidade = st.selectbox("Unidade de medida", ["Milímetros (mm)", "Centímetros (cm)", "Metros (m)"])
    quantidade = st.number_input("Quantidade de itens", min_value=1, value=1, step=1)

with col2:
    largura = st.number_input(f"Largura ({unidade.split()[-1]})", min_value=0.01, value=10.0)
    altura = st.number_input(f"Altura ({unidade.split()[-1]})", min_value=0.01, value=10.0)

# 3. SUA LÓGICA DE CONVERSÃO E CÁLCULO
fator = 1000 if "mm" in unidade else 100 if "cm" in unidade else 1
larg_m, alt_m = largura / fator, altura / fator

area_total_m2 = (larg_m * alt_m) * quantidade
# O valor total agora soma o custo_extra (madeira + ilhós)
valor_total = (area_total_m2 * preco_m2) + custo_extra

# 4. EXIBIÇÃO DOS RESULTADOS
st.divider()
c1, c2 = st.columns(2)
c1.metric("Área Total do Pedido", f"{area_total_m2:.2f} m²")
c2.metric("Valor Total", f"R$ {valor_total:.2f}")

if st.button("Gerar Resumo para Copiar"):
    texto_resumo = f"""
    📌 *ORÇAMENTO - {produto.upper()}*
    - Medida: {largura}x{altura} {unidade.split()[-1]}
    - Quantidade: {quantidade} un{info_extra_resumo}
    - *VALOR TOTAL: R$ {valor_total:.2f}*
    """
    st.code(texto_resumo, language="markdown")