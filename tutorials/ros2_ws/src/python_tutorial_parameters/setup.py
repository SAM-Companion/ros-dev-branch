from setuptools import find_packages, setup

package_name = 'python_tutorial_parameters'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sam-robot-pi',
    maintainer_email='hawkswithmath@gmail.com',
    description='tutorial (for me) on ros node params',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'minimal_param_node = python_tutorial_parameters.python_params_node:main',
        ],
    },
)
