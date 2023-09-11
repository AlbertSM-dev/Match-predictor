from unittest import TestCase

from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.matchresults.results_provider import training_results, validation_results
from matchpredictor.predictors.home_odd_winner_predictor import home_odd_winner_predictor
from test.predictors import csv_location


class Home_ODD_Winner_Predictor(TestCase): 
    def test_accuracy(self) -> None:
        training_data = training_results(csv_location, 2021)
        validation_data = validation_results(csv_location, 2021)
        predictor = home_odd_winner_predictor(training_data)

        accuracy, _ = Evaluator(predictor).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, .33)

