import sqlite3
from database import migration
from menu import home_menu as home
conn = sqlite3.connect("database.db")
migration.migrate(conn)
home.run(conn=conn)
