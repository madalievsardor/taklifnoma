# Dinora va Doston — to'y taklifnomasi

Bitta HTML fayl. Hech qanday build, kutubxona yoki rasm fayli kerak emas —
barcha illustratsiyalar (gulchambar, saroy, dasturxon, nikoh arkasi) SVG bilan
kod ichida chizilgan. Faqat shriftlar Google Fonts'dan yuklanadi.

## Nimalarni o'zgartirish mumkin

`index.html` faylining oxiridagi `CONFIG` blokini oching:

```js
const CONFIG = {
  bride:      "Dinora",
  groom:      "Doston",
  eventISO:   "2026-08-21T06:00:00+05:00",  // countdown shunga qarab sanaydi
  venueName:  "To'yxona nomi",              // to'yxona nomi
  venueAddr:  "Toshkent shahri",            // ko'cha, uy manzili
  mapUrl:     "",                           // Google Maps havolasi (bo'sh = tugma yashirin)
  music:      ""                            // ixtiyoriy mp3 havolasi (bo'sh = tugma yashirin)
};
```

Marosim vaqtlari (06:00 va 18:00) va tavsif matnlari `index.html` ichidagi
`<!-- DASTUR -->` bo'limida, oddiy HTML sifatida yozilgan.

## Lokal ko'rish

```bash
open index.html
```

## render.com'ga chiqarish

1. Papkani GitHub'ga push qiling:
   ```bash
   git init && git add -A && git commit -m "wedding invitation"
   git branch -M main
   git remote add origin git@github.com:<user>/dinora-doston-taklifnoma.git
   git push -u origin main
   ```
2. render.com → **New +** → **Static Site** → repozitoriyni tanlang.
3. Sozlamalar:
   - **Build Command:** bo'sh qoldiring
   - **Publish Directory:** `.`
4. **Create Static Site** → 1-2 daqiqada havola tayyor:
   `https://dinora-doston-taklifnoma.onrender.com`

`render.yaml` fayli allaqachon shu sozlamalarni o'z ichiga oladi, shuning uchun
Blueprint orqali ham chiqarish mumkin.
