from unittest import TestCase
from main import get_all_variations, get_shortest_path, show_way


class TestPathFinder(TestCase):
    def setUp(self):
        self.points1 = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (0, 2)]
        self.points2 = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (6, 7), (0, 2)]
        self.points3 = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (6, 7), (8, 9), (0, 2)]

    def test_variations_five_points(self):
        self.assertEqual(len(get_all_variations(self.points1)), 24)
        self.assertEqual(len(get_all_variations(self.points2)), 120)
        self.assertEqual(len(get_all_variations(self.points3)), 720)

    def test_find_shortest_way_and_show(self):
        shortest_path = get_shortest_path(get_all_variations(self.points1))
        self.assertEqual(shortest_path['path'], ((0, 2), (2, 5), (6, 6), (8, 3), (5, 2), (0, 2)))
        self.assertEqual(show_way(shortest_path), '(0, 2) -> (2, 5)[3.605551275463989] -> '
                                                  '(6, 6)[7.728656901081649] -> (8, 3)[11.334208176545639] -> '
                                                  '(5, 2)[14.496485836714019] -> (0, 2)[19.49648583671402] '
                                                  '= 19.49648583671402')
        shortest_path = get_shortest_path(get_all_variations(self.points2))
        self.assertEqual(shortest_path['path'], ((0, 2), (5, 2), (8, 3), (6, 6), (6, 7), (2, 5), (0, 2)))


