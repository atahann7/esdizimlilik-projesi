import re
import pandas as pd
from snowballstemmer import TurkishStemmer


class Collocation:
    def __init__(self,data,keyword,news=None):
        """

        :param data: ..._clean_data.csv dosyası
        :param keyword: anahtar sözcük
        :param news: haber sitesinin adı
        """
        self.data = pd.read_csv(data)
        self.keyword = keyword
        self.word_data = pd.DataFrame(columns=['news_website', 'news_title', 'left_third_word', 'left_sec_word',
                                               'left_first_word', 'keyword', 'right_first_word', 'right_sec_word',
                                               'right_third_word'])
        self.content = []
        self.n_name = news
        self.stemmer = TurkishStemmer()

    # eşdizimsel sözcükleri ayırmak için fonksiyon
    def word_extractor(self):
        for i, n in enumerate(self.data['news_content']):
            pr_text = re.sub(r"[^\w\s]", "", n) # haber içeriklerini gereksiz karakterlerden ayırmak için
            keyword_pattern = r"\b{}\w*\b".format(re.escape(self.keyword)) # anahtar sözcük için regex ile desen belirleme
            pattern = re.compile(keyword_pattern, flags=re.IGNORECASE)

            words = pr_text.split() # haber içeriklerini sözcüklere ayır

            # anahtar sözcüğü bulmak için
            for match in pattern.finditer(pr_text):
                word = match.group(0)
                word_index = words.index(word) # anahtar sözcüğün indeksini bulmak için

                left_words = []
                right_words = []
                # anahtar sözcüğün indeksinden yola çıkarak soldan ve sağdan üç sözcüğü bulur
                for j in range(1, 4):
                    if word_index - j >= 0:
                        w = words[word_index - j]
                        if not re.match(r'^\w*\d+\w*$', w):
                            self.stemmer.stemWord(w)
                            left_words.append(w)
                    if word_index + j < len(words):
                        w = words[word_index + j]
                        if not re.match(r'^\w*\d+\w*$', w):
                            self.stemmer.stemWord(w)
                            right_words.append(w)
                        if re.match(r'^\w*\d+\w*$', w):
                            w = words[word_index + j]
                            self.stemmer.stemWord(w)
                            right_words.append(w)

                while len(left_words) < 3:
                    left_words.insert(0, '')

                while len(right_words) < 3:
                    right_words.append('')


                left_words[0],left_words[2] = left_words[2], left_words[0]
                print(f"{i}.Haberde, {word} sözcüğü : {word_index}. indekstedir.\nSoldaki üç sözcük: {left_words}\nSağdaki üç sözcük: {right_words} ")
                # elde edilen veriler ile karşılık gelen columnlara ata ve csv dosyasında yeni bir row oluştur
                new_row = {'news_website': self.data.loc[i, 'news_website'], 'news_title': self.data.loc[i, 'news_title'],
                           'left_third_word': left_words[0], 'left_sec_word': left_words[1],
                           'left_first_word': left_words[2], 'keyword': word,
                           'right_first_word': right_words[0], 'right_sec_word': right_words[1],
                           'right_third_word': right_words[2]}

                self.word_data = self.word_data.append(new_row, ignore_index=True)
        # haber sitesinin ismine göre dosyası kaydet
        self.word_data.to_csv(f'data/{self.n_name}_col_words.csv', index=False)

