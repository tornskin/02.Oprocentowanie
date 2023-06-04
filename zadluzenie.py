'''
Stwórz program, który na podstawie

tabeli inflacji wartości
oprocentowania kredytu,
kwoty początkowej kredytu
stałej wartości raty
wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.

Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację) i kwota raty były pobierane ze standardowego wejścia (terminal).

Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.

Wyślij link do swojego repozytorium (nie spakowany kod). Repozytorium powinno zawierać więcej, niż jeden commit.
'''

Inflacja1 = 1.592824484
Inflacja2 = -0.453509101
Inflacja3 = 2.324671717
Inflacja4 = 1.261254407
Inflacja5 = 1.782526286
Inflacja6 = 2.329384541
Inflacja7 = 1.502229842
Inflacja8 = 1.782526286
Inflacja9 = 2.328848994
Inflacja10 = 0.616921348
Inflacja11 = 2.352295886
Inflacja12 = 0.337779545
Inflacja13 = 1.577035247
Inflacja14 = -0.292781443
Inflacja15 = 2.48619659
Inflacja16 = 0.267110318
Inflacja17 = 1.417952672
Inflacja18 = 1.054243267
Inflacja19 = 1.480520104
Inflacja20 = 1.577035247
Inflacja21 = -0.07742069
Inflacja22 = 1.165733399
Inflacja23 = -0.404186718
Inflacja24 = 1.499708521

loan_interest_rate = float(input("Podaj oprocentowanie kredytu: "))
loan_amount = float(input("Podaj kwotę kredytu: "))
installment_amount = float(input("Podaj wysokość raty: "))