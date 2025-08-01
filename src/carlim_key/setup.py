from setuptools import find_packages, setup

package_name = 'carlim_key'

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
    maintainer='limdoyeon',
    maintainer_email='limdoyeon@todo.todo',
    description='Remote keyboard controller for car robot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'car_key = carlim_key.car_key:main'
        ],
    },
)
