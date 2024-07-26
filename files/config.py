# files/config.py
PORT = {{ port }}
DEPLOYMENT_PATH = "{{ deployment_path }}"
WHEEL_FILE = "{{ wheel_file }}"
INSTANCE_PATH = "{{ instance_path }}"
SECRET_KEY = "{{ secret_key }}"
DB_PATH = "{{ db_path }}"
ADMIN_GROUPS = {{ admin_groups | tojson }}

