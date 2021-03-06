# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /MarketplaceAgreements/put/SetMarketplaceTerms
@try_manual
def step_accept(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az term accept '
             '--product "vsec" '
             '--plan "management" '
             '--publisher "checkpoint"',
             checks=[
                 test.check('plan', 'management'),
                 test.check('publisher', 'checkpoint'),
                 test.check('product', 'vsec'),
             ])


# EXAMPLE: /MarketplaceAgreements/get/GetMarketplaceTerms
@try_manual
def step_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az term show '
             '--product "vsec" '
             '--plan "management" '
             '--publisher "checkpoint"',
             checks=[
                 test.check('plan', 'management'),
                 test.check('publisher', 'checkpoint'),
                 test.check('product', 'vsec'),
             ])
