# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval, Not, In


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    party_type = fields.Selection([
        (None, ''),
        ('person', 'Person'),
        ('private', 'Private Organisation'),
        ('foundation', 'Foundation'),
        ('government', 'Government'),
        ], 'Type',
        states={
            'readonly': ~Eval('active', True),
        }, depends=['active'])
    dob = fields.Date('Date of Birth/Establishment')
    gender = fields.Selection([
        (None, ''),
        ('male', 'Male'),
        ('female', 'Female'),
        ], 'Gender',
        states={
            'readonly': ~Eval('active', True),
            'invisible': Not(In(Eval('party_type'), ['person'])),
        }, depends=['party_type'])
    person_legal_state = fields.Selection([
        (None, ''),
        ('married', 'Married'),
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widow', 'Widow(er)'),
        ], 'Legal state',
        states={
            'readonly': ~Eval('active', True),
            'invisible': Not(In(Eval('party_type'), ['person'])),
        }, depends=['party_type'])

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        cls.last_name.states['invisible'] = \
                Not(In(Eval('party_type'), ['person']))
        cls.last_name.depends.add('party_type')
