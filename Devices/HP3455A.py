from AGPIB.agipibi import Agipibi


class HP3455A:
    # These are the GPIB addresses of the controller and the DMM
    cic_address = 0x00
    dmm_address = 0x01

    def __init__(self, port, debug, cic_address=0x00, dmm_address=0x01):
        print("Wait 2 seconds for the serial connection to be established!")
        self.dev = Agipibi(port, debug)
        # Test communication and uC responsiveness.
        if self.dev.interface_ping():
            print("Arduino is alive :-)")
        else:
            print("No reponse to ping, you should reset the board :-(")

        # Set the gpib addresses of the controller and the DMM
        self.cic_address = cic_address
        self.dmm_address = dmm_address
        # Initialize bus lines and become Controller-In-Charge.
        # All lines will be put to HiZ except for NRFD asserted because we gave no
        # argument to the function, so we pause the Talker while setting up.
        # IFC is pulsed to gain CIC status.
        self.dev.gpib_init(address=self.cic_address, controller=True)

        # Activate 'remote' mode of instruments (not required with this scope).
        # It asserts REN untill disabled with False or gpib_init() is called again.
        self.dev.gpib_remote(True)

        # Clear all instruments on the bus.
        # Sends DCL when bus=True, reaching all devices. But it would use SDC
        # if bus=True and Listeners are set.
        self.dev.gpib_clear(bus=True)

    # Two functions to set direction of the communication, they are private
    def __cic_to_dmm(self):
        # Unaddress everyone.
        self.dev.gpib_untalk()
        self.dev.gpib_unlisten()
        # Set ourself as the Talker.
        self.dev.gpib_talker(self.cic_address)
        # Scope will listen.
        self.dev.gpib_listener(self.dmm_address)

    def __dmm_to_cic(self):
        # Unaddress everyone.
        self.dev.gpib_untalk()
        self.dev.gpib_unlisten()
        # Set scope as the Talker.
        self.dev.gpib_talker(self.dmm_address)
        # We'll listen for data.
        self.dev.gpib_listener(self.cic_address)

    def get_reading(self):
        self.__cic_to_dmm()
        # FUNCTION DC (F1), RANGE AUTO (R7), AUTO CAL on (A1)
        # HIGH RESOLUTION on (H1), MATH off (M3), TRIGGER internal (T1) 
        # Refer to HP3455A manual p. 3-7 for further information
        self.dev.gpib_write("F1 R7 A1 H1 M3 T1")
        self.__dmm_to_cic()
        return float(self.dev.gpib_read())
