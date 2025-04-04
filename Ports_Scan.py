import socket
import threading
import queue

def port_test(host, port, result_queue):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            result_queue.put((port, True))
            print(f"Port {port} is open")
        else:
            result_queue.put((port, False))
            print(f"Port {port} is closed")
    except Exception as e:
        result_queue.put((port, None))
        print(f"Error checking port {port}: {e}")
    finally:
        s.close()

def check_ports(host, ports):
    result_queue = queue.Queue()
    threads = []

    for port in ports:
        thread = threading.Thread(target=port_test, args=(host, port, result_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    return results
""""""""" EXAMPLE
host = 'exm.com'
ports = [12345, 443, 8080, 22]

results = check_ports(host, ports)

for port, is_open in results:
    if is_open is None:
        print(f"Error checking port {port}")
    else:
        status = 'open' if is_open else 'closed'
        print(f"Port {port} is {status}.")
""""""""""