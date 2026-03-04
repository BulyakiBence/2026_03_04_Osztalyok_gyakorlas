from auto import Auto
import random
auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Audi", "E-Tron Gt", 2021)
auto4 = Auto("Ford", "Mustang", 2005)
auto5 = Auto("Ford", "Mustang", 2003)


# 3. gyorsitas
autok =  [auto1, auto2, auto3, auto4, auto5]
for auto in autok:
    print(auto)
print("Gyorsít\n")
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

# 4. atlageletkor
autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor
    
atlag_eletkor = ossz_eletkor / autok_szama   
print(f"AZ autók átlagéletkora: {atlag_eletkor}")

# 5. legoregebb auto
# A version: FAVÁGÓ
legidosebb_auto = None
legidosebb_auto_kora = 0


for auto in autok:
    kor = 2026-auto.gyartasi_ev
    if kor > legidosebb_auto_kora:
        legidosebb_auto_kora = kor
        legidosebb_auto = auto

print(f" a legidosebb autó kora: {legidosebb_auto_kora}, adatai: {legidosebb_auto}")     

# B version
autok_kora = []
for auto in autok:
    autok_kora.append(2026 - auto.gyartasi_ev)

legidosebb_auto_indexe= autok_kora.index(max(autok_kora))
print(f" A legidősebb autó kora: {legidosebb_auto_kora}, adati: {autok[legidosebb_auto_indexe]}")

# c version (legjobb)
gyartasi_evek = [auto.gyartasi_ev for auto in autok]
for auto in autok:
    if auto.gyartasi_ev == min(gyartasi_evek):
        print(f"A legidősebb autó adatai: {auto} ____ {2026 - auto.gyartasi_ev} éves")
        print(f"A legidősebb autó: {auto.marka} {auto.tipus}")


auto6 = Auto("BMW", "320d", 2019, 6.5)
print(auto6)
auto6.utazik(200)
print(auto6)
auto6.tankol(10)
print(auto6)