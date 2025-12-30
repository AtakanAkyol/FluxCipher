from flux_cipher import FluxCipher
import time

def ekrana_bas(baslik):
    print("\n" + "="*60)
    print(f" {baslik}")
    print("="*60)

if __name__ == "__main__":
    ekrana_bas("FLUXCIPHER-64 GÜVENLİK TESTİ")
    
    # 1. Anahtar
    anahtar = "GizliAna" 
    cipher = FluxCipher(anahtar)
    print(f"🔑 Anahtar: {anahtar}")

    # 2. Şifreleme Testi
    orijinal_mesaj = "Bu cok gizli bir universite projesidir."
    print(f"\n[TEST 1] Temel Fonksiyonlar")
    print(f"📄 Orijinal: {orijinal_mesaj}")
    
    sifreli = cipher.sifrele(orijinal_mesaj)
    print(f"🔒 Şifreli (Hex): {sifreli.hex()}")
    
    cozulen = cipher.sifre_coz(sifreli)
    print(f"🔓 Çözülen: {cozulen}")
    
    if orijinal_mesaj == cozulen:
        print("✅ DURUM: BAŞARILI")

    # 3. Çığ Etkisi Testi
    ekrana_bas("TEST 2: ÇIĞ ETKİSİ (AVALANCHE EFFECT)")
    print("Senaryo: 'AAAAAAAA' vs 'AAAAAAAB' (1 bit fark)\n")
    
    girdi1 = "AAAAAAAA"
    girdi2 = "AAAAAAAB"
    
    c1 = cipher.sifrele(girdi1)
    c2 = cipher.sifrele(girdi2)
    
    # IV (ilk 8 byte) hariç kıyaslama
    c1_govde = c1[8:]
    c2_govde = c2[8:]
    
    farkli_bit = 0
    toplam_bit = len(c1_govde) * 8
    
    for b1, b2 in zip(c1_govde, c2_govde):
        farkli_bit += bin(b1 ^ b2).count('1')
        
    oran = (farkli_bit / toplam_bit) * 100
    
    print(f"Girdi 1 Şifreli: {c1_govde.hex()[:32]}...")
    print(f"Girdi 2 Şifreli: {c2_govde.hex()[:32]}...")
    print(f"\nDeğişim Oranı: %{oran:.2f}")
    
    if oran > 45:
        print("✅ SONUÇ: MÜKEMMEL ÇIĞ ETKİSİ! (Güvenli)")
    else:
        print("❌ SONUÇ: ZAYIF")
        
    input("\nÇıkmak için Enter'a basın...")