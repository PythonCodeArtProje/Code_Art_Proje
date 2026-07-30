from bank import Bank
from reports import show_transaction_summary, plot_balance_history, plot_all_balances


def menu_goster():
   
    print("\n===== BANKA CONSOLE UYGULAMASI=====")
    print("1. Hesap Oluştur")
    print("2. Para Yatır")
    print("3. Para Çek")
    print("4. Para Transfer Et")
    print("5. Tüm Hesapları Listele")
    print("6. Hesap İşlem Özeti ")
    print("7. Hesap Bakiye Grafiği")
    print("8. Tüm Hesapların Bakiye Grafiği ")
    print("9. Çıkış")


def sayi_al(mesaj):
    """Kullanıcıdan geçerli bir sayı alana kadar tekrar soran fonksiyon."""
    while True:
        deger = input(mesaj)
        try:
            return float(deger)
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


def main():
    banka = Bank("Python Bankası")
    calisiyor = True  

    while calisiyor:
        menu_goster()
        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("Hesap sahibinin adı: ")
            baslangic_bakiye = sayi_al("Başlangıç bakiyesi: ")
            hesap = banka.create_account(isim, baslangic_bakiye)
            print(f"Hesap oluşturuldu -> {hesap}")

        elif secim == "2":
            hesap_no = int(sayi_al("Hesap numarası: "))
            tutar = sayi_al("Yatırılacak tutar: ")
            try:
                banka.deposit(hesap_no, tutar)
                print("Para yatırma işlemi başarılı.")
            except ValueError as hata:
                print(f"Hata: {hata}")

        elif secim == "3":
            hesap_no = int(sayi_al("Hesap numarası: "))
            tutar = sayi_al("Çekilecek tutar: ")
            try:
                banka.withdraw(hesap_no, tutar)
                print("Para çekme işlemi başarılı.")
            except ValueError as hata:
                print(f"Hata: {hata}")

        elif secim == "4":
            gonderen = int(sayi_al("Gönderen hesap numarası: "))
            alici = int(sayi_al("Alıcı hesap numarası: "))
            tutar = sayi_al("Transfer tutarı: ")
            try:
                banka.transfer(gonderen, alici, tutar)
                print("Transfer başarılı.")
            except ValueError as hata:
                print(f"Hata: {hata}")

        elif secim == "5":
            banka.list_accounts()
            print(f"Toplam Bakiye: {banka.total_balance():.2f} TL")

        elif secim == "6":
            hesap_no = int(sayi_al("Hesap numarası: "))
            hesap = banka.get_account(hesap_no)
            if hesap is None:
                print("Hesap bulunamadı.")
            else:
                show_transaction_summary(hesap)

        elif secim == "7":
            hesap_no = int(sayi_al("Hesap numarası: "))
            hesap = banka.get_account(hesap_no)
            if hesap is None:
                print("Hesap bulunamadı.")
            else:
                plot_balance_history(hesap)

        elif secim == "8":
            plot_all_balances(banka)

        elif secim == "9":
            calisiyor = False
            print("Uygulamadan çıkılıyor. Hoşça kalın!")

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()

