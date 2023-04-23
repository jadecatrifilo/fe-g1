# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Datos
alpha = 0.11  # Participación del capital en el mercado del yodo
beta = 0.89  # Participación del capital en el resto de la economía
K_bar = 33420  # Oferta total de capital (humano)
L_bar = 176209  # Oferta laboral total

def F(K, L, alpha=alpha):
    """Función de producción del mercado del yodo"""
    return (K**alpha)*(L**(1-alpha))

def G(K, L, beta=beta):
    """Función de producción del resto de la economía"""
    return (K**beta)*(L**(1-beta))

def edgeworth(L, K_bar=K_bar, L_bar=L_bar, alpha=alpha, beta=beta):
    """Curva de eficiencia de Edgeworth"""
    a = (1-alpha)/alpha
    b = (1-beta)/beta
    return b*L*K_bar/(a*(L_bar-L)+b*L)

def FPP(L_yodo, K_bar=K_bar, L_bar=L_bar, alpha=alpha, beta=beta):
    """Frontera de posibilidades de producción"""
    K_yodo = edgeworth(L_yodo, K_bar, L_bar, alpha, beta)
    Q_yodo = F(K_yodo, L_yodo, alpha)
    Q_resto = G(K_bar-K_yodo, L_bar-L_yodo, beta)
    return Q_yodo, Q_resto

# Gráfico de la FPP
L_yodo = np.arange(0, L_bar)
Q_yodo, Q_resto = FPP(L_yodo)
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(Q_yodo, Q_resto, 'k-', linewidth=2)
ax.set_xlabel('Producción del mercado del yodo', fontsize=14)
ax.set_ylabel('Producción del resto de la economía', fontsize=14)
ax.set_title('Frontera de posibilidades de producción', fontsize=16)
plt.show()
