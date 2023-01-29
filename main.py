from transaction import Transaction

def display_menu() -> None:
    print('-'*40)
    print('Menu Transaksi')
    print('-'*40)
    print('1. Add Item')
    print('2. Update Nama Item')
    print('3. Update Jumlah')
    print('4. Update Harga')
    print('5. Delete Item')
    print('6. Reset Transaction')
    print('7. Check Order')
    print('8. Display Transaction')
    print('9. Display Grand Total Harga')
    print('0. Keluar')

def add_item(trx: Transaction) -> None:
    try:
        item = input('Nama Item: ')
        qty = int(input('Jumlah: '))
        price = float(input('Harga per Item: '))
        
        trx.add_item(item, qty, price)
    except ValueError as e:
        print(e)

def update_item_name(trx: Transaction) -> None:
    try:
        id_item = input('ID Item: ')
        new_name = input('Nama Baru: ')

        trx.update_item(id_item=id_item, new_item=new_name)
    except ValueError as e:
        print(e)

def update_item_qty(trx: Transaction) -> None:
    try:
        id_item = input('ID Item: ')
        new_qty = int(input('Jumlah Baru: '))

        trx.update_qty(id_item=id_item, new_qty=new_qty)
    except ValueError as e:
        print(e)

def update_item_price(trx: Transaction) -> None:
    try:
        id_item = input('ID Item: ')
        new_price = float(input('Harga Baru: '))

        trx.update_price(id_item=id_item, new_price=new_price)
    except ValueError as e:
        print(e)

def delete_item(trx: Transaction) -> None:
    try:
        id_item = input('ID Item: ')
        trx.delete_item(id_item)
    except ValueError as e:
        print(e)

def reset_transaction(trx: Transaction) -> None:
    confirm = None
    while confirm not in ['y', 'n']:
        confirm = input('Apakah Anda yakin? [y/n]: ')
    
    if confirm == 'y':
        trx.reset_transaction()

def check_order(trx: Transaction) -> None:
    if trx.check_order():
        print('Transaksi valid!')
    else:
        print('Transaksi tidak valid!')


if __name__ == '__main__':

    trx = Transaction()
    opt = None

    print('='*40)
    print('Selamat Datang di Super Cashier')
    print('='*40)

    while opt != '0':
        print('')
        display_menu()
        opt = input('Pilih Task: ')
        print('')
        if opt == '1':
            add_item(trx)
        elif opt == '2':
            update_item_name(trx)
        elif opt == '3':
            update_item_qty(trx)
        elif opt == '4':
            update_item_price(trx)
        elif opt == '5':
            delete_item(trx)
        elif opt == '6':
            reset_transaction(trx)
        elif opt == '7':
            check_order(trx)
        elif opt == '8':
            trx.print_transaction()
        elif opt == '9':
            trx.total_price()
