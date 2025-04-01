cmake_minimum_required(VERSION 3.31.3)

# Project languages
project(ti_adc C CXX ASM)

# Set exec name
set(EXEC ${PROJECT_NAME})

# Compile options
set(C_STANDARD 11)
set(CXX_STANDARD 11)

# Configure project sources
include(sources.cmake)

# Set executable output file
add_executable(${EXEC} ${BAREMETALSRC} )

# Set include directories
target_include_directories(${EXEC} PRIVATE ${BAREMETALINC} )

# Defines for TIVA SDK libraries
target_compile_definitions(${EXEC} PUBLIC
    PART_TM4C1294NCPDT=1
)

# Compile options
target_compile_options(${EXEC} PRIVATE
    -mcpu=cortex-m4
    -mfpu=fpv4-sp-d16 
    -march=armv7e-m
    -mthumb
    -mfloat-abi=hard
    -specs=nano.specs
    -fdata-sections
    -ffunction-sections
    -c 
    -fmessage-length=0
    -Wall
    -g 
    -gdwarf-2 
    -Og
)

# Link options
target_link_options(${EXEC} PRIVATE
    -T${CMAKE_SOURCE_DIR}/sdk/ldscript/linkerfile.ld
    -mcpu=cortex-m4
    -march=armv7e-m
    -mfpu=fpv4-sp-d16 
    -mthumb
    -mfloat-abi=hard
    -lc
    -lm
    --specs=nano.specs
    -Wl,-Map=${EXEC}.map,--cref
    -Wl,--gc-sections
    -Wl,--no-warn-rwx-segments 
)

# Указываем путь, где лежит libdriver.a
target_link_directories(${EXEC} PRIVATE sdk/driverlib/static)

# Линкуем библиотеку (указываем только "driver")
target_link_libraries(ti_adc driver)

# Post build options
include(postbuild.cmake)