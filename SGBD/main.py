from Libs.SGBD import SGBD
import pandas as pd #Pandas apenas é utilizado para fins de exibição indentada no terminal, nada mais.
pd.set_option('display.max_rows', None)

Games = SGBD('delimiter')
Games.database.set_database_archive("Data/games.txt")

#Casa base utiliza uma estrategia
MySGBD_1 = SGBD('fixed_size')
MySGBD_2 = SGBD('fixed_fields')
MySGBD_3 = SGBD('size_in_bytes')
MySGBD_4 = SGBD('delimiter')


def Populate():
    for register in Games.read():

        #Dados vindos da base de dados games.txt, se o dado estiver preenchido OK, senao, ""
        Titulo        = register['Titulo']        if ('Titulo' in register)        else ""
        Produtora     = register['Produtora']     if ('Produtora' in register)     else ""
        Genero        = register['Genero']        if ('Genero' in register)        else ""
        Plataforma    = register['Plataforma']    if ('Plataforma' in register)    else ""
        Ano           = register['Ano']           if ('Ano' in register)           else ""
        Classificacao = register['Classificacao'] if ('Classificacao' in register) else ""
        Preco         = register['Preco']         if ('Preco' in register)         else ""
        Midia         = register['Midia']         if ('Midia' in register)         else ""
        Tamanho       = register['Tamanho']       if ('Tamanho' in register)       else ""

        #Abaixo, os dado de games.txt são persistidos nos outros bancos de dados, utilizando outras estrategias de armazenamento
        MySGBD_1.set_attribute('Titulo',Titulo)
        MySGBD_1.set_attribute('Produtora',Produtora)
        MySGBD_1.set_attribute('Genero',Genero)
        MySGBD_1.set_attribute('Plataforma',Plataforma)
        MySGBD_1.set_attribute('Ano',Ano)
        MySGBD_1.set_attribute('Classificacao',Classificacao)
        MySGBD_1.set_attribute('Preco',Preco)
        MySGBD_1.set_attribute('Midia',Midia)
        MySGBD_1.set_attribute('Tamanho',Tamanho)
        MySGBD_1.write()

        MySGBD_2.set_attribute('Titulo',Titulo)
        MySGBD_2.set_attribute('Produtora',Produtora)
        MySGBD_2.set_attribute('Genero',Genero)
        MySGBD_2.set_attribute('Plataforma',Plataforma)
        MySGBD_2.set_attribute('Ano',Ano)
        MySGBD_2.set_attribute('Classificacao',Classificacao)
        MySGBD_2.set_attribute('Preco',Preco)
        MySGBD_2.set_attribute('Midia',Midia)
        MySGBD_2.set_attribute('Tamanho',Tamanho)
        MySGBD_2.write()

        MySGBD_3.set_attribute('Titulo',Titulo)
        MySGBD_3.set_attribute('Produtora',Produtora)
        MySGBD_3.set_attribute('Genero',Genero)
        MySGBD_3.set_attribute('Plataforma',Plataforma)
        MySGBD_3.set_attribute('Ano',Ano)
        MySGBD_3.set_attribute('Classificacao',Classificacao)
        MySGBD_3.set_attribute('Preco',Preco)
        MySGBD_3.set_attribute('Midia',Midia)
        MySGBD_3.set_attribute('Tamanho',Tamanho)
        MySGBD_3.write()

        MySGBD_4.set_attribute('Titulo',Titulo)
        MySGBD_4.set_attribute('Produtora',Produtora)
        MySGBD_4.set_attribute('Genero',Genero)
        MySGBD_4.set_attribute('Plataforma',Plataforma)
        MySGBD_4.set_attribute('Ano',Ano)
        MySGBD_4.set_attribute('Classificacao',Classificacao)
        MySGBD_4.set_attribute('Preco',Preco)
        MySGBD_4.set_attribute('Midia',Midia)
        MySGBD_4.set_attribute('Tamanho',Tamanho)
        MySGBD_4.write()


def ViewDatabases():
    #O metodo read retorna a base de dados como um array de dicionarios, ou seja MySGBD_1.read()[0]["Titulo"], retorna o titulo do primeiro registro
    print("=====================================================================================================================================================================")
    print(pd.DataFrame(MySGBD_1.read()))
    print("=====================================================================================================================================================================")
    print(pd.DataFrame(MySGBD_2.read()))
    print("=====================================================================================================================================================================")
    print(pd.DataFrame(MySGBD_3.read()))
    print("=====================================================================================================================================================================")
    print(pd.DataFrame(MySGBD_4.read()))
    print("=====================================================================================================================================================================")

# Populate() #Popula as bases com os dados de games.txt, com metodos especificos
ViewDatabases()
