import pandas as pd


class Sitemap:
    def __init__(self, sitemap_file=None):
        self.file = sitemap_file
        self.df = None
        if sitemap_file:
            self.setup(sitemap_file)

    def setup(self, file):
        df = pd.read_csv(file, delimiter='|')
        self.df = df

    def content(self, id_):
        row = self.df.query(f'id == {id_}').iloc[0]
        content = row['Child Text']
        return content

    def alias(self, id_):
        row = self.df.query(f'id == {id_}').iloc[0]
        path = row['path']
        return path

    def title(self, id_):
        row = self.df.query(f'id == {id_}').iloc[0]
        title = row['Title']
        return title

    def html_table(self):
        df = self.df
        df = df[['id', 'Title', 'path']]
        return df.to_html()
