#include "Keyboard.h"

/*******************
Copyright:  https://tamilwired.com
Date:       27/11/2017
Author:     Jeeva
URL:        https://github.com/anyms/leo
********************/

void typeKey(int key) {Keyboard.press(key);delay(50);Keyboard.release(key);}void combo(int key, char letter) {Keyboard.press(key);Keyboard.press(letter);Keyboard.releaseAll();}void setup() {Keyboard.begin();Keyboard.print(hello1000);delay(1000);for (int _i = 0; _i < 10; _i++) {char buf[30];sprintf(buf, "this is from arduino %d 1000", _i);Keyboard.print(buf);typeKey(KEY_RETURN);delay(1000);}Keyboard.end();}void loop() {}