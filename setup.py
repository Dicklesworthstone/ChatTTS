from setuptools import setup, find_packages

setup(
    name='ChatTTS',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'omegaconf',
        'torch',
        'tqdm',
        'einops',
        'vector_quantize_pytorch',
        'transformers',
        'vocos',
    ],
    dependency_links=[
        'https://download.pytorch.org/whl/nightly/cu121',
    ],
    extras_require={
        'pre': ['torch']
    },
    include_package_data=True,
)
