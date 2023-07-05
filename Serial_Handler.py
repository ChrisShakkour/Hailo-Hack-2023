import serial
import serial.tools.list_ports as list_ports
import time


def open_serial_port(port_name):
    print('-I- Attempting to connect to port: "{}"'.format(port_name))
    port = serial.Serial('{}'.format(port_name))
    if(port == None): 
        print('-E- Failed to connect to port: "{}"'.format(port_name))
        exit(1)
    else:
        print('-I- Conection to port: "{}" succeeded'.format(port_name))
        return port


def list_com_ports():
    print("\n-I- Listing available COM ports:")
    ports = list_ports.comports()
    port_list=[]
    for port, desc, hwid in sorted(ports):
        port_list.append(port)
        print("\t{}: {}".format(port, desc))
    
    if port_list==[]: 
        print("-E- no COM PORTS detected\n\n")
        exit(1)


#def write_read(x):
#    arduino.write(bytes(x, 'utf-8'))
#    time.sleep(0.05)
#    data = arduino.readline()
#    return data


def main():
    print("Ardiuno Serial Slave code")
    list_com_ports()
    arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)
    while True:
        num = input("Enter a number: ")
        #value = write_read(num)
        arduino.write(bytes(num, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline()
        print(data)
    return


if __name__ == "__main__":
    main()