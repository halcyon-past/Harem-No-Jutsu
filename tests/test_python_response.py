import os
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "python")))
import response  # noqa: E402


class ResponseTests(unittest.TestCase):
    def setUp(self):
        response._client = None

    def test_empty_input_returns_prompt(self):
        self.assertEqual(response.get_response(""), "Well, you're awfully silent...")
        self.assertEqual(response.get_response("   "), "Well, you're awfully silent...")

    def test_calls_interactions_create_with_gemini_3_8_flash(self):
        mock_client = MagicMock()
        mock_client.interactions.create.return_value = SimpleNamespace(
            output_text="Ohayo!"
        )

        with patch.dict(os.environ, {"API_KEY": "test-key"}, clear=False):
            with patch.object(response.genai, "Client", return_value=mock_client):
                reply = response.get_response("Say hi", previous_interaction_id="prev-1")

        self.assertEqual(reply, "Ohayo!")
        mock_client.interactions.create.assert_called_once()
        kwargs = mock_client.interactions.create.call_args.kwargs
        self.assertEqual(kwargs["model"], "gemini-3.8-flash")
        self.assertEqual(kwargs["input"], "Say hi")
        self.assertEqual(kwargs["previous_interaction_id"], "prev-1")
        self.assertNotIn("temperature", kwargs)
        self.assertNotIn("top_p", kwargs)

    def test_blank_model_output_returns_fallback(self):
        mock_client = MagicMock()
        mock_client.interactions.create.return_value = SimpleNamespace(output_text="")

        with patch.dict(os.environ, {"GEMINI_API_KEY": "test-key"}, clear=False):
            with patch.object(response.genai, "Client", return_value=mock_client):
                reply = response.get_response("Hello")

        self.assertEqual(reply, "I have no idea what you are talking about")


if __name__ == "__main__":
    unittest.main()
