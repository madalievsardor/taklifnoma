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

## Saytni yangilash

Fayl o'zgartirilgandan keyin:

```bash
git add -A && git commit -m "update" && git push
```

GitHub Pages 1-2 daqiqada avtomatik yangilaydi, havola o'zgarmaydi:
**https://madalievsardor.github.io/taklifnoma/**

## Boshqa bepul variantlar

- **Cloudflare Pages** — pages.cloudflare.com, GitHub repo'ni ulash kifoya
- **Netlify** — netlify.com, papkani drag&drop qilib ham chiqarish mumkin
- **Vercel** — vercel.com, repo'ni import qilish

`render.yaml` fayli render.com uchun qolgan (kerak bo'lsa ishlatiladi).
