from datetime import datetime

class OceanicCruise:
    def __init__(self, soup):
        article = self.get_article(soup)
        dates = self.get_date(article)
        cruise_chiefs = self.get_cruise_chiefs(article)
        (start_date, end_date) = self.extract_dates(dates)

        self.theme = self.get_theme(soup)
        self.name = self.get_name(article)
        self.year = start_date.year
        self.duration = (end_date - start_date).days
        self.ship = self.get_ship(article)
        self.cruise_chief = self.get_cruise_chiefs_names(cruise_chiefs)
        self.type = self.get_type(article)
        self.mails = self.get_cruise_chiefs_mails(cruise_chiefs)
        self.url = self.get_url(article)

    def get_theme(self, soup) -> str:
        for field in soup.find_all('th'):
            if field.get_text() == 'Discipline(s)':
                return field.parent.td.ul.li.get_text()

        return ""

    def get_article(self, soup):
        return soup.find_all('article')[0]

    def get_name(self, article) -> str:
        return article.h1.get_text()

    def get_date(self, article) -> str:
        for field in article.find_all('th'):
            if field.get_text() == 'Dates':
                return field.parent.td.get_text()

        return ""

    def get_ship(self, article) -> str:
        for field in article.find_all('th'):
            if field.get_text() == 'Navire':
                return field.parent.td.get_text()

        return ""

    def get_cruise_chiefs(self, article):
        for field in article.find_all('th'):
            if field.get_text() == 'Chef(s) de mission':
                return field.parent.td
        
        return None

    def get_cruise_chiefs_names(self, cruise_chiefs) -> str:
        chief_names = []
        for chief in cruise_chiefs.get_text().rsplit(","):
            chief_names.append(chief.strip())

        return chief_names

    def get_cruise_chiefs_mails(self, cruise_chiefs) -> str:
        chief_mails = []
        for chief in cruise_chiefs.find_all('a'):
            link = chief["href"]
            link_split = link.split("mailto:")
            if len(link_split) > 1:
                chief_mails.append(link_split[1])

        return chief_mails

    def get_type(self, article) -> str:
        for field in article.find_all('th'):
            if field.get_text() == 'Type':
                return field.parent.td.get_text()

        return ""

    def get_url(self, article) -> str:
        for field in article.find_all('th'):
            if field.get_text() == 'DOI':
                return field.parent.td.a["href"]

        return ""

    def extract_dates(self, dates) -> (datetime, datetime):
        split_dates = dates.rsplit(" - ")
        start_date = datetime.strptime(split_dates[0], '%d/%m/%Y')
        end_date = datetime.strptime(split_dates[1], '%d/%m/%Y')

        return (start_date, end_date)

    def __str__(self):
        return (
            f"theme: {self.theme}, "
            f"name: {self.name}, "
            f"year: {self.year}, "
            f"duration: {self.duration}, "
            f"ship: {self.ship}, "
            f"cruise_chief: {self.cruise_chief}, "
            f"type: {self.type}, "
            f"mails: {self.mails}, "
            f"url: {self.url}"
            )