

set(CMAKE_MODULE_PATH ${CMAKE_ROOT}/Modules)
list(APPEND CMAKE_MODULE_PATH ${CMAKE_INSTALL_PREFIX}/share/cmake)
message("module path: " ${CMAKE_MODULE_PATH})

include(pods)

pods_find_pkg_config(eigen3 3.2)

if (eigen3_FOUND)
   pods_use_pkg_config_includes( eigen3 )
else()
   # then use the traditional approach to finding Eigen3
   find_package( Eigen3 3.2 )
   if (EIGEN3_FOUND)
      set(eigen3_FOUND 1)
      include_directories( ${EIGEN3_INCLUDE_DIR} )
   else()
      message(FATAL_ERROR "Could not find eigen, which is a required depedency")
   endif()
endif()

include(SwigPython)
add_swig_python_module(wrapperPython wrapper.i
                       CPLUSPLUS
                       INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
                       SWIG_INCLUDE_DIRS ${CMAKE_INSTALL_PREFIX}/share/swig/python ${CMAKE_INSTALL_PREFIX}/share/swig/common
                       DESTINATION ${CMAKE_CURRENT_SOURCE_DIR})