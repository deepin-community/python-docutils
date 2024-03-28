#!/usr/bin/env python3

# $Id: test_null.py 9277 2022-11-26 23:15:13Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Test for Null writer.
"""

from pathlib import Path
import sys
import unittest

if __name__ == '__main__':
    # prepend the "docutils root" to the Python library path
    # so we import the local `docutils` package.
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from docutils.core import publish_string


class WriterPublishTestCase(unittest.TestCase):
    def test_publish(self):
        writer_name = 'null'
        for name, cases in totest.items():
            for casenum, (case_input, case_expected) in enumerate(cases):
                with self.subTest(id=f'totest[{name!r}][{casenum}]'):
                    output = publish_string(
                        source=case_input,
                        writer_name=writer_name,
                        settings_overrides={
                            '_disable_config': True,
                            'strict_visitor': True,
                        },
                    )
                    if isinstance(output, bytes):
                        output = output.decode('utf-8')
                    self.assertEqual(output, case_expected)


totest = {}

totest['basic'] = [
["""\
This is a paragraph.
""",
None]
]

if __name__ == '__main__':
    unittest.main()
