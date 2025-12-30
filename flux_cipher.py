import os

class FluxCipher:
    """
    FluxCipher-64: Gelişmiş Blok Şifreleme Algoritması.
    Mimari: İkame + Permütasyon + CBC Modu
    """
    def __init__(self, key):
        if isinstance(key, str):
            self.key = key.encode('utf-8')
        else:
            self.key = key
            
        if len(self.key) != 8:
            raise ValueError("HATA: Anahtar uzunluğu tam olarak 8 karakter (64 bit) olmalıdır!")

    def _rotate_left(self, val, r_bits, max_bits=8):
        return ((val << r_bits) % (2**max_bits)) | (val >> (max_bits - r_bits))

    def _rotate_right(self, val, r_bits, max_bits=8):
        return ((val >> r_bits) | (val << (max_bits - r_bits))) % (2**max_bits)

    def _sifrele_blok_cekirdek(self, blok_bytes):
        blok = list(blok_bytes)
        key = list(self.key)
        for tur in range(16):
            for i in range(8):
                blok[i] ^= key[i]
                blok[i] = (blok[i] + 42) % 256
                shift = (tur % 7) + 1
                blok[i] = self._rotate_left(blok[i], shift)
                if i < 7:
                    blok[i] ^= blok[i+1]
                else:
                    blok[i] ^= blok[0]
        return bytes(blok)

    def _coz_blok_cekirdek(self, blok_bytes):
        blok = list(blok_bytes)
        key = list(self.key)
        for tur in range(15, -1, -1):
            for i in range(7, -1, -1):
                if i < 7:
                    blok[i] ^= blok[i+1]
                else:
                    blok[i] ^= blok[0]
                shift = (tur % 7) + 1
                blok[i] = self._rotate_right(blok[i], shift)
                blok[i] = (blok[i] - 42) % 256
                blok[i] ^= key[i]
        return bytes(blok)

    def padding_ekle(self, metin):
        eksik = 8 - (len(metin) % 8)
        return metin + (chr(eksik) * eksik).encode('utf-8')

    def padding_cikar(self, metin):
        eksik = metin[-1]
        return metin[:-eksik]

    def sifrele(self, metin):
        ham_veri = self.padding_ekle(metin.encode('utf-8'))
        iv = os.urandom(8)
        sifreli_veri = iv
        onceki_blok = iv
        for i in range(0, len(ham_veri), 8):
            su_anki_blok = ham_veri[i : i+8]
            xorlanmis_blok = bytes([b ^ o for b, o in zip(su_anki_blok, onceki_blok)])
            sifreli_blok = self._sifrele_blok_cekirdek(xorlanmis_blok)
            sifreli_veri += sifreli_blok
            onceki_blok = sifreli_blok
        return sifreli_veri

    def sifre_coz(self, sifreli_veri):
        try:
            iv = sifreli_veri[:8]
            veri = sifreli_veri[8:]
            cozulmus_veri = b""
            onceki_blok = iv
            for i in range(0, len(veri), 8):
                su_anki_sifreli_blok = veri[i : i+8]
                ara_blok = self._coz_blok_cekirdek(su_anki_sifreli_blok)
                orijinal_blok = bytes([b ^ o for b, o in zip(ara_blok, onceki_blok)])
                cozulmus_veri += orijinal_blok
                onceki_blok = su_anki_sifreli_blok
            return self.padding_cikar(cozulmus_veri).decode('utf-8')
        except:
            return "Hata: Şifre çözülemedi!"

# Eğer yanlışlıkla bu dosyayı çalıştırırsan seni uyarsın diye bunu ekledim:
if __name__ == "__main__":
    print("❌ HATA: Bu dosyayı çalıştırma! 'run_test.py' dosyasını çalıştır.")