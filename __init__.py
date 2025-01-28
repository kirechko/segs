import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.components import neopixelbus
from esphome.const import CONF_ID

DEPENDENCIES = ["neopixelbus"]
CODEOWNERS = ["@kirechko"]

segs_ns = cg.esphome_ns.namespace("segs")
Segs = segs_ns.class_(
    "Segs", neopixelbus.NeoPixelBusLightOutputBase
)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(Segs),
    }
).extend(neopixelbus.ESP_BLE_DEVICE_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await light.register_light(var, config)
    await cg.register_component(var, config)
