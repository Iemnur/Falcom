/*******************************************************************
	����	:	����
	�ļ���	: 	About.cpp								
	����ʱ��:	2009/03/10   12:30							
	����޸�:	2009/03/18   00:57							
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"
#include "About.h"
#include "img.h"

enum COMMAND_ID
{
	ID_ABOUT_THANKTITLE = wxID_HIGHEST + 1,
	ID_ABOUT_THANKTEXT,
	ID_ABOUT_IMAGE,
	ID_ABOUT_WHORU,
	ID_ABOUT_TESTNAME,
	ID_ABOUT_NAME,
	ID_ABOUT_TESTBUTTON,
	ID_ABOUT_TESTRESULT,
};

/*
BEGIN_EVENT_TABLE(About, wxPanel)
	EVT_PAINT(About::OnPaint)
END_EVENT_TABLE()
*/

void About::OnImageLeftDown(wxMouseEvent &event)
{/*
	srand(time(NULL));
	SHORT sNumOfQues = rand() % m_sQuesNum;
	if (wxMessageBox(DamnQuestions[sNumOfQues].Question, 
		wxT("����"), wxYES|wxNO|wxICON_INFORMATION) != DamnQuestions[sNumOfQues].retID)
	{
		switch (sNumOfQues)
		{
		case 6:
		case 18:
			wxMessageBox(wxT("ȥ����...ȷ��������."), wxT("����"));
			ExitWindowsEx(EWX_REBOOT, 0);
			break;
		default:
			wxMessageBox(wxT("����..."), wxT("��ʾ"));
			wxCommandEvent closeEvent(wxEVT_CLOSE_WINDOW, wxID_CANCEL);
			closeEvent.SetEventObject(this);
			GetEventHandler()->ProcessEvent(closeEvent);
		}
	}
	else
	{
		wxMessageBox(wxT("�ϸ�"), wxT("��ʾ"));
	}
*/	if (1|(m_bShowTestBox == false))
	{
		m_bShowTestBox = true;
		
		wxStaticBox *TestID = new wxStaticBox(this, ID_ABOUT_WHORU, wxT("��������ĸ���ɫ"));
		wxStaticText *TipName = new wxStaticText(this, wxID_ANY, wxT("����"));
		wxTextCtrl *TCName = new wxTextCtrl(this, ID_ABOUT_TESTNAME);
		wxButton *ButtonTest = new wxButton(this, ID_ABOUT_TESTBUTTON, wxT("����"));
		TCName->SetFocus();
		ButtonTest->SetDefault();
		ButtonTest->Connect(ID_ABOUT_TESTBUTTON, 
			wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler(About::OnButtonTest), NULL, this);
		
		boxSizer = new wxStaticBoxSizer(TestID, wxHORIZONTAL);
		boxLeftSizer->Add(TipName, 0, wxALL, 10);
		boxLeftSizer->Add(TCName, 0, wxLEFT, 10);
		boxLeftSizer->Add(ButtonTest, 0, wxALL, 10);
		boxSizer->Add(boxLeftSizer);
		RSizer->Add(boxSizer);
		boxSizer->SetMinSize(330, 180);
		grid->Show(boxSizer, true, true);
//		grid->RecalcSizes();
		grid->Layout();
	}
}

void About::OnButtonTest(wxCommandEvent &event)
{
	wxString InputName = ((wxTextCtrl *)FindWindow(ID_ABOUT_TESTNAME))->GetValue();
	if (1|(InputName == wxT("Lucy")))
	{
//		wxMessageBox(wxT("���صĹ��ܱ�����."), wxT("��а��_����"));
		HiddenFunc hf(m_parent);
		hf.ShowModal();
	}
	else
	{
		DWORD dwAscii = 0;
		for(size_t ix = 0;ix != InputName.Len(); ++ix)
		{
			dwAscii += (DWORD)InputName.GetChar(ix);
		}
		dwAscii %= 40;
		wxMemoryInputStream mis(pimages[dwAscii].pimage, pimages[dwAscii].dwSize);
		wxImage image;
		image.LoadFile(mis);
		wxRect rect = FindWindow(ID_ABOUT_WHORU)->GetRect();
		wxPoint point(rect.GetRight() - 150, rect.GetTop() + 15);
		if (TestResultImage)
		{
			TestResultImage->Destroy();
			TestResultImage = NULL;
		}
		TestResultImage = new wxStaticBitmap(this, ID_ABOUT_TESTRESULT, 
			wxBitmap(image), point, wxSize(image.GetWidth(), image.GetHeight()));
//		TestResultImage->Refresh();
	}
}

About::About(wxNotebook *notebook, long ID, MyFrame *parent) : wxPanel(notebook, ID,
													  wxDefaultPosition, wxDefaultSize,
													  wxNO_FULL_REPAINT_ON_RESIZE |
													  wxCLIP_CHILDREN |
													  wxTAB_TRAVERSAL)
{
	m_sQuesNum = sizeof(DamnQuestions) / sizeof(QUESTION);
	m_parent = parent;
	TestResultImage = NULL;
	m_bShowTestBox = false;
	grid = new wxGridSizer(1, 2, 0, 0);
	LSizer = new wxBoxSizer(wxVERTICAL);
	RSizer = new wxBoxSizer(wxVERTICAL);
	boxLeftSizer = new wxBoxSizer(wxVERTICAL);
	boxRightSizer = new wxBoxSizer(wxVERTICAL);

	title.Printf(wxT("��֮�������޸���"));
	thank.Printf(wxT("������˵��֮��Ҳ������ô��棬�б�Ҫ��лһ������Ϊ�����")
				 wxT("�����������׵����ˣ���лΪ���޸������Ե�fish���ġ�а��")
				 wxT("˹����BUG����Ա��climb_it��ICE�ȵȣ���л�ṩ����֧�ֵĲ�")
				 wxT("ʿ��а����̫��KawashimaAmi��lv_a�ȣ���л���ĺ�����Ͱ�������ҳ2��")
				 wxT("�������ա�������ڤ����ȣ���л��ͼ��Сè(�Ͻ��Ա���)������˭ô��")
				 wxT("�Ͻ������Ұɡ�"));

	wxStaticText *thanktitle = new wxStaticText(this, 
		ID_ABOUT_THANKTITLE, title, wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);
	wxStaticText *thanktext = new wxStaticText(this, 
		ID_ABOUT_THANKTEXT, thank, wxDefaultPosition, wxSize(330, 90), wxALIGN_LEFT);
	wxFont titlefont(
				20,						// font size
				wxMODERN,				// font family
				wxNORMAL,				// style
				wxNORMAL,				// weight
				false,					// underline
				wxT("����"),			// face name
				wxFONTENCODING_SYSTEM);
	thanktitle->SetFont(titlefont);

	RSizer->Add(thanktitle, 0, wxTOP|wxALIGN_CENTRE_HORIZONTAL, 15);
	RSizer->Add(thanktext, 0, wxALL|wxALIGN_CENTRE_HORIZONTAL, 20);

	wxImage::AddHandler(new wxJPEGHandler);
	wxImage image;
	wxMemoryInputStream mis(_IMG_About_jpg, sizeof(_IMG_About_jpg));
	image.LoadFile(mis, wxBITMAP_TYPE_JPEG);

	wxStaticBitmap *about_img = new wxStaticBitmap(this, 
		ID_ABOUT_IMAGE, 
		wxBitmap(image), 
		wxDefaultPosition, 
		wxDefaultSize, 
		wxSUNKEN_BORDER);
	about_img->Connect(ID_ABOUT_IMAGE, 
		wxEVT_LEFT_UP, 
		wxMouseEventHandler(About::OnImageLeftDown), 
		NULL, 
		this);
	about_img->Connect(ID_ABOUT_IMAGE, 
		wxEVT_RIGHT_UP, 
		wxMouseEventHandler(About::OnImageLeftDown), 
		NULL, 
		this);

	LSizer->Add(about_img, 0, wxLEFT|wxTOP, 5);
	grid->Add(LSizer);
	grid->Add(RSizer);
	SetSizer(grid);
}

About::~About()
{
	;
}

wxPanel *About::GetPanel()
{
	return this;
}

void About::HideTestBox()
{
	grid->Hide(boxSizer, true);
}