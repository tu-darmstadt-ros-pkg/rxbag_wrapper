cmake_minimum_required(VERSION 2.8.3)
project(rxbag_wrapper)

find_package(catkin REQUIRED)
catkin_python_setup()

# install env_hook to append ROS_PACKAGE_PATH
get_filename_component(wxpython_swig_interface_PACKAGE_PATH ../src/rx/wxpython_swig_interface ABSOLUTE)
get_filename_component(rxbag_PACKAGE_PATH ../src/rx/rxbag ABSOLUTE)
get_filename_component(rxbag_plugins_PACKAGE_PATH ../src/visualization/rxbag_plugins ABSOLUTE)
catkin_add_env_hooks(55.rxbag_wrapper SHELLS sh SKIP_INSTALL)

# add wxpython_swig_interface and rxbag as subdirectories
add_subdirectory(../src/rx/wxpython_swig_interface wxpython_swig_interface)
add_subdirectory(../src/rx/rxbag rxbag)

# special rules to wrap rxbag_plugins
install(
  FILES ../src/visualization/rxbag_plugins/manifest.xml
  DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/rxbag_plugins/
)
install(
  DIRECTORY ../src/visualization/rxbag_plugins/icons
  DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/rxbag_plugins/
)
