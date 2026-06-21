
from utils.logger import log_success, log_info

class FeatureManager:
    def __init__(self):
        self.features = {
            "silent_aim": False,
            "triggerbot": False,
            "no_recoil": False,
            "no_spread": False,
            "hitbox_expander": False,
            "esp_boxes": False,
            "esp_skeletons": False,
            "esp_health": False,
            "esp_names": False,
            "wallbang": False,
            "ai_predictor": False,
            "anti_aim": False,
            "fly_hack": False,
            "infinite_ammo": False,
            "auto_reload": False,
        }

    def toggle(self, name):
        if name in self.features:
            self.features[name] = not self.features[name]
            status = "ON" if self.features[name] else "OFF"
            log_success(f"{name.upper()} {status}")

    def trigger(self, name):
        if name == "speed_hack":
            log_success("Speed hack activated (2x speed)")
        else:
            log_success(f"Triggered: {name}")
