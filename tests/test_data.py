import unittest
from unittest.mock import patch, MagicMock
from src.data import clear_history, save_status


class TestData(unittest.TestCase):
    @patch("src.data.db_manager.collection")
    def test_clear_history(self, mock_collection):
        clear_history()
        mock_collection.delete_many.assert_called_once_with({})

    @patch("src.data.db_manager.collection")
    def test_save_status(self, mock_collection):
        test_evaluation = {"score": 90, "explanation": "Good"}
        save_status(test_evaluation)
        mock_collection.insert_one.assert_called_once_with(
            {"evaluation": test_evaluation}
        )


if __name__ == "__main__":
    unittest.main()
