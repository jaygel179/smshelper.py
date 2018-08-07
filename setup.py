from setuptools import setup

setup(
    name='smshelper',
    version='0.0.1',
    description='SMS helper and tool',
    long_description='SMS tool that can help you properly count the length of an SMS, calculate the part and what encoding it is.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    url='https://github.com/jaygel179/smshelper',
    author='Elpedio Adoptante Jr',
    author_email='adoptante.elpedio@gmail.com',
    license='MIT',
    packages=['smshelper'],
    install_requires=[
        'markdown',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
