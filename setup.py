from setuptools import setup, find_packages
 
setup(
    name='django-nice-types',
    version='0.1.0',
    description='Misc types',
    author='Hisham Zarka',
    author_email='hzarka@gmail.com',
    url='http://github.com/hzarka/django-nice-types/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=True,
)
