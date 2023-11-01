from setuptools import setup

setup(
    name='third_party_accern_parser',
    version='0.1',
    description='Unofficial Accern API. ' +
                'Provides access to all Accern features.',
    url='https://github.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/',
    author='Hiroki Fujii',
    author_email='hirokifujii10@gmail.com',
    license='GNU',
    packages=['acc_function'],
    zip_safe=False,
    install_requires=[
      "datasets",
      "pyarrow",
      "accern-data==0.0.4",
    ])