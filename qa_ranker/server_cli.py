import click
from pumpkin.runtime import run_twirp_server


@click.command(help="Run the twirp server on local laptop")
def serve():
    """
    Run twirp server using application definition in server/app.py
    """
    run_twirp_server(
        "qa_ranker.server.app:make_app",
    )
