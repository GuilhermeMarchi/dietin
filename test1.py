from calculator import calculate_nutrition



lista_padrao = [    
    'Iogurte Turbinado', 
    'Pao_com_ovo', 
    'Whey_maquina'
    ]

MP_Arroz_com_Frango = 2*[
    'MP_Arroz com Frango (1/5)',
]

MP_Wrap = 2*[
    'Marmita de Wrap (1/5)'
]

MP_Salmao = 2*[
    'Marmita de Salmão (1/5)'
]

my_day = MP_Arroz_com_Frango + lista_padrao 

calculate_nutrition(my_day)