#!/usr/env python
#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: ErrorDialogs.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxWindows' modules
from wxPython.wx import *

# Custom source
from wxPython.lib.PythonBitmaps import *

# Window functions

wxPyError_ID_TEXT1 = 10000
wxPyError_ID_PROGRAMNAME = 10001
wxPyError_ID_TEXT2 = 10002
wxPyError_ID_VERSIONNUMBER = 10003
wxPyError_ID_STATICBITMAP1 = 10004
wxPyError_ID_STATICBITMAP2 = 10005
wxPyError_ID_TEXT3 = 10006
wxPyError_ID_TEXT4 = 10007
wxPyError_ID_TEXTCTRL = 10008
wxPyError_ID_TEXT5 = 10009
wxPyError_ID_CONTINUE = 10010
wxPyError_ID_MAIL = 10011
wxPyError_ID_TEXT6 = 10012
wxPyError_ID_ADDRESS = 10013
wxPyError_ID_EXIT = 10014
wxPyError_ID_TEXT7 = 10015
wxPyError_ID_TEXT8 = 10016
wxPyError_ID_TEXT9 = 10017
wxPyError_ID_TEXT10 = 10018
wxPyError_ID_TEXT11 = 10019
wxPyError_ID_TEXT12 = 10020

def populate_wxNonFatalErrorDialogWithTraceback( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxBoxSizer( wxHORIZONTAL )
    
    item3 = wxStaticBox( parent, -1, "Non-fatal" )
    item3.SetFont( wxFont( 9, wxSWISS, wxNORMAL, wxBOLD ) )
    item2 = wxStaticBoxSizer( item3, wxVERTICAL )
    
    item4 = wxBoxSizer( wxHORIZONTAL )
    
    item5 = wxStaticText( parent, wxPyError_ID_TEXT1, "Error in ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item5.SetForegroundColour( wxWHITE )
    item5.SetBackgroundColour( wxRED )
    item5.SetFont( wxFont( 21, wxSCRIPT, wxNORMAL, wxBOLD ) )
    item4.AddWindow( item5, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticText( parent, wxPyError_ID_PROGRAMNAME, "name", wxDefaultPosition, wxDefaultSize, 0 )
    item6.SetFont( wxFont( 21, wxROMAN, wxITALIC, wxNORMAL ) )
    item4.AddWindow( item6, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item4, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxBoxSizer( wxHORIZONTAL )
    
    item8 = wxStaticText( parent, wxPyError_ID_TEXT2, "Version ", wxDefaultPosition, wxDefaultSize, 0 )
    item8.SetFont( wxFont( 9, wxROMAN, wxNORMAL, wxNORMAL ) )
    item7.AddWindow( item8, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item9 = wxStaticText( parent, wxPyError_ID_VERSIONNUMBER, "?.?", wxDefaultPosition, wxDefaultSize, 0 )
    item9.SetFont( wxFont( 12, wxROMAN, wxNORMAL, wxBOLD ) )
    item7.AddWindow( item9, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item7, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item1.AddSizer( item2, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP1, PythonBitmaps( 0 ), wxDefaultPosition, wxDefaultSize )
    item1.AddWindow( item10, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP2, PythonBitmaps( 1 ), wxDefaultPosition, wxDefaultSize )
    item1.AddWindow( item11, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item12 = wxStaticText( parent, wxPyError_ID_TEXT3, "The Python interpreter has encountered a so-called \"un-caught exception\".", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item12, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item14 = wxStaticBox( parent, -1, "Traceback" )
    item14.SetFont( wxFont( 6, wxSWISS, wxITALIC, wxNORMAL ) )
    parent.sizerAroundText = item13 = wxStaticBoxSizer( item14, wxVERTICAL )
    
    item15 = wxStaticText( parent, wxPyError_ID_TEXT4, 
        "Please don't worry if this doesn't mean anything to you.\n"
        "It will be included in the \"bug report\" mentioned below.",
        wxDefaultPosition, wxDefaultSize, 0 )
    item15.SetFont( wxFont( 8, wxROMAN, wxNORMAL, wxNORMAL ) )
    item13.AddWindow( item15, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item16 = wxTextCtrl( parent, wxPyError_ID_TEXTCTRL, "Traceback is to go here", wxDefaultPosition, wxDefaultSize, wxTE_READONLY|wxTE_MULTILINE )
    item16.SetFont( wxFont( 9, wxSWISS, wxNORMAL, wxNORMAL ) )
    item16.SetToolTip( wxToolTip("A \"traceback\" reports the nature and location of a Python error.") )
    item13.AddWindow( item16, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item13, 1, wxALIGN_CENTRE|wxALL, 5 )

    item17 = wxStaticText( parent, wxPyError_ID_TEXT5, "Please select one of the options below.", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item17.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item0.AddWindow( item17, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item18 = wxFlexGridSizer( 3, 0, 0, 6 )
    item18.AddGrowableCol( 0 )
    item18.AddGrowableCol( 1 )
    item18.AddGrowableCol( 2 )
    
    item19 = wxButton( parent, wxPyError_ID_CONTINUE, "Continue", wxDefaultPosition, wxDefaultSize, 0 )
    item19.SetDefault()
    item18.AddWindow( item19, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item20 = wxBoxSizer( wxHORIZONTAL )
    
    item21 = wxButton( parent, wxPyError_ID_MAIL, "E-mail support", wxDefaultPosition, wxDefaultSize, 0 )
    item20.AddWindow( item21, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item22 = wxBoxSizer( wxVERTICAL )
    
    item23 = wxStaticText( parent, wxPyError_ID_TEXT6, "Your e-mail address:", wxDefaultPosition, wxDefaultSize, 0 )
    item23.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item22.AddWindow( item23, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item24 = wxTextCtrl( parent, wxPyError_ID_ADDRESS, "", wxDefaultPosition, wxSize(80,-1), 0 )
    item22.AddWindow( item24, 2, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item20.AddSizer( item22, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item18.AddSizer( item20, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item25 = wxButton( parent, wxPyError_ID_EXIT, "Exit immediately", wxDefaultPosition, wxDefaultSize, 0 )
    item18.AddWindow( item25, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item26 = wxStaticText( parent, wxPyError_ID_TEXT7, "Attempt to continue.", wxDefaultPosition, wxDefaultSize, 0 )
    item18.AddWindow( item26, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item27 = wxStaticText( parent, wxPyError_ID_TEXT8, "E-mail a \"bug report\" (if this is indeed a bug!).", wxDefaultPosition, wxDefaultSize, 0 )
    item18.AddWindow( item27, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item28 = wxStaticText( parent, wxPyError_ID_TEXT9, "Attempt to exit immediately.", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item18.AddWindow( item28, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE, 5 )

    item29 = wxStaticText( parent, wxPyError_ID_TEXT10, "", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item29.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item18.AddWindow( item29, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item30 = wxStaticText( parent, wxPyError_ID_TEXT11, "(Please read any accompanying documentation first!)", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item30.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item18.AddWindow( item30, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item31 = wxStaticText( parent, wxPyError_ID_TEXT12, "(Please note that no attempt to save unsaved data will be made.)", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item31.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item18.AddWindow( item31, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item18, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

wxPyError_ID_EXCEPTIONNAME = 10022
wxPyError_ID_EXTRAINFORMATION = 10023
wxPyError_ID_TEXT13 = 10024
wxPyError_ID_TEXT14 = 10025

def populate_wxNonFatalErrorDialog( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxBoxSizer( wxHORIZONTAL )
    
    item2 = wxBoxSizer( wxHORIZONTAL )
    
    item4 = wxStaticBox( parent, -1, "Non-fatal" )
    item4.SetFont( wxFont( 9, wxSWISS, wxNORMAL, wxBOLD ) )
    item3 = wxStaticBoxSizer( item4, wxVERTICAL )
    
    item5 = wxBoxSizer( wxHORIZONTAL )
    
    item6 = wxStaticText( parent, wxPyError_ID_TEXT1, "Error in ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item6.SetForegroundColour( wxWHITE )
    item6.SetBackgroundColour( wxRED )
    item6.SetFont( wxFont( 21, wxSCRIPT, wxNORMAL, wxBOLD ) )
    item5.AddWindow( item6, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxStaticText( parent, wxPyError_ID_PROGRAMNAME, "name", wxDefaultPosition, wxDefaultSize, 0 )
    item7.SetFont( wxFont( 21, wxROMAN, wxITALIC, wxNORMAL ) )
    item5.AddWindow( item7, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item3.AddSizer( item5, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item8 = wxBoxSizer( wxHORIZONTAL )
    
    item9 = wxStaticText( parent, wxPyError_ID_TEXT2, "Version ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item9.SetFont( wxFont( 9, wxROMAN, wxNORMAL, wxNORMAL ) )
    item8.AddWindow( item9, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxStaticText( parent, wxPyError_ID_VERSIONNUMBER, "?.?", wxDefaultPosition, wxDefaultSize, 0 )
    item10.SetFont( wxFont( 12, wxROMAN, wxNORMAL, wxBOLD ) )
    item8.AddWindow( item10, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item3.AddSizer( item8, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item3, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP1, PythonBitmaps( 0 ), wxDefaultPosition, wxDefaultSize )
    item2.AddWindow( item11, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item12 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP2, PythonBitmaps( 1 ), wxDefaultPosition, wxDefaultSize )
    item2.AddWindow( item12, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item1.AddSizer( item2, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 1, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item13 = wxStaticText( parent, wxPyError_ID_TEXT3, "The Python interpreter has encountered a so-called \"un-caught exception\".", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item13, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item15 = wxStaticBox( parent, -1, "Exception information" )
    item15.SetFont( wxFont( 6, wxSWISS, wxITALIC, wxNORMAL ) )
    item14 = wxStaticBoxSizer( item15, wxVERTICAL )
    
    item16 = wxStaticText( parent, wxPyError_ID_TEXT4, 
        "Please don't worry if this doesn't mean anything to you.\n"
        "It will be included in the \"bug report\" mentioned below, along with a \"stack traceback\".",
        wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item16.SetFont( wxFont( 8, wxROMAN, wxNORMAL, wxNORMAL ) )
    item14.AddWindow( item16, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item17 = wxFlexGridSizer( 2, 0, 1, 1 )
    item17.AddGrowableCol( 1 )
    
    item18 = wxStaticText( parent, wxPyError_ID_TEXT5, "Name:", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item18.SetFont( wxFont( 10, wxROMAN, wxITALIC, wxNORMAL ) )
    item18.SetToolTip( wxToolTip("This gives the type of the error.") )
    item17.AddWindow( item18, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item19 = wxStaticText( parent, wxPyError_ID_EXCEPTIONNAME, "text", wxDefaultPosition, wxDefaultSize, 0 )
    item17.AddWindow( item19, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item20 = wxStaticText( parent, wxPyError_ID_TEXT6, 
        "Extra\n"
        "information:",
        wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item20.SetFont( wxFont( 10, wxROMAN, wxITALIC, wxNORMAL ) )
    item17.AddWindow( item20, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item21 = wxStaticText( parent, wxPyError_ID_EXTRAINFORMATION, "text", wxDefaultPosition, wxDefaultSize, 0 )
    item17.AddWindow( item21, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item14.AddSizer( item17, 1, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item14, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 10 )

    item22 = wxStaticText( parent, wxPyError_ID_TEXT7, "Please select one of the options below.", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item22.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item0.AddWindow( item22, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item23 = wxFlexGridSizer( 3, 0, 0, 6 )
    item23.AddGrowableCol( 0 )
    item23.AddGrowableCol( 1 )
    item23.AddGrowableCol( 2 )
    
    item24 = wxButton( parent, wxPyError_ID_CONTINUE, "Continue", wxDefaultPosition, wxDefaultSize, 0 )
    item24.SetDefault()
    item23.AddWindow( item24, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item25 = wxBoxSizer( wxHORIZONTAL )
    
    item26 = wxButton( parent, wxPyError_ID_MAIL, "E-mail support", wxDefaultPosition, wxDefaultSize, 0 )
    item25.AddWindow( item26, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item27 = wxBoxSizer( wxVERTICAL )
    
    item28 = wxStaticText( parent, wxPyError_ID_TEXT8, "Your e-mail address:", wxDefaultPosition, wxDefaultSize, 0 )
    item28.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item27.AddWindow( item28, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item29 = wxTextCtrl( parent, wxPyError_ID_ADDRESS, "", wxDefaultPosition, wxSize(80,-1), 0 )
    item27.AddWindow( item29, 2, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item25.AddSizer( item27, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item23.AddSizer( item25, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item30 = wxButton( parent, wxPyError_ID_EXIT, "Exit immediately", wxDefaultPosition, wxDefaultSize, 0 )
    item23.AddWindow( item30, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item31 = wxStaticText( parent, wxPyError_ID_TEXT9, "Attempt to continue.", wxDefaultPosition, wxDefaultSize, 0 )
    item23.AddWindow( item31, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item32 = wxStaticText( parent, wxPyError_ID_TEXT10, "E-mail a \"bug report\" (if this is indeed a bug!).", wxDefaultPosition, wxDefaultSize, 0 )
    item23.AddWindow( item32, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item33 = wxStaticText( parent, wxPyError_ID_TEXT11, "Attempt to exit immediately.", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item23.AddWindow( item33, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE, 5 )

    item34 = wxStaticText( parent, wxPyError_ID_TEXT12, "", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item34.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item23.AddWindow( item34, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item35 = wxStaticText( parent, wxPyError_ID_TEXT13, "(Please read any accompanying documentation first!)", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item35.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item23.AddWindow( item35, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item36 = wxStaticText( parent, wxPyError_ID_TEXT14, "(Please note that no attempt to save unsaved data will be made.)", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item36.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item23.AddWindow( item36, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item23, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0


def populate_wxFatalErrorDialogWithTraceback( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxBoxSizer( wxHORIZONTAL )
    
    item3 = wxStaticBox( parent, -1, "Fatal" )
    item3.SetFont( wxFont( 9, wxSWISS, wxNORMAL, wxBOLD ) )
    item2 = wxStaticBoxSizer( item3, wxVERTICAL )
    
    item4 = wxBoxSizer( wxHORIZONTAL )
    
    item5 = wxStaticText( parent, wxPyError_ID_TEXT1, "Error in ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item5.SetForegroundColour( wxWHITE )
    item5.SetBackgroundColour( wxRED )
    item5.SetFont( wxFont( 21, wxSCRIPT, wxNORMAL, wxBOLD ) )
    item4.AddWindow( item5, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticText( parent, wxPyError_ID_PROGRAMNAME, "Program-name", wxDefaultPosition, wxDefaultSize, 0 )
    item6.SetFont( wxFont( 21, wxROMAN, wxITALIC, wxNORMAL ) )
    item4.AddWindow( item6, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item4, 1, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item7 = wxBoxSizer( wxHORIZONTAL )
    
    item8 = wxStaticText( parent, wxPyError_ID_TEXT2, "Version ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item8.SetFont( wxFont( 9, wxROMAN, wxNORMAL, wxNORMAL ) )
    item7.AddWindow( item8, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item9 = wxStaticText( parent, wxPyError_ID_VERSIONNUMBER, "?.?", wxDefaultPosition, wxDefaultSize, 0 )
    item9.SetFont( wxFont( 12, wxROMAN, wxNORMAL, wxBOLD ) )
    item7.AddWindow( item9, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item7, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item1.AddSizer( item2, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP1, PythonBitmaps( 0 ), wxDefaultPosition, wxDefaultSize )
    item1.AddWindow( item10, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP2, PythonBitmaps( 1 ), wxDefaultPosition, wxDefaultSize )
    item1.AddWindow( item11, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 1, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item12 = wxStaticText( parent, wxPyError_ID_TEXT3, "The Python interpreter has encountered a so-called \"un-caught exception\".", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item12, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item14 = wxStaticBox( parent, -1, "Traceback" )
    item14.SetFont( wxFont( 6, wxSWISS, wxITALIC, wxNORMAL ) )
    parent.sizerAroundText = item13 = wxStaticBoxSizer( item14, wxVERTICAL )
    
    item15 = wxStaticText( parent, wxPyError_ID_TEXT4, 
        "Please don't worry if this doesn't mean anything to you.\n"
        "It will be included in the \"bug report\" mentioned below.",
        wxDefaultPosition, wxDefaultSize, 0 )
    item15.SetFont( wxFont( 8, wxROMAN, wxNORMAL, wxNORMAL ) )
    item13.AddWindow( item15, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item16 = wxTextCtrl( parent, wxPyError_ID_TEXTCTRL, "Traceback is to go here", wxDefaultPosition, wxDefaultSize, wxTE_READONLY|wxTE_MULTILINE )
    item16.SetFont( wxFont( 9, wxSWISS, wxNORMAL, wxNORMAL ) )
    item16.SetToolTip( wxToolTip("A \"traceback\" reports the nature and location of a Python error.") )
    item13.AddWindow( item16, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item13, 0, wxALIGN_CENTRE|wxALL, 5 )

    item17 = wxStaticText( parent, wxPyError_ID_TEXT5, "Please select one of the options below.", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item17.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item0.AddWindow( item17, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item18 = wxFlexGridSizer( 3, 0, 0, 6 )
    item18.AddGrowableCol( 0 )
    item18.AddGrowableCol( 1 )
    item18.AddGrowableCol( 2 )
    
    item19 = wxBoxSizer( wxHORIZONTAL )
    
    item20 = wxButton( parent, wxPyError_ID_MAIL, "E-mail support", wxDefaultPosition, wxDefaultSize, 0 )
    item19.AddWindow( item20, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item21 = wxBoxSizer( wxVERTICAL )
    
    item22 = wxStaticText( parent, wxPyError_ID_TEXT6, "Your e-mail address:", wxDefaultPosition, wxDefaultSize, 0 )
    item22.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item21.AddWindow( item22, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item23 = wxTextCtrl( parent, wxPyError_ID_ADDRESS, "", wxDefaultPosition, wxSize(80,-1), 0 )
    item21.AddWindow( item23, 2, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item19.AddSizer( item21, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item18.AddSizer( item19, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item24 = wxButton( parent, wxPyError_ID_EXIT, "Exit immediately", wxDefaultPosition, wxDefaultSize, 0 )
    item24.SetDefault()
    item18.AddWindow( item24, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item25 = wxStaticText( parent, wxPyError_ID_TEXT7, "E-mail a \"bug report\" (if this is indeed a bug!).", wxDefaultPosition, wxDefaultSize, 0 )
    item18.AddWindow( item25, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item26 = wxStaticText( parent, wxPyError_ID_TEXT8, "Attempt to exit immediately.", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item18.AddWindow( item26, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE, 5 )

    item27 = wxStaticText( parent, wxPyError_ID_TEXT9, "(Please read any accompanying documentation first!)", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item27.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item18.AddWindow( item27, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item28 = wxStaticText( parent, wxPyError_ID_TEXT10, "(Please note that no attempt to save unsaved data will be made.)", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item28.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item18.AddWindow( item28, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item18, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0


def populate_wxFatalErrorDialog( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxBoxSizer( wxHORIZONTAL )
    
    item3 = wxStaticBox( parent, -1, "Fatal" )
    item3.SetFont( wxFont( 9, wxSWISS, wxNORMAL, wxBOLD ) )
    item2 = wxStaticBoxSizer( item3, wxVERTICAL )
    
    item4 = wxBoxSizer( wxHORIZONTAL )
    
    item5 = wxStaticText( parent, wxPyError_ID_TEXT1, "Error in ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item5.SetForegroundColour( wxWHITE )
    item5.SetBackgroundColour( wxRED )
    item5.SetFont( wxFont( 21, wxSCRIPT, wxNORMAL, wxBOLD ) )
    item4.AddWindow( item5, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item6 = wxStaticText( parent, wxPyError_ID_PROGRAMNAME, "Program-name", wxDefaultPosition, wxDefaultSize, 0 )
    item6.SetFont( wxFont( 21, wxROMAN, wxITALIC, wxNORMAL ) )
    item4.AddWindow( item6, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item4, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxBoxSizer( wxHORIZONTAL )
    
    item8 = wxStaticText( parent, wxPyError_ID_TEXT2, "Version ", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item8.SetFont( wxFont( 9, wxROMAN, wxNORMAL, wxNORMAL ) )
    item7.AddWindow( item8, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item9 = wxStaticText( parent, wxPyError_ID_VERSIONNUMBER, "?.?", wxDefaultPosition, wxDefaultSize, 0 )
    item9.SetFont( wxFont( 12, wxROMAN, wxNORMAL, wxBOLD ) )
    item7.AddWindow( item9, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item2.AddSizer( item7, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item1.AddSizer( item2, 1, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item10 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP1, PythonBitmaps( 0 ), wxDefaultPosition, wxDefaultSize )
    item1.AddWindow( item10, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxStaticBitmap( parent, wxPyError_ID_STATICBITMAP2, PythonBitmaps( 1 ), wxDefaultPosition, wxDefaultSize )
    item1.AddWindow( item11, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item1, 1, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item12 = wxStaticText( parent, wxPyError_ID_TEXT3, "The Python interpreter has encountered a so-called \"un-caught exception\".", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item12, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item14 = wxStaticBox( parent, -1, "Exception information" )
    item14.SetFont( wxFont( 6, wxSWISS, wxITALIC, wxNORMAL ) )
    item13 = wxStaticBoxSizer( item14, wxVERTICAL )
    
    item15 = wxStaticText( parent, wxPyError_ID_TEXT4, 
        "Please don't worry if this doesn't mean anything to you.\n"
        "It will be included in the \"bug report\" mentioned below, along with a \"stack traceback\".",
        wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item15.SetFont( wxFont( 8, wxROMAN, wxNORMAL, wxNORMAL ) )
    item13.AddWindow( item15, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item16 = wxFlexGridSizer( 2, 0, 1, 1 )
    item16.AddGrowableCol( 1 )
    
    item17 = wxStaticText( parent, wxPyError_ID_TEXT5, "Name:", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item17.SetFont( wxFont( 10, wxROMAN, wxITALIC, wxNORMAL ) )
    item17.SetToolTip( wxToolTip("This gives the type of the error.") )
    item16.AddWindow( item17, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item18 = wxStaticText( parent, wxPyError_ID_EXCEPTIONNAME, "text", wxDefaultPosition, wxDefaultSize, 0 )
    item16.AddWindow( item18, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item19 = wxStaticText( parent, wxPyError_ID_TEXT6, 
        "Extra\n"
        "information:",
        wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item19.SetFont( wxFont( 10, wxROMAN, wxITALIC, wxNORMAL ) )
    item16.AddWindow( item19, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item20 = wxStaticText( parent, wxPyError_ID_EXTRAINFORMATION, "text", wxDefaultPosition, wxDefaultSize, 0 )
    item16.AddWindow( item20, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item13.AddSizer( item16, 0, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item13, 1, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 10 )

    item21 = wxStaticText( parent, wxPyError_ID_TEXT7, "Please select one of the options below.", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item21.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item0.AddWindow( item21, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item22 = wxFlexGridSizer( 3, 0, 0, 6 )
    item22.AddGrowableCol( 0 )
    item22.AddGrowableCol( 1 )
    item22.AddGrowableCol( 2 )
    
    item23 = wxBoxSizer( wxHORIZONTAL )
    
    item24 = wxButton( parent, wxPyError_ID_MAIL, "E-mail support", wxDefaultPosition, wxDefaultSize, 0 )
    item23.AddWindow( item24, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item25 = wxBoxSizer( wxVERTICAL )
    
    item26 = wxStaticText( parent, wxPyError_ID_TEXT8, "Your e-mail address:", wxDefaultPosition, wxDefaultSize, 0 )
    item26.SetFont( wxFont( 8, wxROMAN, wxITALIC, wxNORMAL ) )
    item25.AddWindow( item26, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item27 = wxTextCtrl( parent, wxPyError_ID_ADDRESS, "", wxDefaultPosition, wxSize(80,-1), 0 )
    item25.AddWindow( item27, 2, wxADJUST_MINSIZE|wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item23.AddSizer( item25, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item22.AddSizer( item23, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item28 = wxButton( parent, wxPyError_ID_EXIT, "Exit immediately", wxDefaultPosition, wxDefaultSize, 0 )
    item28.SetDefault()
    item22.AddWindow( item28, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item29 = wxStaticText( parent, wxPyError_ID_TEXT9, "E-mail a \"bug report\" (if this is indeed a bug!).", wxDefaultPosition, wxDefaultSize, 0 )
    item22.AddWindow( item29, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item30 = wxStaticText( parent, wxPyError_ID_TEXT10, "Attempt to exit immediately.", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item22.AddWindow( item30, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE, 5 )

    item31 = wxStaticText( parent, wxPyError_ID_TEXT11, "(Please read any accompanying documentation first!)", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE )
    item31.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item22.AddWindow( item31, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item32 = wxStaticText( parent, wxPyError_ID_TEXT12, "(Please note that no attempt to save unsaved data will be made.)", wxDefaultPosition, wxDefaultSize, wxALIGN_RIGHT )
    item32.SetFont( wxFont( 7, wxROMAN, wxNORMAL, wxBOLD ) )
    item22.AddWindow( item32, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item22, 0, wxADJUST_MINSIZE|wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

# End of generated file
