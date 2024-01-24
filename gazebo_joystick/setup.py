import os
import glob

from setuptools import find_packages
from setuptools import setup

package_name = 'gazebo_joystick'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', 'gz.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gihong',
    maintainer_email='gihong@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'gz_joy = gazebo_joystick.gz_joy:main'
        ],
    },
)
