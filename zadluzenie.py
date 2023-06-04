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

print_formula = 'Twoja pozostała kwota kredytu to {loan_to_pay}, to {rate_diff} mniej niż w poprzednim miesiącu'

month_1 = (1 + ((Inflacja1+loan_interest_rate)/1200)) * loan_amount - installment_amount
month_2 = (1 + ((Inflacja2+loan_interest_rate)/1200)) * month_1 - installment_amount
month_3 = (1 + ((Inflacja3+loan_interest_rate)/1200)) * month_2 - installment_amount
month_4 = (1 + ((Inflacja4+loan_interest_rate)/1200)) * month_3 - installment_amount
month_5 = (1 + ((Inflacja5+loan_interest_rate)/1200)) * month_4 - installment_amount
month_6 = (1 + ((Inflacja6+loan_interest_rate)/1200)) * month_5 - installment_amount
month_7 = (1 + ((Inflacja7+loan_interest_rate)/1200)) * month_6 - installment_amount
month_8 = (1 + ((Inflacja8+loan_interest_rate)/1200)) * month_7 - installment_amount
month_9 = (1 + ((Inflacja9+loan_interest_rate)/1200)) * month_8 - installment_amount
month_10 = (1 + ((Inflacja10+loan_interest_rate)/1200)) * month_9 - installment_amount
month_11 = (1 + ((Inflacja11+loan_interest_rate)/1200)) * month_10 - installment_amount
month_12 = (1 + ((Inflacja12+loan_interest_rate)/1200)) * month_11 - installment_amount
month_13 = (1 + ((Inflacja13+loan_interest_rate)/1200)) * month_12 - installment_amount
month_14 = (1 + ((Inflacja14+loan_interest_rate)/1200)) * month_13 - installment_amount
month_15 = (1 + ((Inflacja15+loan_interest_rate)/1200)) * month_14 - installment_amount
month_16 = (1 + ((Inflacja16+loan_interest_rate)/1200)) * month_15 - installment_amount
month_17 = (1 + ((Inflacja17+loan_interest_rate)/1200)) * month_16 - installment_amount
month_18 = (1 + ((Inflacja18+loan_interest_rate)/1200)) * month_17 - installment_amount
month_19 = (1 + ((Inflacja19+loan_interest_rate)/1200)) * month_18 - installment_amount
month_20 = (1 + ((Inflacja20+loan_interest_rate)/1200)) * month_19 - installment_amount
month_21 = (1 + ((Inflacja21+loan_interest_rate)/1200)) * month_20 - installment_amount
month_22 = (1 + ((Inflacja22+loan_interest_rate)/1200)) * month_21 - installment_amount
month_23 = (1 + ((Inflacja23+loan_interest_rate)/1200)) * month_22 - installment_amount
month_24 = (1 + ((Inflacja24+loan_interest_rate)/1200)) * month_23 - installment_amount


print(print_formula.format(loan_to_pay=month_1, rate_diff=loan_amount - month_1))
print(print_formula.format(loan_to_pay=month_2, rate_diff=month_1 - month_2))
print(print_formula.format(loan_to_pay=month_3, rate_diff=month_2 - month_3))
print(print_formula.format(loan_to_pay=month_4, rate_diff=month_3 - month_4))
print(print_formula.format(loan_to_pay=month_5, rate_diff=month_4 - month_5))
print(print_formula.format(loan_to_pay=month_6, rate_diff=month_5 - month_6))
print(print_formula.format(loan_to_pay=month_7, rate_diff=month_6 - month_7))
print(print_formula.format(loan_to_pay=month_8, rate_diff=month_7 - month_8))
print(print_formula.format(loan_to_pay=month_9, rate_diff=month_8 - month_9))
print(print_formula.format(loan_to_pay=month_10, rate_diff=month_9 - month_10))
print(print_formula.format(loan_to_pay=month_11, rate_diff=month_10 - month_11))
print(print_formula.format(loan_to_pay=month_12, rate_diff=month_11 - month_12))
print(print_formula.format(loan_to_pay=month_13, rate_diff=month_12 - month_13))
print(print_formula.format(loan_to_pay=month_14, rate_diff=month_13 - month_14))
print(print_formula.format(loan_to_pay=month_15, rate_diff=month_14 - month_15))
print(print_formula.format(loan_to_pay=month_16, rate_diff=month_15 - month_16))
print(print_formula.format(loan_to_pay=month_17, rate_diff=month_16 - month_17))
print(print_formula.format(loan_to_pay=month_18, rate_diff=month_17 - month_18))
print(print_formula.format(loan_to_pay=month_19, rate_diff=month_18 - month_19))
print(print_formula.format(loan_to_pay=month_20, rate_diff=month_19 - month_20))
print(print_formula.format(loan_to_pay=month_21, rate_diff=month_20 - month_21))
print(print_formula.format(loan_to_pay=month_22, rate_diff=month_21 - month_22))
print(print_formula.format(loan_to_pay=month_23, rate_diff=month_22 - month_23))
print(print_formula.format(loan_to_pay=month_24, rate_diff=month_23 - month_24))

