a=float(input("Enter the Primcipal:"))
b=float(input("Enter the Rate:"))
c=float(input("Enter the Time:"))
CI=a*((1+b/100)**c)-a
print("The compound interest with",a,"principal",b,"percentage rate",c,"years time is:",CI) #