# services/test/test_patterns.py
import unittest
from rules.rule_engine import RuleEngine
from services.download_service.downloader import Downloader

class TestPattern(unittest.TestCase):
    def test_rule_engine(self):
        def mock_action():
            print("Action triggered!")
        
        rules = [{"condition": True, "action": mock_action}]
        engine = RuleEngine(rules)
        engine.evaluate()  # Expected to print "Action triggered!"

    def test_downloader(self):
        downloader = Downloader("http://example.com/testfile", "/path/to/save")
        downloader.download()
        # Here, you would check if the file is downloaded correctly.

if __name__ == "__main__":
    unittest.main()
