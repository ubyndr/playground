import unittest
from utils import queryUtils as qu
from neo4j import GraphDatabase


class TestQueryUtils(unittest.TestCase):
    def test_list_query_length(self):
        # Test list query length
        self.assertEqual(len(qu.region_list_query()), 87)
        self.assertEqual(len(qu.varietal_list_query()), 81)
        self.assertEqual(len(qu.wine_list_query()), 78)

    def test_wine_query_length(self):
        # Test wine_query length, check if the queries are not corrupted
        test_input = {'region': 'Kalecik', 'colour': 'red', 'varietal': 'Kalecik Karası'}
        self.assertEqual(len(qu.wine_query('', '', '')), 278)
        self.assertEqual(len(qu.wine_query(test_input['region'], '', '')), 326)
        self.assertEqual(len(qu.wine_query('', test_input['colour'], '')), 293)
        self.assertEqual(len(qu.wine_query('', '', test_input['varietal'])), 304)
        self.assertEqual(len(qu.wine_query(test_input['region'], test_input['colour'], test_input['varietal'])), 367)

    def test_wine_query_content(self):
        # Test wine_query content, check if query components are added correctly
        test_input = {'region': 'Kalecik', 'colour': 'red', 'varietal': 'Kalecik Karası'}
        input_list = ['WHERE r.label='Kalecik' or subR.label='Kalecik'', '{label: 'red'}', '{label: 'Kalecik Karası'}']
        # add region, colour and varietal one by one and check if corresponding query components are added to the query
        self.assertIn(input_list[0], qu.wine_query(test_input['region'], '', ''))
        self.assertIn(input_list[1], qu.wine_query('', test_input['colour'], ''))
        self.assertIn(input_list[2], qu.wine_query('', '', test_input['varietal']))
        query = qu.wine_query(test_input['region'], test_input['colour'], test_input['varietal'])
        self.assertTrue(all(x in query for x in input_list))
        # add inputs in wrong order and check the unexpected behaviour
        self.assertFalse(input_list[1] in qu.wine_query(test_input['region'], '', ''))
        self.assertFalse(input_list[2] in qu.wine_query('', test_input['colour'], ''))
        self.assertFalse(input_list[0] in qu.wine_query('', '', test_input['varietal']))

    def test_get_result(self):
        # Test query execution on neo4j and result parsing
        driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'neo4j'))
        result = qu.get_result(driver, 'MATCH (c:Class) return c.label as label limit 1')
        self.assertTrue(len(result), 1)
        result = qu.get_result(driver, 'MATCH (c:Class) return c.label as label limit 10')
        self.assertTrue(len(result), 10)


if __name__ == '__main__':
    unittest.main()
