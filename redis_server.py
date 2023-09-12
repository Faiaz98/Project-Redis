import socket
import threading

class RedisServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.data = {}
        
    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
            
        print(f"Listening on {self.host}:{self.port}")
            
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
                
            client_thread = ClientHandler(client_socket, self.data)
            client_thread.start()
                
class ClientHandler(threading.Thread):
    def __init__(self, client_socket, data):
        super().__init__()
        self.client_socket = client_socket
        self.data = data
    
    
    def run(self):
        while True:
            request = self.client_socket.recv(1024).decode("utf-8")
            if not request:
                break
            
            response = self.handle_request(request)
            self.client_socket.send(response.encode("utf-8"))
            
        self.client_socket.close()
    
    def handle_request(self, request):
        
        #for parsing value
        
        pass
    
if __name__ == "__main__":
    server = RedisServer("127.0.0.1", 6379)

        
    