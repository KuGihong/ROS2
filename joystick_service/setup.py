from setuptools import setup
from setuptools import find_packages

package_name = 'joystick_service'

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
    maintainer='gihong',
    maintainer_email='gihong@todo.todo',
    description='Turtle Sim control using service with joystick',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'server = joystick_service.server:main',
        'client = joystick_service.client:main'
        ],
    },
)
