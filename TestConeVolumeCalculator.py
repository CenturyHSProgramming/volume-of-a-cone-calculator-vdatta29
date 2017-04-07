# TestConeVolumeCalculator.py

# What are we testing for?

# Wide range of inputs
    # - proper and improper
# Boundary Conditions
# Correct outputs
# Test for exceptions

# Import Statements
import unittest
import ConeVolumeCalculator

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_calculateConeVolume_forLowRelativeHumidity_WarmTemp(self):
        # Capture the results of the function
        result = ConeVolumeCalculator.calculateConeVolume(40, 80)
        # Check for expected output
        self.assertEqual(80, result)

    def test_calculateConeVolume_forLowRelativeHumidity_HotTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(40, 92)
        expected = 94
        self.assertEqual(expected, result)

    # Add minimum of 5 more unittests
    def test_calculateConeVolume_forLowRelativeHumidity_ExtremeHotTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(45, 108)
        expected = 137
        self.assertEqual(expected, result)

    def test_calculateConeVolume_forMedRelativeHumidity_WarmTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(65, 80)
        expected = 82
        self.assertEqual(expected, result)

    def test_calculateConeVolume_forMedRelativeHumidity_HotTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(65, 90)
        expected = 103
        self.assertEqual(expected, result)

    def test_calculateConeVolume_forMedRelativeHumidity_ExtremeTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(60, 100)
        expected = 129
        self.assertEqual(expected, result)

    def test_calculateConeVolume_forHighRelativeHumidity_WarmTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(95, 80)
        expected = 86
        self.assertEqual(expected, result)

    def test_calculateConeVolume_forHighRelativeHumidity_HotTemp(self):
        result = ConeVolumeCalculator.calculateConeVolume(100, 90)
        expected = 132
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for_80RelativeHumidity_96Temp(self):
        result = ConeVolumeCalculator.calculateConeVolume(80, 96)
        expected = 132
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for_70RelativeHumidity_98Temp(self):
        result = ConeVolumeCalculator.calculateConeVolume(80, 96)
        expected = 134
        self.assertEqual(expected, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()
