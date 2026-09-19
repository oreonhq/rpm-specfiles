# Set  the minimum  required version  of cmake  for a  project.
cmake_minimum_required(VERSION 3.5)
project(voro++)
include(GNUInstallDirs)

add_library(voro++ SHARED
	cell.cc
	common.cc
	container.cc
	unitcell.cc
	v_compute.cc
	c_loops.cc
	v_base.cc wall.cc
	pre_container.cc
	container_prd.cc
)
set_target_properties(voro++ PROPERTIES VERSION 0.0.0 SOVERSION 0)

add_executable(voro++-bin cmd_line.cc)
set_target_properties(voro++-bin PROPERTIES OUTPUT_NAME voro++)
target_link_libraries(voro++-bin voro++)

file(GLOB_RECURSE HDR RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.hh)

install(TARGETS voro++ LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
install(FILES ${HDR} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(TARGETS voro++-bin DESTINATION ${CMAKE_INSTALL_BINDIR})
