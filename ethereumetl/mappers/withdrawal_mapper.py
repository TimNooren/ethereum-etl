# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ethereumetl.domain.withdrawal import EthWithdrawal
from ethereumetl.utils import hex_to_dec, to_normalized_address


class EthWithdrawalMapper(object):
    def json_dict_to_withdrawal(self, json_dict, **kwargs):
        withdrawal = EthWithdrawal()
        withdrawal.index = hex_to_dec(json_dict.get('index'))
        withdrawal.validator_index = hex_to_dec(json_dict.get('validatorIndex'))
        withdrawal.address = to_normalized_address(json_dict.get('address'))
        withdrawal.amount = hex_to_dec(json_dict.get('amount'))
        return withdrawal

    def withdrawal_to_dict(self, withdrawal):
        return {
            'type': 'withdrawal',
            'index': withdrawal.index,
            'validator_index': withdrawal.validator_index,
            'address': withdrawal.address,
            'amount': withdrawal.amount,
        }
