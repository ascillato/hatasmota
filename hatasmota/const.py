"""Tasmota constants."""
AUTOMATION_TYPE_TRIGGER = "trigger"

COMMAND_BACKLOG = "Backlog"
COMMAND_CHANNEL = "Channel"
COMMAND_COLOR = "Color"
COMMAND_CT = "CT"
COMMAND_DIMMER = "Dimmer"
COMMAND_FADE = "Fade"
COMMAND_POWER = "Power"
COMMAND_SCHEME = "Scheme"
COMMAND_SPEED = "Speed"
COMMAND_WHITE = "White"

CONF_BUTTON = "btn"
CONF_DEVICENAME = "dn"
CONF_FRIENDLYNAME = "fn"
CONF_FULLTOPIC = "ft"
CONF_IFAN = "if"
CONF_IP = "ip"
CONF_HOSTNAME = "hn"
CONF_MAC = "mac"
CONF_LIGHT_SUBTYPE = "lt_st"
CONF_LINK_RGB_CT = "lk"  # RGB + white channels linked to a single light
CONF_MODEL = "md"
CONF_OFFLINE = "ofln"
CONF_ONLINE = "onln"
CONF_OPTIONS = "so"
CONF_PREFIX = "tp"
CONF_SENSOR = "sn"
CONF_STATE = "state"
CONF_RELAY = "rl"
CONF_SW_VERSION = "sw"
CONF_SWITCH = "swc"
CONF_SWITCHNAME = "swn"
CONF_TOPIC = "t"
CONF_TUYA = "ty"
CONF_VERSION = "ver"

CONF_MANUFACTURER = "manufacturer"
CONF_NAME = "name"

LST_NONE = 0
LST_SINGLE = 1
LST_COLDWARM = 2
LST_RGB = 3
LST_RGBW = 4
LST_RGBCW = 5

# fmt: off
OPTION_MQTT_RESPONSE = "4"        # Return MQTT response as RESULT or %COMMAND%
OPTION_BUTTON_SWAP = "11"         # Swap button single and double press functionality
OPTION_BUTTON_SINGLE = "13"       # Allow immediate action on single button press
OPTION_DECIMAL_TEXT = "17"        # Show Color string as hex or comma-separated
OPTION_NOT_POWER_LINKED = "20"    # Update of Dimmer/Color/CT without turning power on
OPTION_HASS_LIGHT = "30"          # Enforce Home Assistant auto-discovery as light
OPTION_PWM_MULTI_CHANNELS = "68"  # Multi-channel PWM instead of a single light
OPTION_MQTT_BUTTONS = "73"        # Enable Buttons decoupling and send multi-press and hold MQTT messages
OPTION_SHUTTER_MODE = "80"        # Blinds and shutters support; removed in Tasmota 9.0.0.4
OPTION_REDUCED_CT_RANGE = "82"    # Reduce the CT range from 153..500 to 200.380
OPTION_MQTT_SWITCHES = "114"      # Enable sending switch MQTT messages
# fmt: on

PREFIX_CMND = 0
PREFIX_STAT = 1
PREFIX_TELE = 2

RL_NONE = 0
RL_RELAY = 1
RL_LIGHT = 2
RL_SHUTTER = 3

RSLT_ACTION = "Action"
RSLT_POWER = "POWER"
RSLT_STATE = "STATE"
RSLT_TRIG = "TRIG"

SENSOR_ATTRIBUTE_RSSI = "RSSI"
SENSOR_ATTRIBUTE_UPTIME = "Uptime"
SENSOR_ATTRIBUTE_SIGNAL = "Signal"
SENSOR_ATTRIBUTE_WIFI_LINKCOUNT = "LinkCount"
SENSOR_ATTRIBUTE_WIFI_DOWNTIME = "Downtime"
SENSOR_ATTRIBUTE_MQTTCOUNT = "MqttCount"

SENSOR_TEMPERATURE = "Temperature"
SENSOR_DEWPOINT = "DewPoint"
SENSOR_PRESSURE = "Pressure"
SENSOR_PRESSUREATSEALEVEL = "SeaPressure"
SENSOR_APPARENT_POWERUSAGE = "ApparentPower"
SENSOR_BATTERY = "Battery"
SENSOR_CURRENT = "Current"
SENSOR_DISTANCE = "Distance"
SENSOR_FREQUENCY = "Frequency"
SENSOR_HUMIDITY = "Humidity"
SENSOR_ILLUMINANCE = "Illuminance"
SENSOR_MOISTURE = "Moisture"
SENSOR_PB0_3 = "PB0.3"
SENSOR_PB0_5 = "PB0.5"
SENSOR_PB1 = "PB1"
SENSOR_PB2_5 = "PB2.5"
SENSOR_PB5 = "PB5"
SENSOR_PB10 = "PB10"
SENSOR_PM1 = "PM1"
SENSOR_PM2_5 = "PM2.5"
SENSOR_PM10 = "PM10"
SENSOR_POWERFACTOR = "Factor"
SENSOR_POWERUSAGE = "Power"
SENSOR_SPEED = "Speed"
SENSOR_TOTAL_START_TIME = "TotalStartTime"
SENSOR_REACTIVE_POWERUSAGE = "ReactivePower"
SENSOR_TODAY = "Today"
SENSOR_TOTAL = "Total"
SENSOR_VOLTAGE = "Voltage"
SENSOR_WEIGHT = "Weight"
SENSOR_YESTERDAY = "Yesterday"
SENSOR_CO2 = "CarbonDioxide"
SENSOR_ECO2 = "eCO2"
SENSOR_TVOC = "TVOC"
SENSOR_COLOR_RED = "Red"
SENSOR_COLOR_GREEN = "Green"
SENSOR_COLOR_BLUE = "Blue"
SENSOR_CCT = "CCT"
SENSOR_PROXIMITY = "Proximity"
SENSOR_AMBIENT = "Ambient"
SENSOR_SWITCH = "Switch"
SENSOR_STATUS_MQTT_COUNT = "status_mqtt_count"
SENSOR_STATUS_LINK_COUNT = "status_link_count"
SENSOR_STATUS_SIGNAL = "status_signal"
SENSOR_STATUS_RSSI = "status_rssi"
SENSOR_STATUS_RESTART = "status_restart_reason"
SENSOR_STATUS_IP = "status_ip"
SENSOR_STATUS_UPTIME = "status_Uptime"

SENSOR_UNIT_PRESSURE = "PressureUnit"
SENSOR_UNIT_SPEED = "SpeedUnit"
SENSOR_UNIT_TEMPERATURE = "TempUnit"

STATE_OFF = 0
STATE_ON = 1
STATE_TOGGLE = 2
STATE_HOLD = 3

STATUS_SENSOR = "StatusSNS"

SWITCHMODE_NONE = -1
SWITCHMODE_TOGGLE = 0
SWITCHMODE_FOLLOW = 1
SWITCHMODE_FOLLOW_INV = 2
SWITCHMODE_PUSHBUTTON = 3
SWITCHMODE_PUSHBUTTON_INV = 4
SWITCHMODE_PUSHBUTTONHOLD = 5
SWITCHMODE_PUSHBUTTONHOLD_INV = 6
SWITCHMODE_PUSHBUTTON_TOGGLE = 7
SWITCHMODE_TOGGLEMULTI = 8
SWITCHMODE_FOLLOWMULTI = 9
SWITCHMODE_FOLLOWMULTI_INV = 10
SWITCHMODE_PUSHHOLDMULTI = 11
SWITCHMODE_PUSHHOLDMULTI_INV = 12
SWITCHMODE_PUSHON = 13
SWITCHMODE_PUSHON_INV = 14
