from random import randrange

# ------------------------------------------------------------
# 1. Tahta oluşturma fonksiyonu
# ------------------------------------------------------------
def create_board():
    """
    Oyunun başlangıcında 1'den 9'a kadar numaralı karelerden oluşan
    3x3 bir tahta (liste içinde liste) oluşturur.
    Örnek: [['1','2','3'], ['4','5','6'], ['7','8','9']]
    """
    return [[str(3 * r + c + 1) for c in range(3)] for r in range(3)]


# ------------------------------------------------------------
# 2. Tahtayı ekrana bastıran fonksiyon
# ------------------------------------------------------------
def print_board(board):
    """
    Tahtayı örnek formatta ekrana bastırır.
    Dikey ve yatay çizgiler hizalı olacak şekilde ASCII olarak çizilir.
    """
    line_sep = "+-------+-------+-------+"
    for r in range(3):
        print(line_sep)
        print("|       |       |       |")
        # Her hücre 7 karakter genişliğinde ortalanır
        print("|  {}  |  {}  |  {}  |".format(
            board[r][0].center(3),
            board[r][1].center(3),
            board[r][2].center(3)
        ))
        print("|       |       |       |")
    print(line_sep)


# ------------------------------------------------------------
# 3. Pozisyonu (1..9) dizi indekslerine çevirme
# ------------------------------------------------------------
def pos_to_indices(pos):
    """
    Kullanıcının girdiği 1-9 pozisyonunu (satır, sütun) çiftine dönüştürür.
    Örnek: 1 -> (0,0), 5 -> (1,1), 9 -> (2,2)
    """
    pos = int(pos)
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    return row, col


# ------------------------------------------------------------
# 4. Hücrenin boş olup olmadığını kontrol etme
# ------------------------------------------------------------
def is_cell_free(board, pos):
    """Verilen pozisyondaki hücre 'X' veya 'O' değilse boştur."""
    row, col = pos_to_indices(pos)
    return board[row][col] not in ('X', 'O')


# ------------------------------------------------------------
# 5. Tahtaya hamle yerleştirme
# ------------------------------------------------------------
def place_move(board, pos, mark):
    """Belirtilen pozisyona ('X' veya 'O') işaret yerleştirir."""
    row, col = pos_to_indices(pos)
    board[row][col] = mark


# ------------------------------------------------------------
# 6. Boş hücrelerin listesini döndürme
# ------------------------------------------------------------
def available_positions(board):
    """Tahtadaki tüm boş (rakam içeren) karelerin numaralarını döndürür."""
    avail = []
    for r in range(3):
        for c in range(3):
            val = board[r][c]
            if val not in ('X', 'O'):
                avail.append(int(val))
    return avail


# ------------------------------------------------------------
# 7. Kazananı kontrol etme
# ------------------------------------------------------------
def check_winner(board):
    """
    Kazanan olup olmadığını kontrol eder.
    'X' veya 'O' döndürür, yoksa None döndürür.
    """
    lines = []

    # Satırlar
    for r in range(3):
        lines.append([board[r][0], board[r][1], board[r][2]])

    # Sütunlar
    for c in range(3):
        lines.append([board[0][c], board[1][c], board[2][c]])

    # Çaprazlar
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    # Kazanan var mı?
    for line in lines:
        if line[0] == line[1] == line[2]:
            if line[0] in ('X', 'O'):
                return line[0]
    return None


# ------------------------------------------------------------
# 8. Tahta tamamen dolu mu?
# ------------------------------------------------------------
def is_full(board):
    """Tahtadaki tüm kareler doluysa True döndürür."""
    return all(board[r][c] in ('X', 'O') for r in range(3) for c in range(3))


# ------------------------------------------------------------
# 9. Bilgisayarın rastgele hamlesi
# ------------------------------------------------------------
def computer_move(board):
    """
    Bilgisayar rastgele bir boş kare seçer ve 'X' koyar.
    randrange() fonksiyonu ile rastgele seçim yapılır.
    """
    avail = available_positions(board)
    if not avail:
        return
    idx = randrange(len(avail))  # 0 .. len(avail)-1 arası rastgele index
    pos = avail[idx]
    place_move(board, pos, 'X')


# ------------------------------------------------------------
# 10. Kullanıcıdan hamle alma
# ------------------------------------------------------------
def player_input(board):
    """
    Kullanıcıdan geçerli bir hamle alır.
    - 1 ile 9 arasında olmalı
    - Dolu kare seçilmemeli
    - Hatalı girişlerde tekrar sorar
    """
    while True:
        try:
            s = input("Hamleni yap: ").strip()
            pos = int(s)
            if pos < 1 or pos > 9:
                print("Lütfen 1 ile 9 arasında bir sayı gir.")
                continue
            if not is_cell_free(board, pos):
                print("Bu kare dolu, başka bir kare seç.")
                continue
            return pos
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")


# ------------------------------------------------------------
# 11. Ana oyun döngüsü
# ------------------------------------------------------------
def main():
    # Başlangıçta 3x3 tahta oluşturulur
    board = create_board()

    # Bilgisayar ilk hamlesini her zaman ortadan yapar (pozisyon 5)
    place_move(board, 5, 'X')

    # İlk tahta görünümü
    print_board(board)

    # Oyun ana döngüsü
    while True:
        # --- Kullanıcı hamlesi ---
        pos = player_input(board)
        place_move(board, pos, 'O')
        print_board(board)

        # Kullanıcı kazandı mı?
        winner = check_winner(board)
        if winner == 'O':
            print("Kazandın!")
            break
        if is_full(board):
            print("Berabere!")
            break

        # --- Bilgisayar hamlesi ---
        computer_move(board)
        print_board(board)

        # Bilgisayar kazandı mı?
        winner = check_winner(board)
        if winner == 'X':
            print("Bilgisayar kazandı!")
            break
        if is_full(board):
            print("Berabere!")
            break


# ------------------------------------------------------------
# Program doğrudan çalıştırıldığında main() başlar
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
