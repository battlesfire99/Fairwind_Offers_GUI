from reportlab.pdfgen import canvas #Importe le fond blanc du pdf
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.colors import rgb2cmyk, PCMYKColor
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.pagesizes import landscape, portrait, A4
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.charts.axes import XValueAxis, YValueAxis, AdjYValueAxis, NormalDateXValueAxis
import numpy as np



filename = 'Report.pdf'
documentTitle = "Template Rapport"
nomClient = "Nom du client"
InfoFairwind = ["Fairwind SA", "info@fairwind.be", "www.fairwind.be"]
CoordonnesFairwind = ["299 Chaussée de Gilly", "6220 Fleurs - Belgique", "BE 0893.326.646"]
imageCirculaire = "Photo_Circulaire_PageGarde.png"
imageFond = "Fond_PageGarde.png"
imageClient = "Photo_Rectangulaire_PageGarde.png"
vueAerienne = "VueAerienne.png"
imageLogoFairwind ="LogoFairwind.png"
header_image_portrait = "Fairwind_Header_Portrait.png"
header_image_landscape = "Fairwind_Header_Landscape.png"
date = "25 Janvier 2022"
dictClient = {'NomClient':"NewCCD", 'AdresseClient' : "299 Chaussée de Gilly, 6220 Fleurus - Belgique", 'MailClient' : "jean-yves.bottieau@fairwind.be", 'TelClient' : "+32498405559", 'TVAClient': 'BE 0893.326.646', 'PuissanceMaxClient':'500kW', 'BudgetClient':'500000', 'SurfacePVToiture':'1000','PlacesCarport':'12'}
val_Autoconso = 80 #[%]
val_AutonomieEnerget = 40 #[%]
dictResumeFinancier = {'PrixElec' : 0.15, 'InvestHorsSubsides' : 311000, 'InvestAvecSubsides' : 275000, 'Benefs20ans' : 1000000, 'RendementBrut' : 11.2, 'Payback' : 7.8, 'IRR':12}
symboleEolienne = "SymboleEolienne.png"
symbolePVtoiture = "SymbolePVToiture.png"
symbolePVcarport = "SymbolePVCarport.png"
symbolebornes = "SymboleBornes.png"
symbolestockage = "SymboleStockage.png"
VentMyWindTurbine = "VentMyWindTurbine.png"
dictVent = {'EstimationBasse' : 6, 'EstimationHaute' : 6.5, 'Exposant':0.3, 'HauteurF100':20, 'HauteurF150':24 , 'HauteurF180':35}
WindProfileEquation = "WindProfileEquation.png"
InclinaisonOrientation = "InclinaisonOrientation.png"
dictPlacementPanneaux = {'PVToiture':True, 'PVCarport':True, 'OrientationToiture':12, 'OrientationCarport':12, 'InclinaisonToiture':12, 'InclinaisonCarport':12, 'SurfaceToiture':150, 'SurfaceCarport':150}
dictConsommationActuelle = {'ProfilConso': "Quart-Horaire", 'ConsoTotale':1000000, 'ConsoQuotidienne' : (200,200,200,200,200,200,200,200,200,200,200,200,1000,200,200,200,200,200,200,200,200,200,200,200), 'ConsoHebdomadaire':(5000,5000,5000,5000,5000,5000,10000), 'ConsoAnnuelle':(20000, 20000,20000,20000,20000,20000,50000,20000,20000,20000,20000,20000)}
dictConsommationAdditionnelle = {'ConsoSuppl': True, 'ConsoTotaleSuppl':1000000, 'ConsoQuotidienne' : (200,200,200,200,200,200,200,200,200,200,200,200,1000,200,200,200,200,200,200,200,200,200,200,200), 'ConsoHebdomadaire':(5000,5000,5000,5000,5000,5000,10000), 'ConsoAnnuelle':(20000, 20000,20000,20000,20000,20000,50000,20000,20000,20000,20000,20000)}



def drawMyRulerPortrait(pdf): #Cette fonction permet d'afficher les coordonnées sur la feuille pour faciliter le placement des différents éléments.
    pdf.setStrokeColorRGB(0.75, 0.75, 0.75)


    pdf.line(15 * mm, 7.5 * mm, 15 * mm, 289.5 * mm)   #Limite gauche du document
    pdf.line(195 * mm, 7.5 * mm, 195 * mm, 289.5 * mm)  # Limite droite du document
    pdf.line(15 * mm, 7.5 * mm, 195 * mm, 7.5 * mm)  # Limite basse du document
    pdf.line(15 * mm, 22.5 * mm, 195 * mm, 22.5 * mm)  # Limite footer
    pdf.line(15 * mm, 289.5 * mm, 195 * mm, 289.5 * mm)  # Limite haute du document
    pdf.line(15 * mm, 274.5 * mm, 195 * mm, 274.5 * mm)  # Limite header

    pdf.line(60 * mm, 7.5 * mm, 60 * mm, 289.5 * mm)  # Limite verticale 60mm
    pdf.line(105 * mm, 7.5 * mm, 105 * mm, 289.5 * mm)  # Limite verticale 105mm
    pdf.line(150 * mm, 7.5 * mm, 150 * mm, 289.5 * mm)  # Limite verticale 150mm

    pdf.line(15 * mm, 64.5 * mm, 195 * mm, 64.5 * mm)  # Limite horitonale
    pdf.line(15 * mm, 106.5 * mm, 195 * mm, 106.5 * mm)  # Limite horitonale
    pdf.line(15 * mm, 148.5 * mm, 195 * mm, 148.5 * mm)  # Limite horitonale
    pdf.line(15 * mm, 190.5 * mm, 195 * mm, 190.5 * mm)  # Limite horitonale
    pdf.line(15 * mm, 232.5 * mm, 195 * mm, 232.5 * mm)  # Limite horitonale

    pdf.setFillColorRGB(0.75, 0.75, 0.75)

    pdf.drawCentredString(15 * mm, 2 * mm, '15mm')
    pdf.drawCentredString(60 * mm, 2 * mm, '60mm')
    pdf.drawCentredString(105 * mm, 2 * mm, '105mm')
    pdf.drawCentredString(150 * mm, 2 * mm, '150mm')
    pdf.drawCentredString(198 * mm, 2 * mm, '195mm')

    pdf.drawString(0 * mm, 22.5 * mm, '22.5mm')
    pdf.drawString(0 * mm, 64.5 * mm, '64.5mm')
    pdf.drawString(0 * mm, 106.5 * mm, '106.5mm')
    pdf.drawString(0 * mm, 148.5 * mm, '148.5mm')
    pdf.drawString(0 * mm, 190.5 * mm, '190.5mm')
    pdf.drawString(0 * mm, 232.5 * mm, '232.5mm')
    pdf.drawString(0 * mm, 274.5 * mm, '274.5mm')


def drawMyRulerPaysage(pdf): #Cette fonction permet d'afficher les coordonnées sur la feuille pour faciliter le placement des différents éléments.

    pdf.setStrokeColorRGB(0.75, 0.75, 0.75)
    pdf.line(15 * mm, 7.5 * mm, 282 * mm, 7.5 * mm)   #Limite basse du document
    pdf.line(15 * mm, 22.5 * mm, 282 * mm, 22.5 * mm)  # Limite footer
    pdf.line(15 * mm, 202.5 * mm, 282 * mm, 202.5 * mm)  # Limite haute du document
    pdf.line(15 * mm, 187.5 * mm, 282 * mm, 187.5 * mm)  # Limite header
    pdf.line(15 * mm, 7.5 * mm, 15 * mm, 202.5 * mm)  # Limite gauche
    pdf.line(282 * mm, 7.5 * mm, 282 * mm, 202.5 * mm)  # Limite droite

    pdf.line(15 * mm, 60 * mm, 282 * mm, 60 * mm)  # Limite
    pdf.line(15 * mm, 105 * mm, 282 * mm, 105 * mm)  # Limite
    pdf.line(15 * mm, 150 * mm, 282 * mm, 150 * mm)  # Limite

    pdf.line(64.5 * mm, 7.5 * mm, 64.5 * mm, 202.5 * mm)  # Limite
    pdf.line(106.5 * mm, 7.5 * mm, 106.5 * mm, 202.5 * mm)  # Limite
    pdf.line(148.5 * mm, 7.5 * mm, 148.5 * mm, 202.5 * mm)  # Limite
    pdf.line(190.5 * mm, 7.5 * mm, 190.5 * mm, 202.5 * mm)  # Limite
    pdf.line(232.5 * mm, 7.5 * mm, 232.5 * mm, 202.5 * mm)  # Limite

    pdf.setFillColorRGB(0.75, 0.75, 0.75)

    pdf.drawString(2 * mm, 22.5 * mm, '22.5mm')
    pdf.drawString(2 * mm, 60 * mm, '60mm')
    pdf.drawString(2 * mm, 105 * mm, '105mm')
    pdf.drawString(2 * mm, 150 * mm, '150mm')
    pdf.drawString(2 * mm, 187.5 * mm, '187.5mm')

    pdf.drawCentredString(15 * mm, 1 * mm, '15mm')
    pdf.drawCentredString(64.5 * mm, 1 * mm, '64.5mm')
    pdf.drawCentredString(106.5 * mm, 1 * mm, '106.5mm')
    pdf.drawCentredString(148.5 * mm, 1 * mm, '148.5mm')
    pdf.drawCentredString(190.5 * mm, 1 * mm, '190.5mm')
    pdf.drawCentredString(232.5 * mm, 1 * mm, '232.5mm')
    pdf.drawCentredString(282 * mm, 1 * mm, '282mm')






def coverPage(pdf, fond, logo, circulaire, client, info, coord): #Print la coverPage du projet avec possibilité de changer l'image rectangulaire par un photomontage du projet
    # Import de la police Varela Round
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )
    pdf.setFont(Varela, 12)

    pdf.drawInlineImage(fond, 0, 0, width = 210 * mm, height = 297 * mm)

    pdf.drawImage(logo, 15 * mm, 255 * mm, width=25 * mm, height=17 * mm, mask='auto')
    pdf.drawImage(circulaire, 130 * mm , 215 * mm, width = 90 * mm, height = 90 * mm, mask = 'auto')

    pdf.setFont(Varela, 60)
    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.drawString(42 * mm, 257 * mm, 'Fairwind')

    pdf.setFont(Varela, 26)
    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.drawString(15 * mm, 239 * mm, 'Votre énergie pour l\'avenir')

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)

    pdf.roundRect(15 * mm, 175 * mm, 180 * mm, 20 * mm, 3 * mm, 1 , 1)

    pdf.setFont(Varela, 33)
    pdf.setFillColorRGB(1, 1, 1)
    pdf.drawCentredString(105 * mm, 182 * mm, 'Etude pour projet énergétique')

    pdf.drawInlineImage(client, 15 * mm , 60 * mm , width=180 * mm, height=110 * mm)

    textContact = pdf.beginText(15 * mm , 35 * mm)
    textContact.setFont(Varela, 14)
    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    for line in info :
        textContact.textLine(line)

    pdf.drawText(textContact)

    textCoord = pdf.beginText(140 * mm, 35 * mm)
    textCoord.setFont(Varela, 14)
    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    for line in coord:
        textCoord.textLine(line)

    pdf.drawText(textCoord)


    pdf.showPage()
    pdf.setFont(Varela, 12)
def headerAndFooterPortrait(pdf, headerImage): #Fonction qui sert à ajouter le header et le footer sur chaque page
    pdf.drawInlineImage(headerImage, 15 * mm, 276 * mm, width = 180 * mm, height = 11 * mm)

    # Import de la police Varela Round
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )

    pdf.setFont(Varela, 11)
    pdf.setFillColorRGB(0.75, 0.75, 0.75)

    pdf.drawString(15 * mm, 16 * mm, 'Fairwind SA')
    pdf.drawString(15 * mm, 12 * mm, "BE 0893.326.646")

    pdf.drawCentredString(105 * mm, 16 * mm, '299 Chaussée de Gilly')
    pdf.drawCentredString(105 * mm, 12 * mm, '6220 Fleurus - Belgique')

    pdf.drawRightString(195 * mm, 16 * mm, 'Page')
    page_num = pdf.getPageNumber()-1
    pdf.drawRightString(195 * mm, 12 * mm, '%s' % page_num)

def headerAndFooterLandscape(pdf, headerImage): #Fonction qui sert à ajouter le header et le footer sur chaque page
    pdf.drawInlineImage(headerImage, 15 * mm, 189.5 * mm, width = 267 * mm, height = 11 * mm)

    # Import de la police Varela Round
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )

    pdf.setFont(Varela, 11)
    pdf.setFillColorRGB(0.75, 0.75, 0.75)

    pdf.drawString(15 * mm, 16 * mm, 'Fairwind SA')
    pdf.drawString(15 * mm, 12 * mm, "BE 0893.326.646")

    pdf.drawCentredString(148.5 * mm, 16 * mm, '299 Chaussée de Gilly')
    pdf.drawCentredString(148.5 * mm, 12 * mm, '6220 Fleurus - Belgique')

    pdf.drawRightString(282 * mm, 16 * mm, 'Page')
    page_num = pdf.getPageNumber()-1
    pdf.drawRightString(282 * mm, 12 * mm, '%s' % page_num)


def LettreEnTete(pdf, Date, headerImage):
    # Import de la police Varela Round

    headerAndFooterPortrait(pdf, headerImage)
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )
    pdf.setFont(Varela, 11)
    pdf.setFillColorRGB(0, 0, 0)

    pdf.drawString(15 * mm, 240 * mm, "Madame, ")
    pdf.drawString(15 * mm, 225 * mm, "Monsieur, ")

    pdf.drawRightString(195 * mm, 270 * mm, "Réalisé à Fleurus")
    pdf.drawRightString(195 * mm, 260 * mm, Date)

    pdf.drawString(15 * mm, 190 * mm, "Nous vous remercions de l'intérêt que vous portez à notre société, à nos produits et à nos services.")

    textlines = ["Comme convenu, nous avons le plaisir de vous remettre une offre pour la réalisation de votre",
                 "projet énergétique."]
    text = pdf.beginText(15 * mm, 170 * mm)
    for line in textlines:
        text.textLine(line)
    pdf.drawText(text)

    textlines = ["Nous nous tenons à votre disposition pour tout complément d'information dont vous pourriez ",
                 "avoir besoin et nous vous prions d'agréer, Madame, Monsieur, nos plus sincères salutations."]
    text = pdf.beginText(15 * mm , 145 * mm)
    for line in textlines :
        text.textLine(line)
    pdf.drawText(text)

    pdf.drawString(25 * mm, 100 * mm, "Jean-Yves BOTTIEAU")
    pdf.drawString(25 * mm, 90 * mm, "Aministrateur délégué")
    pdf.drawString(25 * mm, 85 * mm, "Responsable technique")
    pdf.drawImage("Jean-Yves_BOTTIEAU.PNG", 25* mm, 45 * mm, width=40 * mm, height=35 * mm)
    pdf.drawString(25 * mm, 40 * mm, "+32 498 40 55 59")
    pdf.drawString(25 * mm, 35 * mm, "jean-yves.bottieau@fairwind.be")

    pdf.drawRightString(185 * mm, 100 * mm, "Philippe MONTIRONI")
    pdf.drawRightString(185 * mm, 90 * mm, "Aministrateur ")
    pdf.drawRightString(185 * mm, 85 * mm, "Responsable commercial")

    pdf.drawImage("Philippe_MONTIRONI.PNG", 145 * mm, 45 * mm, width=42 * mm, height=37 * mm)
    pdf.drawRightString(185 * mm, 40 * mm, "+32 475 23 30 63")
    pdf.drawRightString(185 * mm, 35 * mm, "philippe.montironi@fairwind.be")

    pdf.showPage()

def ColorPalette():
    Palette = []

    lightbluecolor = colors.Color(red=37 / 256, green=150 / 256, blue=190 / 256)
    mediumbluecolor = colors.Color(red=192 / 256, green=212 / 256, blue=244 / 256)
    bluecolor = colors.Color(red=0.223, green=0.41, blue=0.73)
    orangecolor = colors.Color(red=252 / 256, green=140 / 256, blue=3 / 256)

    Palette.append(lightbluecolor)
    Palette.append(mediumbluecolor)
    Palette.append(bluecolor)
    Palette.append(orangecolor)


    return Palette

def InfosClientEtResume(pdf, headerImage, InfosClient, ResumeFinancier, Autoconso, AutonomieEnerget):
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )
    pdf.setFont(Varela, 25)

    headerAndFooterPortrait(pdf, headerImage)

    ################################## Coordonnées du client #######################################
    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.roundRect(15 * mm, 264 * mm, 180 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(105 * mm, 266 * mm, 'Coordonnées')

    pdf.setFont(Varela, 11)
    pdf.setFillColorRGB(0, 0, 0)

    pdf.drawString(15 * mm, 257 * mm, "Nom du client : ")
    pdf.drawString(15 * mm, 251 * mm, "N° TVA : ")
    pdf.drawString(15 * mm, 245 * mm, "Adresse du site : ")
    pdf.drawString(15 * mm, 239 * mm, "N°Téléphone : ")
    pdf.drawString(15 * mm, 233 * mm, "Adresse Mail : ")

    pdf.drawString(60 * mm, 257 * mm, InfosClient['NomClient'])
    pdf.drawString(60 * mm, 251 * mm, InfosClient['TVAClient'])
    pdf.drawString(60 * mm, 245 * mm, InfosClient['AdresseClient'])
    pdf.drawString(60 * mm, 239 * mm, InfosClient['TelClient'])
    pdf.drawString(60 * mm, 233 * mm, InfosClient['MailClient'])

    ################################## Résumé énergétique #######################################
    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.roundRect(15 * mm, 220 * mm, 180 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(105 * mm, 222 * mm, 'Résumé énergétique')

    d1 = Drawing()
    pieChartAutoconso = Pie()
    pieChartAutoconso.x = 27.5 * mm
    pieChartAutoconso.y = 142 * mm
    pieChartAutoconso.width = 65 * mm
    pieChartAutoconso.height = 65 * mm
    pieChartAutoconso.data = [Autoconso, 100-Autoconso]
    pieChartAutoconso.strokeWidth = 0
    pieChartAutoconso.strokeColor = None

    palette = ColorPalette()
    lightbluecolor = palette[0]
    mediumbluecolor = palette[1]
    bluecolor = palette[2]
    orangecolor =palette[3]
    pieChartAutoconso.slices[0].fillColor = bluecolor
    pieChartAutoconso.slices[1].fillColor = orangecolor

    pieChartAutoconso.slices[0].strokeColor = bluecolor
    pieChartAutoconso.slices[1].strokeColor = orangecolor

    pieChartAutoconso.innerRadiusFraction = 0.6
    d1.add(pieChartAutoconso)
    d1.wrapOn(pdf, 0 * mm, 0 * mm)
    d1.drawOn(pdf, 0 * mm, 0 * mm)

    d2 = Drawing()
    pieChartAutonomie = Pie()
    pieChartAutonomie.x = 117.5 * mm
    pieChartAutonomie.y = 142 * mm
    pieChartAutonomie.width = 65 * mm
    pieChartAutonomie.height = 65 * mm
    pieChartAutonomie.data = [AutonomieEnerget, 100 - AutonomieEnerget]
    pieChartAutonomie.slices[0].fillColor = bluecolor
    pieChartAutonomie.slices[1].fillColor = orangecolor
    pieChartAutonomie.slices[0].strokeColor = bluecolor
    pieChartAutonomie.slices[1].strokeColor = orangecolor

    pieChartAutonomie.innerRadiusFraction = 0.6
    d2.add(pieChartAutonomie)
    d2.wrapOn(pdf, 0 * mm, 0 * mm)
    d2.drawOn(pdf, 0 * mm, 0 * mm)

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.setFont(Varela, 30)
    pdf.drawCentredString(60 * mm, 180 * mm, "%s %%"%Autoconso)

    pdf.setFont(Varela, 10)
    pdf.drawCentredString(60 * mm, 172 * mm, "Autoconsommation")

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.setFont(Varela, 30)
    pdf.drawCentredString(150 * mm, 180 * mm, "%s %%" % AutonomieEnerget)

    pdf.setFont(Varela, 10)
    pdf.drawCentredString(150 * mm, 172 * mm, "Autonomie")
    pdf.drawCentredString(150 * mm, 169 * mm, "énergétique")

    pdf.setFont(Varela, 11)


    pdf.drawImage("co2-reduction.png", 28 * mm, 80 * mm, 65*mm, 65 * mm, mask = 'auto')

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setFont(Varela, 25)
    pdf.drawCentredString(145 * mm, 114 * mm, "Economie de CO2")
    pdf.drawCentredString(145 * mm, 104 * mm, "178 Tonnes")

    ################################## Résumé Financier #######################################

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.roundRect(15 * mm, 69 * mm, 180 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(105 * mm, 71 * mm, 'Résumé financier')

    data = [["Prix du kWh d'électricité", ResumeFinancier['PrixElec'], '€'],
            ["Investissement hors subsides", ResumeFinancier['InvestHorsSubsides'], '€'],
            ["Investissement subsides inclus", ResumeFinancier['InvestAvecSubsides'], '€'],
            ["Bénéfices sur 20 ans", ResumeFinancier['Benefs20ans'], '€'],
            ["Retour sur investissement", ResumeFinancier['Payback'], 'ans'],
            ["Rendement brut", ResumeFinancier['RendementBrut'], '%'],
            ["IRR", ResumeFinancier['IRR'], '%']]


    t = Table(data, colWidths= [118 * mm, 50 * mm, 10 * mm])
    style = TableStyle([
        ('ALIGN', (2, 0), (2, 6), 'CENTER'),
        ('ALIGN', (1, 0), (1, 6), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Varela'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),

    ])


    t.setStyle(style)

    t.wrapOn(pdf, 178 * mm, 50 * mm)
    t.drawOn(pdf, 16 * mm , 22.5*mm)

    pdf.showPage()

def Implantation(pdf, implantation, headerImage, LegendeEolienne, LegendePVtoiture, LegendePVcarport, LegendeBornes, LegendeStockage):
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )

    pdf.setPageSize(landscape(A4))
    headerAndFooterLandscape(pdf, headerImage)

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)

    pdf.roundRect(15 * mm, 177 * mm, 267 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(148.5 * mm, 179 * mm, 'Implantation')

    pdf.drawImage(implantation, 15 * mm, 22.5 * mm, 215 * mm, 150*mm)
    pdf.roundRect(232.5 * mm, 60 * mm, 49.5 * mm, 75 * mm, 3 * mm, 1, 0)

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.drawCentredString(257.25 * mm, 128*mm, "Légende")

    pdf.drawImage(LegendeEolienne, 233.5 * mm, 116 * mm, 7 * mm, 7 * mm, mask = 'auto')
    pdf.drawImage(LegendePVtoiture, 233.5 * mm, 103 * mm, 7 * mm, 4 * mm, mask = 'auto')
    pdf.drawImage(LegendePVcarport, 233.5 * mm, 90 * mm, 7 * mm, 4 * mm, mask = 'auto')
    pdf.drawImage(LegendeBornes, 233.5 * mm, 77 * mm, 5 * mm, 7 * mm, mask = 'auto')
    pdf.drawImage(LegendeStockage, 233.5 * mm, 64 * mm, 7 * mm, 7 * mm, mask = 'auto')

    pdf.setFillColorRGB(0, 0, 0)
    pdf.setStrokeColorRGB(0, 0, 0)
    pdf.setFont(Varela, 15)
    pdf.drawCentredString(260 * mm, 117.75 * mm, "Eolienne")
    pdf.drawCentredString(260 * mm, 104 * mm, "PV en toiture")
    pdf.drawCentredString(260 * mm, 91 * mm, "PV sur carport")
    pdf.drawCentredString(260 * mm, 78.7 * mm, "Bornes")
    pdf.drawCentredString(260 * mm, 65.75 * mm, "Stockage")

    pdf.showPage()

def AnalyseVent(pdf,headerImage, vent, DataVent, equation):
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )

    pdf.setPageSize(portrait(A4))
    headerAndFooterPortrait(pdf, headerImage)

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.roundRect(15 * mm, 264 * mm, 180 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(105 * mm, 266 * mm, 'Analyse des vents')

    pdf.drawImage(vent, 15 * mm, 162 * mm, 125 * mm , 95 * mm)

    pdf.setFillColorRGB(0,0,0)
    pdf.setFont(Varela, 11)

    data1 = [
        ["Type de terrain", "Exposant de terrain a"],
        ["Plat : neige, glace, marécages, herbes courtes, ...", "0.10"],
        ["Mer", "0.13"],
        ["Terrain plat avec champs, paturages, ... (sans arbre)", "0.14"],
        ["Bord de mer / Terrain plat avec peu d'arbres", "0.16"],
        ["Terrain au relief limité / Champ avec herbes hautes", "0.20"],
        ["Inégal : Arbes, zônes peu habitées", "0.23"],
        ["Terrain plat boisé", "0.24"],
        ["Terrain plat boisé avec habitations / Villages / Quatier Résidentiel", "0.27"],
        ["Zoning industriel", "0.29"],
        ["Ville", "0.4"]
    ]

    palette = ColorPalette()

    t1 = Table(data1, colWidths=[128 * mm, 50 * mm])
    style1 = TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), palette[2]),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Varela'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 0.5, colors.black),

    ])

    t1.setStyle(style1)

    t1.wrapOn(pdf, 178 * mm, 70 * mm)
    t1.drawOn(pdf, 16 * mm, 85 * mm)

    Vbasse_F100 = np.around(DataVent['EstimationBasse'] * ((DataVent['HauteurF100'] / 50) ** DataVent['Exposant']), decimals = 2)
    Vhaute_F100 = np.around(DataVent['EstimationHaute'] * ((DataVent['HauteurF100'] / 50) ** DataVent['Exposant']), decimals = 2)
    Vbasse_F150 = np.around(DataVent['EstimationBasse'] * ((DataVent['HauteurF150'] / 50) ** DataVent['Exposant']), decimals = 2)
    Vhaute_F150 = np.around(DataVent['EstimationHaute'] * ((DataVent['HauteurF150'] / 50) ** DataVent['Exposant']), decimals = 2)
    Vbasse_F180 = np.around(DataVent['EstimationBasse'] * ((DataVent['HauteurF180'] / 50) ** DataVent['Exposant']), decimals = 2)
    Vhaute_F180 = np.around(DataVent['EstimationHaute'] * ((DataVent['HauteurF180'] / 50) ** DataVent['Exposant']), decimals = 2)


    data2 = [
        ["Machine", "F100", "F100", "F150", "F150", "F180", "F180"],
        ["Estimation", "Haute", "Basse", "Haute", "Basse", "Haute", "Basse"],
        ["Vitesse du vent à 50m de hauteur [m/s]", DataVent['EstimationBasse'], DataVent['EstimationHaute'], DataVent['EstimationBasse'], DataVent['EstimationHaute'], DataVent['EstimationBasse'], DataVent['EstimationHaute']],
        ["Hauteur de l'éolienne [m]", DataVent['HauteurF100'], DataVent['HauteurF100'], DataVent['HauteurF150'], DataVent['HauteurF150'], DataVent['HauteurF180'], DataVent['HauteurF180']],
        ["Exposant de terrain [~]", DataVent['Exposant'], DataVent['Exposant'], DataVent['Exposant'], DataVent['Exposant'], DataVent['Exposant'], DataVent['Exposant']],
        ["Vitesse du vent à hauteur de l'éolienne [m/s]", Vbasse_F100, Vhaute_F100, Vbasse_F150, Vhaute_F100, Vbasse_F180, Vhaute_F180]
    ]

    style2 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), palette[2]),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Varela'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 0.5, colors.black),
        ('SPAN', (1, 0), (2, 0)),
        ('SPAN', (3, 0), (4, 0)),
        ('SPAN', (5, 0), (6, 0)),
        ('SPAN', (1, 3), (2, 3)),
        ('SPAN', (3, 3), (4, 3)),
        ('SPAN', (5, 3), (6, 3)),
        ('SPAN', (1, 4), (6, 4)),



    ])

    t2 = Table(data2)
    t2.setStyle(style2)
    t2.wrapOn(pdf, 178 * mm, 70 * mm)
    t2.drawOn(pdf, 16 * mm, 39 * mm)

    pdf.setFont(Varela, 11)
    style3 = ParagraphStyle('Normal', fontName = 'Varela', fontSize = 11, alignment = TA_JUSTIFY, spaceBefore = 1 * mm, spaceAfter = 1 * mm)
    p3 = Paragraph("Après une analyse de vent réalisée avec l'outil www.mywindturbine.com, l'estimation de la vitesse moyenne annuelle à 50m de hauteur est comprise entre %s et %s m/s." %(DataVent['EstimationBasse'], DataVent['EstimationHaute']), style3)
    p3.wrapOn(pdf, 49 * mm, 70 * mm)
    p3.drawOn(pdf, 145 * mm, 224 * mm)

    p4 = Paragraph(
        "La vitesse du vent doit être adaptée à la hauteur réelle de l'éolienne en utilisant la formule ci-dessous: ", style3)
    p4.wrapOn(pdf, 49 * mm, 70 * mm)
    p4.drawOn(pdf, 145 * mm, 189 * mm)

    pdf.drawImage(equation, 153 * mm, 167 * mm, 39* mm, 17 * mm)

    p4 = Paragraph(
        "Les données de vent présentées sont communiquées à titre indicatif. Fairwind ne peut garantir l'actualité, la précision et l'exactitude de ces données et en décline donc toute responsabilité.",
        style3)
    p4.wrapOn(pdf, 180 * mm, 70 * mm)
    p4.drawOn(pdf, 15 * mm, 22.5 * mm)

    pdf.showPage()

def AnalyseSoleil(pdf,headerImage, imageIrradiance, placementPanneaux):
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )

    pdf.setPageSize(portrait(A4))
    headerAndFooterPortrait(pdf, headerImage)

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.roundRect(15 * mm, 264 * mm, 180 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(105 * mm, 266 * mm, 'Analyse d\'ensoleillement')

    pdf.drawImage(imageIrradiance, 37.5 * mm, 124 * mm, 135 * mm, 135 * mm)

    CorrectionOrientationToiture = 95
    CorrectionInclinaisonToiture = 95
    CorrectionOrientationCarport = 95
    CorrectionInclinaisonCarport = 95


    data1 = [
        ["Installation en toiture"],
        ["Surface", placementPanneaux['SurfaceToiture'], "m2"],
        ["Orientation", placementPanneaux['OrientationToiture'], "°"],
        ["Inclinaison", placementPanneaux['InclinaisonToiture'], "°"],
        ["Facteur de correction lié à l'orientation", CorrectionOrientationToiture, "%"],
        ["Facteur de correction lié à l'inclinaison", CorrectionInclinaisonToiture , "%"],
        ["Production annuelle estimée par kWc installé ", (0.9*CorrectionInclinaisonToiture*CorrectionOrientationToiture)/100000, "kWh"],


    ]

    palette = ColorPalette()

    t1 = Table(data1, colWidths=[120 * mm, 30 * mm, 28 * mm])
    style1 = TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), palette[2]),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Varela'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 0.5, colors.black),
        ('SPAN', (0, 0), (2, 0)),
        ('ALIGN', (0, 0), (2, 0), 'CENTER')


    ])

    t1.setStyle(style1)
    t1.wrapOn(pdf, 178 * mm, 70 * mm)
    t1.drawOn(pdf, 16 * mm, 76 * mm)

    data2 = [
        ["Installation sur carport"],
        ["Surface", placementPanneaux['SurfaceCarport'], "m2"],
        ["Orientation", placementPanneaux['OrientationToiture'], "°"],
        ["Inclinaison", placementPanneaux['InclinaisonToiture'], "°"],
        ["Facteur de correction lié à l'orientation", CorrectionOrientationToiture, "%"],
        ["Facteur de correction lié à l'inclinaison", CorrectionInclinaisonToiture, "%"],
        ["Production annuelle estimée par kWc installé ",
         (0.9 * CorrectionInclinaisonToiture * CorrectionOrientationToiture) / 100000, "kWh"],

    ]

    t2 = Table(data2, colWidths=[120 * mm, 30 * mm, 28 * mm])
    style2 = TableStyle([
        ('BACKGROUND', (0, 0), (2, 0), palette[2]),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Varela'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 0.5, colors.black),
        ('SPAN', (0, 0), (2, 0)),
        ('ALIGN', (0, 0), (2, 0), 'CENTER')

    ])

    t2.setStyle(style2)
    t2.wrapOn(pdf, 178 * mm, 70 * mm)
    t2.drawOn(pdf, 16 * mm, 25 * mm)

    pdf.showPage()


def ConsommationActuelle(pdf,headerImage, conso, consoSuppl):
    Varela = "Varela"
    pdfmetrics.registerFont(
        TTFont(Varela, 'VarelaRound-Regular.ttf')
    )

    Palette = ColorPalette()

    pdf.setPageSize(portrait(A4))
    headerAndFooterPortrait(pdf, headerImage)

    pdf.setFillColorRGB(0.223, 0.41, 0.73)
    pdf.setStrokeColorRGB(0.223, 0.41, 0.73)
    pdf.roundRect(15 * mm, 264 * mm, 180 * mm, 7 * mm, 1 * mm, 1, 1)

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setFont(Varela, 14)
    pdf.drawCentredString(105 * mm, 266 * mm, 'Consommation du site')

    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont(Varela, 11)

    stylePara = ParagraphStyle('Normal', fontName='Varela', fontSize=11, alignment=TA_JUSTIFY, spaceBefore=1 * mm,
                            spaceAfter=1 * mm)

    if consoSuppl['ConsoSuppl']==False:
        if conso['ProfilConso'] == 'Quart-Horaire':
            p1 = Paragraph(
                "L'étude énergétique présentée dans ce document se base sur un quart-horaire du site fourni par le client.",
                stylePara)

        else:
            p1 = Paragraph(
                "L'étude énergétique présentée dans ce document se base sur un profil de consommation de type %s discuté avec le client." %conso['ProfilConso'],
                stylePara)

        p1.wrapOn(pdf, 180 * mm, 70 * mm)
        p1.drawOn(pdf, 15 * mm, 250 * mm)

        pdf.drawString(15 * mm, 240 * mm,
                       "La consommation actuelle du site est estimée à %s kWh/an." % conso['ConsoTotale'])
    else:
        if conso['ProfilConso'] == 'Quart-Horaire':
            p1 = Paragraph(
                "L'étude énergétique présentée dans ce document se base sur un quart-horaire du site fourni par le client.La consommation actuelle du site est estimée à %s kWh/an."%conso['ConsoTotale'],
                stylePara)

        else:
            p1 = Paragraph(
                "L'étude énergétique présentée dans ce document se base sur un profil de consommation de type %s discuté avec le client.La consommation actuelle du site est estimée à %s kWh/an." %(conso['ProfilConso'],conso['ConsoTotale']),
                stylePara)

        p1.wrapOn(pdf, 180 * mm, 70 * mm)
        p1.drawOn(pdf, 15 * mm, 250 * mm)

        p2 = Paragraph("De plus, après discussion avec le client, une consommation supplémentaire équivalente à environ %s kWh/an. Dès lors, la consommation annuelle du site considérée pour cette étude est d'environ %s kWh/an."%(consoSuppl['ConsoTotaleSuppl'],conso['ConsoTotale']+consoSuppl['ConsoTotaleSuppl']),
                stylePara)

        p2.wrapOn(pdf, 180 * mm, 70 * mm)
        p2.drawOn(pdf, 15 * mm, 234 * mm)

    #Graphe récapitulant la consommation
    Heure = ["00-01h", "01-02h", "02-03h", "03-04h", "04-05h", "05-06h", "06-07h", "07-08h" , "08-09h" , "09-10h", "10-11h", "11-12h", "12-13h", "13-14h", "14-15h", "15-16h", "16-17h", "17-18h", "18-19h", "19-20h", "20-21h", "21-22h", "22-23h", "23-00h"]
    Jour = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    Mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    ConsoQuotidienne = VerticalBarChart()
    ConsoHebdomadaire = VerticalBarChart()
    ConsoAnnuelle = VerticalBarChart()
    if consoSuppl['ConsoSuppl'] == False:
        ConsoQuotidienne.data = [conso['ConsoQuotidienne']]
        ConsoHebdomadaire.data = [conso['ConsoHebdomadaire']]
        ConsoAnnuelle.data = [conso['ConsoAnnuelle']]


    else:
        ConsoQuotidienne.data = [tuple(map(sum,zip(conso['ConsoQuotidienne'],consoSuppl['ConsoQuotidienne'])))]
        ConsoHebdomadaire.data = [tuple(map(sum, zip(conso['ConsoHebdomadaire'], consoSuppl['ConsoHebdomadaire'])))]
        ConsoAnnuelle.data = [tuple(map(sum, zip(conso['ConsoAnnuelle'], consoSuppl['ConsoAnnuelle'])))]

    # Graphe récapitulant la consommation quotidienne
    d1 = Drawing(150*mm, 60*mm)

    ConsoQuotidienne.valueAxis.valueMin = 0
    ConsoQuotidienne.width = 150 * mm
    ConsoQuotidienne.height = 40 * mm
    ConsoQuotidienne.categoryAxis.categoryNames = Heure
    ConsoQuotidienne.categoryAxis.labels.fontName = Varela
    ConsoQuotidienne.categoryAxis.labels.angle = 90
    ConsoQuotidienne.categoryAxis.labels.dx = -2 * mm
    ConsoQuotidienne.categoryAxis.labels.dy = -8 * mm


    ConsoQuotidienne.valueAxis.labels.fontName = Varela
    ConsoQuotidienne.valueAxis.visibleGrid = True
    ConsoQuotidienne.valueAxis.labelTextFormat = '%d kWh'

    ConsoQuotidienne.bars[0].fillColor  = Palette[2]
    ConsoQuotidienne.bars[0].strokeColor = Palette[2]
    ConsoQuotidienne.barLabels.boxStrokeColor = Palette[2]

    d1.add(ConsoQuotidienne)
    d1.wrapOn(pdf, 200 * mm, 0 * mm)
    d1.drawOn(pdf, 34 * mm, 178 * mm)

    # Graphe récapitulant la consommation hebdomadaire
    d2 = Drawing(150 * mm, 60 * mm)
    ConsoHebdomadaire.valueAxis.valueMin = 0
    ConsoHebdomadaire.width = 150 * mm
    ConsoHebdomadaire.height = 40 * mm
    ConsoHebdomadaire.categoryAxis.categoryNames = Jour
    ConsoHebdomadaire.categoryAxis.labels.fontName = Varela
    ConsoHebdomadaire.categoryAxis.labels.angle = 90
    ConsoHebdomadaire.categoryAxis.labels.dx = -2 * mm
    ConsoHebdomadaire.categoryAxis.labels.dy = -10.5 * mm

    ConsoHebdomadaire.valueAxis.labels.fontName = Varela
    ConsoHebdomadaire.valueAxis.visibleGrid = True
    ConsoHebdomadaire.valueAxis.labelTextFormat = '%d kWh'

    ConsoHebdomadaire.bars[0].fillColor = Palette[2]
    ConsoHebdomadaire.bars[0].strokeColor = Palette[2]
    ConsoHebdomadaire.barLabels.boxStrokeColor = Palette[2]

    d2.add(ConsoHebdomadaire)
    d2.wrapOn(pdf, 200 * mm, 0 * mm)
    d2.drawOn(pdf, 34 * mm, 110 * mm)

    # Graphe récapitulant la consommation hebdomadaire
    d3 = Drawing(150 * mm, 60 * mm)
    ConsoAnnuelle.valueAxis.valueMin = 0
    ConsoAnnuelle.width = 150 * mm
    ConsoAnnuelle.height = 40 * mm
    ConsoAnnuelle.categoryAxis.categoryNames = Mois
    ConsoAnnuelle.categoryAxis.labels.fontName = Varela
    ConsoAnnuelle.categoryAxis.labels.angle = 90
    ConsoAnnuelle.categoryAxis.labels.dx = -2 * mm
    ConsoAnnuelle.categoryAxis.labels.dy = -10.5 * mm

    ConsoAnnuelle.valueAxis.labels.fontName = Varela
    ConsoAnnuelle.valueAxis.visibleGrid = True
    ConsoAnnuelle.valueAxis.labelTextFormat = '%d kWh'

    ConsoAnnuelle.bars[0].fillColor = Palette[2]
    ConsoAnnuelle.bars[0].strokeColor = Palette[2]
    ConsoAnnuelle.barLabels.boxStrokeColor = Palette[2]

    d3.add(ConsoAnnuelle)
    d3.wrapOn(pdf, 200 * mm, 0 * mm)
    d3.drawOn(pdf, 34 * mm, 38 * mm)

    pdf.drawCentredString(105 * mm, 225 * mm, "Consommation quotidienne")
    pdf.drawCentredString(105 * mm, 157 * mm, "Consommation hebdomadaire")
    pdf.drawCentredString(105 * mm, 85 * mm, "Consommation annuelle")

    pdf.showPage()







#Création du fichier
pdf = canvas.Canvas(filename)

#Appelle de la fonction qui créé la page de garde
coverPage(pdf, imageFond, imageLogoFairwind, imageCirculaire, imageClient, InfoFairwind, CoordonnesFairwind) #Permet de débugger la position des objets

#Permet d'écrire la lettre d'en tête
LettreEnTete(pdf, date, header_image_portrait)

#Affiche le résumé de l'étude
InfosClientEtResume(pdf, header_image_portrait, dictClient, dictResumeFinancier, val_Autoconso, val_AutonomieEnerget)

#Affiche la page d'implantaion de l'installation
Implantation(pdf, vueAerienne, header_image_landscape,symboleEolienne, symbolePVtoiture, symbolePVcarport, symbolebornes, symbolestockage)

#Page concernant l'analyse de vent
AnalyseVent(pdf, header_image_portrait, VentMyWindTurbine, dictVent, WindProfileEquation)


#Page concernant l'analyse de l'ensoleillement
AnalyseSoleil(pdf, header_image_portrait, InclinaisonOrientation, dictPlacementPanneaux)

#Page conernant la consommation du client
ConsommationActuelle(pdf, header_image_portrait, dictConsommationActuelle, dictConsommationAdditionnelle)


#Permet de débugger la position des objets
drawMyRulerPortrait(pdf)
#drawMyRulerPaysage(pdf)


#Import de la police Varela Round
Varela = "Varela"
pdfmetrics.registerFont(
    TTFont(Varela, 'VarelaRound-Regular.ttf')
)
pdf.setFont(Varela, 12)




pdf.save()