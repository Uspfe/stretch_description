from setuptools import setup, find_packages
from glob import glob

package_name = 'stretch_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    install_requires=['setuptools'],
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='Minimal ROS 2 Python package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dynamic_tf_broadcaster = stretch_description.dynamic_tf_broadcaster:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/meshes', glob('meshes/*')),
        ('share/' + package_name + '/urdf', glob('urdf/*.xacro')),
        ('share/' + package_name + '/rviz', glob('rviz/*')),
    ],
)