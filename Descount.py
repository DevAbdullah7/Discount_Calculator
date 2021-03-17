klint = int(input('Price After Descount 1: \nPersent of Descount 2: \n: '))
try:
  if klint == 1:
    try:
      Descount = int(input('Enter persent of Descount: '))
      price = int(input('Enter price: '))
      if 0 <= Descount <= 100 and price > 0:
        after_descount = price - (price * Descount / 100)
        print('\npersent of descount: '+str(Descount)+'%')
        print('price befour descount: '+str(price))
        print('price after descount: '+str(after_descount))
      else:
        raise Exception('\nError: Thr persent of descount or price is incorrect!')
    except Exception as Error:
      print(Error)
  elif klint == 2:
    try:
      price = int(input('Enter price befour descount: '))
      price2 = int(input('Enter price after descount: '))
      if price > 0 and price2 > 0:
        Descount = int((price - price2) * 100 / price)
        print('\npersent of descount: '+str(Descount)+'%')
        print('price befour descount: '+str(price))
        print('price after descount: '+str(price2))
      else:
        raise Exception('\nError: The price is incorrect!')
    except Exception as Error:
      print(Error)
  else:
    raise Exception('Error: Your choice is incorrect!')
except Exception as Error:
  print(Error)
