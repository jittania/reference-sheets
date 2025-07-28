# Writing and Running Unit Tests for Arduino with PlatformIO + Unity

## General Notes On Writing Unity Tests For Arduino

1.  **PlatformIO lets you organize tests into folders:** Each subfolder (like test/receiving/test_parse_message/) is treated as a separate test application. You can group related tests into their own directories for modularity.

    ```
    test/
    ├── receiving/
    │   ├── test_bit_decoder/
    │   │   └── bit_decoder.cpp         ← test suite (file)
    │   ├── test_packet_parser/
    │   │   └── packet_parser.cpp       ← test suite (file)
    ├── transmitting/
    │   ├── test_packetizer/
    │   │   └── packetizer.cpp          ← test suite (file)
    ```

    Each file (test suite) might contain multiple test cases:

    ```
    void test_valid_packet_is_created() { ... }

    void test_empty_input_returns_error() { ... }
    ```

2. **Folder depth doesn't matter:** Test files can be nested arbitrarily deep and PlatformIO will still find them as long as the test file and containing subfolder itself is prefixed with `test_`.

3. **Make sure to configure your `platformio.ini` file correctly:** I had to add `test_build_src = yes` to get tests to work.

4. **When writing unit tests in Platformio using the Arduino framework, each test file has 4 default functions: `setUp`, `tearDown`, `setup` and `loop`**
   - Functions `setUp` and `tearDown` are used to initialize and finalize test conditions. Implementations of these functions are not required for running tests, but if you need to initialize some variables before you run a test, use `setUp`. Likewise, if you need to clean up variables, use `tearDown`.
   - The `setup` and `loop` functions act as a simple Arduino program where we describe our test plan.

---

## Arduino/Teensy/Unity Test Template

    ```
    #include <Arduino.h>
    #include <unity.h>

    #include "file_with_func.h"

    void setUp(void) {
      // optional: runs before each test case
      // use to initialize test variables, reset globals, clear buffers,
      // or set known hardware states before each test
    }

    void tearDown(void) {
      // optional: runs after each test case
      // use to free memory, reset mock counters or flags,
      // or clean up any state that could affect the next test
    }

    void test_your_test_name_here() {
      // test logic here
    }

    void setup() {
      UNITY_BEGIN(); // starts testing session
      RUN_TEST(test_your_test_name_here);
      UNITY_END(); // ends testing session
    }

    void loop() {
      // optional: runs continuously after setup()
      // usually left empty in tests, unless doing async checks or timing
    }
    ```

**Refer to these resources for Unity syntax to use in test case logic:**
   - https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityAssertionsReference.md
   - https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityAssertionsCheatSheetSuitableforPrintingandPossiblyFraming.pdf

---
## Configuring `platformio.ini`

**Example of configuring `platformio.ini` to only use one environment (for both testing and production):**

Remember to add `test_build_src = true` if you want to be able to write tests that use code from src/. It includes everything in /src (your production firmware code) in the test build.
Without it, your test file can’t call functions that exist in /src unless you duplicate the implementation.
HOWEVER, with it, this also means you can't use setup() and loop() in your test because main.cpp also gets included, and the linker exploded with 'multiple definition of `setup`' errors. If you want to use use setup() and loop() in your tests (best practice for Arduino projects), you have to add a second environment - see next `platformio.ini` example.

```
[env:teensy40]
platform = teensy
board = teensy40
framework = arduino
lib_deps =
  kurte/ILI9341_t3n
; run using: pio run -e teensy40 -t upload

[env:teensy40_test]
platform = teensy
board = teensy40
framework = arduino
lib_deps =
  kurte/ILI9341_t3n
build_flags = -DUNIT_TEST -Itest
test_build_src = true
; run using: pio test -e teensy40_test
```

---

## Overview of basic pio syntax

>Note that environment names need to match the labels used in `platformio.ini`

- `-e, --environment` -> use to select environment
- `-f, --filter` -> use with `pio test` to process only test suites whose path relative to the test_dir matches the specified pattern
- `-v, -vv, -vvv` -> use to control verbosity level of output

### **General purpose commands:**
>For a complete list of pio commands, go [here](https://docs.platformio.org/en/latest/core/userguide/index.html#commands)

| Purpose                  | `pio` command                          |
| ------------------------ | -------------------------------------- |
| Compile your code        | `pio run`                              |
| Upload firmware to board | `pio run --target upload`              |
| Monitor serial output    | `pio device monitor`                   |

### **Command line options for running tests:**
>For a complete list of pio test commands, go [here](https://docs.platformio.org/en/latest/core/userguide/cmd_test.html)

| Purpose                   | `pio` command                                         |
|---------------------------|-------------------------------------------------------|
| Run all tests              | `pio test -e teensy40_test`                           |
| Run all tests with Serial monitor output | `pio test -e teensy40_test -v`   |
| Run all receiving/ tests   | `pio test -e teensy40_test -f "receiving/*"`          |
| Run only one test          | `pio test -e teensy40_test -f "receiving/test_parse_message"` |

---

# Resources:

- **Conventions for naming/organizing tests so Platformio can find them:**  https://docs.platformio.org/en/latest/advanced/unit-testing/structure/hierarchy.html
- **Best practices for writing Platformio tests:** https://docs.platformio.org/en/latest/advanced/unit-testing/structure/best-practices.html
- **Writing unit tests in Platformio using the Arduino framework:** https://docs.platformio.org/en/latest/tutorials/espressif32/arduino_debugging_unit_testing.html#writing-unit-tests
