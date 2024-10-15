
#define KEY_LANG  10
#define KEY_COLS  9
#define KEY_CAPS  8

#define OUT_LANG  0
#define OUT_COLS  1
#define OUT_CAPS  2

#define LED_CAPS  3

bool lang_state = false;
bool cols_state = false;
bool caps_state = false;

void setup() {
  pinMode(KEY_LANG, INPUT_PULLUP);
  pinMode(KEY_COLS, INPUT_PULLUP);
  pinMode(KEY_CAPS, INPUT_PULLUP);

  pinMode(OUT_LANG, OUTPUT);
  digitalWrite(OUT_LANG, LOW);
  
  pinMode(OUT_COLS, OUTPUT);
  digitalWrite(OUT_COLS, LOW);
  
  pinMode(OUT_CAPS, INPUT);

  pinMode(LED_CAPS, OUTPUT);
}

void loop() {

  if (digitalRead(KEY_LANG) == LOW) {
    while (digitalRead(KEY_LANG) == LOW) {
      delay(100);
    }
    if (!lang_state) {
      lang_state = true;
      digitalWrite(OUT_LANG, HIGH);
    } else {
      lang_state = false;
      digitalWrite(OUT_LANG, LOW);      
    }
  }

  if (digitalRead(KEY_COLS) == LOW) {
    while (digitalRead(KEY_COLS) == LOW) {
      delay(100);
    }
    if (!cols_state) {
      cols_state = true;
      digitalWrite(OUT_COLS, HIGH);
    } else {
      cols_state = false;
      digitalWrite(OUT_COLS, LOW);      
    }
  }

  if (digitalRead(KEY_CAPS) == LOW) {
    while (digitalRead(KEY_CAPS) == LOW) {
      delay(100);
    }
    if (caps_state) {
      caps_state = false;
      pinMode(OUT_CAPS, INPUT);
      digitalWrite(LED_CAPS, LOW);      
    } else {
      caps_state = true;
      pinMode(OUT_CAPS, OUTPUT);
      digitalWrite(OUT_CAPS, LOW);      
      digitalWrite(LED_CAPS, HIGH);    
    }
  }
}
