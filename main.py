from bs4 import BeautifulSoup
from urllib.request import urlopen
import click

from oceanic_cruise import OceanicCruise

@click.command()
@click.argument('doi')
@click.argument('filepath', type=click.Path())
@click.option('--append', is_flag=True, help='Append result to existing file')
def main(doi, filepath, append):
    """Extract oceanographic cruise information based on DOI"""

    try:
        url = f"https://campagnes.flotteoceanographique.fr/campagnes/{doi}/fr/index.htm"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        oceanic_cruise = OceanicCruise(soup)
        mode = 'a' if append else 'w'
        oceanic_cruise.to_csv(filepath, mode)

        click.echo(f"Successfully extracted {doi} information to {filepath}")

    except Exception as e:
        raise click.ClickException(e)

if __name__ == "__main__":
    main()
