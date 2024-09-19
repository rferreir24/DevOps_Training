import calculator


#pytest knows that it to run tests since 
#both file name and methods have the prefix : "test"
class TestCalculator:
    
    def test_addition(self):
        assert 4 == calculator.add(2,2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4,2)

        