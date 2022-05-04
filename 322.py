# BANK = ['Сбер', 'Тинькофф', 'Альфа']
#
#
# def task1():
#     n = int(input())
#     bank_nomer_schet = {}
#     for _ in range(n):
#         info = input()
#         info_split = info.split()
#         bank = info_split[0]
#         nomer = info_split[1]
#         if bank not in BANK:
#             continue
#         if len(nomer) != 11:
#             continue
#         if nomer[0] != '8':
#             continue
#         schet = int(info_split[3])
#         if info_split[2] == '-':
#             schet = schet * -1
#         if bank not in bank_nomer_schet:
#             bank_nomer_schet[bank] = {}
#         if nomer not in bank_nomer_schet[bank]:
#             bank_nomer_schet[bank][nomer] = 0
#         bank_nomer_schet[bank][nomer] += schet
#
#     for bank, nomer_schet in bank_nomer_schet.items():
#         for nomer, schet in nomer_schet.items():
#             # nomer = j[0]
#             # schet = j[1]
#             if schet < 0:
#                 print(f'{bank} {nomer} ЗАБЛОКИРОВАНО')
#             else:
#                 print(f'{bank} {nomer} {schet}')
#
#
# task1()
#

#
# a = {1: 1, 2: 2, 3: 3}
# print(a.get(4, 15))
# print(a)
# print(a.setdefault(4, 15))
# print(a)