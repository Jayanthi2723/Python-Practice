def feistel_round(plaintext, key):
  """Implements a single round of the Feistel cipher.

  Args:
    plaintext: The plaintext to be encrypted.
    key: The encryption key.

  Returns:
    The ciphertext.
  """

  L0, R0 = plaintext[:4], plaintext[4:]
  R1 = L0 ^ f(R0, key)
  L1 = R0
  return R1 + L1

def f(R0, key):
  """Computes the round function F(R0, k).

  Args:
    R0: The left half of the plaintext.
    key: The encryption key.

  Returns:
    The output of the round function.
  """

  return (2 * R0 ** key) % 16

def text_to_binary(text):
  """Converts a string to a binary string.

  Args:
    text: The string to be converted.

  Returns:
    The binary string representation of the text.
  """

  binary_string = ""
  for char in text:
    binary_string += format(ord(char), "08b")
  return binary_string

def binary_to_text(binary_string):
  """Converts a binary string to a string.

  Args:
    binary_string: The binary string to be converted.

  Returns:
    The string representation of the binary string.
  """

  text = ""
  for i in range(0, len(binary_string), 8):
    byte = binary_string[i:i+8]
    text += chr(int(byte, 2))
  return text

def main():
  plaintext = "hello"
  key = "1010"
  ciphertext = ""
  for i in range(len(plaintext)):
    binary_plaintext = text_to_binary(plaintext[i])
    ciphertext += feistel_round(binary_plaintext, key)
  ciphertext = binary_to_text(ciphertext)
  print(ciphertext)

if __name__ == "__main__":
  main()
