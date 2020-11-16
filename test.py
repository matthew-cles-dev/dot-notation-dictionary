from dot_notation_dictionary import DotDict, DefaultDotDict
import unittest

test_dot_dict = DotDict(
    alpha=1,
    beta=2,
    gamma=5,
)

test_default_dot_dict = DefaultDotDict(
    'default_value',
    alpha=1,
    beta=2,
    gamma=5,
)

class TestDotDictMethods(unittest.TestCase):

    def test_DotDict_isinstances(self):
        self.assertEqual(isinstance(test_dot_dict, dict), True)
        self.assertEqual(isinstance(test_dot_dict, DotDict), True)
        self.assertEqual(isinstance(test_dot_dict, list), False)

    def test_DotDict_initialization_with_keywords(self):
        dot_dict = DotDict(
            alpha=1,
            beta=2,
            gamma=5,
        )
        self.assertEqual(dot_dict.alpha, 1)
        self.assertEqual(dot_dict.beta, 2)
        self.assertEqual(dot_dict.gamma, 5)

    def test_DotDict_initialization_with_dict_parameter(self):
        dot_dict = DotDict(
            {
                'alpha': 1,
                'beta': 2,
                'gamma': 5,
            },
        )
        self.assertEqual(dot_dict.alpha, 1)
        self.assertEqual(dot_dict.beta, 2)
        self.assertEqual(dot_dict.gamma, 5)

    def test_DotDict_initialization_with_keywords_and_dict(self):
        dot_dict = DotDict(
            {
                'alpha': 1,
                'beta': 2
            },
            gamma=5,
        )
        self.assertEqual(dot_dict.alpha, 1)
        self.assertEqual(dot_dict.beta, 2)
        self.assertEqual(dot_dict.gamma, 5)

    def test_access_index_with_brackets(self):
        self.assertEqual(test_dot_dict['alpha'], 1)
        self.assertEqual(test_dot_dict['beta'], 2)
        self.assertEqual(test_dot_dict['gamma'], 5)

    def test_access_index_with_get_method(self):
        self.assertEqual(test_dot_dict.get('alpha'), 1)
        self.assertEqual(test_dot_dict.get('beta'), 2)
        self.assertEqual(test_dot_dict.get('gamma'), 5)

    def test_access_index_with_dot_notation(self):
        self.assertEqual(test_dot_dict.alpha, 1)
        self.assertEqual(test_dot_dict.beta, 2)
        self.assertEqual(test_dot_dict.gamma, 5)

    @unittest.expectedFailure
    def test_access_index_that_does_not_exist_with_brackets(self):
        test_dot_dict['delta']

    @unittest.expectedFailure
    def test_access_index_that_does_not_exist_with_get_method(self):
        _default_value = -1
        self.assertNotEqual(test_dot_dict.get('delta', _default_value), _default_value)

    @unittest.expectedFailure
    def test_access_index_that_does_not_exist_with_dot_notation(self):
        test_dot_dict.delta

class TestDefaultDotDictMethods(unittest.TestCase):

    def test_DefaultDotDict_isinstances(self):
        self.assertEqual(isinstance(test_default_dot_dict, dict), True)
        self.assertEqual(isinstance(test_default_dot_dict, DefaultDotDict), True)
        self.assertEqual(isinstance(test_default_dot_dict, list), False)

    def test_DefaultDotDict_initialization_with_keywords(self):
        dot_dict = DotDict(
            alpha=1,
            beta=2,
            gamma=5,
        )
        self.assertEqual(dot_dict.alpha, 1)
        self.assertEqual(dot_dict.beta, 2)
        self.assertEqual(dot_dict.gamma, 5)

    def test_DefaultDotDict_initialization_with_dict_parameter(self):
        dot_dict = DotDict(
            {
                'alpha': 1,
                'beta': 2,
                'gamma': 5,
            },
        )
        self.assertEqual(dot_dict.alpha, 1)
        self.assertEqual(dot_dict.beta, 2)
        self.assertEqual(dot_dict.gamma, 5)

    def test_DefaultDotDict_initialization_with_keywords_and_dict(self):
        dot_dict = DotDict(
            {
                'alpha': 1,
                'beta': 2
            },
            gamma=5,
        )
        self.assertEqual(dot_dict.alpha, 1)
        self.assertEqual(dot_dict.beta, 2)
        self.assertEqual(dot_dict.gamma, 5)

    def test_access_index_with_brackets(self):
        self.assertEqual(test_default_dot_dict['alpha'], 1)
        self.assertEqual(test_default_dot_dict['beta'], 2)
        self.assertEqual(test_default_dot_dict['gamma'], 5)

    def test_access_index_with_get_method(self):
        self.assertEqual(test_default_dot_dict.get('alpha'), 1)
        self.assertEqual(test_default_dot_dict.get('beta'), 2)
        self.assertEqual(test_default_dot_dict.get('gamma'), 5)

    def test_access_index_with_dot_notation(self):
        self.assertEqual(test_default_dot_dict.alpha, 1)
        self.assertEqual(test_default_dot_dict.beta, 2)
        self.assertEqual(test_default_dot_dict.gamma, 5)

    def test_access_index_that_does_not_exist_with_brackets(self):
        self.assertEqual(test_default_dot_dict['delta'], 'default_value')

    def test_access_index_that_does_not_exist_with_get_method(self):
        _default_value = -1
        self.assertEqual(test_default_dot_dict.get('delta', _default_value), 'default_value')

    def test_access_index_that_does_not_exist_with_dot_notation(self):
        self.assertEqual(test_default_dot_dict.delta, 'default_value')

if __name__ == '__main__':
    unittest.main()
