import wx
import wx.xrc
import wx.aui

from plt import Plt
from Lot import Lot
from Plt_Shop import Plt_Shop

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.mainFrameHud = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), 0 )
		self.m_mgr.AddPane( self.mainFrameHud, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( -1,-1 ) ) )

		self.m_mgr.Update()
		self.Centre( wx.BOTH )

		# Custom
		self.lots = [Lot(self)]

		self.mainFrameHud.shop_button = wx.Button( self.mainFrameHud, wx.ID_ANY, u"Shop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mainFrameHud.shop_button.Bind( wx.EVT_BUTTON, self.openShop )
		
	def openShop( self, parent ):
		self.shop = Plt_Shop(self)	
	# Custom End

	def __del__( self ):
		self.m_mgr.UnInit()
