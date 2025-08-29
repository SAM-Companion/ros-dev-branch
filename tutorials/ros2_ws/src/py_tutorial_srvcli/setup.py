from setuptools import find_packages, setup

package_name = 'py_tutorial_srvcli'

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
    description='Basic ros service and client.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'service = py_tutorial_srvcli.service_member_function:main',
                'client = py_tutorial_srvcli.client_member_function:main',
		'mult_service = py_tutorial_srvcli.mult_ints_service_func:main',
		'mult_client = py_tutorial_srvcli.mult_client_func:main',
        ],
    },
)
