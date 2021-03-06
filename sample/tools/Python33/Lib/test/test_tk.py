from test import support
# Skip test if _tkinter wasn't built.
support.import_module('_tkinter')

# Skip test if tk cannot be initialized.
from tkinter.test.support import check_tk_availability
check_tk_availability()

from tkinter.test import runtktests

def test_main(enable_gui=False):
    if enable_gui:
        if support.use_resources is None:
            support.use_resources = ['gui']
        elif 'gui' not in support.use_resources:
            support.use_resources.append('gui')

    support.run_unittest(
            *runtktests.get_tests(text=False, packages=['test_tkinter']))

if __name__ == '__main__':
    test_main(enable_gui=True)
