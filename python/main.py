import sqlite3
from database import migration
from controller import transaction_controller
from menu import contact_menu
conn = sqlite3.connect("database.db")
migration.migrate(conn)

# transaction_controller.create_incoming_transaction(conn, "Nabung", 20000)
# transaction_controller.create_outbound_transaction(conn, "Makan jajan", 10000)
# transaction_controller.show_saldo(conn)
# transaction_controller.get_all(conn)
contact_menu.run(conn)
