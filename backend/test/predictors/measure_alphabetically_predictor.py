from unittest import TestCase

from matchpredictor.matchresults.results_provider import validation_results
from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.predictors.alphabetically_predictor import AlphabeticallyPredictor
from test.predictors import csv_location


class TestAlphabeticallyPredictor(TestCase):
    def test_accuracy(self) -> None:
        validation_data = validation_results(csv_location, 2019)
        accuracy, _ = Evaluator(AlphabeticallyPredictor()).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, .33)
