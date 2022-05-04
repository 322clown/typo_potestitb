BANK = ['Сбер', 'Тинькофф', 'Альфа']


def task1():
    n = int(input())
    bank_nomer_schet = {}
    for _ in range(n):
        info = input()
        info_split = info.split()
        bank = info_split[0]
        nomer = info_split[1]
        if bank not in BANK:
            continue
        if len(nomer) != 11:
            continue
        if nomer[0] != '8':
            continue
        schet = int(info_split[3])
        if info_split[2] == '-':
            schet = schet * -1
        bank_nomer_schet.setdefault(bank, {})
        bank_nomer_schet[bank].setdefault(nomer, 0)
        if bank_nomer_schet[bank][nomer] == 'ЗАБЛОКИРОВАНО':
            continue
        bank_nomer_schet[bank][nomer] += schet
        if bank_nomer_schet[bank][nomer] < 0:
            bank_nomer_schet[bank][nomer] = 'ЗАБЛОКИРОВАНО'
    for bank, nomer_schet in bank_nomer_schet.items():
        for nomer, schet in nomer_schet.items():
            print(f'{bank} {nomer} {schet}')


task1()



# a = {1: 1, 2: 2, 3: 3}
# print(a.get(4, 15))
# print(a)
# print(a.setdefault(4, 15))
# print(a)