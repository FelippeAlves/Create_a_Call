import PySimpleGUI as sg

class Projeto:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome do Cliente:', size=(10,0)), sg.Input(size=(10,0),key='nome')],
            [sg.Text('Situação:'), sg.Radio('Sem acesso','situaçao',key='semacesso'), sg.Radio('Lentidão','situaçao',key='lentidao'), sg.Radio('Quedas','situaçao',key='quedas')],
            [sg.Text("Link depura?: "),sg.Radio('Sim','linkdepura',key='linksim'), sg.Radio('Não', 'linkdepura',key='linknao')],
            [sg.Text('Caso Link depure --->'), sg.Text('Tempo de sessão:'),sg.Input(size=(11,0),key='sessao'), sg.Text('Ping médio:'),sg.Input(size=(3,0),key='ping'), sg.Text('Consumo:'),sg.Input(size=(8,0),key='consumo'),sg.Text('dBm:'),sg.Input(size=(6,0),key='dbm')],
            [sg.Text('Qual ONU/SXT/Cabeada?:'), sg.Radio('Nokia','onu',key='nokia'),sg.Radio('Parks','onu',key='parks'),sg.Radio('Huawei','onu',key='huawei'),sg.Radio('SXT','onu',key='sxt'),sg.Radio('Cabeada','onu',key='cabeada')],
            [sg.Text("Luzes acendendo:"), sg.Checkbox('Auth', key='auth'), sg.Checkbox('Link',key='link'),sg.Checkbox('PON',key='pon'),sg.Checkbox('WAN', key='wan'),sg.Checkbox('LOS', key='los')],
            [sg.Text('Procedimentos:'), sg.Checkbox('Reboot', key='reboot'), sg.Checkbox('Verificou Cabos', key='cabos'), sg.Checkbox('Alterou Channel do Wifi', key='wifi')],
            [sg.Text('Link voltou a depurar?:'), sg.Radio('Sim','linkvoltou',key='linkvoltousim'),sg.Radio('Não','linkvoltou',key='linkvoltounao')],
            [sg.Text('Caso Link volte a depurar --->'), sg.Text('Ping médio:'),sg.Input(size=(3,0),key='ping2'), sg.Text('Consumo:'),sg.Input(size=(8,0),key='consumo2'),sg.Text('dBm:'),sg.Input(size=(6,0),key='dbm2')],
            [sg.Text('Qual a disponibilidade do cliente?:'), sg.Radio('Comercial', 'horario', key='comercial'), sg.Radio('Somente de Manhã', 'horario', key='manha'),sg.Radio('Somente de Tarde', 'horario', key='tarde'), sg.Checkbox('Disponibilidade para adiantar', key='disp')],
            [sg.Checkbox('Vai haver um responsável, maior de 18 anos na residência',key='resp')],
            [sg.Text('Telefone:'), sg.Input(size=(11,0),key='tel')],
            [sg.Button('Construir')],
            [sg.Output(), sg.Text('Aplicação desenvolvida por: Felippe Alves de Paula')]
        ]
        #Janela
        self.janela = sg.Window("Chamado").layout(layout)
        #Extrair dados
        

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            semacesso = self.values['semacesso']
            lentidao = self.values['lentidao']
            quedas = self.values['quedas']
            linkdepura = self.values['linksim']
            linknaodepura = self.values['linknao']
            nokia = self.values['nokia']
            parks = self.values['parks']
            huawei = self.values['huawei']
            sxt = self.values['sxt']
            cabeada = self.values['cabeada']
            auth = self.values['auth']
            link = self.values['link']
            pon = self.values['pon']
            wan = self.values['wan']
            los = self.values['los']
            sessao = self.values['sessao']
            ping = self.values['ping']
            consumo = self.values['consumo']
            dbm = self.values['dbm']
            reboot = self.values['reboot']
            cabos = self.values['cabos']
            wifi = self.values['wifi']
            linkvoltousim = self.values['linkvoltousim']
            linkvoltounão = self.values['linkvoltounao']
            ping2 = self.values['ping2']
            consumo2 = self.values['consumo2']
            dbm2 = self.values['dbm2']
            comercial = self.values['comercial']
            manha = self.values['manha']
            tarde = self.values['tarde']
            disp = self.values['disp']
            tel = self.values['tel']
            resp = self.values['resp']

            result = 'Sr(a) ' +nome
            if(semacesso == True):
                result += ' reporta estar sem acesso.'
            elif(lentidao == True):
                result+= ' reporta estar com lentidão na conexão.'
            elif(quedas == True):
                result+= ' reporta estar com quedas na conexão.'
            
            if(linkdepura == True):
                result+= ' Link depura à '+sessao +', ping médio de '+ping+'ms, consumo de '+consumo+'mbps.'
                if(nokia == True or huawei == True or parks == True or sxt == True):
                    result+= ' Fechando à '+dbm+' dBm.' 
            else:
                result+= ' Link não depura.'

            if(nokia == True):
                if(link == True and auth == False):
                    result+= ' Luz Link acende, mas Auth está apagada.'
                elif(link == False and auth == False):
                    result+= ' Luz Link e Auth não acendem.'
                elif(link == False and auth == True):
                    result+= ' Luz Auth acendendo, mas Link está apagada.'
                elif(link == True and auth == True):
                    result+= ' Luz Auth e Link estão acendendo.'

            if(huawei == True or parks == True):
                if(pon == True and los == False):
                    result+= ' Luz PON acende.'
                if(pon == False and los == True):
                    result+= ' Luz LOS acendendo.'
            

            if(sxt == True or cabeada == True):
                if(wan == True):
                    result+= ' Luz WAN acende.'
                elif(wan == False):
                    result+= ' Luz WAN não acende.'
            
            if(reboot == True and cabos == True and wifi == True):
                result+= ' Realizado o reboot, verificado os cabos e realizado alteração da frequencia do Wi-Fi.'
            if(reboot == True and cabos == True and wifi == False):
                result+= ' Realizado o reboot e verificado os cabos.'
            if(reboot == True and cabos == False and wifi == False):
                result+= ' Realizado o reboot.'
            if(reboot == False and cabos == True and wifi == False):
                result+= ' Verificado os cabos.'
            if(reboot == False and cabos == False and wifi == True):
                result+= ' Realizado a alteração da frequencia do Wi-Fi.'
            if(reboot == False and cabos == True and wifi == True):
                result+= ' Verificado os cabos e realizado alteração da frequencia do Wi-Fi.'

            if(linkvoltousim == True):
                result+= ' Link voltou a depurar, '+'ping médio de '+ping+'ms, consumo de '+consumo+'mbps.'
                if(nokia == True or huawei == True or parks == True or sxt == True):
                    result+= ' Fechando à '+dbm+' dBm.'
            else:
                result+= ' Link continua sem depurar.'
            
            if(comercial == True and disp == True):
                result = 'Disponibilidade para adiantar em período comercial. '+result
            elif(comercial == True and disp == False):
                result = 'Disponibilidade em período comercial. '+result
            
            if(manha == True and disp == True):
                result = 'Disponibilidade para adiantar no período da manhã. '+result
            elif(manha == True and disp == False):
                result = 'Disponibilidade no período manhã. '+result
            
            if(tarde == True and disp == True):
                result = 'Disponibilidade para adiantar no período da tarde. '+result
            elif(tarde == True and disp == False):
                result = 'Disponibilidade no período tarde. '+result
            
            if(resp == True):
                result+= 'Haverá um responsável, maior de 18 anos na residência e estará ciente dos procedimentos preventivos do COVID-19.'
            
            result+= ' Telefone: '+tel+'.'
        

            print(f'{result}')
tela = Projeto()
tela.Iniciar()

