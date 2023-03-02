from pumpkin.app import PumpkinApp
from qa_ranker.server.handler import QARankerHandler
from instacart.algorithms.general_ml.qa_ranker.v1.qaranker_twirp import QARankerServiceServer


def make_app():
    """Twirp handler."""
    app = PumpkinApp()
    handler = QARankerHandler()
    server = QARankerServiceServer(handler)
    app.add_twirp_server(server)
    return app
