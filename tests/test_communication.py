import unittest
from unittest.mock import patch
from src.communication import send_message, notify_slack, notify_threshold_downgrade


class TestCommunication(unittest.TestCase):
    @patch("src.communication.message_sender.requests.post")
    def test_send_message(self, mock_post):
        mock_post.return_value.raise_for_status.return_value = None
        send_message()
        mock_post.assert_called_once()

    @patch("src.communication.slack_notifier.WebClient")
    def test_notify_slack(self, mock_client):
        notify_slack("Test message")
        mock_client.return_value.chat_postMessage.assert_called_once()

    @patch("src.communication.slack_notifier.notify_slack")
    def test_notify_threshold_downgrade(self, mock_notify):
        notify_threshold_downgrade("TestClient", "TestThreshold")
        mock_notify.assert_called_once()


if __name__ == "__main__":
    unittest.main()
