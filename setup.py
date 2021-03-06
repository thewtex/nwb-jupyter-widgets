from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    author='Neurodata Without Border (NWB) developers',
    author_email='matt.mccormick@kitware.com',
    classifiers=['Operating System :: OS Independent',
                 'Development Status :: 3 - Alpha',
                 'Framework :: Jupyter',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 ],
    description='This is nwb-jupyter-widgets, widgets for viewing the contents of a '
                'NWB-file in Jupyter Notebooks using ipywidgets.',
    install_requires=['pynwb', 'itkwidgets', 'ipympl', 'ipywidgets>=7.4', 'matplotlib', 'numpy'],
    license='MIT',
    keywords=['jupyter', 'hdf5', 'notebook', 'nwb'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='nwbwidgets',
    packages=['nwbwidgets'],
    python_requires='>=2.7',
    setup_requires=['setuptools>=38.6.0', 'setuptools_scm'],
    url='https://github.com/NeurodataWithoutBorders/nwb-jupyter-widgets',
    use_scm_version=True)
