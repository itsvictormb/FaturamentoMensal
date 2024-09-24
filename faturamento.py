import json


def calcular_faturamento():
    
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    
    valores = [item['valor'] for item in dados]
    
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    
    dias_com_faturamento = [valor for valor in valores if valor > 0]
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento) if dias_com_faturamento else 0
    
    
    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    print(f'Menor faturamento: {menor_faturamento}')
    print(f'Maior faturamento: {maior_faturamento}')
    print(f'Dias com faturamento acima da média mensal: {dias_acima_media}')


if __name__ == "__main__":
    calcular_faturamento()
