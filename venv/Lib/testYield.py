def getName():
    print("This is before yield")
    yield "Mahendra"
    print("This is After Yield Statement")


print("This is calling getname with yeild",getName())