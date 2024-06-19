import requests


data = [
    {
        "nama_produk": "Biji Jagung Hibrida",
        "deskripsi": "Biji jagung hibrida unggulan yang dirancang untuk memberikan hasil panen maksimal dengan kualitas biji yang superior. Cocok untuk berbagai kondisi tanah dan iklim, produk ini merupakan solusi terbaik bagi para petani yang menginginkan produktivitas tinggi dan ketahanan terhadap berbagai penyakit tanaman.",
        "harga": 30000,
        "gambar": "https://benihcitraasia.co.id/assets/images/kemasan/aeeb038754fc3e6d3df0acfd70ccbc61.webp"
    },
    {
        "nama_produk": "Pupuk Organik Cair",
        "deskripsi": "Pupuk Organik Cair adalah solusi ramah lingkungan untuk meningkatkan kesuburan tanah dan kesehatan tanaman. Mengandung nutrisi lengkap dan mikroorganisme aktif, pupuk ini mempercepat pertumbuhan dan hasil panen yang optimal. Mudah diaplikasikan, cocok untuk semua jenis tanaman dan metode pertanian.",
        "harga": 50000,
        "gambar": "https://image1ws.indotrading.com/s3/productimages/webp/co241031/p895160/w425-h425/894bd79f-8397-46a3-8ab5-47931e30d2a7.png"
    },
    {
        "nama_produk": "Alat Semprot Hama",
        "deskripsi": "Alat semprot hama yang efisien dan mudah digunakan",
        "harga": 75000,
        "gambar": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//92/MTA-10316368/plasindo_alat_semprot_hama_sprayer_16_liter_sp-16_full01_h9xbjifq.jpg"
    },
    {
        "nama_produk": "Bibit Padi Unggul",
        "deskripsi": "Alat Semprot Hama adalah solusi efisien dan andal untuk perlindungan tanaman. Dengan kapasitas besar dan nozzle yang dapat disesuaikan, alat ini memastikan penyemprotan merata dan efektif. Dirancang ergonomis, memudahkan petani dalam mengendalikan hama dan menjaga kesehatan tanaman.",
        "harga": 45000,
        "gambar": "https://img.id.my-best.com/product_images/9aa07a752a76e764fdbba61db535b26f.png?ixlib=rails-4.3.1&q=70&lossless=0&w=800&h=800&fit=clip&s=9c4bb1d5843b62858399624311c1e624"
    },
    {
        "nama_produk": "Traktor Mini",
        "deskripsi": "Traktor mini ini adalah solusi ideal untuk petani dengan lahan terbatas. Dengan desain kompak dan mesin bertenaga, traktor ini memudahkan pengolahan tanah, penanaman, dan pemeliharaan tanaman. Dilengkapi dengan fitur kemudi yang mudah dan konsumsi bahan bakar yang efisien, traktor mini ini memastikan produktivitas tinggi dan pengoperasian yang ekonomis.",
        "harga": 1500000,
        "gambar": "https://ae01.alicdn.com/kf/H292570715467454abaccb6ca875690e7S/Traktor-Mini-25HP-Traktor-Kebun-Kebun-Pembudidaya-Mesin-Diesel-Rotary-Kemudi.jpg"
    },
    {
        "nama_produk": "Pestisida Nabati",
        "deskripsi": "Pestisida nabati ini adalah solusi alami untuk mengendalikan hama pada tanaman. Dibuat dari bahan-bahan organik, pestisida ini aman bagi lingkungan dan tidak meninggalkan residu berbahaya. Efektif melawan berbagai jenis hama, produk ini menjaga kesehatan tanaman tanpa mengganggu keseimbangan ekosistem. Ideal untuk pertanian berkelanjutan dan ramah lingkungan.",
        "harga": 60000,
        "gambar": "https://images.tokopedia.net/img/cache/700/VqbcmM/2021/12/30/3ae85fc2-59bb-4720-bf1d-ded12935d644.jpg"
    },
    {
        "nama_produk": "Pompa Air Pertanian",
        "deskripsi": "Pompa air pertanian ini adalah alat andal untuk mengalirkan air ke lahan pertanian Anda. Dengan kapasitas tinggi dan efisiensi energi, pompa ini memastikan irigasi yang optimal bahkan di lahan luas. Didesain tahan lama dan mudah dioperasikan, alat ini membantu petani meningkatkan produktivitas dan menjaga kelembaban tanah secara konsisten.",
        "harga": 1200000,
        "gambar": "https://orient.co.id/cdn/shop/products/HONDA-WB-20-XN-2-INCH-POMPA-AIR-IRIGASI-BENSIN_1.jpg?v=1631247829"
    },
    {
        "nama_produk": "Sistem Irigasi Tetes",
        "deskripsi": "Sistem irigasi tetes ini adalah solusi cerdas untuk pengelolaan air yang efisien di lahan pertanian. Dengan teknologi tetes yang presisi, sistem ini menghemat air hingga 50% dan memastikan distribusi air langsung ke akar tanaman. Mudah dipasang dan dirawat, sistem irigasi tetes ini meningkatkan hasil panen dan mendukung pertanian berkelanjutan.",
        "harga": 900000,
        "gambar": "https://images.tokopedia.net/img/cache/500-square/product-1/2019/7/27/3219708/3219708_625e9cc0-b3e9-41cf-b853-ea2f6ff76f37_800_800.jpg"
    },
    {
        "nama_produk": "Bibit Cabai Merah",
        "deskripsi": "Bibit cabai merah ini dirancang untuk menghasilkan tanaman dengan buah yang besar, berwarna cerah, dan memiliki rasa pedas yang khas. Tahan terhadap berbagai penyakit dan hama, bibit ini memastikan pertumbuhan yang optimal dan hasil panen yang melimpah. Cocok untuk berbagai kondisi tanah dan iklim, bibit cabai merah ini adalah pilihan terbaik untuk petani yang ingin mendapatkan hasil berkualitas tinggi.",
        "harga": 30000,
        "gambar": "https://id-live-02.slatic.net/p/bdaaac67586c85fb4aba49b77fbe9576.jpg"
    },
    {
        "nama_produk": "Jaring Burung",
        "deskripsi": "Jaring burung ini adalah solusi efektif untuk melindungi tanaman dari serangan burung. Terbuat dari bahan berkualitas tinggi dan tahan lama, jaring ini mudah dipasang dan memberikan perlindungan maksimal tanpa mengganggu pertumbuhan tanaman. Ideal untuk berbagai jenis tanaman, jaring burung ini membantu menjaga hasil panen tetap optimal dan bebas dari kerusakan.",
        "harga": 150000,
        "gambar": "https://s1.bukalapak.com/img/68788162882/large/data.jpeg"
    },
    {
        "nama_produk": "Bibit Tomat Unggul",
        "deskripsi": "Bibit tomat unggul ini dirancang untuk menghasilkan buah tomat yang besar, berwarna merah cerah, dan memiliki rasa manis yang lezat. Dengan ketahanan yang tinggi terhadap penyakit dan hama, bibit ini memastikan pertumbuhan yang sehat dan hasil panen yang melimpah. Cocok untuk berbagai kondisi tanah dan iklim, bibit tomat unggul ini adalah pilihan ideal bagi petani yang menginginkan kualitas dan produktivitas tinggi.",
        "harga": 35000,
        "gambar": "https://down-id.img.susercontent.com/file/da1fb01b69a69d2853166315da5e4a2c"
    },
    {
        "nama_produk": "Kultivator Tanah",
        "deskripsi": "Kultivator tanah ini adalah alat yang efektif untuk mempersiapkan tanah sebelum penanaman. Didesain dengan pisau yang tajam dan roda penggerak yang kuat, kultivator ini mampu mengolah tanah dengan cepat dan efisien. Cocok untuk lahan pertanian skala kecil hingga menengah, alat ini membantu meningkatkan struktur tanah dan memfasilitasi penyerapan nutrisi yang optimal bagi tanaman.",
        "harga": 1100000,
        "gambar": "https://images.tokopedia.net/img/cache/500-square/product-1/2019/3/31/2166904/2166904_4db97dc2-0a45-4227-ac23-82bb507d2f9c_720_720.jpg"
    },
    {
        "nama_produk": "Alat Penyemprot Manual",
        "deskripsi": "Alat penyemprot manual ini merupakan pilihan praktis untuk aplikasi pestisida dan pupuk cair di lahan pertanian. Didesain ergonomis untuk kenyamanan pengguna, alat ini dilengkapi dengan tangki yang cukup besar dan nozzle yang dapat disesuaikan untuk distribusi cairan yang merata. Mudah dioperasikan dan dirawat, alat penyemprot manual ini membantu petani dalam menjaga kesehatan tanaman secara efektif dan efisien. Ideal untuk penggunaan di kebun, perkebunan, dan lahan pertanian skala kecil hingga menengah.",
        "harga": 180000,
        "gambar": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//93/MTA-10664651/plasindo_alat_semprot_elektrik_-_manual_sprayer_16_liter_smb-16_full01_o4f7ulzd.jpg"
    },
    {
        "nama_produk": "Pupuk NPK",
        "deskripsi": "Pupuk NPK ini merupakan campuran nutrisi lengkap yang penting untuk pertumbuhan optimal tanaman. Mengandung konsentrasi nitrogen (N), fosfor (P), dan kalium (K) yang seimbang, pupuk ini memberikan dukungan esensial bagi perkembangan akar, pertumbuhan vegetatif, dan pembentukan buah yang berkualitas. Dirancang untuk aplikasi yang mudah dan hasil yang konsisten, pupuk NPK ini ideal untuk memenuhi kebutuhan nutrisi tanaman di berbagai fase pertumbuhannya.",
        "harga": 55000,
        "gambar": "https://images.tokopedia.net/img/cache/700/product-1/2018/12/18/44660431/44660431_4903d09f-afba-45ad-97c8-c5c314304d1e_2048_2886.jpg"
    },
    {
        "nama_produk": "Bibit Terong Ungu",
        "deskripsi": "Bibit terong unggul ini merupakan pilihan terbaik untuk menghasilkan buah terong yang besar, berwarna cerah, dan memiliki tekstur yang renyah. Tahan terhadap penyakit dan hama, bibit ini memastikan pertumbuhan tanaman yang sehat dan produktif. Cocok untuk ditanam di berbagai jenis tanah dan kondisi iklim, bibit terong unggul ini akan menghasilkan panen yang melimpah dengan kualitas yang terjamin.",
        "harga": 35000,
        "gambar": "https://down-id.img.susercontent.com/file/6363c4fed1740db1abb6c563a57ba583"
    }
]

for item in data:
    response = requests.post(url, json=item)
    if response.status_code == 201:
        print(f"Successfully added: {item['nama_produk']}")
    else:
        print(f"Failed to add: {item['nama_produk']}. Status code: {response.status_code}, Response: {response.text}")
