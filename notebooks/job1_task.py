
# Job 1: Notebook + Wheel
dbutils.widgets.text("env", "dev")
env = dbutils.widgets.get("env")

from mypkg.core import run_logic
run_logic(env)
