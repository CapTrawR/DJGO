from unittest import TestCase
from utils.pagination import make_pagination_range

class TestPagination(TestCase):
    
    def test_make_pagination_range_returns_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=7,
            current_page=1,
        )['pagination']
        self.assertEqual([1,2,3,4,5,6,7], pagination)


    def test_first_range_is_static_if_less_than_middle_page(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        #Range should change here
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)

            #Range should change here
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=4,
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)

        # testing the middle range

    def test_make_sure_middle_range_are_correct(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9,10,11,12], pagination)

        #Range should change here
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=12,
        ) ['pagination']
        self.assertEqual([11,12,13,14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_page=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)