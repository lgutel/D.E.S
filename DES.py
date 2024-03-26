from sympy import symbols, div, roots

# Définir les variables
x = symbols('x')

def algoEuclide(numérateur,dénominateur):

    # Convertir les expressions en polynômes
    numérateur = eval(numérateur)
    dénominateur = eval(dénominateur)

    # Effectuer la division polynomiale
    quotient, reste = div(numérateur, dénominateur)

    # Afficher le résultat
    print(f"f(x)=: {quotient} + ({reste}/{dénominateur})")
    return (dénominateur, reste)

def racine(dénominateur, reste):

    racine=roots(dénominateur)
    racine2=roots(reste)
    if racine2==racine:
        return False
    else:
        return True

def main():
    # Définir les polynômes
    numérateur = input("Entrez le numérateur (par exemple, 22*x**3 + 1) : ")
    dénominateur = input("Entrez le dénominateur (par exemple, 2*x**2 + 1) : ")

    dénominateur, reste = algoEuclide(numérateur,dénominateur)

    if racine(dénominateur, reste) == True:
        print("Fraction Irréductible")
    else:
        print("OSEF")

if __name__ == "__main__":
    main()