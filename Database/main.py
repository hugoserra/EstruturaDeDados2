from Libs.SGBD import SGBD

# self.register_size = {"Titulo":50, "Produtora":40, "Genero":25, "Plataforma":15, "Ano":4, "Classificacao":12, "Preco":7, "Midia":8, "Tamanho":7}

MySGBD = SGBD()
MySGBD.set_attribute('Titulo','The Wither 2')
MySGBD.set_attribute('Produtora','Riot Games')
MySGBD.set_attribute('Genero','Medieval')
MySGBD.set_attribute('Plataforma','All')
MySGBD.set_attribute('Ano','2016')
MySGBD.set_attribute('Classificacao','16')
MySGBD.set_attribute('Preco','R$ 130')
MySGBD.set_attribute('Midia','Xbox')
MySGBD.set_attribute('Tamanho','23.5')
MySGBD.write_register()

print(MySGBD.read_registers())





























#a
