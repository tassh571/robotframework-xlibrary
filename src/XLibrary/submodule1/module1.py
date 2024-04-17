# -*- coding: utf-8 -*-
from robot.api.deco import keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from AppiumFlutterLibrary import AppiumFlutterLibrary
from .module2 import XDrint
from AppiumFlutterLibrary.finder import ElementFinder
import time


class XPrint(AppiumFlutterLibrary):
    def __init__(self):
        super().__init__()
        self._ne = XDrint()
        self._bi = BuiltIn()
        self.finder = ElementFinder()


    @keyword("XPrint Log")
    def XPrint_log(self):
        print("Hello, world! ,สวัสดีชาวโลก เทสภาษาไทย")

    def TestModule2(self):
        instance = XDrint()  
        instance.CDCDCD()   
        self._ne.CDCDCD() 

    def XQuit_App(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""
        driver = self._current_application()
        driver.quit()

    @keyword('Switch Mode')
    def XSwitch_Mode(self, mode):
        """Switch Mode to NATIVE_APP OR FLUTTER."""
        driver = self._current_application()
        if mode == 'NATIVE_APP':
            driver.switch_to.context('NATIVE_APP')
        elif mode == 'FLUTTER':  # Changed from 'if' to 'elif' for logical correctness
            driver.switch_to.context('FLUTTER')

    def _current_application(self):
        """คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน"""
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()


