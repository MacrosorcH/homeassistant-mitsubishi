"""Constants for the Mitsubishi Air Conditioner integration."""

DOMAIN = "mitsubishi"

# Update interval
DEFAULT_SCAN_INTERVAL = 30  # seconds

# Configuration
CONF_ENCRYPTION_KEY = "encryption_key"
DEFAULT_ENCRYPTION_KEY = "unregistered"
CONF_ADMIN_USERNAME = "admin_username"
DEFAULT_ADMIN_USERNAME = "admin"
CONF_ADMIN_PASSWORD = "admin_password"
DEFAULT_ADMIN_PASSWORD = "me1debug@0567"
CONF_SCAN_INTERVAL = "scan_interval"

# Optimistic UI updates: show a requested value immediately and hold it until
# the device confirms it, instead of waiting for the next refresh.
CONF_OPTIMISTIC_UPDATES = "optimistic_updates"
DEFAULT_OPTIMISTIC_UPDATES = False

# Experimental Features
CONF_EXPERIMENTAL_FEATURES = "experimental_features"

# Remote Temperature Configuration (experimental)
CONF_EXTERNAL_TEMP_ENTITY = "external_temperature_entity"
CONF_REMOTE_TEMP_MODE = "remote_temp_mode"

# Temperature Source Modes
TEMP_SOURCE_INTERNAL = "Internal"
TEMP_SOURCE_REMOTE = "Remote"
