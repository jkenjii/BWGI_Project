
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from bwgi_project.core.reconcile import reconcile_accounts

class TestReconcileAccounts(unittest.TestCase):
    def test_match_date_priority(self):
        lista1 = [['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket']]
        lista2 = [['2020-12-04', 'Tecnologia', '16.00', 'Bitbucket'],
                  ['2020-12-05', 'Tecnologia', '16.00', 'Bitbucket']]
        out1, _ = reconcile_accounts(lista1, lista2)
        assert out1[0][-1] == 'FOUND'
