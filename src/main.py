
import sys
import time
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.feature_manager import FeatureManager
from utils.logger import log_info, log_success
from utils.hotkey_manager import HotkeyManager
from gui.console_renderer import ConsoleRenderer

def main():
    log_info("RIVALS Ultimate PvP Helper v1.0 starting...")
    feature_mgr = FeatureManager()
    hotkey_mgr = HotkeyManager()
    renderer = ConsoleRenderer()

    hotkey_mgr.register_hotkey('f1', lambda: renderer.toggle_menu())
    hotkey_mgr.register_hotkey('f2', lambda: feature_mgr.toggle('silent_aim'))
    hotkey_mgr.register_hotkey('f3', lambda: feature_mgr.toggle('triggerbot'))
    hotkey_mgr.register_hotkey('f4', lambda: feature_mgr.toggle('no_recoil'))
    hotkey_mgr.register_hotkey('f5', lambda: feature_mgr.toggle('no_spread'))
    hotkey_mgr.register_hotkey('f6', lambda: feature_mgr.toggle('hitbox_expander'))
    hotkey_mgr.register_hotkey('f7', lambda: feature_mgr.toggle('esp_boxes'))
    hotkey_mgr.register_hotkey('f8', lambda: feature_mgr.toggle('esp_skeletons'))
    hotkey_mgr.register_hotkey('f9', lambda: feature_mgr.toggle('esp_health'))
    hotkey_mgr.register_hotkey('f10', lambda: feature_mgr.toggle('esp_names'))
    hotkey_mgr.register_hotkey('f11', lambda: feature_mgr.toggle('wallbang'))
    hotkey_mgr.register_hotkey('f12', lambda: feature_mgr.toggle('ai_predictor'))
    hotkey_mgr.register_hotkey('insert', lambda: feature_mgr.toggle('anti_aim'))
    hotkey_mgr.register_hotkey('home', lambda: feature_mgr.trigger('speed_hack'))
    hotkey_mgr.register_hotkey('end', lambda: feature_mgr.toggle('fly_hack'))
    hotkey_mgr.register_hotkey('pageup', lambda: feature_mgr.toggle('infinite_ammo'))
    hotkey_mgr.register_hotkey('pagedown', lambda: feature_mgr.toggle('auto_reload'))

    log_success("Helper ready. Press F1 for menu.")
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        log_info("Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
