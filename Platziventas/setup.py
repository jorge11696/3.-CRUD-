from setuptools import setup


setup( #Definimos como vamos a invocar a nuestra linea de comandos
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)
