from jsonalyze import compare_dict


def test_compare_dict_basic_types():
    d1 = {'a': 1, 'b': None, 'c': 'k', 'd': True}
    d2 = {'a': 1, 'b': None, 'c': 'k', 'd': True}
    assert compare_dict(d1, d2, {'a': None, 'b': None, 'c': None, 'd': None})


def test_compare_dict_number_fail():
    d1 = {'a': 1}
    d2 = {'a': 2}
    assert not compare_dict(d1, d2, {'a': None})


def test_compare_dict_string_fail():
    d1 = {'a': 'test'}
    d2 = {'a': 'fail'}
    assert not compare_dict(d1, d2, {'a': None})


def test_compare_dict_null_fail():
    d1 = {'a': None}
    d2 = {'a': 'fail'}
    assert not compare_dict(d1, d2, {'a': None})


def test_compare_dict_boolean_fail():
    d1 = {'a': True}
    d2 = {'a': False}
    assert not compare_dict(d1, d2, {'a': None})


def test_compare_dict_missing_key():
    d1 = {'a': 'test'}
    d2 = {'a': 'test'}
    assert not compare_dict(d1, d2, {'b': None})


def test_compare_dict_array():
    d1 = {'a': [1, 2, 3, 4]}
    d2 = {'a': [1, 2, 3, 4]}
    assert compare_dict(d1, d2, {'a': None})


def test_compare_dict_array_fail():
    d1 = {'a': [1, 2, 3, 4]}
    d2 = {'a': [1, 2, 3, 5]}
    assert not compare_dict(d1, d2, {'a': None})


def test_compare_dict_dict():
    d1 = {'a': {'b': 1, 'c': 2, 'j': 3}}
    d2 = {'a': {'b': 1, 'c': 2, 'j': 9}}
    assert compare_dict(d1, d2, {'a': {'b': None, 'c': None}})


def test_compare_dict_dict_fail():
    d1 = {'a': {'b': 1, 'c': 2, 'j': 3}}
    d2 = {'a': {'b': 1, 'c': 2, 'j': 9}}
    assert not compare_dict(d1, d2, {'a': {'b': None, 'c': None, 'j': None}})


def test_compare_dict_dict_arr():
    d1 = {'a': [{'b': 1, 'c': 2}, {'b': 3, 'c': 4}]}
    d2 = {'a': [{'b': 3, 'c': 4}, {'b': 1, 'c': 2}]}
    assert compare_dict(d1, d2, {'a': [{'b': None, 'c': None}]})


def test_compare_dict_dict_arr_fail():
    d1 = {'a': [{'b': 1, 'c': 2}, {'b': 2, 'c': 4}]}
    d2 = {'a': [{'b': 3, 'c': 4}, {'b': 1, 'c': 2}]}
    assert not compare_dict(d1, d2, {'a': [{'b': None, 'c': None}]})


def test_compare_dict_arr_arr():
    d1 = {'a': [[1, 2, 3], [4, 5, 6]]}
    d2 = {'a': [[4, 5, 6], [1, 2, 3]]}
    assert compare_dict(d1, d2, {'a': [[]]})


def test_compare_dict_arr_arr_fail():
    d1 = {'a': [[1, 2, 3], [4, 5, 6]]}
    d2 = {'a': [[4, 5, 6], [1, 2, 2]]}
    assert not compare_dict(d1, d2, {'a': [[]]})


def test_deep_recursion():
    d1 = {
        'a': {
            'b': {
                'c': [
                    {'d': [[1, 2, 3], [4, 5, 6]]},
                    {'d': [[1, 2, 3], [5, 6, 7]]},
                ],
                'e': 'k',
                'f': 'eh',
            }
        }
    }
    d2 = {
        'a': {
            'b': {
                'c': [
                    {'d': [[1, 2, 3], [5, 6, 7]]},
                    {'d': [[4, 5, 6], [1, 2, 3]]},
                ],
                'e': 'k',
                'f': 'oh',
            }
        }
    }
    assert compare_dict(d1, d2, {'a': {'b': {'c': [{'d': [[]]}], 'e': None}}})
