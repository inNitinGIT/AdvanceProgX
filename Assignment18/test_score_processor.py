import pytest
from score_processor import ScoreProcessor


# Test successful calculation
def test_valid_score_file(tmp_path):

    # Create temporary file
    file_path = tmp_path / "score.txt"

    # Write valid numeric data
    file_path.write_text("5")

    processor = ScoreProcessor()

    result = processor.process_score_file(str(file_path))

    assert result == 50


# Test missing file handling
def test_missing_file():

    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_file.txt")


# Test invalid data handling
def test_invalid_data(tmp_path):

    # Create temporary file
    file_path = tmp_path / "invalid.txt"

    # Write invalid text
    file_path.write_text("hello")

    processor = ScoreProcessor()

    with pytest.raises(ValueError):
        processor.process_score_file(str(file_path))