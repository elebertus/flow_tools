from setuptools import setup, find_packages

setup(
    name="flow_tools",
    version="0.1.0",
    py_modules=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "flow_tools = ratios:cli",
        ],
    },
)
