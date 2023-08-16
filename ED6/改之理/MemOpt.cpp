/*******************************************************************
	����	:	�ڴ��޸�����
	�ļ���	: 	MemOpt.cpp
	����ʱ��:	2009-3-17   13:08
	����޸�:	2009-3-17   13:08

	������ʷ:	2009-3-17	�����ļ�
				2009-3-24	��ȡ����
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"
#include <Winuser.h>
#include "MemOpt.h"

enum ID_CONTROL
{
	ID_MEMOPT_STATICBOX = wxID_HIGHEST + 1,
	ID_MEMOPT_GAMEVER,
	ID_MEMOPT_VERFC,
	ID_MEMOPT_VERSC,
	ID_MEMOPT_VER3RD,
	ID_MEMOPT_FCTITLE,
	ID_MEMOPT_SCTITLE,
	ID_MEMOPT_3RDTITLE,
	ID_MEMOPT_WINDOWLIST,
	ID_MEMOPT_BNCHANGETITLE,
	ID_MEMOPT_BNSAVE,
	ID_MEMOPT_BNCHANGEADDR,
};

static wxString strVersions[] =
{
	wxT("FC "),
	wxT("SC "),
	wxT("3rd"),
};

static const wxString strSection = wxT("MemoryOption");

static const wxString strKey[] = 
{
	wxT("FCTitle"),
	wxT("SCTitle"),
	wxT("3rdTitle"),
	wxT("FCFirstHP"),
	wxT("SCFirstHP"),
	wxT("3rdFirstHP"),
};

static const wxString strTipText = wxT("\
�����ڴ��޸�ʱһ�������������ģ��,ֻ��\n\
�޸Ľ������ȷʱ�����ֶ�����.һ����˵ֻ\n\
��Ҫ����������Ϸ����,������һ��HP��ַ��\n\
��.��Ϸ�����Ƽ�ʹ�ñ����򸽴��Ĳ�����.");

MemOpt *MemOpt::This = NULL;

BEGIN_EVENT_TABLE(MemOpt, wxPanel)
	EVT_RADIOBUTTON(ID_MEMOPT_VERFC,		MemOpt::OnRBGameVerFC)
	EVT_RADIOBUTTON(ID_MEMOPT_VERSC,		MemOpt::OnRBGameVerSC)
	EVT_RADIOBUTTON(ID_MEMOPT_VER3RD,		MemOpt::OnRBGameVer3rd)
	EVT_BUTTON(ID_MEMOPT_BNSAVE,			MemOpt::OnBnSaveOption)
	EVT_LISTBOX_DCLICK(ID_MEMOPT_WINDOWLIST,MemOpt::OnLBSelWindow)
	EVT_BUTTON(ID_MEMOPT_BNCHANGETITLE,		MemOpt::OnBnChangeTitle)
END_EVENT_TABLE()

MemOpt::MemOpt(wxNotebook *notebook, long ID, MyFrame *parent) : wxPanel(notebook, ID,
															wxDefaultPosition, wxDefaultSize,
															wxNO_FULL_REPAINT_ON_RESIZE |
															wxCLIP_CHILDREN |
															wxTAB_TRAVERSAL)
{
	wxString temp;
	wxChar szCfgValue[MAX_PATH];
	This = this;
	wxFont TipTextFont(12, wxMODERN, wxNORMAL, wxNORMAL, false, wxT("����"), wxFONTENCODING_SYSTEM);
	wxSizer *HSizer,								// ˮƽSizer
			*VSizer = new wxBoxSizer(wxVERTICAL);	// ��ֱSizer
	m_GSizer = new wxBoxSizer(wxVERTICAL);

	m_StaticBox = new wxStaticBox(this, ID_MEMOPT_STATICBOX, wxT("�ڴ��޸Ļ�������"));
	wxSizer *BoxSizer = new wxStaticBoxSizer(m_StaticBox, wxVERTICAL);

	// select game version
	for (BYTE ix = 0; ix != 3; ++ix)
	{
		if (!ix)
		{
			m_rbGameVer[ix] = new wxRadioButton(this, ID_MEMOPT_VERFC + ix,
				strVersions[ix], wxDefaultPosition, wxDefaultSize, wxRB_GROUP);
		}
		else
		{
			m_rbGameVer[ix] = new wxRadioButton(this, ID_MEMOPT_VERFC + ix,	strVersions[ix]);
		}
		HSizer = new wxBoxSizer(wxHORIZONTAL);
		m_tcGameTitle[ix] = new wxTextCtrl(this, wxID_ANY, wxEmptyString,
			wxDefaultPosition, wxDefaultSize, wxSUNKEN_BORDER);
		m_tcFirstHPAddress[ix] = new wxTextCtrl(this, wxID_ANY, wxEmptyString,
			wxDefaultPosition, wxDefaultSize, wxSUNKEN_BORDER);
		GetPrivateProfileString(strSection, strKey[ix], 
			0, szCfgValue, sizeof(szCfgValue), MyFrame::strCfgFileName);
		m_tcGameTitle[ix]->SetValue(szCfgValue);
		temp.Printf("%X", 
			GetPrivateProfileInt(strSection, strKey[ix + 3], 0, MyFrame::strCfgFileName));
		m_tcFirstHPAddress[ix]->SetValue(temp);
		HSizer->Add(m_rbGameVer[ix], 0, wxRIGHT|wxGROW, 5);
		HSizer->Add(100, 0, 0, wxGROW);
		HSizer->Add(m_tcGameTitle[ix], 1, wxRIGHT|wxGROW, 5);
		HSizer->Add(m_tcFirstHPAddress[ix], 0, wxRIGHT|wxGROW, 5);
		HSizer->Add(80, 0, 0, wxGROW);
		VSizer->Add(HSizer, 0, wxTOP|wxGROW, 10);
		m_rbGameVer[ix]->SetValue(false);
	}
	BoxSizer->Add(VSizer, 0, wxGROW);
	m_bGameVer = GetPrivateProfileInt(wxT("SavePath"), wxT("Default"), 2, MyFrame::strCfgFileName);
	m_rbGameVer[m_bGameVer]->SetValue(true);

	HSizer = new wxBoxSizer(wxHORIZONTAL);

	// buttons
	m_bnChangeTitle = new wxButton(this, ID_MEMOPT_BNCHANGETITLE, wxT("���ı���"));
	m_bnChangeAddress = new wxButton(this, ID_MEMOPT_BNCHANGEADDR, wxT("����ĵ�ַ"));
	m_bnSave = new wxButton(this, ID_MEMOPT_BNSAVE, wxT("����"));

	HSizer->Add(m_bnChangeTitle, 0, wxALIGN_RIGHT|wxRIGHT|wxBOTTOM, 5);
	HSizer->Add(m_bnChangeAddress, 0, wxALIGN_RIGHT|wxRIGHT|wxBOTTOM, 5);
	HSizer->Add(m_bnSave, 0, wxALIGN_RIGHT|wxRIGHT|wxBOTTOM, 5);
	HSizer->Add(30, 0, 0, wxGROW);
	BoxSizer->Add(HSizer, 0, wxALIGN_RIGHT|wxTOP, 10);

	// tip text
	m_tcTipText = new wxStaticText(this, wxID_ANY, strTipText);
	m_tcTipText->SetFont(TipTextFont);
	m_tcTipText->SetForegroundColour(wxColour(206, 120, 166));

	// window list
	wxRect rect = m_StaticBox->GetRect();
	m_lbWindowList = new wxListBox(this, ID_MEMOPT_WINDOWLIST, 
		wxPoint(rect.GetLeft() + 10, rect.GetBottom() + 120), wxSize(250, 180));
	m_lbWindowList->Show(false);

	m_GSizer->Add(BoxSizer, 0, wxGROW|wxALL&~wxBOTTOM, 10);
	m_GSizer->Add(0, 90, 0, wxGROW);
	m_GSizer->Add(m_tcTipText, 0, wxALIGN_RIGHT|wxALL, 30);
	SetSizer(m_GSizer);
}

MemOpt::~MemOpt()
{
	;
}

BOOL CALLBACK MemOpt::EnumWindowsProc(HWND hWnd,LPARAM lParam)
{
	wxChar szWinText[MAX_PATH];
	if (InternalGetWindowText(hWnd, szWinText, sizeof(szWinText)))
	{
		This->m_lbWindowList->Append(szWinText);
		This->m_vhWnd.push_back(hWnd);
	}
	return TRUE;
}

void MemOpt::OnBnChangeTitle(wxCommandEvent &event)
{
	m_lbWindowList->Clear();
	std::vector<HWND>().swap(m_vhWnd);
	EnumWindows(&MemOpt::EnumWindowsProc,0);
	m_lbWindowList->SetFocus();
	m_lbWindowList->Show();
}

void MemOpt::OnLBSelWindow(wxCommandEvent &event)
{
	MyFrame::hWindow = m_vhWnd[event.GetSelection()];
	std::vector<HWND>().swap(m_vhWnd);
	m_lbWindowList->Show(false);
	m_tcGameTitle[m_bGameVer]->SetValue(m_lbWindowList->GetStringSelection());
}

void MemOpt::OnRBGameVerFC(wxCommandEvent &event)
{
	m_bGameVer = 0;
}

void MemOpt::OnRBGameVerSC(wxCommandEvent &event)
{
	m_bGameVer = 1;
}

void MemOpt::OnRBGameVer3rd(wxCommandEvent &event)
{
	m_bGameVer = 2;
}

void MemOpt::OnBnSaveOption(wxCommandEvent &event)
{
	// title
	if (1) for (BYTE ix = 0; ix != 3; ++ix)
	{
		WritePrivateProfileString(strSection, 
			strKey[ix], m_tcGameTitle[ix]->GetValue(), MyFrame::strCfgFileName);
	}

	// first hp address
	for (BYTE ix = 3; ix != 6; ++ix)
	{
		WritePrivateProfileString(strSection, 
			strKey[ix], m_tcFirstHPAddress[ix - 3]->GetValue(), MyFrame::strCfgFileName);
	}
}