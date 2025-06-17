**Project file structure before migration:**

```
/firmware
├── firmware.ino            
├── config.h
├── hardware_config.h
├── chat_logic.cpp/h
├── display.cpp/h
├── keyboard.cpp/h
├── comm.cpp/h
└── goertzel.cpp/h
```

**Project file structure after migration:**

```
firmware/
├── platformio.ini
├── src/
│   ├── main.cpp
│   ├── chat_logic.cpp
│   ├── display.cpp
│   ├── keyboard.cpp
│   ├── comm.cpp
│   └── goertzel.cpp
├── include/
│   ├── config.h
│   ├── hardware_config.h
│   ├── chat_logic.h
│   ├── display.h
│   ├── keyboard.h
│   ├── comm.h
│   └── goertzel.h
└──test/
```

---
## **Migration Steps (Mac OS)**

### **General Setup**

1. Set Up PlatformIO - as an extension in VSCode: https://platformio.org/install/ide?install=vscode
2. Back up your original Arduino project (`~/<your path>/firmware`)
3. Make need to give VSCode and/or Terminal some permissions here in order to be able to upload to the Teensy (will likely be prompted to do this later):
![alt text](<InputMonitoringSettings.png>)


### Migrate using `pio` (CLI for PlatformIO)

Can also reference: https://docs.platformio.org/en/latest/core/quickstart.html#core-quickstart

1. May need to get access to pio in your terminal is you're using the PlatformIO VS Code extension:

   If you want pio to work in any terminal window (not just in VS Code), you can install the CLI directly:

    `pip3 install -U platformio`

    Then add this to your ~/.zshrc:

    `export PATH="$HOME/.platformio/penv/bin:$PATH"`

    And reload:

    `source ~/.zshrc`

    Then try:

    `pio --version`

2. Cd into `~/<your path>/firmware` and create a new PlatformIO project with `pio project init --board teensy40`
   This will create:

    - include - Put project header files here
    - lib - Put project specific (private) libraries here
    - src - Put project source files here
    - platformio.ini - Project Configuration File

3. Move and rename files:
   1. Rename `firmware.ino` to `main.cpp`
   2. Move all .cpp files (including `main.cpp`) to `src/`
   3. Move all .h files to `include/`
   4. (Not relevant to this project) Move all project specific (private) libraries to `lib/`

4. Configure `platformio.ini` to declare your libraries
   Open the platformio.ini file created by PlatformIO in your project root. Replace its contents with the following :

   ```
    [env:teensy40]
    platform = teensy
    board = teensy40
    framework = arduino

    lib_deps =
      kurte/ILI9341_t3n
    ```

    Note: any libs that are part of the Teensy core do not need to be listed.
    You can confirm this for any lib by searching the Teensy core source files:
    1. `cd ~/.platformio/packages/framework-arduinoteensy`
    2. `find . -name <lib_name>.h`

5. (Optional if your project has dependencies) Run `pio pkg install` from project root to install all dependencies

6. Run `pio run` from project root to compile

7. More common `pio` commands:

> See https://piolabs.com/blog/news/platformio-core-6-0-released.html for other helpful package management commands

| Purpose                  | `pio` command                          |
| ------------------------ | -------------------------------------- |
| Compile your code        | `pio run`                              |
| Upload firmware to board | `pio run --target upload`              |
| Monitor serial output    | `pio device monitor`                   |
| Install libs             | `pio pkg install` or `pio lib install` |
| Run unit tests           | `pio test` or `pio run -t test`        |

---

### Migrate using VS Code/Platformio GUI

Use Quick Start instructions for reference: https://docs.platformio.org/en/latest/integration/ide/vscode.html#quick-start

Will still have to manually change file names - refer to step 5 from the CLI setup instructions.

