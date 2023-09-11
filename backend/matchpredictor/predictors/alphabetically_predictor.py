import string
from matchpredictor.matchresults.result import Fixture, Outcome
from matchpredictor.predictors.predictor import Prediction, Predictor


class AlphabeticallyPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        home_name = fixture.home_team.name
        away_name = fixture.away_team.name

        if home_name < away_name :
            return Prediction(outcome=Outcome.HOME)
        elif home_name > away_name :
            return Prediction(outcome=Outcome.AWAY)
        else:
            return Prediction(outcome=Outcome.DRAW)
