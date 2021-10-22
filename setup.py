from setuptools import setup, find_packages

NAME = 'pytorch-meta-dataset'

with open("requirements.txt", "r") as f:
    install_requirements = f.readlines()


def run_setup():
    setup(
        name=NAME,
        version='0.1',
        description='Pytorch Meta Dataset',
        author='NA',
        author_email='NA',
        url="NA",
        install_requires=install_requirements,
        packages=find_packages(),
    )


if __name__ == "__main__":
    run_setup()
