# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

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

	def __del__( self ):
		self.m_mgr.UnInit()



###########################################################################
## Class Lot
###########################################################################

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

	def __del__( self ):
		self.m_mgr.UnInit()



###########################################################################
## Class plt_shop
###########################################################################

class plt_shop ( wx.Frame ):

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



