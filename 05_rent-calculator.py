def calcular_lucro(inv_inicial, dias_inv, retorno_inv):

  retorno_diario = retorno_inv / 100 / dias_inv

  lucro_diario = dias_inv * retorno_inv
  lucro_semanal = lucro_diario * 7
  lucro_mensal = lucro_diario * 30
  lucro_total = inv_inicial * ( 1 + retorno_inv / 100)


  print("Lucro diario: {:.2f}".format( lucro_diario))
  print("Lucro semanal: {:.2f}".format( lucro_semanal))
  print("Lucro mensal: {:.2f}".format( lucro_mensal))
  print("Lucro total: {:.2f}".format( lucro_total))


calcular_lucro(5000, 30, 5)