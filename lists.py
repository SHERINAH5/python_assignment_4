#syntax
#list[]
#tuple()
 
products=['pen','pencil','book']
colors=('red','green','pink')
#add rubber to the pdts list, use append
products.append('rubber')
print(products)
#add ruler at the second position, use insert
products.insert(1,'ruler')
print(products)
#display the length of each product in the list
print(len(products))
#add purple to the color tuple
new_colors=list(colors)# convert tuple to a list
print(type(new_colors))
print(new_colors)
new_colors.append('purple')
print(new_colors)
colors=(tuple(new_colors))
print(colors)



