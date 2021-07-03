/*******************************************************************
	����	:	�ƻ���ľ
	�ļ���	: 	Package.cpp
	����ʱ��:	2009-3-24   20:49
	����޸�:	2009-3-24   20:49

	������ʷ:	2009-3-24	�����ļ�
				2009-3-25	��ɲ���
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"
#include "Package.h"
#include <wx/wxm>

enum ID_CONTROL
{
	ID_PKG_LISTBOX = wxID_HIGHEST + 1,
	ID_PKG_BNOPENDIR,
	ID_PKG_BNOPENDAT,
	ID_PKG_BNSAVE,
	ID_PKG_BNRESTORE,
	ID_PKG_BNPLAY,
	ID_PKG_BNCLOSEALL,
	ID_PKG_BNEXTRACT,
	ID_PKG_BNADDFILE,
	ID_PKG_BNFIND,
	ID_PKG_STATICBOX,
	ID_PKG_TCSEARCH,
	ID_PKG_COMPRESS,
	ID_PKG_NOENCODE,
	ID_PKG_DECOMPRESS,
	ID_PKG_KEEPNAME,
	ID_PKG_WARNING,
	ID_PKG_README,
};

static const wxString strReadme = wxT(\
"���ϸ�ģ�����ò�ͬ,�ƻ���ľ������\n\
���ڴ�һ��DAT�ļ��е������ݽ�����\n\
��һ��DAT,����CH�ļ����㷨δ֪,��\n\
�Բ��ܵ����Զ�����Դ��ȥ,ֻ�ܴ�ĳ\n\
���ļ��е���ĳ����Դ�滻�����ļ���\n\
�ĵ�ͬ��Դ,����WAV�ļ���DAT28�Ǹ�\n\
����,���Ե�������WAV�ļ�����DAT28\n\
(���������Ŀ����Լ�����.....)�����\n\
���ĳ���ļ���ʲô,�����ø����Ľ��\n\
���⿪��......ʹ�����,���������ú�\n\
��ʿ��½FC/SC......����,FC��DT08.");

static const wxString strWarning = wxT(\
"û��������Ҫ�벻Ҫʹ���½���Դ����,������ܻ�ر�\n\
\"�����ļ���\"����,û�б����ļ���֧�ֵĻ������滻��\n\
��Դ�󽫲��ܱ���Ϸʶ��,���Լ�Ҫ�滻��Դ����Ҫд��\n\
����Դ��ʱ����ط�����ִ��.");

BEGIN_EVENT_TABLE(Package, wxPanel)
//	EVT_CHECKLISTBOX(id, func)
	EVT_LISTBOX(ID_PKG_LISTBOX	, Package::OnLBShowInfo)
	EVT_BUTTON(ID_PKG_BNFIND	, Package::OnBnSearch)
	EVT_BUTTON(ID_PKG_BNOPENDIR	, Package::OnBnOpenDir)
	EVT_BUTTON(ID_PKG_BNCLOSEALL, Package::OnBnCloseAll)
END_EVENT_TABLE()

void Package::OnBnSearch(wxCommandEvent &event)
{
	int pos = m_clbFileList->FindString(m_tcSearch->GetValue(), false);
	if (pos != wxNOT_FOUND)
	{
		m_clbFileList->SetSelection(pos, true);
	}
}

void Package::OnBnOpenDir(wxCommandEvent &event)
{
	m_strDirPath = wxFileSelector(wxT("Open dir file"), wxEmptyString,
		wxEmptyString, wxT("dir"), wxT("Dir file (*.dir)|*.dir"));
	if (!m_strDirPath.IsEmpty())
	{
		OpenDirFile(m_strDirPath);
		EnableButton(true);
	}
	EmptyWorkingSet(GetCurrentProcess());
}

void Package::OpenDirFile(const wxString &strDirPath)
{	
	char	szFileName[0xD];szFileName[0xC] = 0;
	DWORD	dwDirFileNum, dwRead, dwDirOffset = 0x10, dwSize;
	HANDLE	hDir = CreateFile(strDirPath,
		GENERIC_READ,
		FILE_SHARE_READ,
		0,
		OPEN_EXISTING,
		FILE_ATTRIBUTE_NORMAL,
		NULL);
	if (hDir == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("�޷���dir�ļ�."), wxT("����"));
		return;
	}
	SetFilePointer(hDir, 0x8, 0, FILE_BEGIN);
	ReadFile(hDir, &dwDirFileNum, 4, &dwRead, NULL);
	if (dwRead == NULL)
	{
		wxMessageBox(wxT("��ȡdirʧ��."), wxT("����"));
	}
	else if (dwDirFileNum > 0xFFFF)
	{
		wxMessageBox(wxT("�Ƿ���dir�ļ�(�ļ���������)."), wxT("����"));
	}
	else
	{
		dwSize = GetFileSize(hDir, NULL);
		m_clbFileList->Clear();
		while (dwDirFileNum--&&dwDirOffset < dwSize)
		{
			SetFilePointer(hDir, dwDirOffset, 0, FILE_BEGIN);
			ReadFile(hDir, szFileName, 0xC, &dwRead, NULL);
			m_clbFileList->Append(szFileName);
			dwDirOffset += 0x24;
		}
		m_bnSreach->SetDefault();
	}
	CloseHandle(hDir);
}

void Package::EnableButton(bool enable)
{
	for (size_t ID = ID_PKG_BNOPENDAT; ID != ID_PKG_BNFIND + 1; ++ID)
		(wxButton *)FindWindow(ID)->Enable(enable);
}

void Package::OnBnCloseAll(wxCommandEvent &event)
{
	m_clbFileList->Clear();
	m_bnOpenDir->SetDefault();
	m_StaticBox->SetLabel(wxT("��/�����"));
	EnableButton(false);
	SetProcessWorkingSetSize(GetCurrentProcess(), -1, -1);
}

void Package::OnLBShowInfo(wxCommandEvent &event)
{
	char	cDirInfo[0x14];
	DWORD	dwRead;
	HANDLE	hDir = CreateFile(m_strDirPath,
		GENERIC_READ,
		FILE_SHARE_READ,
		0,
		OPEN_EXISTING,
		FILE_ATTRIBUTE_NORMAL,
		NULL);
	if (hDir == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("�޷���dir�ļ�."), wxT("����"));
		return;
	}
	SetFilePointer(hDir, event.GetInt() * 0x24 + 0x20, 0, FILE_BEGIN);
	ReadFile(hDir, cDirInfo, 0x14, &dwRead, NULL);
	if (dwRead == NULL)
	{
		wxMessageBox(wxT("��ȡdirʧ��."), wxT("����"));
		OnBnCloseAll(wxCommandEvent(wxEVT_NULL));
	}
	else
	{
		wxString strInfo;
		strInfo.Printf(wxT("�ļ���ʼλ��: 0x%X, �ļ���С: 0x%X bytes"), 
			*(DWORD *)(cDirInfo + 0x10), *(DWORD *)(cDirInfo));
		m_StaticBox->SetLabel(strInfo);
	}
	CloseHandle(hDir);
}

Package::Package(wxNotebook *notebook, long ID, MyFrame *parent) : wxPanel(notebook, ID,
															wxDefaultPosition, wxDefaultSize,
															wxNO_FULL_REPAINT_ON_RESIZE |
															wxCLIP_CHILDREN |
															wxTAB_TRAVERSAL)
{
	m_StaticBox = new wxStaticBox(this, ID_PKG_STATICBOX, wxT("��/�����"));

	wxSizer *VSizer = new wxBoxSizer(wxVERTICAL),
			*HSizer = new wxBoxSizer(wxHORIZONTAL),
			*BoxSizer = new wxStaticBoxSizer(m_StaticBox, wxHORIZONTAL);
	m_GSizer = new wxBoxSizer(wxHORIZONTAL);

	// �ļ��б�
	m_clbFileList = new wxCheckListBox(this, ID_PKG_LISTBOX, 
		wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_SINGLE);
	VSizer->Add(m_clbFileList, 1, wxALL|wxGROW, 5);

	// ��������
	m_tcSearch = new wxTextCtrl(this, ID_PKG_TCSEARCH);
	HSizer->Add(m_tcSearch, 0, wxGROW|wxLEFT|wxTOP, 5);

	// ���Ұ�ť
	m_bnSreach = new wxButton(this, ID_PKG_BNFIND, wxT("���ٲ���"));
	HSizer->Add(m_bnSreach, 0, wxLEFT|wxTOP|wxGROW, 5);

	VSizer->Add(HSizer);

	// ������ߵĲ���
	HSizer = new wxBoxSizer(wxHORIZONTAL);
	HSizer->Add(VSizer, 0, wxGROW, 10);

	// ��ʼ�Ұ��
	VSizer = new wxBoxSizer(wxVERTICAL);

	// �Ұ�ߵ����а�ť
	m_bnOpenDir = new wxButton(this, ID_PKG_BNOPENDIR, wxT("��DIR�ļ�"));
	m_bnOpenDir->SetDefault();
	VSizer->Add(m_bnOpenDir, 0, wxTOP|wxGROW, 5);
	m_bnOpenDat = new wxButton(this, ID_PKG_BNOPENDAT, wxT("��DAT�ļ�"));
	VSizer->Add(m_bnOpenDat, 0, wxTOP|wxGROW, 10);
	m_bnExtract = new wxButton(this, ID_PKG_BNEXTRACT, wxT("������ļ�"));
	VSizer->Add(m_bnExtract, 0, wxTOP|wxGROW, 10);
	m_bnAddFile = new wxButton(this, ID_PKG_BNADDFILE, wxT("����ļ�"));
	VSizer->Add(m_bnAddFile, 0, wxTOP|wxGROW, 10);
	m_bnSave = new wxButton(this, ID_PKG_BNSAVE, wxT("����DAT/DIR"));
	VSizer->Add(m_bnSave, 0, wxTOP|wxGROW, 10);
	m_bnRestore = new wxButton(this, ID_PKG_BNRESTORE, wxT("��ԭDAT/DIR"));
	VSizer->Add(m_bnRestore, 0, wxTOP|wxGROW, 10);
	m_bnPlay = new wxButton(this, ID_PKG_BNPLAY, wxT("����WAV(DT28)"));
	VSizer->Add(m_bnPlay, 0, wxTOP|wxGROW, 10);
	m_bnCloseAll = new wxButton(this, ID_PKG_BNCLOSEALL, wxT("�ر������ļ�"));
	VSizer->Add(m_bnCloseAll, 0, wxTOP|wxGROW, 10);
	m_cbDecompress	= new wxCheckBox(this, ID_PKG_COMPRESS,		wxT("��ѹ"));
	m_cbNoEncode	= new wxCheckBox(this, ID_PKG_NOENCODE,		wxT("������"));
	m_cbCompress	= new wxCheckBox(this, ID_PKG_DECOMPRESS,	wxT("ѹ��"));
	m_cbBackup		= new wxCheckBox(this, ID_PKG_KEEPNAME,		wxT("�����ļ���"));
	VSizer->Add(m_cbDecompress, 0, wxTOP|wxLEFT|wxGROW, 10);
	VSizer->Add(m_cbNoEncode, 0, wxTOP|wxLEFT|wxGROW, 10);
	VSizer->Add(m_cbCompress, 0, wxTOP|wxLEFT|wxGROW, 10);
	VSizer->Add(m_cbBackup, 0, wxTOP|wxLEFT|wxGROW, 10);

	// ���StaticBox
	HSizer->Add(VSizer, 0, wxGROW, 10);
	BoxSizer->Add(HSizer, 0, wxGROW|wxALL, 5);

	// ˵������
	HSizer = new wxBoxSizer(wxVERTICAL);
	HSizer->Add(new wxStaticText(this, ID_PKG_README, strReadme), 0, wxGROW|wxALL, 10);
	HSizer->AddSpacer(150);
	HSizer->Add(new wxStaticText(this, ID_PKG_WARNING, strWarning), 0, wxGROW|wxALL, 10);
	((wxStaticText *)FindWindow(ID_PKG_WARNING))->SetForegroundColour(wxColour(206, 120, 166));

	m_GSizer->Add(BoxSizer, 0, wxGROW|wxALL, 5);
	m_GSizer->Add(HSizer, 0, wxGROW, 0);
	SetSizer(m_GSizer);
	EnableButton(false);
}

Package::~Package()
{
	;
}
