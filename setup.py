
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='python-utils',
      version='0.1',
      description='General library for setting up linux-based environments for developing, running, and evaluating planners.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/AI-Planning/planning-utils',
      author='',
      author_email='',
      license='MIT',
      packages=['planning_utils'],
      scripts=['bin/planning-utils'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Linux",
      ],
      python_requires='>=3.6',
      include_package_data=True,
      zip_safe=False)