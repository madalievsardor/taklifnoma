# -*- coding: utf-8 -*-
"""Bitta shablondan ikkita taklifnoma yasaydi: nahor/ va kechki/

Ishga tushirish:  python3 src/build.py
"""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASEURL = "https://madalievsardor.github.io/taklifnoma"

COMMON = {
    "DATE":  "21-avgust, juma",
    "PHOTO": "photo.jpg",   # har papkada o'z nusxasi bor (Vercel root directory uchun)
    "BASEURL": BASEURL,
}

PAGES = {
    "nahor": {
        "TITLE":  "Dinora va Doston — nahor oshi taklifnomasi",
        "OGDESC": "21-avgust, soat 06:00. «Baxt uyi» to'yxonasi, Bekobod shahri.",
        "LABEL":  "Nahor oshi",
        "TIME":   "06:00",
        "NOTE":   "Ertalabki nahor oshimizga marhamat qiling.",
        "INTRO1": "Sizni nikoh to'yimiz munosabati bilan beriladigan nahor oshimizga lutfan taklif qilamiz.",
        "INTRO2": "Duo va oq fotihalaringiz biz uchun eng qimmatli sovg'adir.",
        "VENUE":  "«Baxt uyi» to'yxonasi",
        "ADDR":   "Toshkent viloyati, Bekobod shahri",
        "MAP":    "https://yandex.uz/maps/?ll=69.260247%2C40.222797&z=17&l=map&pt=69.260247%2C40.222797%2Cpm2rdm",
        "BG":     "#F7F2EC",
        "PAPER":  "#FCF9F5",
        "ACCENT": "#BE9C6E",
    },
    "kechki": {
        "TITLE":  "Dinora va Doston — to'y taklifnomasi",
        "OGDESC": "21-avgust, soat 18:00. «Ziyoda» banket zali, Bekobod shahri.",
        "LABEL":  "To'y dasturxoni",
        "TIME":   "18:00",
        "NOTE":   "Bayramona ziyofatimizda siz bilan birga bo'lishni orzu qilamiz.",
        "INTRO1": "Sizni nikoh to'yimiz munosabati bilan tashkil etilayotgan quvonchli tantanamizga lutfan taklif qilamiz.",
        "INTRO2": "Hayotimizdagi eng baxtli kunda samimiy tilaklaringizni eshitish biz uchun beqiyos qadrlidir.",
        "VENUE":  "«Ziyoda» banket zali",
        "ADDR":   "Bekobod shahri, 14-daha",
        "MAP":    "https://yandex.uz/maps/-/CTg6AE28",
        "BG":     "#F5EFEC",
        "PAPER":  "#FBF7F5",
        "ACCENT": "#AC8781",
    },
}

tpl = io.open(os.path.join(ROOT, "src", "template.html"), encoding="utf-8").read()

for slug, data in PAGES.items():
    out = tpl
    for k, v in dict(COMMON, **data).items():
        out = out.replace("{{%s}}" % k, v)
    assert "{{" not in out, "to'ldirilmagan joy qoldi: " + slug
    d = os.path.join(ROOT, slug)
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(out)
    print("yasaldi: %s/index.html" % slug)
