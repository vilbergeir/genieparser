# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.iosxr.show_prefix_list import ShowRplPrefixSet

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ===================================
# Unit test for 'show rpl prefix-set'
# ===================================

class test_show_rpl_prefix_set(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'prefix_set_name': {
            'test': {
                'prefix_set_name': 'test',
                'protocol': 'ipv4',
                'prefixes': {
                    '35.0.0.0/8 8..8': {
                        'prefix': '35.0.0.0/8',
                        'masklength_range': '8..8'
                    },
                    '35.0.0.0/8 8..16': {
                        'prefix': '35.0.0.0/8',
                        'masklength_range': '8..16'
                    },
                    '36.0.0.0/8 8..16': {
                        'prefix': '36.0.0.0/8',
                        'masklength_range': '8..16'
                    },
                    '37.0.0.0/8 24..32': {
                        'prefix': '37.0.0.0/8',
                        'masklength_range': '24..32'
                    },
                    '38.0.0.0/8 16..24': {
                        'prefix': '38.0.0.0/8',
                        'masklength_range': '16..24'
                    }
                }
            },
            'test6': {
                'prefix_set_name': 'test6',
                'protocol': 'ipv6',
                'prefixes': {
                    '2001:db8:1::/64 64..64': {
                        'prefix': '2001:db8:1::/64',
                        'masklength_range': '64..64'
                    },
                    '2001:db8:2::/64 65..128': {
                        'prefix': '2001:db8:2::/64',
                        'masklength_range': '65..128'
                    },
                    '2001:db8:3::/64 64..128': {
                        'prefix': '2001:db8:3::/64',
                        'masklength_range': '64..128'
                    },
                    '2001:db8:4::/64 65..98': {
                        'prefix': '2001:db8:4::/64',
                        'masklength_range': '65..98'
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Thu Jul 20 12:07:25.163 EDT
        Listing for all Prefix Set objects

        prefix-set test
             35.0.0.0/8,
             35.0.0.0/8 le 16,
             36.0.0.0/8 le 16,
             37.0.0.0/8 ge 24,
             38.0.0.0/8 ge 16 le 24
        end-set
        !
        prefix-set test6
            2001:db8:1::/64,
             2001:db8:2::/64 ge 65,
             2001:db8:3::/64 le 128,
             2001:db8:4::/64 ge 65 le 98
        end-set
        !
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRplPrefixSet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRplPrefixSet(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
