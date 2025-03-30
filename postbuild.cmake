# Print executable size
add_custom_command(TARGET ${EXEC}
        POST_BUILD
        COMMAND arm-none-eabi-size ${EXEC})

# Create hex file
add_custom_command(TARGET ${EXEC} POST_BUILD
    COMMAND arm-none-eabi-objcopy -O ihex ${EXEC} ${EXEC}.hex
    COMMAND arm-none-eabi-objcopy -O binary ${EXEC} ${EXEC}.bin
    COMMAND mv ${EXEC} ${EXEC}.elf
)