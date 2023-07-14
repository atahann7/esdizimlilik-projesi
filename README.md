# Eşdizimlilik Projesi

## Giriş 

Bitirme projem içindir. Bu projede, Türkçe haber sitelerinden belirli bir anahtar sözcüğe göre içerikleri toplamak, eşdizimsel ögelerini tespit etmek ve eşdizimsel ögelerin bulunduğu konumlara göre kullanım sıklığına göre hesaplamak ve son olarak elde edilen sıklık verileri sözcükleri sıcaklık haritasını oluşturmak amaçlanmaktadır.

## Kullanımı

>-news_scraper.py ile belirli beş haber sitesinden anahtar sözcüğe göre içerikler site adı, içerik, url vs. olmak üzere habersitesi_data.csv dosyasına dönüştürülür. 
>-data.cleaner.py ile .csv dosyalarındaki veriler arındırılır ve temizlenmiş habersitesi_clean_data.csv dosyaları olarak kaydedilir. 
>-collocation_ext.py ile eşdizimsel ögeler tespit edilir ve habersitesi_col_words.csv olarak dosyaları olarak kaydeder.  
>-to_heatmap_merged.py habersitesi_col_words.csv dosyaları alır ve sıcaklık haritasını dönüşütürüp left_heatmap ve right_heatmap olarak kaydeder. 
