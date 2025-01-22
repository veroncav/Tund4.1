# def summa3(arv1:int, arv2: int, arv3: int) -> int:
#    """Tagastab kolme taisarvu summa


#    :param int arv1: Esineme number
#    :param int arv2: Teine number
#    :param int arv3: Kolmas number
#    :rtype: int

#     """
#     summa=arv1+arv2+arv3
#     return summa

from re import A, I


def arithmetic(a:float, b:float, f:str) -> any:
    """Lihtne kalkulaator.
    +- liitmine
    -- lahutamine
    *- korrutamine
    /- jagamine
    :param float a:arv1
    :param float b: arv2
    :param str t: arifmeetiline tehing
    :rtype:var Maaramata tuup (float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
           vastus="DIV/0"
         else:
             vastus=eval(str(a)+t+str(b))
    else:
            vastus="Tundmatu tehe"
   return vastus


#U2

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine 
    tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus


    """
    if aasta%4==0
      v=True
      else:
                  v=False
                  return v





#U3

def square(a:float)->any
"""
"""
S=A**2
P=4*A
d=(2)**(1/2)*2
return S,P,d

def square_text(a:float)->str:
    """
    """
S=A**2
P=4*A
d=(2)**(1/2)*2
return "Pindala\n"+str(S)+",Umbermoot\n"+str(P)+",Labimoot\n"+str(d)

#U4

def season(month: int) -> str:
    """Määrab aastaaja vastavalt kuu numbrile.

    :param int month: kuu number (1 kuni 12)
    :rtype: str
    """
    if 1 <= month <= 2 or month == 12:
        return "talv"
    elif 3 <= month <= 5:
        return "kevad"
    elif 6 <= month <= 8:
        return "suvi"
    elif 9 <= month <= 11:
        return "sügis"
    else:
        return "Tundmatu kuu"


    #U5

def bank(a: float, years: int) -> float:
    """
    """
    for i in range(years):
        a *= 1*1
    return a

#U6

def is_prime(n: int) -> bool:
    """Kontrollib, kas arv on algarv.

    :param int n: arv (0 kuni 1000)
    :rtype: bool
    """
    print(a)
    v=True i in range(2,a):
        if a%i==0
        v=False
  


#U7

def date(day: int, month: int, year: int) -> bool:
    """Kontrollib, kas kuupäev on kalendris olemas.

    :param int day: päev
    :param int month: kuu
    :param int year: aasta
    :rtype: bool
    """
    from datetime import datetime
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

    #U8
    def XOR_cipher(s: str, key: int) -> str:
        """Sone kodeerimine ASCII votiga 0-255
        """
        kodeeritud=""
        for symbol in text:
            kodeeritud+=chr(ord(symbol)^key)
        return kodeeritud