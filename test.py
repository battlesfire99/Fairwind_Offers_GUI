from reportlab.graphics.shapes import Drawing,colors
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.lineplots import LinePlot, YValueAxis
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

drawing = Drawing(400, 200)
data = [(13, 5, 20, 22, 37, 45, 19, 4)
        ]
noOfBars=len(data[0])

bc = VerticalBarChart()
bc.x = 50
bc.y = 50
bc.height = 125
bc.width = 300
bc.data = data

bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 50
bc.categoryAxis.categoryNames = ['Jan-99','Feb-99','Mar-99','Apr-99','May-99','Jun-99','Jul-99','Aug-99']
drawing.add(bc)

data3=[[(0.5, 4), (1.5, 3), (2.5, 4), (3.5, 6), (4.5, 4), (5.5, 2), (6.5, 5), (7.5, 6)]
       ]

lp = LinePlot()
lp.x = bc.x
lp.y = bc.y
lp.height = bc.height
lp.width = bc.width
lp.data = data3
lp.joinedLines = 1
lp.lines[0].symbol = makeMarker('Circle')
lp.lines[0].strokeColor=colors.blue
lp.lineLabelFormat = '%2.0f'
lp.xValueAxis.valueMin = 0
lp.xValueAxis.valueMax = noOfBars
lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 8
lp.xValueAxis.visible=False
lp.yValueAxis.visible=False #Hide 2nd plot its Yaxis
drawing.add(lp)

y2Axis = YValueAxis()#Replicate 2nd plot Yaxis in the right
y2Axis.setProperties(lp.yValueAxis.getProperties())
y2Axis.setPosition(lp.x+lp.width,lp.y,lp.height)
y2Axis.tickRight=5
y2Axis.tickLeft=0

y2Axis.configure(data3)
y2Axis.visible=True
drawing.add(y2Axis)

pdf = canvas.Canvas("DualAxisGraph.pdf")

drawing.drawOn(pdf, 50* mm, 50 *mm)
pdf.save()