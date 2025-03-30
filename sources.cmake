# Setting SDK sources
set(BAREMETALSRC
    # Startup scripts
    sdk/startup/tm4c1294ncpdt_startup_ccs_gcc.c

    # Entry point
    core/main.c
)

# Setting SDK includes
set(BAREMETALINC
    sdk/CMSIS/inc

    # Driver peripheral library
    lib/driverlib/inc
)

