import unittest
from EmotionDetection.emotion_detection import emotion_analyzer

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_analyzer(self):
        # Get results from test strings
        result_1 = emotion_analyzer('I am glad this happened')
        result_2 = emotion_analyzer('I am really mad about this')
        result_3 = emotion_analyzer('I feel disgusted just hearing about this')
        result_4 = emotion_analyzer('I am so sad about this')
        result_5 = emotion_analyzer('I am really afraid that this will happen')
        # Test results
        self.assertEqual(result_1['dominant_emotion'], "joy")
        self.assertEqual(result_2['dominant_emotion'], "anger")
        self.assertEqual(result_3['dominant_emotion'], "disgust")
        self.assertEqual(result_4['dominant_emotion'], "sadness")
        self.assertEqual(result_5['dominant_emotion'], "fear")

if __name__ == '__main__':
    unittest.main()
