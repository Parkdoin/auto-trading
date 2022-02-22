import pyupbit

access = "VRaakqxCgfDhsoyTHDShAC1lLWJZE3ncxUxgPNBC"          # 본인 값으로 변경
secret = "cacu3q5uj8EoTxrAxwfXKUy0iuziduI8RQybeyTp"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회


