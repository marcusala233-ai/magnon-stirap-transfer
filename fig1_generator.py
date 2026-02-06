import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_prl_schematic():
    # Configuração da Figura (Largura de coluna única PRL ~3.4 polegadas, mas faremos maior para clareza)
    fig = plt.figure(figsize=(8, 6), dpi=300)
    
    # --- PAINEL A: VISTA SUPERIOR (Top-View) ---
    ax_top = fig.add_axes([0.1, 0.4, 0.8, 0.55]) # x, y, width, height
    ax_top.set_xlim(0, 10)
    ax_top.set_ylim(0, 5)
    ax_top.axis('off')
    ax_top.set_title('(a) Top-Down Architecture', loc='left', fontsize=12, fontweight='bold')

    # 1. Substrato GGG (Fundo)
    ggg = patches.Rectangle((1, 1), 8, 3, linewidth=1, edgecolor='gray', facecolor='#f0f0f0', label='GGG Substrate')
    ax_top.add_patch(ggg)
    ax_top.text(8.2, 1.2, "GGG Substrate", fontsize=8, color='gray')

    # 2. Guia de Onda YIG (A "Estrada" Vermelha)
    yig = patches.Rectangle((2, 2.2), 6, 0.6, linewidth=0, facecolor='#d62728', alpha=0.8) # Vermelho YIG
    ax_top.add_patch(yig)
    ax_top.text(5, 2.35, "YIG Waveguide\n(Magnon Channel)", ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # 3. Chip de Silício (Transparente/Azul Claro - Contorno)
    # Representa o chip de cima virado para baixo
    si_chip = patches.Rectangle((1.5, 1.5), 7, 2, linewidth=2, edgecolor='#1f77b4', facecolor='none', linestyle='--')
    ax_top.add_patch(si_chip)
    ax_top.text(1.6, 3.6, "Top Si Chip (Flip-Chip)", fontsize=8, color='#1f77b4', fontweight='bold')

    # 4. Qubits (Transmons - Cruz Dourada)
    # Qubit 1 (Emissor) - Esquerda
    q1_x, q1_y = 2.5, 2.5
    q1_pad1 = patches.Rectangle((q1_x-0.2, q1_y-0.4), 0.4, 0.8, color='#bcbd22') # Vertical
    q1_pad2 = patches.Rectangle((q1_x-0.4, q1_y-0.2), 0.8, 0.4, color='#bcbd22') # Horizontal
    ax_top.add_patch(q1_pad1); ax_top.add_patch(q1_pad2)
    ax_top.text(q1_x, q1_y+0.6, "Qubit 1\n(Sender)", ha='center', fontsize=9)

    # Qubit 2 (Receptor) - Direita
    q2_x, q2_y = 7.5, 2.5
    q2_pad1 = patches.Rectangle((q2_x-0.2, q2_y-0.4), 0.4, 0.8, color='#bcbd22')
    q2_pad2 = patches.Rectangle((q2_x-0.4, q2_y-0.2), 0.8, 0.4, color='#bcbd22')
    ax_top.add_patch(q2_pad1); ax_top.add_patch(q2_pad2)
    ax_top.text(q2_x, q2_y+0.6, "Qubit 2\n(Receiver)", ha='center', fontsize=9)

    # 5. Acopladores (Loops Indutivos)
    # Devem sobrepor as pontas do YIG
    # Loop 1
    loop1 = patches.Arc((2.5, 2.5), 1.0, 1.0, theta1=270, theta2=90, color='black', linewidth=1.5)
    ax_top.add_patch(loop1)
    # Loop 2
    loop2 = patches.Arc((7.5, 2.5), 1.0, 1.0, theta1=90, theta2=270, color='black', linewidth=1.5)
    ax_top.add_patch(loop2)

    # 6. Setas de Pulso STIRAP
    # Seta Pump (Q1 -> YIG) - Atrasada
    ax_top.arrow(2.8, 3.2, 0.5, -0.5, head_width=0.1, color='blue')
    ax_top.text(3.0, 3.3, r"$\Omega_P(t)$", color='blue')

    # Seta Stokes (YIG -> Q2) - Adiantada
    ax_top.arrow(7.2, 3.2, -0.5, -0.5, head_width=0.1, color='green')
    ax_top.text(6.5, 3.3, r"$\Omega_S(t)$", color='green')


    # --- PAINEL B: CORTE LATERAL (Cross-Section) ---
    ax_side = fig.add_axes([0.1, 0.05, 0.8, 0.3]) 
    ax_side.set_xlim(0, 10)
    ax_side.set_ylim(0, 3)
    ax_side.axis('off')
    ax_side.set_title('(b) Cross-Section View', loc='left', fontsize=12, fontweight='bold')

    # Camadas
    # 1. Base (GGG)
    ax_side.add_patch(patches.Rectangle((1, 0.5), 8, 0.5, facecolor='#f0f0f0', edgecolor='gray'))
    ax_side.text(9.1, 0.6, "GGG", fontsize=8)

    # 2. YIG
    ax_side.add_patch(patches.Rectangle((2, 1.0), 6, 0.2, facecolor='#d62728', edgecolor='none'))
    ax_side.text(5, 1.05, "YIG", ha='center', fontsize=8, color='white')

    # 3. Gap de Vácuo (Espaçadores)
    ax_side.add_patch(patches.Rectangle((1.5, 1.2), 0.2, 0.3, color='black')) # Bump bond
    ax_side.add_patch(patches.Rectangle((8.3, 1.2), 0.2, 0.3, color='black')) # Bump bond

    # 4. Chip Topo (Si) virado para baixo
    ax_side.add_patch(patches.Rectangle((1.5, 1.5), 7, 0.5, facecolor='#cceeff', edgecolor='#1f77b4'))
    ax_side.text(9.1, 1.6, "Si Top Chip", fontsize=8)

    # 5. Qubits (Embaixo do Si, perto do YIG)
    ax_side.add_patch(patches.Rectangle((2.3, 1.4), 0.4, 0.1, color='#bcbd22')) # Q1
    ax_side.add_patch(patches.Rectangle((7.3, 1.4), 0.4, 0.1, color='#bcbd22')) # Q2

    # Campos Magnéticos (Ilustrativo)
    # Field lines Q1 -> YIG
    ax_side.annotate("", xy=(2.5, 1.1), xytext=(2.5, 1.4), arrowprops=dict(arrowstyle="->", color='blue', lw=1.5))
    ax_side.text(2.6, 1.2, r"$g_1(t)$", color='blue', fontsize=9)

    # Field lines Q2 -> YIG
    ax_side.annotate("", xy=(7.5, 1.1), xytext=(7.5, 1.4), arrowprops=dict(arrowstyle="->", color='green', lw=1.5))
    ax_side.text(7.1, 1.2, r"$g_2(t)$", color='green', fontsize=9)
    
    # Campo Estático B0
    ax_side.arrow(4, 0.2, 2, 0, head_width=0.1, color='purple')
    ax_side.text(5, 0.35, r"$B_0 \approx 180$ mT", color='purple', ha='center')

    plt.savefig('fig1_schematic.png', bbox_inches='tight')
    print("Figura 1 gerada: fig1_schematic.png")
    plt.show()

if __name__ == "__main__":
    create_prl_schematic()