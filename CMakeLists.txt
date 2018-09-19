cmake_minimum_required(VERSION 2.6)
project(mc_watchdog_bip)


configure_file(mc_watchdog_bip.pc.in mc_watchdog_bip.pc @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/mc_watchdog_bip.pc
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/pkgconfig)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/BipModel/lib/libpack__InterfaceView.a
              ${CMAKE_CURRENT_SOURCE_DIR}/BipEngine/lib/libengine.a
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/BipEngine/include/generic/
                  ${CMAKE_CURRENT_SOURCE_DIR}/BipEngine/include/specific/
                  ${CMAKE_CURRENT_SOURCE_DIR}/BipModel/include/
        DESTINATION ${CMAKE_INSTALL_PREFIX}/include/${CMAKE_PROJECT_NAME})
