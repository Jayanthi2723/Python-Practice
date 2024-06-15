#include <iostream>

using namespace std;

int main() {
  const int NUM_ROWS = 2;
  const int NUM_COLS = 2;
  int miles_tracker[NUM_ROWS][NUM_COLS] = {
    {-10, 20},
    {30, 40}
  };

  int max_miles = miles_tracker[0][0];
  int min_miles = miles_tracker[0][0];

  for (int i = 0; i < NUM_ROWS; i++) {
    for (int j = 0; j < NUM_COLS; j++) {
      if (miles_tracker[i][j] > max_miles) {
        max_miles = miles_tracker[i][j];
      } else if (miles_tracker[i][j] < min_miles) {
        min_miles = miles_tracker[i][j];
      }
    }
  }

  cout << "Max miles: " << max_miles << endl;
  cout << "Min miles: " << min_miles << endl;

  return 0;
}
