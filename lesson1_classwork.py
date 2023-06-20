# def str_count(string):        - O(n^2)
#     for symbol in string:
#         counter = 0# def str_count(string):
#     for symbol in set(string):
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, "-", counter)


# def str_count(string):      - O(n*m)
#     for symbol in set(string):
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, "-", counter)

# str_count("absa")

def str_count(string):  
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)
str_count('askftaosdgifisgfijwegbknflsdbligsildgfliseglkjhdg')