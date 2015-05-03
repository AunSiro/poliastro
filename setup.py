#!/usr/bin/env python

from setuptools import setup


if __name__ == '__main__':
    setup(name="poliastro",
          version='0.3.0-dev',
          description="poliastro - Python package for Orbital Mechanics",
          author="Juan Luis Cano",
          author_email="juanlu001@gmail.com",
          url="http://poliastro.github.io/",
          download_url="https://github.com/poliastro/poliastro",
          license="MIT",
          keywords=[
              "aero", "aerospace", "engineering",
              "astrodynamics", "orbits", "kepler", "orbital mechanics"
          ],
          requires=["numpy", "numba", "astropy", "pytest"],
          packages=['poliastro', 'poliastro.twobody'],
          classifiers=[
              "Development Status :: 3 - Pre-Alpha",
              "Intended Audience :: Education",
              "Intended Audience :: Science/Research",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
              "Programming Language :: Python",
              "Programming Language :: Python :: 3",
              "Programming Language :: Python :: Implementation :: CPython",
              "Topic :: Scientific/Engineering",
              "Topic :: Scientific/Engineering :: Physics",
              "Topic :: Scientific/Engineering :: Astronomy",
          ],
          long_description=open('README').read(),
          package_data={"poliastro": ['tests/*.py']})
