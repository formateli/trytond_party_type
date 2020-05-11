# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval, Not, In

__all__ = ['Party']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    party_type = fields.Selection([
        (None, ''),
        ('person', 'Person'),
        ('private', 'Private Organisation'),
        ('foundation', 'Foundation'),
        ('government', 'Government'),
        ], 'Type')
    dob = fields.Date('Date of Birth/Establishment')
    gender = fields.Selection([
        (None, ''),
        ('male', 'Male'),
        ('female', 'Female'),
        ], 'Gender',
        states={
            'invisible': Not(In(Eval('party_type'), ['person'])),
        }, depends=['party_type'])
