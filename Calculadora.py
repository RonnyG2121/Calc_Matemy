


import wx
import wx.adv
import math


class Calculadora(wx.Frame):
    def __init__(self, *args, **kw):
        super(Calculadora, self).__init__(*args, **kw)
        self.SetTitle("calculadora Max")
        self.SetSize((450, 350))
        self.Centre()
        self.Show(True)

        self.barramenu = wx.MenuBar()
        self.archivomenu = wx.Menu()
        self.salir = wx.MenuItem(self.archivomenu, wx.ID_EXIT, "&Salir\tCtrl+s")
        self.acercaD = wx.MenuItem(self.archivomenu, wx.ID_ABOUT, "&Acerca de la aplicación\tCtrl+D")
        self.Bind(wx.EVT_MENU, self.OnAcercaD, self.acercaD)
        self.Bind(wx.EVT_MENU, self.OnSalir, self.salir)
        self.archivomenu.Append(self.acercaD)
        self.archivomenu.Append(self.salir)
        self.barramenu.Append(self.archivomenu, "&Barra De Menú")
        self.SetMenuBar(self.barramenu)
        self.caja = wx.BoxSizer(wx.HORIZONTAL)
        self.panel = wx.Panel(self, -1)
        self.label_ingresar1 = wx.StaticText(self.panel, wx.ID_ANY, "Ingrese el primer Número")
        self.ingresar1 = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        self.ingresar1.SetFocus()
        self.label_operaciones = wx.StaticText(self.panel, wx.ID_ANY, "Elija la operación a realizar:")
        self.listaOperaciones = ["Suma", "Resta", "Multiplicación", "División", "Potencia"]
        self.choice = wx.ListBox(self.panel, wx.ID_ANY, choices = self.listaOperaciones)
        self.choice.SetSelection(0)
        self.label_ingresar2 = wx.StaticText(self.panel, wx.ID_ANY, "Ingrese segundo número")
        self.ingresar2 = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        self.boton_calculador = wx.Button(self.panel, wx.ID_ANY, "&Calcular")
        self.boton_calculador.Bind(wx.EVT_BUTTON, self.OnCalcular)
        self.btn_eliminar = wx.Button(self.panel, wx.ID_ANY, "&Borrar Todo\tCtrl+b")
        self.btn_eliminar.Bind(wx.EVT_BUTTON, self.OnBorrarTodo)
        self.label_resultado = wx.StaticText(self.panel, wx.ID_ANY, "&Resultado")
        self.resultado = wx.TextCtrl(self.panel, wx.ID_ANY, "0.0", style = wx.TE_READONLY)
        self.caja.Add(self.label_ingresar1, 0, wx.ALL, 5)
        self.caja.Add(self.ingresar1, wx.ALL, 5)
        self.caja.Add(self.label_operaciones, wx.ALL, 5)
        self.caja.Add(self.choice, wx.ALL, 5)
        self.caja.Add(self.label_ingresar2, wx.ALL, 5)
        self.caja.Add(self.ingresar2, wx.ALL, 5)
        self.caja.Add(self.boton_calculador, wx.ALL, 5)
        self.caja.Add(self.btn_eliminar, wx.ALL, 5)
        self.caja.Add(self.label_resultado, wx.ALL, 5)
        self.caja.Add(self.resultado, wx.ALL, 5)
        self.panel.SetSizer(self.caja)
        self.panel.Layout()
        self.panel.Fit()
    def OnCalcular(self, event):
        operacion = self.choice.GetString(self.choice.GetSelection())
        if operacion == "Suma":
            resultado = float(self.ingresar1.GetValue()) + float(self.ingresar2.GetValue())
            self.resultado.SetValue(str(resultado))
            self.resultado.SetFocus()
        elif operacion == "Resta":
            resultado = float(self.ingresar1.GetValue()) - float(self.ingresar2.GetValue())
            self.resultado.SetValue(str(resultado))
            self.resultado.SetFocus()
        elif operacion == "Multiplicación":
            resultado = float(self.ingresar1.GetValue()) * float(self.ingresar2.GetValue())
            self.resultado.SetValue(str(resultado))
            self.resultado.SetFocus()
        elif operacion == "División":
            resultado = float(self.ingresar1.GetValue()) / float(self.ingresar2.GetValue())
            self.resultado.SetValue(str(resultado))
            self.resultado.SetFocus()
        if operacion == "Potencia":
            resultado =  math.pow(self.ingresar1.GetValue(), self.ingresar2.GetValue())
            self.resultado.SetValue(str(resultado))
            self.resultado.SetFocus()

    def OnBorrarTodo(self, evento):
        self.ingresar1.SetValue("")
        self.ingresar2.SetValue("")
        self.resultado.SetValue("")
        self.choice.SetSelection(0)
        self.ingresar1.SetFocus()
    def OnSalir(self, evento):
        self.Close(True)
    def OnAcercaD(self, evt):
        self.descripcion = """Esta es una calculadora accesible como su nombre así lo indica. cuenta con todas las operaciones básicas y avanzadas de la matemática."""
        self.lisencia = """Esta aplicación es completamente gratuita."""
        self.informacion = wx.adv.AboutDialogInfo()
        self.informacion.SetName("Calculadora Max Accesible")
        self.informacion.SetVersion("1.0.0")
        self.informacion.SetDescription(self.descripcion)
        self.informacion.SetLicence(self.lisencia)
        self.informacion.AddDeveloper("Ronny González y Johan G")
        wx.adv.AboutBox(self.informacion)



if __name__ == "__main__":
    app = wx.App()
    Calculadora(None)
    app.MainLoop()