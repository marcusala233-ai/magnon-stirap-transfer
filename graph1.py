import numpy as np
import matplotlib.pyplot as plt
from qutip import *
import csv
from google.colab import files  # Importante para o download no Colab

def run_simulation_and_export():
    print("Iniciando simulação e exportação de dados para PRL...")
    
    # --- 1. Configuração do Sistema ---
    w_q = 5000.0 * 2 * np.pi
    w_m = 5000.0 * 2 * np.pi
    g_max = 60.0 * 2 * np.pi
    gamma_q = 0.05 * 2 * np.pi
    
    tlist = np.linspace(0, 0.3, 500) 
    sigma = 0.04
    tau = 0.05
    
    args = {'g_max': g_max, 'sigma': sigma, 'tau': tau}
    
    def omega_s(t, args):
        return args['g_max'] * np.exp(-(t - 0.15 + args['tau']/2)**2 / (2*args['sigma']**2))

    def omega_p(t, args):
        return args['g_max'] * np.exp(-(t - 0.15 - args['tau']/2)**2 / (2*args['sigma']**2))

    # --- 2. Hamiltoniano e Operadores ---
    dim_mag = 3
    psi0 = tensor(basis(2,1), basis(dim_mag,0), basis(2,0))
    target_state = tensor(basis(2,0), basis(dim_mag,0), basis(2,1))
    
    a = tensor(qeye(2), destroy(dim_mag), qeye(2))
    sm1 = tensor(destroy(2), qeye(dim_mag), qeye(2))
    sm2 = tensor(qeye(2), qeye(dim_mag), destroy(2))
    
    H = [
        [sm1 * a.dag() + sm1.dag() * a, omega_p],
        [sm2 * a.dag() + sm2.dag() * a, omega_s]
    ]
    
    # --- 3. Varredura e Coleta de Dados ---
    kappa_list = np.linspace(0.1, 10.0, 50) 
    fidelities = []
    
    print("Calculando...", end="")
    for k_val in kappa_list:
        kappa = k_val * 2 * np.pi
        c_ops = [np.sqrt(kappa) * a, np.sqrt(gamma_q) * sm1, np.sqrt(gamma_q) * sm2]
        
        result = mesolve(H, psi0, tlist, c_ops, args=args)
        rho_final = result.states[-1]
        F = fidelity(rho_final, target_state)**2
        fidelities.append(F)
    print(" Concluído!")

    # --- 4. Plotagem (Visualização Rápida) ---
    plt.figure(figsize=(8, 5))
    plt.plot(kappa_list, fidelities, 'b-', linewidth=2.5, label='STIRAP Fidelity')
    plt.axhline(y=0.90, color='g', linestyle='--', label='Correção de Erro (90%)')
    plt.axhline(y=0.66, color='r', linestyle='--', label='Limite Clássico (2/3)')
    plt.title('Robustez (Figura 2)')
    plt.xlabel('Kappa (MHz)')
    plt.ylabel('Fidelidade')
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.show()

    # --- 5. Exportação dos Dados (CSV) ---
    filename = "dados_fig2_prl.csv"
    header = ["Kappa_MHz", "Fidelidade"]
    # Aqui unimos as duas listas para escrita
    data_rows = zip(kappa_list, fidelities)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_rows)

    print(f"Arquivo '{filename}' gerado com sucesso.")
    files.download(filename) # Dispara o download no navegador

# Executar tudo
if __name__ == "__main__":
    run_simulation_and_export()