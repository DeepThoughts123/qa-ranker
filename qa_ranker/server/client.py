from pumpkin.twirp.client import PumpkinTwirpClient
from instacart.algorithms.general_ml.qa_ranker.v1.qaranker_pb2 import QARankerRequest


def get_twirp_client(host):
    return PumpkinTwirpClient.from_interface_name(
            interface_name="instacart.algorithms.general_ml.qa_ranker.v1.QARankerService",
            host=host,
            url_prefix="/twirp/")


def query_server(feature_ids, host='http://0.0.0.0:3000'):
    client = get_twirp_client(host)
    response = client.GetQARankerScores(QARankerRequest(feature_ids=feature_ids))
    return response._message.scores
