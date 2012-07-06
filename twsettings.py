# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

def restorePlacement(widget, regkey, pos=QPoint(200, 200), size=QSize(450, 450)):
    settings = createSettings()
    pos = settings.value("{0}/pos".format(regkey), pos).toPoint()
    size = settings.value("{0}/size".format(regkey), size).toSize()
    widget.resize(size)
    widget.move(pos)

def savePlacement(widget, regkey):
    settings = createSettings()
    settings.setValue("{0}/pos".format(regkey), widget.pos())
    settings.setValue("{0}/size".format(regkey), widget.size())

def createSettings():
    return QSettings("prefab", "twclient")
