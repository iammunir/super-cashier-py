'''

'''
import uuid
import pandas as pd
from tabulate import tabulate

class Transaction():

    def __init__(self) -> None:
        self.trx = dict()
        self.is_valid = False

    def add_item(self, name: str, qty: int, price: float) -> None:
        '''Fungsi untuk menambahkan item baru ke dalam transaksi.
        name (str) = nama item yang dibeli
        qty (int) = jumlah item yang dibeli
        price (float) = harga per item'''

        err_message = []
        if type(name) != str:
            err_message.append('Item harus bertipe string')
        if type(qty) != int:
            err_message.append('Qty harus bertipe integer')
        if type(price) != float and type(price) != int:
            err_message.append('Price harus bertipe float atau integer')
        
        if len(err_message) > 0:
            print("\n".join(err_message))
            return

        new_id = uuid.uuid4().hex
        id_item = new_id[:5]
        new_item = {
            id_item: [id_item, name, qty, price, qty*price]
        }
        self.trx.update(new_item)

    def delete_item(self, id_item: str) -> None:
        '''Fungsi untuk menghapus data nama item beserta jumlah dan harganya dari transaksi.
        id_item (str) = id item yang ingin dihapus'''

        err_message = []
        if type(id_item) != str:
            err_message.append('ID harus bertipe string')
        
        if len(err_message) > 0:
            print("\n".join(err_message))
            return

        if id_item not in self.trx:
            print('ID tidak ditemukan dalam daftar belanja Anda')
            return

        self.trx.pop(id_item)
        print(f'Item dengan id {id_item} berhasil dihapus')

    def clear_transaction(self) -> None:
        '''Fungsi untuk menghapus semua data pesanan dalam transaksi.'''
        
        self.trx.clear()
        print('Daftar transaksi berhasil direset')

    def update_name(self, id_item: str, new_name: str) -> None:
        '''Fungsi untuk mengubah nama item yang sudah diinput ke dalam transaksi.
        id_item (str) = id item yang namanya ingin diganti
        new_name (str) = nama baru untuk item yang diganti'''
        
        err_message = []
        if type(new_name) != str:
            err_message.append('Item harus bertipe string')
        if type(id_item) != str:
            err_message.append('ID harus bertipe string')
        
        if len(err_message) > 0:
            print("\n".join(err_message))
            return

        if id_item not in self.trx:
            print('ID tidak ditemukan dalam daftar belanja Anda')
            return

        self.trx[id_item][1] = new_name
        print(f'Nama item dengan id {id_item} berhasil diupdate')

    def update_qty(self, id_item: str, new_qty: int) -> None:
        '''Fungsi untuk mengubah jumlah item yang sudah diinput ke dalam transaksi.
        id_item (str) = id item yang jumlahnya ingin diganti
        new_qty (int) = jumlah baru untuk item yang diganti'''

        err_message = []
        if type(new_qty) != int:
            err_message.append('Qty harus bertipe integer')
        if type(id_item) != str:
            err_message.append('ID harus bertipe string')
        
        if len(err_message) > 0:
            print("\n".join(err_message))
            return

        if id_item not in self.trx:
            print('ID tidak ditemukan dalam daftar belanja Anda')
            return

        self.trx[id_item][2] = new_qty
        self.trx[id_item][4] = new_qty * self.trx[id_item][3]
        print(f'Jumlah item dengan id {id_item} berhasil diupdate')

    def update_price(self, id_item: str, new_price: float) -> None:
        '''Fungsi untuk mengubah harga per item yang sudah diinput ke dalam transaksi.
        id_item (str) = id item yang harganya ingin diganti
        new_price (float) = harga baru untuk item yang diganti'''

        err_message = []
        if type(new_price) != float and type(new_price) != int:
            err_message.append('Price harus bertipe float atau integer')
        if type(id_item) != str:
            err_message.append('ID harus bertipe string')
        
        if len(err_message) > 0:
            print("\n".join(err_message))
            return

        if id_item not in self.trx:
            print('ID tidak ditemukan dalam daftar belanja Anda')
            return

        self.trx[id_item][3] = new_price
        self.trx[id_item][4] = self.trx[id_item][2] * new_price
        print(f'Harga item dengan id {id_item} berhasil diupdate')
    
    def print_transaction(self) -> None:
        '''Fungsi untuk menampilkan semua pesanan dalam transaksi.'''

        if len(self.trx) <= 0:
            print('Anda belum mempunyai daftar item di dalam transaksi.')
            return

        trx_table = pd.DataFrame(self.trx).T
        headers = ["ID", "Nama Item", "Qty", "Harga", "Total Harga"]
        print(tabulate(trx_table, headers, tablefmt="github", showindex=False))
    
    def check_order(self) -> bool:
        '''Fungsi untuk cek validitas dan menampilkan pesan kesalahan jika terdapat data yang tidak valid.'''

        if len(self.trx) <= 0:
            print('Anda belum mempunyai daftar item di dalam transaksi.')
            return
        
        err_message = []
        for id, item in self.trx.items():
            if len(item[1]) <= 0:
                err_message.append(f'Nama item dengan ID {id} tidak valid')
            if item[2] <= 0:
                err_message.append(f'Jumlah item dengan ID {id} tidak valid')
            if item[3] <= 0:
                err_message.append(f'Harga item dengan ID {id} tidak valid')
            
        if len(err_message) > 0:
            self.is_valid = False
            print("\n".join(err_message))
        else:
            self.is_valid = True

        return self.is_valid

    def total_price(self) -> None:
        '''Fungsi untuk menampilkan total belanja.'''

        # memeriksa apakah ada item di dalam transaksi
        if len(self.trx) <= 0:
            print('Anda belum mempunyai daftar item di dalam transaksi.')
            return

        # memastikan pesanan sudah valid
        if not self.check_order():
            print('Transaksi tidak valid, silahkan diupdate terlebih dahulu')
            return
        
        # menghitung total transaksi
        grand_total = 0
        for item in self.trx.values():
            grand_total += item[4]
        
        # menghitung diskon
        if grand_total > 500_000:
            discount = float(grand_total * 0.1) # 10%
            grand_total = float(grand_total - discount)
            print(f"Anda mendapatkan diskon 10% sebesar Rp {discount:,}. Total belanja Anda adalah Rp {grand_total:,}.")
        
        elif grand_total>300_000:
            discount = int(grand_total*0.08) # 8%
            grand_total = int(grand_total-discount)
            print(f"Anda mendapatkan diskon 8% sebesar Rp {discount:,}. Total belanja Anda adalah Rp {grand_total:,}.")
        
        elif grand_total>200_000:
            discount = int(grand_total*0.05) # 5%
            grand_total = int(grand_total-discount)
            print(f"Anda mendapatkan diskon 5% sebesar Rp {discount:,}. Total belanja Anda adalah Rp {grand_total:,}.")
        
        else:
            print(f"Total belanja Anda adalah Rp {grand_total:,}.")