def plot_dynamics_figure3():
    print("Gerando Dinâmica Temporal (Figura 3)...")
    
    # Usamos um Kappa intermediário/alto para provar robustez visualmente
    kappa = 5.0 * 2 * np.pi 
    
    # (Reutilizando os mesmos parâmetros do sistema anterior para consistência)
    w_q = 5000.0 * 2 * np.pi
    g_max = 60.0 * 2 * np.pi
    gamma_q = 0.05 * 2 * np.pi
    tlist = np.linspace(0, 0.3, 500) # 0 a 300ns
    sigma = 0.04
    tau = 0.05
    args = {'g_max': g_max, 'sigma': sigma, 'tau': tau}
    
    # Definição dos Pulsos (Apenas para visualização no gráfico também)
    vals_omega_p = g_max * np.exp(-(tlist - 0.15 - tau/2)**2 / (2*sigma**2))
    vals_omega_s = g_max * np.exp(-(tlist - 0.15 + tau/2)**2 / (2*sigma**2))

    # Operadores e Hamiltoniano
    dim_mag = 3
    psi0 = tensor(basis(2,1), basis(dim_mag,0), basis(2,0))
    a = tensor(qeye(2), destroy(dim_mag), qeye(2))
    sm1 = tensor(destroy(2), qeye(dim_mag), qeye(2))
    sm2 = tensor(qeye(2), qeye(dim_mag), destroy(2))
    
    def omega_s_func(t, args):
        return args['g_max'] * np.exp(-(t - 0.15 + args['tau']/2)**2 / (2*args['sigma']**2))
    def omega_p_func(t, args):
        return args['g_max'] * np.exp(-(t - 0.15 - args['tau']/2)**2 / (2*args['sigma']**2))

    H = [[sm1 * a.dag() + sm1.dag() * a, omega_p_func], [sm2 * a.dag() + sm2.dag() * a, omega_s_func]]
    
    # Colapso
    c_ops = [np.sqrt(kappa)*a, np.sqrt(gamma_q)*sm1, np.sqrt(gamma_q)*sm2]
    
    # Solver
    result = mesolve(H, psi0, tlist, c_ops, args=args)
    
    # Extrair Populações
    # População do Qubit 1 (Emissor)
    pop_q1 = expect(tensor(projection(2,1,1), qeye(dim_mag), qeye(2)), result.states)
    # População do Magnon (Canal) - O que deve ser zero!
    pop_mag = expect(tensor(qeye(2), projection(dim_mag,1,1), qeye(2)), result.states)
    # População do Qubit 2 (Receptor)
    pop_q2 = expect(tensor(qeye(2), qeye(dim_mag), projection(2,1,1)), result.states)

    # --- PLOTAGEM ---
    fig, ax1 = plt.subplots(figsize=(9, 6))

    # Eixo Esquerdo: Populações
    ax1.plot(tlist, pop_q1, 'b-', label=r'Emissor ($P_{Q1}$)')
    ax1.plot(tlist, pop_q2, 'g-', label=r'Receptor ($P_{Q2}$)')
    ax1.fill_between(tlist, pop_mag, color='red', alpha=0.3, label=r'Magnon ($P_{mag}$)')
    ax1.set_xlabel('Tempo ($\mu s$)')
    ax1.set_ylabel('População')
    ax1.set_ylim(-0.05, 1.05)
    
    # Eixo Direito: Pulsos de Controle (Pontilhados) para mostrar a sequência STIRAP
    ax2 = ax1.twinx()
    ax2.plot(tlist, vals_omega_s/(2*np.pi), 'g--', alpha=0.5, label='Pulso Stokes (Q2)')
    ax2.plot(tlist, vals_omega_p/(2*np.pi), 'b--', alpha=0.5, label='Pulso Pump (Q1)')
    ax2.set_ylabel('Rabi Frequency $\Omega(t)$ (MHz)', color='gray')
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')
    
    plt.title(f'Transferência Adiabática com YIG "Sujo" ($\kappa = 5$ MHz)')
    plt.show()

    # Dados numéricos rápidos
    print(f"População Máxima no Magnon: {max(pop_mag)*100:.4f}% (Isso prova o Dark State!)")
    print(f"Sucesso da Transferência: {pop_q2[-1]*100:.2f}%")

plot_dynamics_figure3()