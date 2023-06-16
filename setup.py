import setuptools

__VERSION__ = '0.0.2'

setuptools.setup(
    name='ak-ipatool-py',
    version=__VERSION__,
    entry_points={
        'console_scripts': [
            'ipatoolpy = main:main'
        ]
    },
    author='appknox',
    author_email='engineering@appknox.com',
    url='https://github.com/appknox/ak-ipatool-py',
    description='Appknox forked ipatoolpy is a command line tool that allows you to search for iOS apps on the App Store and download a copy of the app package, known as an ipa file.',
    packages=['reqs'],
    install_requires=[
        'setuptools',
        'requests',
        'rich'
    ],
    python_requires='>=3.7'
)