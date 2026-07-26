cmake_minimum_required(VERSION 3.5...4.0)

project(chunkfs
	LANGUAGES C
	)


set(VERSION 0.8)
add_definitions(-DVERSION="${VERSION}")
set(CMAKE_CXX_FLAGS "-O3 -Wall -Wextra -Wshadow -Wconversion -Wcast-qual -Wformat=2 ${CMAKE_CXX_FLAGS}")

include(GNUInstallDirs)
mark_as_advanced(CLEAR
    CMAKE_INSTALL_BINDIR
    CMAKE_INSTALL_DOCDIR
    CMAKE_INSTALL_MANDIR
	)

add_executable(chunkfs
    chunkfs.c
	utils.c
	)

target_link_libraries(chunkfs fuse)

add_executable(unchunkfs
    unchunkfs.c
	utils.c
	)

target_link_libraries(unchunkfs fuse)

# Define the manpage output file
set(MANPAGE_OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/chunkfs.1")

# Custom command to generate the manpage
add_custom_command(
    OUTPUT ${MANPAGE_OUTPUT}
    COMMAND pod2man
        --center=""
        --name="CHUNKFS"
        --release="ChunkFS ${VERSION}"
        --section=1
        "${CMAKE_SOURCE_DIR}/manpage.pod"
        "${MANPAGE_OUTPUT}"
    DEPENDS "${CMAKE_SOURCE_DIR}/manpage.pod"
    COMMENT "Generating chunkfs.1 manpage"
    VERBATIM
)

# Custom target to depend on the manpage output
add_custom_target(
    manpage
    ALL
    DEPENDS ${MANPAGE_OUTPUT}
)

execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink  chunkfs.1 unchunkfs.1
                WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

install(TARGETS chunkfs unchunkfs
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
	)

install(FILES ${CMAKE_BINARY_DIR}/chunkfs.1 ${CMAKE_BINARY_DIR}/unchunkfs.1

    DESTINATION ${CMAKE_INSTALL_MANDIR}/man1
	)

install(FILES ${CMAKE_SOURCE_DIR}/writeoverlay.sh
    DESTINATION ${CMAKE_INSTALL_DOCDIR}/examples
	)
