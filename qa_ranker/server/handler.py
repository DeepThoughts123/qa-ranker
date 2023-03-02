from instacart.algorithms.general_ml.qa_ranker.v1.qaranker_twirp import QARankerServiceHandler
from instacart.algorithms.general_ml.qa_ranker.v1.qaranker_pb2 import QARankerResponse


class QARankerHandler(QARankerServiceHandler):
    """
    Handler to execute predictions
    """
    def __init__(self, *args, **kwargs):
        """Initialize the server and load the model."""
        pass

    def GetQARankerScores(self, request, context):
        """Implement model inference here."""
        feature_ids = request.feature_ids
        return QARankerResponse(scores=feature_ids)
