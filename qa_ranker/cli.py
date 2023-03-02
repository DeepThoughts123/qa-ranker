import click


@click.group()
def cli():
    pass


def main():
    cli(prog_name="command line interface to manage the project")
