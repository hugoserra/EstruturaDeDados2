from Libs.SGBD import SGBD

MySGBD = SGBD('delimiter')

MySGBD.set_attribute('Titulo','The Wither 2')
MySGBD.set_attribute('Produtora','Riot Games')
MySGBD.set_attribute('Genero','Medieval')
MySGBD.set_attribute('Plataforma','All')
MySGBD.set_attribute('Ano','2016')
MySGBD.set_attribute('Classificacao','16')
MySGBD.set_attribute('Preco','R$ 130')
MySGBD.set_attribute('Midia','Digital')
MySGBD.set_attribute('Tamanho','23.5')
MySGBD.write()

MySGBD.set_attribute('Titulo','Assassins Creed')
MySGBD.set_attribute('Produtora','Epic Games')
MySGBD.set_attribute('Genero','Medieval')
MySGBD.set_attribute('Plataforma','Xbox')
MySGBD.set_attribute('Ano','2016')
MySGBD.set_attribute('Classificacao','18')
MySGBD.set_attribute('Midia','Digital')
# MySGBD.set_attribute('Preco','R$ 110') #NULL
MySGBD.set_attribute('Tamanho','18.5')
MySGBD.write()

print(MySGBD.read())





























#a
