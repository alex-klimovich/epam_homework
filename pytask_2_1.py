import time
import BaseHTTPServer
import subprocess
import shlex
import urllib

HOST_NAME = 'localhost'
PORT_NUMBER = 8000
COMMANDS_BLACK_LIST = ['rm', 'del']


class CustomHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):

        SHELL_PROMPT = '/shell;'

        if self.path.startswith(SHELL_PROMPT):

            # cut shell prompt
            cmd = urllib.unquote(self.path[len(SHELL_PROMPT):])

            # verify if the command not in black list, minimal security
            cmd_list = shlex.split(cmd)
            if any(c in COMMANDS_BLACK_LIST for c in cmd_list):
                self.send_error(501, "Command is blacklisted")
                return

            # try to execute command in shell
            try:
                out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)  # insecure
            except subprocess.CalledProcessError as err:
                out = err.output

            self.send_response(200)
            self.send_header("Accept-Charset", "UTF-8")
            self.send_header("Content-type", "text/plain; charset=UTF-8")
            self.end_headers()
            self.wfile.write(out)

        else:
            self.send_error(501, "Command not supported")


if __name__ == "__main__":
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = BaseHTTPServer.HTTPServer(server_address, CustomHTTPRequestHandler)
    print time.asctime(), "Server Starts - %s:%s" % server_address
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % server_address
