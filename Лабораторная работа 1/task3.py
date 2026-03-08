# TODO Найдите количество книг, которое можно разместить на дискете
disk_mb = 1.44
pages = 100
lines = 50
symbols = 25
bytes = 4

disk_bytes = disk_mb * 1024 * 1024

total_symbols = pages * lines * symbols

book_bytes = total_symbols * bytes

nomber_books = int(disk_bytes // book_bytes)

print("Количество книг, помещающихся на дискету:", nomber_books)
