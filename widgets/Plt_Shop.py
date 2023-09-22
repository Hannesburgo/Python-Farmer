import wx
import wx.xrc
import wx.aui

class Plt_Shop ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 249,171 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.plt_buy = wx.Button( self, wx.ID_ANY, u"Buy", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.plt_buy, wx.aui.AuiPaneInfo() .Bottom() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 90,60 ) ).Floatable( False ).Position( 150 ).Layer( 1 ) )

		self.plt_qnty = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 99, 0 )
		self.m_mgr.AddPane( self.plt_qnty, wx.aui.AuiPaneInfo() .Bottom() .CaptionVisible( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 42,62 ) ).Layer( 1 ) )

		plt_choicerChoices = [ u"Barley", u"Wheat", u"Hops" ]
		self.plt_choicer = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, plt_choicerChoices, 0 )
		self.plt_choicer.SetSelection( 0 )
		self.m_mgr.AddPane( self.plt_choicer, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).Dock().Resizable().FloatingSize( wx.Size( 124,62 ) ).Layer( 1 ) )


		self.m_mgr.Update()
		self.Centre( wx.BOTH )

	def __del__( self ):
		self.m_mgr.UnInit()
