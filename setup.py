from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.main:main',  # Посилання на функцію main() з clean_folder.main
        ],
    },
    install_requires=[
        # Залежності вашого пакету, якщо є
    ],
)