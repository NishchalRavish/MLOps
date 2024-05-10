import pytest
import sys
import os
from pathlib import Path

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# Output from predict script should not be null
# Output from predict script is str data type
# the output is Y for an example data

# Fixtures --> functions that are run before execution of each test function --> ensure single_prediciton

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

# To check if values are being displayed(Output is not none)
def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None

# To check if data type is a string
def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('predictions')[0],str)

# To check if the out put is Y(Yes)
def test_single_pred_validate(single_prediction):
    assert single_prediction.get('predictions')[0] =='Y'
