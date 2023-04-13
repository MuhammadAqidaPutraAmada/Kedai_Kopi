class Pesanan:

    def __init__(self, menu, jumlahPesanan):
        self.__menu          = menu
        self.__jumlahPesanan = jumlahPesanan
        self.__harga         = menu
        self.__ppn           = menu
        self.__diskon        = menu
        self.__totalHarga    = menu
    
    def getMenu (self) :

        if self.__menu == "A" :
            self.__menu = "ES Kopi Susu"

        elif self.__menu == "B" :
            self.__menu = "ES Kopi Coklat"
        
        elif self.__menu == "C" :
            self.__menu = "ES Kopi Hitam"
        
        elif self.__menu == "D" :
            self.__menu = "Ice Americano"

        return self.__menu
    
    def getJumlahPesanan (self) :

        return self.__jumlahPesanan
    
    def getHarga (self) :

        if self.__harga == "A" :
            self.__harga = 11000 * self.__jumlahPesanan
        
        elif self.__harga == "B" :
            self.__harga = 12000 * self.__jumlahPesanan
        
        elif self.__harga == "C" :
            self.__harga = 11000 * self.__jumlahPesanan
        
        elif self.__harga == "D" :
            self.__harga = 14000 * self.__jumlahPesanan
      
        return self.__harga
    
    def getPPN (self) :

        if self.__ppn == "A" :
            self.__ppn = int((11000 * self.__jumlahPesanan) * 0.1)

        elif self.__ppn == "B" :
            self.__ppn = int((12000 * self.__jumlahPesanan) * 0.1)

        elif self.__ppn == "C" :
            self.__ppn = int((11000 * self.__jumlahPesanan) * 0.1)

        elif self.__ppn == "D" :
            self.__ppn = int((14000 * self.__jumlahPesanan) * 0.1)

        return self.__ppn
    
    def getDiskon (self) :

        if self.__jumlahPesanan >= 5 :

            if self.__diskon == "A":
                self.__diskon = int((11000*self.__jumlahPesanan) * 0.2)

            elif self.__diskon == "B":
                self.__diskon = int((12000*self.__jumlahPesanan) * 0.2)

            elif self.__diskon == "C":
                self.__diskon = int((11000*self.__jumlahPesanan) * 0)

            elif self.__diskon == "D":
                self.__diskon = int((14000*self.__jumlahPesanan) * 0)

        else :
            self.__diskon = 0

        return self.__diskon
    
    def getTotalHarga (self) :

        if self.__totalHarga == "A" :
            __hargaPesanan  = (11000 * self.__jumlahPesanan)

            if self.__jumlahPesanan >= 5 :
                __diskonPesanan = ((11000*self.__jumlahPesanan) * 0.2)
            else :
                __diskonPesanan = 0

            __ppnPesanan    =((11000 * self.__jumlahPesanan) * 0.1)


        elif self.__totalHarga == "B" :
            __hargaPesanan  = (12000 * self.__jumlahPesanan)

            if self.__jumlahPesanan >= 5 :
                __diskonPesanan = ((12000*self.__jumlahPesanan) * 0.2)
            else :
                __diskonPesanan = 0

            __ppnPesanan    =((12000 * self.__jumlahPesanan) * 0.1)


        elif self.__totalHarga == "C" :
            __hargaPesanan  = (11000 * self.__jumlahPesanan)

            if self.__jumlahPesanan >= 5 :
                __diskonPesanan = ((11000*self.__jumlahPesanan) * 0)
            else :
                __diskonPesanan = 0

            __ppnPesanan    =((11000 * self.__jumlahPesanan) * 0.1)


        elif self.__totalHarga == "D" :
            __hargaPesanan  = (14000 * self.__jumlahPesanan)

            if self.__jumlahPesanan >= 5 :
                __diskonPesanan = ((14000*self.__jumlahPesanan) * 0)
            else :
                __diskonPesanan = 0

            __ppnPesanan    =((14000 * self.__jumlahPesanan) * 0.1)


        self.__totalHarga = int((__hargaPesanan - __diskonPesanan) + __ppnPesanan)

        return self.__totalHarga

class Laporan:

    def __init__(self):

        self.__dataPesanan = []
    
    def addPesanan (self, data) :

        self.__dataPesanan.append(data)
    
    def hapusPesanan (self, data) :

        self.__dataPesanan.remove(data)
    
    def tampilkanMenu (self) :

        print("""
    ==============================
    
    Ananda Coffe
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    \n
    """)
    
    def tampilkanPesanan (self) :

        for data in self.__dataPesanan:

            print("--------------------------")
            print("Ananda Coffe")
            print("--------------------------")

            menu   = print (f"Menu         : {data.getMenu()}")
            jumlah = print (f"Jumlah Pesan : {data.getJumlahPesanan()} cup")
            harga  = print (f"Harga        : {data.getHarga()} K")
            ppn    = print (f"PPN          : {data.getPPN()} K")
            diskon = print (f"Diskon       : {data.getDiskon()} K")

            print("--------------------------")
            ttl    = print (f"Jumlah Bayar : {data.getTotalHarga()}K")
            print("--------------------------")

        return menu, jumlah, harga, ppn, diskon ,ttl



lup = "Y"
while lup == "Y" :
    a = Laporan ()
    a.tampilkanMenu ()

    inputMenu = input ("Masukan Menu: ")
    while inputMenu != "A" and inputMenu != "B" and inputMenu != "C" and inputMenu != "D" :
        print ("Menu tidak terdaftar")
        inputMenu = input ("Masukan Menu: ")
    
    inputJumlah = int(input ("Masukan jumlah: "))
    
    Memesan = Pesanan(inputMenu,inputJumlah)
    a.addPesanan(Memesan)
    a.tampilkanPesanan()
    
    lup = input ("Apakah ingin melakukan pemesanan lainnya? (Y/T)")
