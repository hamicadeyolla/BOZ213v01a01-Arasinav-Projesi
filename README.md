#  Tic-Tac-Toe (XOX) Oyunu - Python Projesi

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Course](https://img.shields.io/badge/Ders-BOZ213-green)
![Status](https://img.shields.io/badge/Durum-Tamamlandı-success)

Bu proje, **Ankara Üniversitesi BOZ213** dersi vize ödevi kapsamında geliştirilmiş, konsol tabanlı bir Tic-Tac-Toe (XOX) oyunudur.

##  Proje Hakkında

Bu uygulama, kullanıcının bilgisayara karşı oynadığı klasik Tic-Tac-Toe oyununun Python ile implementasyonudur. Oyun, standart kurallara sadık kalmakla birlikte, proje gereksinimleri doğrultusunda özelleştirilmiş bir senaryoya sahiptir.

**Senaryo Gereği:**
* **Bilgisayar (X):** Oyuna her zaman başlar ve ilk hamlesini daima tahtanın tam ortasına (5 numaralı kare) yapar. Sonraki hamleleri rastgeledir.
* **Kullanıcı (O):** 1-9 arasındaki numaraları tuşlayarak hamle yapar.

##  Özellikler

* **Dinamik Tahta Görünümü:** Oyun tahtası her hamleden sonra güncellenerek ekrana basılır.
* **Hata Yönetimi (Input Validation):** Kullanıcının geçersiz hamle yapması (harf girmesi, dolu kareyi seçmesi veya 1-9 dışına çıkması) engellenir.
* **Oyun Durumu Kontrolü:** Her hamleden sonra kazanma, kaybetme veya beraberlik durumları otomatik olarak hesaplanır.
* **Modüler Yapı:** Kod, okunabilirliği artırmak için fonksiyonel parçalara bölünmüştür.

## 🛠️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/hamicadeyolla/BOZ213v01a01-Arasinav-Projesi.git](https://github.com/hamicadeyolla/BOZ213v01a01-Arasinav-Projesi.git)
    ```
2.  **Proje Dizinine Girin:**
    ```bash
    cd BOZ213v01a01-Arasinav-Projesi
    ```
3.  **Oyunu Başlatın:**
    ```bash
    python "tic tac toe.py"
    ```

##  Kod Yapısı ve Fonksiyonlar

Proje içerisinde kullanılan temel fonksiyonların görevleri aşağıdadır:

| Fonksiyon | Açıklama |
| :--- | :--- |
| `display_board(board)` | Oyun tahtasının güncel durumunu konsola formatlı bir şekilde çizer. |
| `enter_move(board)` | Kullanıcıdan hamle alır ve bu hamlenin geçerliliğini (boş kare mi, sayı mı vb.) denetler. |
| `make_list_of_free_fields(board)` | Tahtadaki boş kareleri tarar ve bir liste olarak döndürür. Beraberlik kontrolü ve yapay zeka hamlesi için kullanılır. |
| `victory_for(board, sign)` | Yatay, dikey ve çapraz düzlemleri tarayarak oyunu kazanan tarafı belirler. |
| `draw_move(board)` | Bilgisayarın boş karelerden rastgele birini seçerek hamle yapmasını sağlar. |

## 📷 Örnek Oyun Görüntüsü

```text
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Hazırlayan
Ad Soyad: Hamza Osman Erdoğan
 Bölüm: Bilgisayar ve Öğretim Teknolojileri Öğretmenliği
Ders: BOZ213 - Nesne Tabanlı Programlama

Bu proje BOZ213 dersi ara sınav ödevi olarak hazırlanmıştır.
