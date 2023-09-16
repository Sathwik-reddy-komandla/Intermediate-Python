
# **************************************************************
A=type('A',(),{'fields':['a']})

x=A()

print(x.fields)
print(x)

B=type('B',(A,),{'new_fields':['b','c']})

x=B()

print(x.fields)
print(x.new_fields)
print(x)
print(getattr(B,'fields'))
print(getattr(A,'fields'))
print(getattr(x,'new_fields'))


# **************************************************************

