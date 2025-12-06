from setuptools import setup, find_packages


setup(name='ssqaapitest',
      version='1.0',
      description="Practice API testing",
      author='Admas Kinfu',
      author_email='admas@supersqa.com',
      url='https://supersqa.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==8.3.4",
          "pytest-html==4.1.1",
          "requests==2.32.3",
          "requests-oauthlib==2.0.0",
          "PyMySQL==1.1.1",
          "woocommerce==3.0.0"
      ]
      )