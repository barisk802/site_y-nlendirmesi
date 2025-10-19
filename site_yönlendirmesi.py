import webbrowser

print("""
Site Yönlendirme

İşlemler:

1-İnstagram'a Gitmek İçin

2-Twitter'a Gitmek için

3-Youtube'a Gitmek İçin

Programdan Çıkmak için 'q'ya basınız.
""")

while True:
    işlem=input("Lütfen yapmak istediğiniz işlemi seçiniz :")

    if işlem=="q":
        print("Tekrar Bekleriz")
        break
    elif işlem=="1":
        print("İnstagrama Yönlendiriliyorsunuz...")
        webbrowser.open("https://www.instagram.com/bariskaya_1912/")
    elif işlem=="2":
        print("Twitter'a Yönlendiriliyorsunuz...")
        webbrowser.open("https://x.com/Bariskaya_1907")
    elif işlem=="3":
        print("Youtube'a Yönlendiriliyorsunuz...")
        webbrowser.open("https://www.youtube.com/@bariskaya1907")
    else:
        print("Geçersiz İşlem.")

