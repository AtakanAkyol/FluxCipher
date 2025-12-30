# 🔐 FluxCipher-64: Gelişmiş Blok Şifreleme Algoritması

Bu proje, **Bilgi Sistemleri Güvenliği** dersi kapsamında geliştirilmiş, 64-bit blok boyutuna ve 64-bit anahtar uzunluğuna sahip simetrik bir şifreleme algoritmasıdır.

## 🚀 Proje Hakkında

FluxCipher-64, modern kriptografinin temel taşları olan **Karıştırma (Confusion)** ve **Yayılma (Diffusion)** ilkelerini en üst düzeyde uygulamak için tasarlanmıştır. Algoritma, özellikle frekans analizine ve desen takibi saldırılarına karşı dirençli olacak şekilde 16 turluk bir yapı üzerine kurulmuştur.

### 🛠 Teknik Özellikler
* **Algoritma Tipi:** Blok Şifre (Block Cipher)
* **Çalışma Modu:** CBC (Cipher Block Chaining) - Zincirleme Blok Modu
* **Blok Boyutu:** 64-bit (8 Byte)
* **Anahtar Boyutu:** 64-bit
* **Tur Sayısı (Rounds):** 16

## 🛡️ Güvenlik Mimarisi

Algoritma her blok üzerinde sırasıyla şu işlemleri uygular:

1.  **XOR İşlemi:** Anahtar ile temel karıştırma.
2.  **Modüler Aritmetik (+42):** Doğrusal olmayan değişim (Non-linearity) sağlayarak matematiksel analizi zorlaştırır.
3.  **Dairesel Kaydırma (Bitwise Rotation):** Bitlerin yerini değiştirerek Yayılma (Diffusion) sağlar.
4.  **Permütasyon:** Blok içindeki byte'ların birbirini etkilemesini sağlar.

> **Güvenlik Kanıtı:** Yapılan "Çığ Etkisi" (Avalanche Effect) testlerinde, girdideki tek bir bitlik değişimin, şifreli metinde **%50 civarında** bir değişime yol açtığı kanıtlanmıştır.

## 💻 Kurulum ve Çalıştırma

Proje standart Python kütüphanelerini kullanır, harici kurulum gerektirmez.

1. Projeyi indirin:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/FluxCipher-Project.git](https://github.com/KULLANICI_ADIN/FluxCipher-Project.git)
   cd FluxCipher-Project
