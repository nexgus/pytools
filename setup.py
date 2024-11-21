from setuptools import setup, find_packages


def find_version(filepath) -> str:
    # major.minor[.patch[.sub]]
    target = "version_string = '"
    with open(filepath, 'r') as fp:
        while True:
            line = fp.readline()
            if len(line) == 0:
                return '0.1.0'

            line = line.strip()
            if not line.startswith(target):
                continue

            return line[len(target):-1]


setup(
    name='pytools',
    version=find_version('pytools/version.py'),
    description='Useful Python tools',
    maintainer='Augustus Chen',
    maintainer_email='augustuschen@nexcom.com.tw',
    packages=find_packages(),
    platforms=[
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    license='License :: OSI Approved :: MIT License',
)
