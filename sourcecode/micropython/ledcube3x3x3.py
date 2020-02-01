import machine
import utime

class ledcube :

    """a 3x3x3 LED cube controlled with serial connections to µC with 2 SN74HC595 shift register ICs - only 3 pins required
       - 1 data pin (SN74HC595 SER pin 14) to input 12 bits of data (9 Colums & 3 Levels (rows))
       - 1 clock pin (SN74HC595 SRCLK pin 11) to shift the data bits into the register
       - 1 latch pin (SN74HV595 RCLK pin 12) to copy the 12 data bits into the latch register and set the output pins
       
       the SN74HC595 shift registers are daisy chained :
       shift #1  shift #2  µController
       ========  ========  =========== 
        QH'    --> SER    --> gpio pin
        SRCLK  --> SRCLK  --> gpio pin
        RCLK   --> RCLK   --> gpio pin
        OE#    --> OE#    --> GND
        GND    --> GND    --> GND
        SRCLR# --> SRCLR# --> VCC
        VCC    --> VCC    --> VCC
       
       the LEDs are connected as follows :
       LED  shift #1  shift #2
       ==== ========  ========
        C0 --> QA
        C1 --> QB
        C2 --> QC
        C3 --> QD
        C4 --> QE
        C5 --> QF
        C6 --> QG
        C7 --> QH
        C8 -----------> QA
        L0 -----------> QB
        L1 -----------> QC
        L2 -----------> QD 
    """
       
 
    def __init__(self, data_pin, clock_pin, latch_pin, debug=True):
        
        """constructor 3x3x3 LED cube """
        
        try:
            self.data = data_pin
            self.clock = clock_pin
            self.latch = latch_pin
            self.da = None
            self.cl = None
            self.la = None
            self.debug = debug
        
        except Exception as E:
            if self.debug:
                print("3x3x3 LED Cube __init__ error: ",E)

    
    def start(self):
        
        """Initialise 3x3x3 LED Cube"""
        
        try:
            # make pin objects
            self.da = machine.Pin(self.data, machine.Pin.OUT)
            self.cl = machine.Pin(self.clock, machine.Pin.OUT)
            self.la = machine.Pin(self.latch, machine.Pin.OUT)
            # initialise pin objects
            self.da.value(0)
            self.cl.value(0)
            self.la.value(0)
        
        except Exception as E:
            if self.debug:
                print("3x3x3 LED Cube start error: ",E)

    
    def shift_data(self, data):
        
        """ helper function to put data (list of 16 bit values) in the shift registers and to the output pins
            the SN74HC595 shift registers will be filled as follows:
              shift register #1       shift register #2
            ======================= =======================
            QA QB QC QD QE QF QG QH QA QB QC QD QE QF QG QH <-- SN74HC595
             |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
             v  v  v  v  v  v  v  v  v  v  v  v  v  v  v  v
            C0 C1 C2 C3 C4 C5 C6 C7 C8 L0 L1 L2  x  x  x  x <-- LED data col/level
            ======================= =======================
            15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0 <-- bit positions (shift in reverse order !!!)
        """
        
        # set latch low to begin shifting
        self.la.value(0)
        # shift bits from bit list into the shift registers
        for bit in data:
            self.cl.value(0)
            self.da.value(bit)
            self.cl.value(1)
        # set latch high to set data to output pins
        self.la.value(1)
        self.cl.value(0)
        self.da.value(0)


    def display(self, pat_L0, pat_L1, pat_L2, delay_ms):
        
        """ display the LED patterns for the levels L0, L1 and L2 of the 3x3x3 LED Cube during delay_ms microseconds

           LED levels : set high to activate (source current from external VCC)
           ==========
           L2 : level 2 -> top
           L1 : level 1 -> middle
           L0 : level 0 -> bottom

           LED columns : set low to activate (sink current to ground)
           ===========
           C6 -- C7 -- C8  -> back
            |     |     |
           C3 -- C4 -- C5
            |     |     |
           C0 -- C1 -- C2  -> front
 
           LED pattern frame --> 0b012345678, 0b012345678, 0b012345678, 150
                                       |            |            |       | 
                                      L0           L1           L2    delay (ms) 

           A LED frame consists of 3 LED patterns for each level of LEDs, followed by a delay time in milliseconds.
           The different patterns on each level are multiplexed until the delay time has elapsed.
        """
 
        try:
            # column pattern from different levels to list
            patterns = [pat_L0, pat_L1, pat_L2]
            # start timer
            start_ms = utime.ticks_ms()
            current_ms = start_ms
            # multiplex levels of LEDs until time_ms has passed
            while current_ms < start_ms + delay_ms:
                # loop through patterns
                for idx, pat in enumerate(patterns):
                    # convert column pattern to binary list
                    # complement of bit pattern (low to activate LED) 
                    bits = []
                    bits = [(~int(x) + 2) for x in list('{0:0b}'.format(pat))]
                    # insert missing 1 bits if necessary - format 
                    while len(bits) < 9: 
                        bits.insert(0, 1)
                    # insert level bits (high to activate)
                    bits[9:] = [0]*3
                    bits[9 + idx] = 1
                    # set unused bits to 0
                    bits[12:] = [0]*4   
                    # debug info
                    if self.debug:
                        print('column pattern: ', bits[0:9], '\tlevel: ', bits[9:12], '\tunused: ', bits[12:])
                    # reverse shift the bits into the shift registers
                    bits.reverse()
                    self.shift_data(bits)
                    # minimum display time
                    utime.sleep_ms(5)
                    # turnoff layer & columns
                    bits = []
                    bits = [1]*9
                    bits[9:] = [0]*7
                    bits.reverse()
                    self.shift_data(bits)                    
                # update current time
                current_ms = utime.ticks_ms()
           
        except Exception as E:
            if self.debug:
                print("3x3x3 LED Cube display error: ",E)
            
    
    def clear(self):
        
        """ clear 3x3x3 LED Cube """

        self.display(0b000000000, 0b000000000, 0b000000000, 100)

    
    def stop(self):
        
        """ stop 3x3x3 LED Cube """
        
        try:
            self.clear()
            del self.da
            del self.cl
            del self.la
        
        except Exception as E:
            if self.debug:
                print("3x3x3 LED Cube stop error: ",E)
