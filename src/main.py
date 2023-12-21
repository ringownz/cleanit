import click
import time
from src.CleanAutomation import clean_automation
from src.ChaosAutomation import chaos_automation


@click.command()
@click.option('--abspathfrom', default="", prompt='Where do you want to organise? Absolute path', help='Absolute path to the folder we want to clean.')
@click.option('--abspathto', default="", prompt='Where do you want to move files? Absolute path', help='Absolute path to the folder we want create organised folders.')
def cleanIt(abspathfrom, abspathto):
    # TODO: Call clean automation
    click.echo('CleanIt PROCESSING')
    time.sleep(1)
    click.echo('CleanIt PROCESSING .')
    time.sleep(0.5)
    click.echo('CleanIt PROCESSING ..')
    time.sleep(0.5)
    click.echo('CleanIt PROCESSING ...')
    time.sleep(0.5)
    print('''\n\n\n\n
        ┌───── •✧✧• ─────┐
        ±   -CLEAN IT-   ± 
        └───── •✧✧• ─────┘
        ''')

    clean_automation(abspathfrom, abspathto)


@click.command()
@click.option('--chaoswhere', default="", prompt='Where do you want to apply CHAOS? Absolute path', help='Absolute path to folder we want to destroyed organized files')
@click.option('--chaosto', default="", prompt='Where do you want to send CHAOS? Absolute path', help='Absolute path to folder we want to throw everything')
def randomIt(chaoswhere, chaosto):
    # TODO: Call clean automation
    click.echo('PROCESSING')
    time.sleep(1)
    click.echo('PROCESSING .')
    time.sleep(0.5)
    click.echo('PROCESSING ..')
    time.sleep(0.5)
    click.echo('PROCESSING ...')
    time.sleep(0.5)
    print('''\n\n\n\n
    ┌───── •✧✧• ─────┐
    ±     -CHAOS-    ± 
    └───── •✧✧• ─────┘
    ''')

    chaos_automation(chaoswhere, chaosto)


if __name__ == '__main__':
    #cleanIt()
    randomIt()
