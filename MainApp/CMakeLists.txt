cmake_minimum_required(VERSION 3.5)
find_package(Qt5 5.5 COMPONENTS Core Gui Widgets REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(MainApp_SRCS
    main.cpp
    MainApp.cpp
    MainApp.h
    MainApp.ui
    Resources.qrc
    menubutton.cpp
    menubutton.h
    about.cpp
    about.h
    about.ui
)

add_executable(MainApp ${MainApp_SRCS})

target_link_libraries(MainApp PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
target_link_libraries(MainApp PRIVATE qtadvanceddocking)
target_include_directories(MainApp PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../Library/QtAds")
set_target_properties(MainApp PROPERTIES 
    AUTOMOC ON
    AUTORCC ON
    AUTOUIC ON
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED ON
    CXX_EXTENSIONS OFF
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)
