# Calcula o acréscimo a partir dos juros e os juros a partir do acréscimo
# Versões
# 0.1 24/08/2023 Primeiros métodos e propriedades, para testes
# 0.2 25/08/2023 Cálculos e testes com prints
import Juros

juros = Juros.Juros(3, True, 30)
juros.setpagamentos(",", "0,30,60")
juros.setpesos(",", "2,1,1")

print(juros.Quantidade)
print(juros.Composto)
print(juros.Periodo)
print(juros.Pagamentos[0])
print(juros.Pagamentos[1])
print(juros.Pagamentos[2])
print(juros.Pesos[0])
print(juros.Pesos[1])
print(juros.Pesos[2])
print(juros.getpesototal())
print(juros.jurosparaacrescimo(2))
print(juros.acrescimoparajuros(juros.jurosparaacrescimo(2), 18))
