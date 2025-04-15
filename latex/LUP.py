#Filip Šrámek - semestrální projekt do numerické lineární algebry

#LUP ROZKLAD

#rozkládá matici A na součin tří matic L, U, P
#soušitem techto matic dostaneme matici A
#A = P * L * U

#P je matice permutací (Uchovává v sobě pořadí řádků) 
#L je dolní trojúhelníková matice 
#U je horní trojúhelníková matice
print("LUP rozklad matice A na součin L, U a P")
import numpy as np

#funkce pro LUP rozklad s částečnou pivotizací
def LUP(A):
    n = A.shape[0]
    L = np.eye(n)  # Inicializace matice L jako jednotková matice
    U = A          # Inicializace matice U jako kopie matice A
    P = np.eye(n)  # Inicializace matice P jako jednotková matice

    for k in range(n):
        # Částečná pivotizace
        pivot_index = np.argmax(np.abs(U[k:n, k]))              #najede největší hodnotu ze: skoupce k od řádku k dolů
        pivot_index = pivot_index + k                           #přičte číslo soupce do indexu
                                                                #v případě, že největší prvěk je na hlavní diagonále je pivot_index = k

        if pivot_index != k:                                    #pokud je pivot_index jiný než k, provedeme výměnu řádků
                                                                #Tahle situace nastane když je nejvěětší pravek mimo hlavní diagonálu

           
            U[[k, pivot_index], :] = U[[pivot_index, k], :]     #Vymění řádek o indexu "k" s řádkem o indexu "pivot_index" 


            P[[k, pivot_index], :] = P[[pivot_index, k], :]     #Provedu stejnou výměnu i pto jednotkovou patici P, abych si uložil pořadí řádků
            

            L[[k, pivot_index], :k] = L[[pivot_index, k], :k]   #Vymění řádek o indexu "k" s řádkem o indexu "pivot_index"

        
        # Klasický LU rozklad
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U


#------------------------------------Kód pro ověření funkčnosti------------------------------------

A = np.random.rand(4, 4)  # Náhodná matice 4x4
print("Matice A:\n", A)

P, L, U = LUP(A)
B = P @ L @ U

print("Matice L:\n", L)
print("Matice U:\n", U)
print("Matice P:\n", P)
print("Součin L, U a P:\n", B)