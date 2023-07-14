import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import config as cf
import re

#
class DataVis:
    def __init__(self):
        self.csv_path = cf.TO_HEATMAP_PATH
        self.dfs = []

    def extract_word_positions(self, df):
        left_words = [
            df['left_third_word'],
            df['left_sec_word'],
            df['left_first_word']
        ]
        right_words = [
            df['right_first_word'],
            df['right_sec_word'],
            df['right_third_word']

        ]
        left_words = [words.dropna() if words is not None else pd.Series() for words in left_words]
        right_words = [words.dropna() if words is not None else pd.Series() for words in right_words]

        # for i in range(len(left_words)):
        #     left_words[i] = left_words[i][left_words[i].apply(lambda x: isinstance(x, str))]
        #     right_words[i] = right_words[i][right_words[i].apply(lambda x: isinstance(x, str))]

        return left_words, right_words


    def data_to_heatmap(self):
        for filename in os.listdir(self.csv_path):
            if filename.endswith(".csv"):
                filepath = os.path.join(self.csv_path, filename)
                try:
                    df = pd.read_csv(filepath)
                    df = df.drop_duplicates(subset=['left_third_word', 'left_sec_word', 'left_first_word'], keep=False)
                    df = df.drop_duplicates(subset=['right_first_word', 'right_sec_word', 'right_third_word'], keep=False)
                    columns_to_lower = ['left_third_word', 'left_sec_word', 'left_first_word','right_first_word', 'right_sec_word', 'right_third_word']
                    df[columns_to_lower] = df[columns_to_lower].apply(lambda x: x.str.lower())
                    self.dfs.append(df)
                    self.process_dataframe()
                except Exception as e:
                    print(f"Error reading file {filename}: {str(e)}")
    def process_dataframe(self):
        self.test = pd.concat(self.dfs)

        left_words, right_words = self.extract_word_positions(self.test)
        # Create subplot for left word counts
        fig, axs = plt.subplots(1, 3, figsize=(16, 10))
        plt.subplots_adjust(wspace=0.5)
        for i, words in enumerate(left_words):
            word_counts = words.value_counts()
            if word_counts.empty:
                continue
            max_words = 25
            # word_counts = word_counts.sort_values(ascending=False)
            ax = axs[i]
            ax = sns.heatmap(pd.DataFrame(word_counts.head(max_words)), annot=True, fmt='d', cmap='rocket_r', annot_kws={'fontsize': 12 },
                             ax=ax)
            ax.set_xlabel('Frequency')
            ax.set_ylabel('Words')
            ax.set_title(f'Left Words (Position {i + 1})')

            ax.tick_params(axis='y', labelsize=14)

        # Save subplot as PNG file
        # news_name = re.sub(r'[^\w]+', '', df['news_website'].iloc[0])
        plt.savefig(f'heatmaps/heatmap_left.png', dpi=300, bbox_inches='tight')
        plt.close()

        # Create subplot for right word counts
        fig, axs = plt.subplots(1, 3, figsize=(16, 10))
        plt.subplots_adjust(wspace= 0.5)
        for i, words in enumerate(right_words):
            word_counts = words.value_counts()
            if word_counts.empty:
                continue

            max_words = 25
            ax = axs[i]
            ax = sns.heatmap(pd.DataFrame(word_counts.head(max_words)), annot=True, fmt='d', cmap='rocket_r', annot_kws={'fontsize': 12},
                             ax=ax)
            ax.set_xlabel('Frequency')
            ax.set_ylabel('Words')
            ax.set_title(f'Right Word (Position {i + 1})')

            ax.tick_params(axis='y', labelsize=14)

        # Save subplot as PNG file
        plt.savefig(f'heatmaps/heatmap_right.png', dpi=300, bbox_inches='tight')
        plt.close()



test = DataVis()
test.data_to_heatmap()