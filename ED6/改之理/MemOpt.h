/*******************************************************************
	����	:	�ڴ��޸�����
	�ļ���	: 	MemOpt.h
	����ʱ��:	2009-3-17   13:04
	����޸�:	2009-3-17   13:04

	������ʷ:	2009-3-17	�����ļ�
*********************************************************************/

#ifndef _MEMOPT_H_
#define _MEMOPT_H_

#include <vector>
#include <wx/panel.h>

class MyFrame;

class MemOpt : public wxPanel
{
public:
	MemOpt(wxNotebook *notebook, long ID, MyFrame *parent);
	virtual ~MemOpt();

protected:
	void OnRBGameVerFC(wxCommandEvent &event);
	void OnRBGameVerSC(wxCommandEvent &event);
	void OnLBSelWindow(wxCommandEvent &event);
	void OnBnSaveOption(wxCommandEvent &event);
	void OnRBGameVer3rd(wxCommandEvent &event);
	void OnBnChangeTitle(wxCommandEvent &event);
	static BOOL CALLBACK EnumWindowsProc(HWND hwnd,LPARAM lParam);

private:
	static MemOpt *This;
	BYTE m_bGameVer;

	// ѡ����Ϸ�汾
	wxStaticBox *m_StaticBox;
	wxRadioButton *m_rbGameVer[3];

	// ����, ���ı���, �ĵ�ַ
	wxButton *m_bnSave,
			 *m_bnChangeTitle,
			 *m_bnChangeAddress;

	// ��ǰ���д����б�
	wxListBox *m_lbWindowList;

	// ��Ϸ����
	wxTextCtrl *m_tcGameTitle[3];

	// ��һ��HP��ַ
	wxTextCtrl *m_tcFirstHPAddress[3];

	// ��ʾ�ı�
	wxStaticText *m_tcTipText;

	// ȫ��Sizer
	wxSizer *m_GSizer;

	// ��Ŵ��ھ��
	std::vector<HWND> m_vhWnd;
	DECLARE_EVENT_TABLE()
};

#endif	/* _MEMOPT_H_ */