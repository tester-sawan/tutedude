# Since tuple is non-mutable in nature, we cannot modify any element but we can do by changing the type from tuple to list.
month_name = ("jan","feb","march","april","may","jun","july","aug","sept","oct","nov","dec")
print(type(month_name))
month_name=list(month_name)
print(type(month_name))
month_name[0]="Sawan"
print(month_name)
month_name=tuple(month_name)
print(type(month_name))
print(month_name)

# Join two or more tuple - Use the + operator to join multiple tuple.
# Repeat the tuple - Use the * operator to multiply the tuple.