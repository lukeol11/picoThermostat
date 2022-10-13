import web_server
import time

time.sleep(10)
try:
    ip = web_server.connect()
    connection = web_server.open_socket(ip)
    web_server.serve(connection)
except KeyboardInterrupt:
    machine.reset()
