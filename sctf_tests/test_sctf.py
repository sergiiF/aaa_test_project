__author__ = 'sergii'
import os


def test_hello_world():
    test_dir = os.path.dirname(__file__)
    test_script = os.path.join(test_dir, 'sctfile_ws_macro')
    cmd = ' '.join(('sct',
                    '-v -v -f',
                    test_script,
                    'hello_world.macro_check_hello'))
    cmd = 'PYTHONPATH=$PYTHONPATH:%s && %s' % (test_dir, cmd)
    assert os.system(cmd) == 0
