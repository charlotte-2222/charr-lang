from distutils.core import setup

setup(name="Charr Language",
      version="0.0.1",
      description="A simple language for programming",
      author="Charlotte Childers",
      author_email="ayy.charlotte@gmail.com",
      url="https://charlotte-2222.github.io/char-site/",
      packages=["charr"],
      package_dir={"charr": "charr"},
      package_data={"charr": ["*.charr"]},
      scripts=["compiler/__main__.py"],
      py_modules=["charr.charr"]
      )

