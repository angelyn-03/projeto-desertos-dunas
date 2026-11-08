# script.py
# Aluna: Evelyn Kauany Lemes da Silva
# Tema: Zonas Desérticas e Camadas de Areia (Uniformes e Dunas)

def carregar_camada_satelite(lista_altitudes):
    """
    Simula o carregamento de camadas de satélite (LoD) com base na altitude.
    """
    print("--- Iniciando Simulação de Voo e Renderização (Tema: Desertos e Dunas) ---\n")
    
    for altitude in lista_altitudes:
        print(f"Altitude atual da câmera: {altitude} metros")
        
        if altitude > 10000:
            # Altitude > 10.000m
            print(">> Nível de Detalhe: BAIXA RESOLUÇÃO")
            print("   [Renderizando] Mosaico geral da Terra: Visualização macro das grandes faixas climáticas áridas e continentes.\n")
            
        elif 1000 <= altitude <= 10000:
            # Altitude entre 1.000m e 10.000m
            print(">> Nível de Detalhe: MÉDIA RESOLUÇÃO")
            print("   [Renderizando] Mosaico regional: Mapeamento de campos de dunas contínuos, padrões de ventos e áreas de areia uniforme.\n")
            
        else:
            # Altitude < 1000m
            print(">> Nível de Detalhe: ALTA RESOLUÇÃO")
            print("   [Renderizando] Detalhes finos: Textura da areia, cristas das dunas, sombras projetadas pelo relevo e pequenas formações rochosas (yardangs).\n")

# Simulando a aproximação da câmera com uma lista de 6 altitudes
minhas_altitudes = [15000, 8500, 5000, 1200, 800, 150]
carregar_camada_satelite(minhas_altitudes)
