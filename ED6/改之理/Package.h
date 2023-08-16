/*******************************************************************
	����	:	�ƻ���ľ
	�ļ���	: 	Package.h
	����ʱ��:	2009-3-24   20:44
	����޸�:	2009-3-24   20:44

	������ʷ:	2009-3-24	�����ļ�
*********************************************************************/

#ifndef _Package_H__
#define _Package_H__

#include <wx/panel.h>

class MyFrame;

class Package : public wxPanel
{
public:
	Package(wxNotebook *notebook, long ID, MyFrame *parent);
	virtual ~Package();
	
protected:
	void OnBnSearch(wxCommandEvent &event);
	void OnBnOpenDir(wxCommandEvent &event);
	void OnLBShowInfo(wxCommandEvent &event);
	void OnBnCloseAll(wxCommandEvent &event);

protected:
	void EnableButton(bool enable);
	void OpenDirFile(const wxString &strDirPath);
	
private:
	wxSizer *m_GSizer;
	wxCheckListBox *m_clbFileList;
	wxTextCtrl *m_tcSearch;
	wxCheckBox *m_cbBackup,
			   *m_cbNoEncode,
			   *m_cbCompress,
			   *m_cbDecompress;

	wxButton *m_bnOpenDir,
			 *m_bnOpenDat,
			 *m_bnExtract,
			 *m_bnSave,
			 *m_bnRestore,
			 *m_bnPlay,
			 *m_bnCloseAll,
			 *m_bnSreach,
			 *m_bnAddFile;

	wxStaticBox *m_StaticBox;

	wxString m_strDirPath,
			 m_strDatPath;
	DECLARE_EVENT_TABLE()
};

#endif /* Package_H__ */