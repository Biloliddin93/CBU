# ov-assistant

Requirements
- python version 3.7.2
- python requests library (pip install requests)
- python onevizion library (pip install onevizion)

To start integration, you need to fill files

settings_template.json:
- URL to site (e.g., trackor.onevizion.com)
- account username and password 
- trackor type (e.g., Case)

.integration:
- settings_file_name (File that contains additional settings. e.g., settings_template.json)
- default_schedule (Must be specified in the quartz cron expression format. e.g., 0 * * * * ?)
- read_from_stdout (Checkbox that indicates that STDOUT is added to Log Trackor. e.g., true)

After that run startIntegration.py