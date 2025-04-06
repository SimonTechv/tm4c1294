import os

app_name = "eval"

def options(opt):
    
    opt.load('compiler_c') # Подгружаем модуль компилятора C


def configure(conf): 

    conf.find_program('arm-none-eabi-gcc', var='CC')       # Компилятор
    conf.find_program('arm-none-eabi-gcc', var='LINK_CC')  # Компоновщик
    conf.find_program('arm-none-eabi-ar',  var='AR')       # Ассемблер

    # Подгружаем компилятор
    conf.load('gcc')


def build(bld):

    # Скрипт линковщика
    linker_script = bld.path.find_node('sdk/ldscript/linkerfile.ld')

    # Флаги компиляции
    bld.env.CFLAGS = [
        '-mcpu=cortex-m4',
        '-mfpu=fpv4-sp-d16', 
        '-march=armv7e-m',
        '-mthumb',
        '-mfloat-abi=hard',
        '-specs=nano.specs',
        '-fdata-sections',
        '-ffunction-sections',
        '-fmessage-length=0',
        '-Wall',
        '-g',
        '-c',
        '-gdwarf-2',
        '-Og'
    ]

    # Флаги линковки
    bld.env.LINKFLAGS = [
        f'-T{linker_script}',
        '-mcpu=cortex-m4',
        '-march=armv7e-m',
        '-mfpu=fpv4-sp-d16', 
        '-mthumb',
        '-mfloat-abi=hard',
        '-lc',
        '-lm',
        '--specs=nano.specs',
        '-Wl,--gc-sections',
        '-Wl,--no-warn-rwx-segments'
    ]

    # Заголовочные файлы
    includes = ['sdk/CMSIS/inc', 'sdk/driverlib/inc']

    # Исходные файлы
    sources  = [
        'sdk/startup/tm4c1294ncpdt_startup_ccs_gcc.c',
        'core/main.c'
    ]

    # Натравливаем WAF на проект
    bld(
        features='c cprogram',
        source=sources,         # Ваш исходный файл(ы)
        includes=includes,       # Заголовочные файлы
        target='app.elf',        # Имя выходного файла
    )