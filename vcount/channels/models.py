from xml.etree import ElementTree as et
import ast

# Create your models here.

def setSettingsToView(settings):
    initial = {}
    
    initial['isswitched'] = ast.literal_eval(settings.content.find('Entrances/Entrance/IsSwitched').text)
    initial['savevideo'] = ast.literal_eval(settings.content.find('Entrances/Entrance/VideoSurveillance/Enabled').text)
    initial['useautocalibration'] = ast.literal_eval(settings.content.find('Entrances/Entrance/UseAutocalibration').text)

    initial['y_offset1'] = settings.content.find('Entrances/Entrance/YOffset1').text
    initial['y_offset2'] = settings.content.find('Entrances/Entrance/YOffset2').text
    
    initial['minflow'] = settings.content.find('Entrances/Entrance/MinObjFlow').text
    initial['maxflow'] = settings.content.find('Entrances/Entrance/MaxObjFlow').text
    
    cellsList = ['0'] * 1000
    
    root =  settings.content.getroot()
    for child in root.findall('./Entrances/Entrance/IgnorableCells/CellIndex'):
        index = int(child.text)
        cellsList[index] = '1'
    
    initial['ignoredcells'] = ''.join(cellsList)
    
    return initial

def setSettingsToXML(form, settings):
    cd  = form.cleaned_data

    settings.content.find('Entrances/Entrance/IsSwitched').text = str(cd['isswitched'])
    settings.content.find('Entrances/Entrance/VideoSurveillance/Enabled').text = str(cd['savevideo'])
    settings.content.find('Entrances/Entrance/UseAutocalibration').text = str(cd['useautocalibration'])
    
    settings.content.find('Entrances/Entrance/YOffset1').text = cd['y_offset1']
    settings.content.find('Entrances/Entrance/YOffset2').text = cd['y_offset2']
    
    settings.content.find('Entrances/Entrance/MinObjFlow').text = cd['minflow']
    settings.content.find('Entrances/Entrance/MaxObjFlow').text = cd['maxflow']
    
    cells = settings.content.find('Entrances/Entrance/IgnorableCells')
    cellsList = list(cd['ignoredcells'])
        
    for child in cells.findall('CellIndex'):
        cells.remove(child)
        
    for i in xrange(1000):
        if cellsList[i] == '1':
            cell = et.SubElement(cells, 'CellIndex')
            cell.text = str(i)
    
    return settings.writeSettings()