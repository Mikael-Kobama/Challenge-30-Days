from scipy.optimize import minimize

# Função de buff total com base nas fórmulas descritas
def total_buff(vars):
    x, y = vars  # x = dano crítico do 3º, y = do 4º

    buff_3 = 0.16 * x + 20
    dc_4 = y + buff_3
    buff_4 = 0.132 * dc_4 + 26.4
    dc_2 = 200 + buff_3 + buff_4
    buff_2 = 0.3 * dc_2 + 12

    total_buff = buff_3 + buff_4 + buff_2
    return (total_buff - 244) ** 2  # queremos que o total seja 244

# Limites razoáveis para os valores
bounds = [(200, 300), (200, 350)]  # (x, y)

# Valores iniciais próximos dos originais
initial_guess = [206.1, 277.3]

# Otimização
result = minimize(total_buff, initial_guess, bounds=bounds)

# Resultado
x_opt, y_opt = result.x
print(f"Novo dano crítico necessário:")
print(f"3º personagem: {x_opt:.2f}%")
print(f"4º personagem: {y_opt:.2f}%")
