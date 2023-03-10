#!/usr/bin/env python
# coding: utf-8

# # Code to draw the circuit

# In[ ]:


from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer,execute
from numpy import pi



def Comparison(a,b):
    
    #Selecting the maximum no. of qubits required to represent a single qubit
    n = max(a.bit_length(), b.bit_length())
    
    #Converting interger to binary 
    a_binary = format(a, f'0{n}b')
    b_binary = format(b, f'0{n}b')
    res_a = [int(x) for x in str(a_binary)]
    res_b = [int(x) for x in str(b_binary)]
    
    #Creating a quantum circuit with 3n qubits and n classical bits
    
    qreg_q = QuantumRegister(3*n, 'q')
    creg_c = ClassicalRegister(n, 'c')
    qc = QuantumCircuit(qreg_q, creg_c)
    
   # Applying x-gates accoring to the binary conversion. e.g. '1' in binary is '01' for two qubits
    for i in range(2*n):
        if i < n:
            
            if res_a[i] == 1:
                qc.x(qreg_q[i])
            else:
                qc.id(qreg_q[i])
            
        else :
            if res_b[i-n] == 1:
                qc.x(qreg_q[i])
            else:
                qc.id(qreg_q[i])
                
    #comparing first qubits of both the integer inputs. Applying cnot on a & ancilla qubit and 
    #ccnot on qubits of a,b & ancilla such that ancilla is one only when a = 1 and b=/1
    for i in range(n):
        if i < n-1:
            qc.cx(qreg_q[i],qreg_q[2*n+i])
            qc.ccx(qreg_q[i],qreg_q[i+n],qreg_q[2*n+i])
           # qc.ccx(qreg_q[i+n],qreg_q[i+1],qreg_q[2*n+i+1])
           # qc.ccx(qreg_q[i+n],qreg_q[i+1+n],qreg_q[2*n+i+1])
        else:
            qc.cx(qreg_q[i],qreg_q[2*n+i])
            qc.ccx(qreg_q[i],qreg_q[i+n],qreg_q[2*n+i])
        
        qc.measure(qreg_q[i+2*n], creg_c[i]) # measurement 
    
    #Calling the simulator
    simulator = Aer.get_backend('qasm_simulator')
   

    job = execute(qc, simulator, shots=1000)
   

    result = job.result()
   

    counts = result.get_counts(qc)
        
    
    
    return qc

Comparison(3,5).draw()





# # Code to get the output

# In[ ]:


from ibm_quantum_widgets import CircuitComposer
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer,execute
from numpy import pi



def Comparison(a,b):
    
    #Selecting the maximum no. of qubits required to represent a single qubit
    n = max(a.bit_length(), b.bit_length())
    
    #Converting interger to binary 
    a_binary = format(a, f'0{n}b')
    b_binary = format(b, f'0{n}b')
    res_a = [int(x) for x in str(a_binary)]
    res_b = [int(x) for x in str(b_binary)]
    
    #Creating a quantum circuit with 3n qubits and n classical bits
    
    qreg_q = QuantumRegister(3*n, 'q')
    creg_c = ClassicalRegister(n, 'c')
    qc = QuantumCircuit(qreg_q, creg_c)
    
   # Applying x-gates accoring to the binary conversion. e.g. '1' in binary is '01' for two qubits
    for i in range(2*n):
        if i < n:
            
            if res_a[i] == 1:
                qc.x(qreg_q[i])
            else:
                qc.id(qreg_q[i])
            
        else :
            if res_b[i-n] == 1:
                qc.x(qreg_q[i])
            else:
                qc.id(qreg_q[i])
                
    #comparing first qubits of both the integer inputs. Applying cnot on a & ancilla qubit and 
    #ccnot on qubits of a,b & ancilla such that ancilla is one only when a = 1 and b=/1
    for i in range(n):
        if i < n-1:
            qc.cx(qreg_q[i],qreg_q[2*n+i])
            qc.ccx(qreg_q[i],qreg_q[i+n],qreg_q[2*n+i])
           # qc.ccx(qreg_q[i+n],qreg_q[i+1],qreg_q[2*n+i+1])
           # qc.ccx(qreg_q[i+n],qreg_q[i+1+n],qreg_q[2*n+i+1])
        else:
            qc.cx(qreg_q[i],qreg_q[2*n+i])
            qc.ccx(qreg_q[i],qreg_q[i+n],qreg_q[2*n+i])
        
        qc.measure(qreg_q[i+2*n], creg_c[i]) # measurement 
    
    #Calling the simulator
    simulator = Aer.get_backend('qasm_simulator')
   

    job = execute(qc, simulator, shots=1000)
   

    result = job.result()
   

    counts = result.get_counts(qc)
        
    
    
    return counts






print("Measurement state:", Comparison(3,5))


# In[ ]:




