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
    include_package_data=True,
)
