import wx
import wx.xrc
import wx.aui

from plt import Plt

class Lot ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 100,100 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.lot_progress = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL )
		self.lot_progress.SetValue( 0 )
		self.m_mgr.AddPane( self.lot_progress, wx.aui.AuiPaneInfo() .Bottom() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 203,54 ) ).Layer( 3 ) )

		self.lot_button = wx.Button( self, wx.ID_ANY, u"Plant", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.lot_button, wx.aui.AuiPaneInfo() .Bottom() .CaptionVisible( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 91,62 ) ).Layer( 2 ) )

		self.lot_label = wx.StaticText( self, wx.ID_ANY, u"Empty", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.lot_label.Wrap( -1 )

		self.m_mgr.AddPane( self.lot_label, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.Size( 49,60 ) ).Layer( 1 ) )


		self.m_mgr.Update()

		# Custom 
		self.plt = None
		self.Position = (self.Position[0], self.Position[1]+26)
		# Custom End

		# Connect Events
		self.lot_button.Bind( wx.EVT_BUTTON, self.lot_plant )

	def __del__( self ):
		self.m_mgr.UnInit()

	# Virtual event handlers, override them in your derived class
	def lot_plant( self, event ):
		if self.plt == None:
			self.plt = Plt("Barley", 60)
			self.lot_progress.Range = 60
			self.lot_label.Label = "Barley"
		
		if self.lot_progress.Value >= self.lot_progress.Range:
			self.plt = None
			self.lot_progress.Value = 0
			self.lot_label.Label = "Empty"
		
		self.lot_progress.Value += 1