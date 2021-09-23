import platform
import sys
from setuptools import setup
from setuptools import Extension


# ABI 3 compatibility for the wheel
if sys.version_info >= (3,) and platform.python_implementation() == 'CPython':
    try:
        import wheel.bdist_wheel
    except ImportError:
        cmdclass = {}
    else:
        class bdist_wheel(wheel.bdist_wheel.bdist_wheel):
            def finalize_options(self):
                self.py_limited_api = 'cp3{}'.format(sys.version_info[1])
                super().finalize_options()

        cmdclass = {'bdist_wheel': bdist_wheel}


setup(
    name='hello-world-go',
    setup_requires=['setuptools-golang'],
    ext_modules=[
        Extension(
            'hello_world_go',
            ['hello_world_go.go'],

            # ABI 3 compatibility for the extension
            py_limited_api=True,
            define_macros=[('Py_LIMITED_API', None)],
        ),
    ],
    build_golang={'root': 'github.com/fredrikaverpil/python-go-extension'},
    cmdclass=cmdclass,
)
