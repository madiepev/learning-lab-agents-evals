import importlib.util
import os
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).parent / "evaluation" / "scripts" / "cognitive-load-rubric.py"


def load_module():
    spec = importlib.util.spec_from_file_location("cognitive_load_rubric", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    fake_openai = types.ModuleType("openai")
    fake_openai.OpenAI = object
    with patch.dict(sys.modules, {"openai": fake_openai}):
        spec.loader.exec_module(module)
    return module


class CognitiveLoadRubricConfigTests(unittest.TestCase):
    def test_blank_model_name_falls_back_to_default(self):
        with patch.dict(
            os.environ,
            {
                "GITHUB_TOKEN": "test-token",
                "INPUT_FILE": "dummy-input",
                "MODEL_NAME": "",
            },
            clear=True,
        ):
            module = load_module()

        self.assertEqual(module.MODEL_NAME, "openai/gpt-4o")

    def test_explicit_model_name_is_preserved(self):
        with patch.dict(
            os.environ,
            {
                "GITHUB_TOKEN": "test-token",
                "INPUT_FILE": "dummy-input",
                "MODEL_NAME": "openai/gpt-4.1",
            },
            clear=True,
        ):
            module = load_module()

        self.assertEqual(module.MODEL_NAME, "openai/gpt-4.1")


if __name__ == "__main__":
    unittest.main()
