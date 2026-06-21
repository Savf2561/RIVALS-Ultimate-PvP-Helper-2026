
from utils.logger import log_info

class ConsoleRenderer:
    def __init__(self):
        self.menu_visible = False

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.show_menu()
        else:
            log_info("Menu hidden")

    def show_menu(self):
        print("╔══════════════════════════════════════════════════════════╗")
        print("║   RIVALS ULTIMATE PVP HELPER v1.0                      ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  COMBAT                                                ║")
        print("║  F2 - Silent Aim      F3 - Triggerbot                  ║")
        print("║  F4 - No Recoil       F5 - No Spread                   ║")
        print("║  F6 - Hitbox Expander F11 - Wallbang                   ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  ESP                                                   ║")
        print("║  F7 - Boxes           F8 - Skeletons                   ║")
        print("║  F9 - Health          F10 - Names                      ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  AI & MOVEMENT                                         ║")
        print("║  F12 - AI Predictor   Insert - Anti-Aim                ║")
        print("║  Home - Speed Hack    End - Fly Hack                   ║")
        print("║  PgUp - Infinite Ammo PgDn - Auto-Reload               ║")
        print("╚══════════════════════════════════════════════════════════╝")
