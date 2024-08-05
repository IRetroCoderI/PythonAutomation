
sections = {'top-L': 'a', 'top-M': 'b', 'top-R': 'c',
            'mid-L': 'd', 'mid-M': 'e', 'mid-R': 'f',
            'low-L': 'g', 'low-M': 'h', 'low-R': 'i'}


def print_board():
    print(f'{sections["top-L"]} | {sections['top-M']} | {sections['top-R']}')
    print(f'--+---+--')
    print(f'{sections["mid-L"]} | {sections['mid-M']} | {sections['mid-R']}')
    print(f'--+---+--')
    print(f'{sections["low-L"]} | {sections['low-M']} | {sections['low-R']}')
    

active = True

while(active):
    

