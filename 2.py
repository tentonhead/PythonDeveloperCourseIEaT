# TODO Найдите количество книг, которое можно разместить на дискете
#bytes4rune    = 4
BYTES_IN_RUNE = 4
RUNES_IN_LINE = 25
LINES_IN_PAGE = 50
PAGES_IN_BOOK = 100
BOOK_WEIGHT = BYTES_IN_RUNE * RUNES_IN_LINE\
              * LINES_IN_PAGE * PAGES_IN_BOOK
DISK_SPACE = 1.44 * 1024 * 1024
books_on_disk = int(DISK_SPACE/BOOK_WEIGHT)
print("Количество книг, помещающихся на дискету:", books_on_disk)
