from setuptools import setup, find_packages

setup(
    name='ChatTTS',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'omegaconf~=2.3.0',
        'torch~=2.0',
        'tqdm',
        'einops',
        'vector_quantize_pytorch',
        'transformers~=4.41.1',
        'vocos',
    ],
    include_package_data=True,
)
