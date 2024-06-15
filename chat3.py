def control_signals(instruction):
  """Returns the control signals for the given DLX instruction."""

  # The first two clock cycles are always the same.
  control_signals = {
      "RegDst": 0,
      "ALUOp": 2,
      "ALUSrc": 1,
      "MemRead": 0,
      "MemWrite": 0,
  }

  # The remaining clock cycles depend on the instruction type.
  if instruction == "sub":
    control_signals["ALUOp"] = 2
  elif instruction == "addi":
    control_signals["ALUOp"] = 1
  elif instruction == "lhi":
    control_signals["ALUOp"] = 4
  elif instruction == "jal":
    control_signals["RegDst"] = 1
    control_signals["ALUOp"] = 3
  elif instruction == "sh":
    control_signals["MemWrite"] = 1
  elif instruction == "bnez":
    control_signals["ALUOp"] = 5
  elif instruction == "slti":
    control_signals["ALUOp"] = 6
  elif instruction == "srl":
    control_signals["ALUOp"] = 7

  return control_signals


def main():
  print(control_signals("sub"))
  print(control_signals("addi"))
  print(control_signals("lhi"))
  print(control_signals("jal"))
  print(control_signals("sh"))
  print(control_signals("bnez"))
  print(control_signals("slti"))
  print(control_signals("srl"))


if __name__ == "__main__":
  main()
