"""
Bazı gerekli/gereksiz parametler
"""

# news-scraper parametreleri
# haber sitesi ve linkleri
news_websites = {
    "milliyet": {'url': 'https://www.milliyet.com.tr/haberleri/'},
    "haberturk": {'url': 'https://www.haberturk.com/arama/{keyword}?tr={keyword}'},
    "hurriyet": {'url': 'https://www.hurriyet.com.tr/arama/#/?page=1&key={keyword}&where=/&how=Article&isDetail=false'},
    "posta": {'url': 'https://www.posta.com.tr/haberleri/'},
    "takvim": {'url': 'https://www.takvim.com.tr/arama/arsiv/'},
    "sozcu": {'url': ''}
}

# data-cleaner parametreleri
# verilerin arındırılması için paratmerler
clean_params = {
    'takvim': {'forbidden': 'yazarlar'}

}
# to_heatmap_merged için ..col_words dosyalarının konumu
TO_HEATMAP_PATH = "..\words\data"

