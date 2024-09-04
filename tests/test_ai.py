import unittest
from unittest.mock import patch
from src.ai import generate_conversation, evaluate_conversation


class TestAI(unittest.TestCase):
    @patch("src.ai.conversation_generator.openai.ChatCompletion.create")
    def test_generate_conversation(self, mock_create):
        mock_create.return_value.choices[0].message = {"content": "Test conversation"}
        result = generate_conversation()
        self.assertEqual(result, "Test conversation")

    @patch("src.ai.ai_evaluator.openai.ChatCompletion.create")
    def test_evaluate_conversation(self, mock_create):
        mock_create.return_value.choices[0].message = {
            "content": "90 Good conversation"
        }
        result = evaluate_conversation("Test conversation")
        self.assertEqual(result, {"score": 90, "explanation": "Good conversation"})


if __name__ == "__main__":
    unittest.main()
