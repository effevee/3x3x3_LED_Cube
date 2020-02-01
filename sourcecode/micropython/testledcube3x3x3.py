import ledcube3x3x3

# pins
DATA = 19
CLOCK = 18
LATCH = 5

# frames
FRAME = [
    # ---------------------------------------
    # round and round
    # ---------------------------------------
    0b000000001, 0b000000000, 0b000000000, 150,
    0b000000010, 0b000000000, 0b000000000, 150,
    0b000000100, 0b000000000, 0b000000000, 150,
    0b000100000, 0b000000000, 0b000000000, 150,
    0b100000000, 0b000000000, 0b000000000, 150,
    0b010000000, 0b000000000, 0b000000000, 150,
    0b001000000, 0b000000000, 0b000000000, 150,
    0b000001000, 0b000000000, 0b000000000, 150,
    0b000010000, 0b000000000, 0b000000000, 150,
    #
    0b000000000, 0b000000001, 0b000000000, 150,
    0b000000000, 0b000000010, 0b000000000, 150,
    0b000000000, 0b000000100, 0b000000000, 150,
    0b000000000, 0b000100000, 0b000000000, 150,
    0b000000000, 0b100000000, 0b000000000, 150,
    0b000000000, 0b010000000, 0b000000000, 150,
    0b000000000, 0b001000000, 0b000000000, 150,
    0b000000000, 0b000001000, 0b000000000, 150,
    0b000000000, 0b000010000, 0b000000000, 150,
    #
    0b000000000, 0b000000000, 0b000000001, 150,
    0b000000000, 0b000000000, 0b000000010, 150,
    0b000000000, 0b000000000, 0b000000100, 150,
    0b000000000, 0b000000000, 0b000100000, 150,
    0b000000000, 0b000000000, 0b100000000, 150,
    0b000000000, 0b000000000, 0b010000000, 150,
    0b000000000, 0b000000000, 0b001000000, 150,
    0b000000000, 0b000000000, 0b000001000, 150,
    0b000000000, 0b000000000, 0b000010000, 150,
    #
    0b000000000, 0b000000001, 0b000000000, 150,
    0b000000000, 0b000000010, 0b000000000, 150,
    0b000000000, 0b000000100, 0b000000000, 150,
    0b000000000, 0b000100000, 0b000000000, 150,
    0b000000000, 0b100000000, 0b000000000, 150,
    0b000000000, 0b010000000, 0b000000000, 150,
    0b000000000, 0b001000000, 0b000000000, 150,
    0b000000000, 0b000001000, 0b000000000, 150,
    0b000000000, 0b000010000, 0b000000000, 150,
    # ---------------------------------------
    # dancing diagonals
    # ---------------------------------------
    0b000000001, 0b000010000, 0b100000000, 150,
    0b000000000, 0b100010001, 0b000000000, 150,
    0b100000000, 0b000010000, 0b000000001, 150,
    #
    0b010000000, 0b000010000, 0b000000010, 150,
    0b000000000, 0b010010010, 0b000000000, 150,
    0b000000010, 0b000010000, 0b010000000, 150,
    #
    0b000000100, 0b000010000, 0b001000000, 150,
    0b000000000, 0b001010100, 0b000000000, 150, 
    0b001000000, 0b000010000, 0b000000100, 150,          
    #
    0b000001000, 0b000010000, 0b000100000, 150,
    0b000000000, 0b000111000, 0b000000000, 150,
    0b000100000, 0b000010000, 0b000001000, 150,   
    #
    0b100000000, 0b000010000, 0b000000001, 150,
    0b000000000, 0b100010001, 0b000000000, 150,
    0b000000001, 0b000010000, 0b100000000, 150,
    #
    0b000000010, 0b000010000, 0b010000000, 150,
    0b000000000, 0b010010010, 0b000000000, 150,
    0b010000000, 0b000010000, 0b000000010, 150,
    #
    0b001000000, 0b000010000, 0b000000100, 150,
    0b000000000, 0b001010100, 0b000000000, 150,
    0b000000100, 0b000010000, 0b001000000, 150,
    #
    0b000100000, 0b000010000, 0b000001000, 150,
    0b000000000, 0b000111000, 0b000000000, 150,
    0b000001000, 0b000010000, 0b000100000, 150,
    # ---------------------------------------
    # helicopter rotors
    # ---------------------------------------
    0b100010001, 0b000000000, 0b000000000, 150,
    0b010010010, 0b000000000, 0b000000000, 150,
    0b001010100, 0b000000000, 0b000000000, 150,
    0b000111000, 0b000000000, 0b000000000, 150,
    0b100010001, 0b000000000, 0b000000000, 150,
    0b010010010, 0b000000000, 0b000000000, 150,
    0b001010100, 0b000000000, 0b000000000, 150,
    0b000111000, 0b000000000, 0b000000000, 150,
    #
    0b000000000, 0b100010001, 0b000000000, 150,
    0b000000000, 0b000111000, 0b000000000, 150,
    0b000000000, 0b001010100, 0b000000000, 150,
    0b000000000, 0b010010010, 0b000000000, 150,
    0b000000000, 0b100010001, 0b000000000, 150,   
    0b000000000, 0b000111000, 0b000000000, 150,
    0b000000000, 0b001010100, 0b000000000, 150,
    0b000000000, 0b010010010, 0b000000000, 150,
    #
    0b000000000, 0b000000000, 0b100010001, 150,
    0b000000000, 0b000000000, 0b010010010, 150,
    0b000000000, 0b000000000, 0b001010100, 150,
    0b000000000, 0b000000000, 0b000111000, 150,
    0b000000000, 0b000000000, 0b100010001, 150,
    0b000000000, 0b000000000, 0b010010010, 150,
    0b000000000, 0b000000000, 0b001010100, 150,
    0b000000000, 0b000000000, 0b000111000, 150,
    #
    0b100010001, 0b100010001, 0b100010001, 150,
    0b010010010, 0b000111000, 0b010010010, 150,
    0b001010100, 0b001010100, 0b001010100, 150,
    0b000111000, 0b010010010, 0b000111000, 150,
    0b100010001, 0b100010001, 0b100010001, 150,
    0b010010010, 0b000111000, 0b010010010, 150,
    0b001010100, 0b001010100, 0b001010100, 150,
    0b000111000, 0b010010010, 0b000111000, 150,   
    # ---------------------------------------
    # crazy x's
    # ---------------------------------------
    0b101010101, 0b000000000, 0b000000000, 150,
    0b010111010, 0b000000000, 0b000000000, 150,
    0b101010101, 0b000000000, 0b000000000, 150,
    0b010111010, 0b000000000, 0b000000000, 150,
    0b101010101, 0b000000000, 0b000000000, 150,
    0b010111010, 0b000000000, 0b000000000, 150,
    0b101010101, 0b000000000, 0b000000000, 150,
    0b010111010, 0b000000000, 0b000000000, 150,
    #
    0b000000000, 0b010111010, 0b000000000, 150,
    0b000000000, 0b101010101, 0b000000000, 150,
    0b000000000, 0b010111010, 0b000000000, 150,
    0b000000000, 0b101010101, 0b000000000, 150,
    0b000000000, 0b010111010, 0b000000000, 150,
    0b000000000, 0b101010101, 0b000000000, 150,
    0b000000000, 0b010111010, 0b000000000, 150,
    0b000000000, 0b101010101, 0b000000000, 150,
    #
    0b000000000, 0b000000000, 0b101010101, 150,
    0b000000000, 0b000000000, 0b010111010, 150,
    0b000000000, 0b000000000, 0b101010101, 150,
    0b000000000, 0b000000000, 0b010111010, 150,
    0b000000000, 0b000000000, 0b101010101, 150,
    0b000000000, 0b000000000, 0b010111010, 150,
    0b000000000, 0b000000000, 0b101010101, 150,
    0b000000000, 0b000000000, 0b010111010, 150,
    #
    0b000000101, 0b000000010, 0b000000101, 150,
    0b000000010, 0b000000111, 0b000000010, 150,
    0b000000101, 0b000000010, 0b000000101, 150,
    0b000000010, 0b000000111, 0b000000010, 150,
    0b000000101, 0b000000010, 0b000000101, 150,
    0b000000010, 0b000000111, 0b000000010, 150,
    0b000000101, 0b000000010, 0b000000101, 150,
    0b000000010, 0b000000111, 0b000000010, 150,
    #
    0b100000100, 0b000100000, 0b100000100, 150,
    0b000100000, 0b100000100, 0b000100000, 150,
    0b100000100, 0b000100000, 0b100000100, 150,
    0b000100000, 0b100000100, 0b000100000, 150,
    0b100000100, 0b000100000, 0b100000100, 150,
    0b000100000, 0b100000100, 0b000100000, 150,
    0b100000100, 0b000100000, 0b100000100, 150,
    0b000100000, 0b100000100, 0b000100000, 150,
    #
    0b101000000, 0b010000000, 0b101000000, 150,
    0b010000000, 0b101000000, 0b010000000, 150,
    0b101000000, 0b010000000, 0b101000000, 150,
    0b010000000, 0b101000000, 0b010000000, 150,
    0b101000000, 0b010000000, 0b101000000, 150,
    0b010000000, 0b101000000, 0b010000000, 150,
    0b101000000, 0b010000000, 0b101000000, 150,
    0b010000000, 0b101000000, 0b010000000, 150,
    #
    0b001000001, 0b000001000, 0b001000001, 150,
    0b000001000, 0b001000001, 0b000001000, 150,
    0b001000001, 0b000001000, 0b001000001, 150,
    0b000001000, 0b001000001, 0b000001000, 150,
    0b001000001, 0b000001000, 0b001000001, 150,
    0b000001000, 0b001000001, 0b000001000, 150,
    0b001000001, 0b000001000, 0b001000001, 150,
    0b000001000, 0b001000001, 0b000001000, 150, 
    #
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    #
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    #
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    #
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    #
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    0b100000001, 0b000010000, 0b100000001, 150,
    0b000010000, 0b100010001, 0b000010000, 150,
    #
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    0b010000010, 0b000010000, 0b010000010, 150,
    0b000010000, 0b010010010, 0b000010000, 150,
    #
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    0b001000100, 0b000010000, 0b001000100, 150,
    0b000010000, 0b001010100, 0b000010000, 150,
    #
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150,
    0b000101000, 0b000010000, 0b000101000, 150,
    0b000010000, 0b000111000, 0b000010000, 150, 
    # ---------------------------------------
    # elevator
    # ---------------------------------------
    0b000011011, 0b000000000, 0b000000000, 150,
    0b000000000, 0b000011011, 0b000000000, 150,
    0b000000000, 0b000000000, 0b000011011, 150,
    0b000000000, 0b000011011, 0b000000000, 150,
    0b000011011, 0b000000000, 0b000000000, 150,
    #
    0b000110110, 0b000000000, 0b000000000, 150,
    0b000000000, 0b000110110, 0b000000000, 150,
    0b000000000, 0b000000000, 0b000110110, 150,
    0b000000000, 0b000110110, 0b000000000, 150,
    0b000110110, 0b000000000, 0b000000000, 150,
    #
    0b110110000, 0b000000000, 0b000000000, 150,
    0b000000000, 0b110110000, 0b000000000, 150,
    0b000000000, 0b000000000, 0b110110000, 150,
    0b000000000, 0b110110000, 0b000000000, 150,
    0b110110000, 0b000000000, 0b000000000, 150,
    #
    0b011011000, 0b000000000, 0b000000000, 150,
    0b000000000, 0b011011000, 0b000000000, 150,
    0b000000000, 0b000000000, 0b011011000, 150,
    0b000000000, 0b011011000, 0b000000000, 150,
    0b011011000, 0b000000000, 0b000000000, 150,
    #
    0b111101111, 0b000000000, 0b000000000, 150,
    0b000000000, 0b111101111, 0b000000000, 150,
    0b000000000, 0b000000000, 0b111101111, 150,
    0b000000000, 0b111101111, 0b000000000, 150,
    0b111101111, 0b000000000, 0b000000000, 150,
    #
    0b010101010, 0b000000000, 0b000000000, 150,
    0b000000000, 0b010101010, 0b000000000, 150,
    0b000000000, 0b000000000, 0b010101010, 150,
    0b000000000, 0b010101010, 0b000000000, 150,
    0b010101010, 0b000000000, 0b000000000, 150,
    #
    0b000010111, 0b000000000, 0b000000000, 150,
    0b000000000, 0b000010111, 0b000000000, 150,
    0b000000000, 0b000000000, 0b000010111, 150,
    0b000000000, 0b000010111, 0b000000000, 150,
    0b000010111, 0b000000000, 0b000000000, 150,
    #
    0b100110100, 0b000000000, 0b000000000, 150,
    0b000000000, 0b100110100, 0b000000000, 150,
    0b000000000, 0b000000000, 0b100110100, 150,
    0b000000000, 0b100110100, 0b000000000, 150,
    0b100110100, 0b000000000, 0b000000000, 150, 
    #
    0b111010000, 0b000000000, 0b000000000, 150,
    0b000000000, 0b111010000, 0b000000000, 150,
    0b000000000, 0b000000000, 0b111010000, 150,
    0b000000000, 0b111010000, 0b000000000, 150,
    0b111010000, 0b000000000, 0b000000000, 150, 
    #
    0b001011001, 0b000000000, 0b000000000, 150, 
    0b000000000, 0b001011001, 0b000000000, 150,
    0b000000000, 0b000000000, 0b001011001, 150,
    0b000000000, 0b001011001, 0b000000000, 150,
    0b001011001, 0b000000000, 0b000000000, 150, 
    #
    0b000011011, 0b000000000, 0b000000000, 150,
    0b000000000, 0b000110110, 0b000000000, 150,
    0b000000000, 0b000000000, 0b110110000, 150,
    0b000000000, 0b011011000, 0b000000000, 150,
    0b000011011, 0b000000000, 0b000000000, 150,
    #
    0b000000000, 0b000011011, 0b000000000, 150,
    0b000000000, 0b000000000, 0b000110110, 150,
    0b000000000, 0b110110000, 0b000000000, 150,
    0b011011000, 0b000000000, 0b000000000, 150,
    0b000000000, 0b000011011, 0b000000000, 150,
    #
    0b000000000, 0b000000000, 0b000011011, 150,
    0b000000000, 0b000110110, 0b000000000, 150,
    0b110110000, 0b000000000, 0b000000000, 150,
    0b000000000, 0b011011000, 0b000000000, 150,
    0b000000000, 0b000000000, 0b000011011, 150, 
    # ---------------------------------------
    # snake
    # ---------------------------------------
    0b000000001, 0b000000000, 0b000000000, 150,
    0b000000001, 0b000000001, 0b000000000, 150,
    0b000000001, 0b000000001, 0b000000001, 150,
    0b000000000, 0b000000001, 0b000000011, 150,
    0b000000000, 0b000000010, 0b000000011, 150,
    0b000000010, 0b000000010, 0b000000010, 150,
    #
    0b000000110, 0b000000010, 0b000000000, 150,
    0b000000110, 0b000000100, 0b000000000, 150,
    0b000000100, 0b000000100, 0b000000100, 150,
    0b000000000, 0b000000100, 0b000100100, 150,
    0b000000000, 0b000100000, 0b000100100, 150,
    0b000100000, 0b000100000, 0b000100000, 150,
    #
    0b100100000, 0b000100000, 0b000000000, 150,
    0b100100000, 0b100000000, 0b000000000, 150,
    0b100000000, 0b100000000, 0b100000000, 150,
    0b000000000, 0b100000000, 0b110000000, 150,
    0b000000000, 0b010000000, 0b110000000, 150,
    0b010000000, 0b010000000, 0b010000000, 150,
    #
    0b011000000, 0b010000000, 0b000000000, 150,
    0b011000000, 0b001000000, 0b000000000, 150,
    0b001000000, 0b001000000, 0b001000000, 150,
    0b000000000, 0b001000000, 0b001001000, 150,
    0b000000000, 0b000001000, 0b001001000, 150,
    0b000001000, 0b000001000, 0b000001000, 150,
    #
    0b000001010, 0b000001000, 0b000000000, 150,
    0b000001010, 0b000000010, 0b000000000, 150,
    0b000000010, 0b000000010, 0b000000010, 150,
    0b000000000, 0b000000010, 0b000100010, 150,
    0b000000000, 0b000100000, 0b000100010, 150,
    0b000100000, 0b000100000, 0b000100000, 150,
    #
    0b010100000, 0b000100000, 0b000000000, 150,
    0b010100000, 0b010000000, 0b000000000, 150,
    0b010000000, 0b010000000, 0b010000000, 150,
    0b000000000, 0b010000000, 0b010001000, 150,
    0b000000000, 0b000001000, 0b010001000, 150,
    0b000001000, 0b000001000, 0b000001000, 150,
    #
    0b000011000, 0b000001000, 0b000000000, 150,
    0b000011000, 0b000010000, 0b000000000, 150,
    0b000010000, 0b000010000, 0b000010000, 150,
    0b000000000, 0b000010000, 0b000110000, 150,
    0b000000000, 0b000100000, 0b000110000, 150,
    0b000100000, 0b000100000, 0b000100000, 150,
    #
    0b000100010, 0b000100000, 0b000000000, 150,
    0b000100010, 0b000000010, 0b000000000, 150,
    0b000000010, 0b000000010, 0b000000010, 150,
    0b000000000, 0b000000010, 0b000010010, 150,
    0b000000000, 0b000010000, 0b000010010, 150,
    0b000010000, 0b000010000, 0b000010000, 150,
    #
    0b010010000, 0b000010000, 0b000000000, 150,
    0b010010000, 0b010000000, 0b000000000, 150,
    0b010000000, 0b010000000, 0b010000000, 150,
    #
    0b000000000, 0b010000000, 0b111000000, 150,
    0b000000000, 0b000000000, 0b111101000, 150,
    0b000000000, 0b000000000, 0b101101101, 150,
    0b000000000, 0b000000000, 0b000101111, 150,
    0b000000000, 0b000000000, 0b000010111, 150,
    #
    0b000000000, 0b000010000, 0b000010010, 150,
    0b000000000, 0b010010000, 0b000010000, 150,
    0b000000000, 0b111010000, 0b000000000, 150,
    0b000000000, 0b111101000, 0b000000000, 150,
    0b000000000, 0b101101101, 0b000000000, 150,
    0b000000000, 0b000101111, 0b000000000, 150,
    #
    0b000000010, 0b000000111, 0b000000000, 150,
    0b000000111, 0b000000010, 0b000000000, 150,
    0b000101111, 0b000000000, 0b000000000, 150,
    0b101101101, 0b000000000, 0b000000000, 150,
    0b111101000, 0b000000000, 0b000000000, 150,
    0b111000000, 0b000000000, 0b000000000, 150,
    0b010000000, 0b000000000, 0b000000000, 150
    ]

# instantiate ledcube3x3x3
lc = ledcube3x3x3.ledcube(DATA, CLOCK, LATCH, debug=True)

lc.start()

try:
    # loop to display the frames on the LED cube
    currentFrame = 0
    while True:
        # parameters for LED cube frame display
        L0pattern = FRAME[currentFrame]
        L1pattern = FRAME[currentFrame + 1]
        L2pattern = FRAME[currentFrame + 2]
        delay_ms = FRAME[currentFrame + 3]
        # display frame on LED cube   
        lc.display(L0pattern, L1pattern, L2pattern, delay_ms)
        # move to next frame        
        currentFrame += 4
        if currentFrame >= len(FRAME):
            currentFrame = 0

except KeyboardInterrupt as e:
    print("programma onderbroken met Ctrl-C")
    
finally:
    # stop display
    lc.stop()

