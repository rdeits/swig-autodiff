include(SwigPython)
add_swig_python_module(wrapperPython wrapper.i
                       CPLUSPLUS
                       INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
                       SWIG_INCLUDE_DIRS ${CMAKE_INSTALL_PREFIX}/share/swig/python ${CMAKE_INSTALL_PREFIX}/share/swig/common
                       DESTINATION ${CMAKE_CURRENT_SOURCE_DIR})