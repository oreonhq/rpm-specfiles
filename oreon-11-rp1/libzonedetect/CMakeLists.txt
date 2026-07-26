cmake_minimum_required(VERSION 3.4)

project(libzonedetect C)
include(GNUInstallDirs)

set(LIBMAJOR 0)
set(LIBMINOR 0)
set(LIBPOINT 0)
set(LIBVER "${LIBMAJOR}.${LIBMINOR}.${LIBPOINT}")

set(zonedetect_SRC
    library/zonedetect.c
)

### Build library / tools

include_directories(${CMAKE_SOURCE_DIR}/library)
add_library(zonedetect SHARED ${zonedetect_SRC})
target_link_libraries(zonedetect m)
set_target_properties(zonedetect PROPERTIES VERSION ${LIBVER} SOVERSION ${LIBMAJOR})
if(WIN32)
    set_target_properties(zonedetect PROPERTIES SUFFIX "-${LIBMAJOR}${CMAKE_SHARED_LIBRARY_SUFFIX}")
endif(WIN32)

add_executable(ZoneDetect demo.c)
target_link_libraries(ZoneDetect zonedetect)

### Installation

install(TARGETS zonedetect
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(TARGETS ZoneDetect DESTINATION ${CMAKE_INSTALL_BINDIR})

install(FILES library/zonedetect.h DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
