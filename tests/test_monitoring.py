import unittest
from unittest.mock import patch
from src.monitoring import check_llm_consistency, check_health


class TestMonitoring(unittest.TestCase):
    def test_check_llm_consistency(self):
        result = check_llm_consistency()
        self.assertIn("coherencia", result)
        self.assertIn("diversidad", result)
        self.assertIn("relevancia", result)

    @patch("src.monitoring.health_checker.app")
    def test_check_health(self, mock_app):
        mock_app.test_client().get.return_value.status_code = 200
        result = check_health()
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
