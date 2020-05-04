Feature: Sanity
	Scenario: Order barang 
		Given buka browser baru dan login ke cicil
		When checkout barang di contoh homepage
		Then barang berhasil checkout dan tampil di halaman pesanan saya