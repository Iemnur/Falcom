/*******************************************************************
	����	:	�����
	�ļ���	: 	MainFrame.cpp
	����ʱ��:	2009/03/09   16:59
	����޸�:	2009/03/15   16:59
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"

enum ID_COMMANDS
{
		ID_MAINFRAME = wxID_HIGHEST + 1,
		ID_TAB ,								// ѡ�
		ID_TAB_MEMNORMAL,						// �ڴ泣���޸�
		ID_TAB_MEMITEM,							// �ڴ���Ʒ�޸�
		ID_TAB_MEMCRAFT,						// �ڴ漼���޸�
		ID_TAB_MEMDIALOG,						// �Ի��޸�
		ID_TAB_MEMDIFF,							// �Ѷȵ���
		ID_TAB_BATTLEFIGURE,					// ս�������޸�
		ID_TAB_SAVENORMAL,						// �浵�����޸�
		ID_TAB_SAVEPOS,							// �浵λ���޸�
		ID_TAB_SAVEHANDBOOK,					// �浵�ֲ��޸�
		ID_TAB_SAVEMISSION,						// �浵�����޸�
		ID_TAB_SAVEITEM,						// �浵��Ʒ�޸�
		ID_TAB_SAVECRAFT,						// �浵ս���޸�
		ID_TAB_LOADSAVE,						// ��ȡ�浵
		ID_TAB_MEMOPT,							// �ڴ��޸�����
		ID_TAB_TLHZ,							// ͵������
		ID_TAB_PACKAGE,							// �ƻ���ľ
		ID_TAB_LIMITED,							// �޶��汾����
		ID_TAB_ABOUT,							// ����
};

static const wxChar *szTabName[] =
{
	wxT("�ڴ泣���޸�"), wxT("�ڴ���Ʒ�޸�"), wxT("�ڴ漼���޸�"), 
	wxT("�Ի��޸�"),	 wxT("�Ѷȵ���"),	  wxT("ս�������޸�"),

	wxT("�浵�����޸�"), wxT("�浵λ���޸�"), wxT("�浵�ֲ��޸�"), 
	wxT("�浵�����޸�"), wxT("�浵��Ʒ�޸�"), wxT("�浵ս���޸�"),

	wxT("��ȡ�浵"), wxT("�ڴ��޸�����"),	wxT("͵������"), 
	wxT("�ƻ���ľ"), wxT("�޶��汾�Ĺ���"), wxT("����"),
};

DECLARE_APP(MyApp)
IMPLEMENT_APP(MyApp)

HWND		MyFrame::hWindow		= NULL;
wxString	MyFrame::strCurSavFile	= wxT("");
wxString	MyFrame::strCfgFileName	= wxT("");
char		*MyFrame::cSaveBuff		= NULL;

bool MyApp::OnInit()
{
	// get config file full path
	wxChar buff[_MAX_PATH];
	GetModuleFileName(GetModuleHandle(NULL), buff, sizeof(buff));
	MyFrame::strCfgFileName = buff;
	MyFrame::strCfgFileName.replace(MyFrame::strCfgFileName.Last('\\') + 1, 
		WXSIZEOF(wxT("Config.ini")), wxT("Config.ini"));

	// initialization MyFrame object frame
	MyFrame *frame = new MyFrame(wxT("��֮�� Reload"));
	frame->SetSize(757, 463);
	wxSize wxFrameSize = frame->GetSize();
	frame->SetMaxSize(wxFrameSize);
	frame->SetMinSize(wxFrameSize);
	frame->CenterOnScreen();
	frame->SetWindowStyle(wxDEFAULT_FRAME_STYLE&~wxMAXIMIZE_BOX);
//	frame->ShowWithEffect(wxSHOW_EFFECT_BLEND);
	frame->Show(true);
//	frame->Refresh();

//	SetProcessWorkingSetSize(GetCurrentProcess(), -1, -1);
	EmptyWorkingSet(GetCurrentProcess());
	return true;
}

BEGIN_EVENT_TABLE(MyFrame, wxFrame)
	EVT_CLOSE(MyFrame::OnExit)
END_EVENT_TABLE()

MyFrame::MyFrame(const wxString &strTitle) : wxFrame(NULL, ID_MAINFRAME, strTitle)
{
	DWORD dwPosition = 0;
	SetIcon(wxICON(Lucy));
	m_dwTabNum = sizeof(szTabName) / 4;
	notebook = new wxNotebook(this, ID_TAB, wxDefaultPosition, wxDefaultSize, wxNB_MULTILINE);

	DlgPackage = new Package(notebook, ID_TAB_PACKAGE, this);
	notebook->InsertPage(dwPosition++, DlgPackage, wxT("�ƻ���ľ"));

	DlgMemOpt = new MemOpt(notebook, ID_TAB_MEMOPT, this);
	notebook->InsertPage(dwPosition++, DlgMemOpt, wxT("�ڴ��޸�����"));

	DlgLoadSave = new LoadSave(notebook, ID_TAB_LOADSAVE, this);
	notebook->InsertPage(dwPosition++, DlgLoadSave, wxT("��ȡ�浵"));

	DlgAbout = new About(notebook, ID_TAB_ABOUT, this);
	notebook->InsertPage(dwPosition++, DlgAbout, wxT("����"));
}

void MyFrame::OnExit(wxCloseEvent &event)
{
	if (cSaveBuff)
	{
		VirtualFree(cSaveBuff, 0, MEM_RELEASE);
	}
	Destroy();
}