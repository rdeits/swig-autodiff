cmake_minimum_required(VERSION 2.8)

project(SwigAutoDiffExternals)

# PODs out-of-source build logic
if (CMAKE_INSTALL_PREFIX STREQUAL "/usr/local" OR CMAKE_INSTALL_PREFIX STREQUAL "C:/Program Files/${PROJECT_NAME}")
    find_file(_build_dir build PATHS ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/.. ${PROJECT_SOURCE_DIR}/../.. ${PROJECT_SOURCE_DIR}/../../.. ${PROJECT_SOURCE_DIR}/../../../..)
    if (_build_dir)
        set(CMAKE_INSTALL_PREFIX "${_build_dir}")
    else()
        execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_SOURCE_DIR}/../build)
        set(CMAKE_INSTALL_PREFIX ${PROJECT_SOURCE_DIR}/../build)
    endif()
endif()
message(STATUS CMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX})

include(ExternalProject)

find_program(MAKE_EXECUTABLE make)
if (NOT MAKE_EXECUTABLE)
	message(FATAL_ERROR "couldn't find gnu make")
endif()
if (${CMAKE_GENERATOR} STREQUAL "Unix Makefiles")
	set(PODS_MAKE_COMMAND "$(MAKE)")   # so we can pass through commandline arguments.
else()
	set(PODS_MAKE_COMMAND ${MAKE_EXECUTABLE})
endif()

ExternalProject_Add(pods-cmake
    DOWNLOAD_DIR ${CMAKE_INSTALL_PREFIX}/share/cmake
    SOURCE_DIR ${CMAKE_INSTALL_PREFIX}/share/cmake
    GIT_REPOSITORY https://github.com/RobotLocomotion/cmake.git
    GIT_TAG 94a181859aca6512861084077066e1080678b819
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    )

ExternalProject_Add(swigmake
	SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/swigmake
	DOWNLOAD_DIR ${CMAKE_CURRENT_SOURCE_DIR}/swigmake
	GIT_REPOSITORY https://github.com/rdeits/swigmake.git
	GIT_TAG 02a79d96a44d88d5fd83469f4334612cf6e31d9c
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    )

ExternalProject_Add(cxx11-pod
	SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/cxx11-pod
	DOWNLOAD_DIR ${CMAKE_CURRENT_SOURCE_DIR}/cxx11-pod
	GIT_REPOSITORY https://github.com/rdeits/cxx11-pod.git
	GIT_TAG 6aec1ddba5e907a3b6f752b654787a3a5090a581
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    )

ExternalProject_Add(eigen-pod
	SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/eigen-pod
	DOWNLOAD_DIR ${CMAKE_CURRENT_SOURCE_DIR}/eigen-pod
	GIT_REPOSITORY https://github.com/RobotLocomotion/eigen-pod.git
	GIT_TAG ceba39500b89a77a8649b3e8b421b10a3d74d42b
	BUILD_IN_SOURCE 1
	CONFIGURE_COMMAND ""
	BUILD_COMMAND ${PODS_MAKE_COMMAND} BUILD_PREFIX=${CMAKE_INSTALL_PREFIX} BUILD_TYPE=${CMAKE_BUILD_TYPE}
	UPDATE_COMMAND ""
	INSTALL_COMMAND ""
	)
