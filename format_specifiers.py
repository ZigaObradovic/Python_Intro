# format specifiers = {value:flags} format a value based on what flags are inserted.

price1 = 3.12848
price2 = -958.258
price3 = 12002500.34
# FLAGS:
# za decimalna mesta: .()f - oklepaj je število decimalnih mest (1, 2, 3, 4,...), f pa predstavlja floating point number
# mesta, ki jih string zasede: () - oklepaj je število, string bo zasedel () mest kjer bodo prva (prazna) presledki
# za 0-le pred številom : 0() - oklepaj je število mest, ki jih bo string zasedel
# <() - zasede () mest in zapiše na levo
# >() - zasede () mest in zapiše na desno
# ^() - centrira
# + - bo pozitivnim vrednostim dodal +
# , - loči tisočice

print(f"Price 1 is {price1:.2f}€")
print(f"Price 2 is {price2:20}€")
print(f"Price 3 is {price3:010}€")
print(f"Price 1 is {price1:<10}€")
print(f"Price 2 is {price2:>10}€")
print(f"Price 3 is {price3:^10}€")
print(f"Price 1 is {price1:+}€")
print(f"Price 3 is {price3:,}€")
print(f"Price 1 is {price1:+,.2f}€") # flags lahko kombiniramo
