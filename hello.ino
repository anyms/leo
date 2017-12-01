#include "Keyboard.h"

/*******************
Copyright:  https://tamilwired.com
Date:       27/11/2017
Author:     Jeeva
URL:        https://github.com/anyms/leo
********************/

void typeKey(int key) {Keyboard.press(key);delay(50);Keyboard.release(key);}void combo(int key, char letter) {Keyboard.press(key);Keyboard.press(letter);Keyboard.releaseAll();}void setup() {Keyboard.begin();delay(1000);combo(KEY_LEFT_GUI, 'r');delay(1000);Keyboard.print("notepad");typeKey(KEY_RETURN);delay(1000);for (int _i = 0; _i < 100; _i++) {char buf[30];sprintf(buf, "hello\" %d 1000", _i);Keyboard.print(buf);typeKey(KEY_RETURN);delay(100);}Keyboard.end();}void loop() {}