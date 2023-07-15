# .csv dosyalarındaki verileri arındırmak için

import pandas as pd
from config import clean_params


class Data_cleaner:

    def __init__(self,data,word):
        """

        :param data: ..._data.csv dosyası
        :param word: anahtar sözcük
        """
        self.data = pd.read_csv(data)
        self.params = clean_params
        self.word = word
        print(self.data.isna().sum())

    def clean_unwanted(self,news_name,parameter=None,save_file=False, clean_url=None):
        """
        :param news_name: haber sitesi adı
        :param parameter: parametre --gereksiz
        :param save_file: dosya kaydedilsin mi
        :param clean_url: belirli bir parametreye göre url temizlensin mi --çalışmıyor
        """
        if self.data.isnull().values.any():
            self.data = self.data.dropna(subset=['news_content'])
        # news_content içinde keyword geçmiyorsa, o satırı siler
        self.data = self.data[self.data['news_content'].str.contains(self.word, case=False)]

        # köşe yazılarını silmek için
        if clean_url == True:
            self.data = self.data[~self.data['news_url'].str.contains(self.params[news_name][parameter])]
        print(self.data.head(10))
        # dosyası silemk için
        if save_file == True:
            self.data.to_csv(f"{news_name}_clean_data.csv")

    # koplayarı temizlemek için --gereksiz
    def clean_dupes(self,news_name,save_file=False):
        self.data.drop_duplicates()
        print(self.data.head(15))
        if save_file == True:
            self.data.to_csv(f"{news_name}_clean_data.csv")


