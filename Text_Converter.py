from functools import lru_cache
from string import ascii_uppercase,digits,ascii_lowercase
from math import pi
class Encode:
    def __init__(self):
        self.full=ascii_lowercase+digits+ascii_uppercase+"!@#$%^&*()<>?|}{"
    @lru_cache(maxsize=5)
    def TextToBinary(self,text):
        """
        :param text (str):
        :return binary (str) :
        """
        try:
            b=""
            textbin = []
            for i in text:
                # print(f"{i}:{ord(i)}:{bin(ord(i))}")
                textbin.append(bin(ord(i))[2:])
            for j in textbin:
                b += j + " "
            return b
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def TextToDecimal(self, text):
        """
        :param text (str):
        :return decimal (str):
        """
        try:
            dec = ""
            for i in text:
                dec += str(ord(i)) + " "
            return dec
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def TextToHex(self, tex):
        """
        :param tex:
        :return:
        """
        try:
            declis = self.TextToDecimal(tex)
            h = self.DecimalToHex(declis)
            return h
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def TextToOctal(self, texxx):
        """
        :param octaa:
        :return:
        """
        try:
            textodec = self.TextToDecimal(texxx)
            o = self.DecimalToOctal(textodec)
            return o
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def TextToCeasar(self,ceasar):
        rotation_text=self.rotate()
        plane_text=""
        try:
            for i in ceasar:
                if i in rotation_text and i in self.full:
                    r_pos=rotation_text.find(i)
                    plane_text+=self.full[r_pos]
                else:
                    plane_text+=" "
            return plane_text
        except Exception as e:
            print(e)

    @lru_cache(maxsize=5)
    def BinaryToText(self,binary):
        """
        :param binary (str):
        :return text (str):
        """
        try:
            t=""
            BinToTexLis=binary.split()
            for i in BinToTexLis:
                t+=chr(int(i,2))
            return t
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def BinaryToDecimal(self, byn):
        """
        :param byn (str):
        :return :
        """
        try:
            d = ""
            bynlis = byn.split()
            for i in bynlis:
                d += str(int(i, 2)) + " "
            return d
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def BinaryToHex(self, binn):
        """
        :param binn:
        :return:
        """
        try:
            btod = self.BinaryToDecimal(binn)
            h = self.DecimalToHex(btod)
            return h
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def BinaryToOctal(self, binn):
        """
                                :param octaa:
                                :return:
        """
        try:
            bintodec = self.BinaryToDecimal(binn)
            o = self.DecimalToOctal(bintodec)
            return o
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def BinaryToCeasar(self, binn):
        try:
            b=self.BinaryToText(binn)
            t=self.TextToCeasar(b)
            return t
        except Exception as e:
            print(e)


    @lru_cache(maxsize=5)
    def DecimalToText(self,dec):
        """
        :param dec (str):
        :return text (str):
        """
        t=""
        declis=dec.split()
        try:
            for i in declis:
               t+=chr(int(i))
            return t
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def DecimalToBinary(self,dec):
        """
        :param dec (str):
        :return binary (str):
        """
        try:
            b=""
            declis=dec.split()
            for i in declis:
                b+=str(bin(int(i))[2:])+" "
            return b
        except TabError as e:
            print(e)
    @lru_cache(maxsize=5)
    def DecimalToHex(self,decs):
        """
        :param decs:
        :return:
        """
        decls=decs.split()
        h=""
        try:
            for i in decls:
                h+=str(hex(int(i)).split('x')[-1])+" "
            return h
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def DecimalToOctal(self, decs):
        """
        :param decs:
        :return:
        """
        try:
            o = ""
            decslis = decs.split()
            for i in decslis:
                o += str(oct(int(i))).split("o")[-1] + " "
            return o
        except Exception as e:
            print(e)

    @lru_cache(maxsize=5)
    def HexToDecimal(self,hexx):
        """
        :param hexx:
        :return:
        """
        try:
            d=""
            hexxlis=hexx.split()
            for i in hexxlis:
               d+=str(int(i,16))+" "
            return d
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def HexToText(self,hexxx):
        """
        :param hexxx:
        :return:
        """
        try:
            htod=self.HexToDecimal(hexxx)
            t=self.DecimalToText(htod)
            return t
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def HexToBinary(self,hexxx):
        """
        :param hexxx:
        :return:
        """
        try:
            htod=self.HexToDecimal(hexxx)
            b=self.DecimalToBinary(htod)
            return b
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def HexToOctal(self, hexxx):
        """
                :param octaa:
                :return:
                """
        try:
            hexatdec = self.HexToDecimal(hexxx)
            o = self.DecimalToOctal(hexatdec)
            return o
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def HexToCeasar(self, hexxx):
        """
                :param octaa:
                :return:
                """
        try:
            hexattex = self.HexToText(hexxx)
            c = self.TextToCeasar(hexattex)
            return c
        except Exception as e:
            print(e)


    @lru_cache(maxsize=5)
    def OctalToDecimal(self,octa):
        """
        :param otca:
        :return:
        """
        try:
            d=""
            octa_lis=octa.split()
            for i in octa_lis:
               d+=str(int(i,8))+" "
            return d
        except Exception :
            print("Octal Number is Incorrect")
    @lru_cache(maxsize=5)
    def OctalToText(self,octaa):
        """
        :param octaa:
        :return:
        """
        try:
            octatod=self.OctalToDecimal(octaa)
            t=self.DecimalToText(octatod)
            return t
        except Exception:
            print("Octal Number is not correct")
    @lru_cache(maxsize=5)
    def OctalToBinary(self,octaa):
        """
        :param octaa:
        :return:
        """
        try:
            octatodec=self.OctalToDecimal(octaa)
            b=self.DecimalToBinary(octatodec)
            return b
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def OctalToHex(self,octaa):
        """
                :param octaa:
                :return:
                """
        try:
            octatodec = self.OctalToDecimal(octaa)
            h = self.DecimalToHex(octatodec)
            return h
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def OctalToCeasar(self,octaa):
        try:
            c=self.OctalToText(octaa)
            return c
        except Exception as e:
            print(e)

    @lru_cache(maxsize=5)
    def rotate(self,rotation_level=4.3):
        half=int(len(self.full)/rotation_level)
        return self.full[half:]+self.full[:-half]

    @lru_cache(maxsize=5)
    def CeasarToText(self,tex):
        rotation_text=self.rotate()
        ceasar_text=""
        try:
            for i in tex:
                if i not in self.full:
                    ceasar_text+=" "
                elif i in self.full:
                    i_pos=self.full.find(i)
                    ceasar_text+=rotation_text[i_pos]
            return ceasar_text
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def CeasarToBinary(self,ceasar):
        """
        """
        try:
            b=self.TextToBinary(ceasar)
            return b
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def CeasarToHex(self,ceasar):
        """"""
        try:
            h=self.TextToHex(ceasar)
            return h
        except Exception as e:
            print(e)
    @lru_cache(maxsize=5)
    def CeasarToOctal(self,ceasar):
        try:
            o=self.TextToOctal(ceasar)
            return o
        except Exception as e:
            print(e)

# class Constant:
#     def __init__(self):
#         self.Pi=pi
#         self.Gravity=9.8 # N
#         self.Avogedro=6.0221409e+23
#         self.atm=101325 # Pa
#         self.Proton_Mass=1.6726219e-27 # Kg
#         self.Electron_Mass=9.10938356e-31 # Kg
#         self.Neutron_Mass=1.674929e-27 # Kg
#         self.Atomic_Mass_Unit=1.660540e-27 # Kg
