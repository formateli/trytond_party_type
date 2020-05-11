# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool


class PartyTypeTestCase(ModuleTestCase):
    'Test Party type module'
    module = 'party_type'

    @with_transaction()
    def test_party_type(self):
        pool = Pool()
        Party = pool.get('party.party')

        party, = Party.create([{
                    'name': 'Jhon Doe',
                    'party_type': 'person',
                    'gender': 'male',
                    }])
        self.assertTrue(party.id)


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyTypeTestCase))
    return suite
