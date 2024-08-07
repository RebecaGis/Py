def maior_primo(num):
  def e_primo(numero):
  
    if numero <= 1:
      return False
    divisor = 2
    while divisor * divisor <= numero:
      if numero % divisor == 0:
        return False
      divisor += 1
    return True

  maior_primo_encontrado = 0
  numero = num
  while numero >= 2:
    if e_primo(numero):
      maior_primo_encontrado = numero
      break
    numero -= 1
  return maior_primo_encontrado
