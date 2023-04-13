# APLIKASI KEDAI KOPI
Aplikasi penggajian ini adalah tugas dari mata kuliah PBO, dalam aplikasi ini user dapat memesan beberapa menu yang tersedia dan menentukan jumlah menu yang dipesan. Sistem akan melakukan perhitungan meliputi harga pesanan, diskon dan ppn sehingga akan ditotal menjadi harga yang harus dibayar.
## Penjelasan Program
##### Pembuatan Class Pelanggan :
kelas Pelanggan memiliki beberapa private object/ variable yang tidak boleh dipanggil selain di dalam kelas Pelanggan. Apabila object ingin dipanggil selain di dalam kelas Pelanggan, maka harus menggunakan fungsi yang dibuat untuk kebutuhan tersebut.
```sh
class Pesanan:

    def __init__(self, menu, jumlahPesanan):
        self.__menu          = menu
        self.__jumlahPesanan = jumlahPesanan
        self.__harga         = menu
        self.__ppn           = menu
        self.__diskon        = menu
        self.__totalHarga    = menu
```
Fungsi untuk menampilkan nama menu sesuai kode huruf yang diinputkan user.
Fungsi ini dibuat untuk menampilkan objek "menu" apabila ingin dipanggil di luar kelas Pelanggan.
```sh
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
```
Fungsi untuk menampilkan jumlah pesanan sesuai dengan angka yang diinputkan user.
Fungsi ini dibuat untuk menampilkan objek "jumlah pesanan" apabila ingin dipanggil di luar kelas Pelanggan.
```sh
def getJumlahPesanan (self) :

        return self.__jumlahPesanan
```
