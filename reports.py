import pandas as pd
import matplotlib.pyplot as plt


def transactions_to_dataframe(account):
    """Hesabın işlem geçmişini (liste) bir pandas DataFrame'e çevirir."""
    df = pd.DataFrame(account.transactions)
    return df


def show_transaction_summary(account):
    """Hesabın işlemlerine dair pandas ile özet tablo yazdırır."""
    df = transactions_to_dataframe(account)

    if df.empty:
        print(f"{account.owner_name} adlı hesapta henüz işlem yok.")
        return

    print(f"\n--- {account.owner_name} - İşlem Özeti ---")
    print(df)

    print("\nİşlem türüne göre toplam tutar:")
    # groupby -> pandas konusu
    print(df.groupby("tur")["tutar"].sum())


def plot_balance_history(account, output_path="bakiye_grafigi.png"):
    """Hesabın bakiye geçmişini çizgi grafik olarak kaydeder."""
    df = transactions_to_dataframe(account)

    if df.empty:
        print("Grafik çizilecek işlem bulunamadı.")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(df) + 1), df["bakiye"], marker="o", color="tab:blue")
    plt.title(f"{account.owner_name} - Bakiye Değişimi")
    plt.xlabel("İşlem Sırası")
    plt.ylabel("Bakiye (TL)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()import pandas as pd
import matplotlib.pyplot as plt


def transactions_to_dataframe(account):
    """Hesabın işlem geçmişini (liste) bir pandas DataFrame'e çevirir."""
    df = pd.DataFrame(account.transactions)
    return df


def show_transaction_summary(account):
    """Hesabın işlemlerine dair pandas ile özet tablo yazdırır."""
    df = transactions_to_dataframe(account)

    if df.empty:
        print(f"{account.owner_name} adlı hesapta henüz işlem yok.")
        return

    print(f"\n--- {account.owner_name} - İşlem Özeti ---")
    print(df)

    print("\nİşlem türüne göre toplam tutar:")
    # groupby -> pandas konusu
    print(df.groupby("tur")["tutar"].sum())


def plot_balance_history(account, output_path="bakiye_grafigi.png"):
    """Hesabın bakiye geçmişini çizgi grafik olarak kaydeder."""
    df = transactions_to_dataframe(account)

    if df.empty:
        print("Grafik çizilecek işlem bulunamadı.")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(df) + 1), df["bakiye"], marker="o", color="tab:blue")
    plt.title(f"{account.owner_name} - Bakiye Değişimi")
    plt.xlabel("İşlem Sırası")
    plt.ylabel("Bakiye (TL)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Grafik kaydedildi: {output_path}")


def plot_all_balances(bank, output_path="tum_hesaplar.png"):
    """Bankadaki tüm hesapların bakiyelerini bar grafikte gösterir."""
    if len(bank.accounts) == 0:
        print("Grafik çizilecek hesap bulunamadı.")
        return

    # pandas ile hesap bilgilerini tablo haline getiriyoruz
    veriler = []
    for account in bank.accounts.values():
        veriler.append({"isim": account.owner_name, "bakiye": account.balance})

    df = pd.DataFrame(veriler)

    plt.figure(figsize=(8, 5))
    plt.bar(df["isim"], df["bakiye"], color="tab:green")
    plt.title(f"{bank.name} - Hesap Bakiyeleri")
    plt.xlabel("Hesap Sahibi")
    plt.ylabel("Bakiye (TL)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Grafik kaydedildi: {output_path}")
    print(f"Grafik kaydedildi: {output_path}")


def plot_all_balances(bank, output_path="tum_hesaplar.png"):
    """Bankadaki tüm hesapların bakiyelerini bar grafikte gösterir."""
    if len(bank.accounts) == 0:
        print("Grafik çizilecek hesap bulunamadı.")
        return

    # pandas ile hesap bilgilerini tablo haline getiriyoruz
    veriler = []
    for account in bank.accounts.values():
        veriler.append({"isim": account.owner_name, "bakiye": account.balance})

    df = pd.DataFrame(veriler)

    plt.figure(figsize=(8, 5))
    plt.bar(df["isim"], df["bakiye"], color="tab:green")
    plt.title(f"{bank.name} - Hesap Bakiyeleri")
    plt.xlabel("Hesap Sahibi")
    plt.ylabel("Bakiye (TL)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Grafik kaydedildi: {output_path}")
