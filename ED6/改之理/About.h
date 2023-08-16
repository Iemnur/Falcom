/*******************************************************************
	����	:	����
	�ļ���	: 	About.h								
	����ʱ��:	2009/03/10   12:30							
	����޸�:	2009/03/16   17:13						
*********************************************************************/


#ifndef _ABOUT_H_
#define _ABOUT_H_

#include <wx/panel.h>
#include <wx/mstream.h>
#include "HiddenFunc.h"

struct QUESTION
{
	wxString Question;
	int retID;
};

static const QUESTION DamnQuestions[] =
{
	{wxT("�ж��⣬CFDȫ�Ƽ���������ѧ��"), wxYES},
	{wxT("�ж��⣬PSP��֮�����������С�"), wxNO},
	{wxT("�ж��⣬_������_��ʵ�ǡ�_����z�W�Y��"), wxYES},
	{wxT("�ж��⣬fish������12��31�ա�"), wxNO},
	{wxT("�ж��⣬lv_a�ṩ��д���۵Ĺ��ܡ�"), wxNO},
	{wxT("�ж��⣬zlzhcqblf���EVA��"), wxYES},
	{wxT("�ж��⣬��֮�������ʵ����abcfy2��"), wxNO},
	{wxT("�ж��⣬��֮�������YSO��adol����չ졣"), wxNO},
	{wxT("�ж��⣬��֮��ʹ��Visual C++6.0��д��"), wxNO},
	{wxT("�ж��⣬������ڤ�������ڤ�����һ���ˡ�"), wxNO},
	{wxT("�ж��⣬���ȹ����ر䲻һ��Ϊ0��"), wxYES},
	{wxT("�ж��⣬ĳ���Saber��Arcueid��"), wxYES},
	{wxT("�ж��⣬��ά-˹�п�˹���̡������Է��̡�����������CFD���Ļ�����"), wxYES},
	{wxT("�ж��⣬�����Ƿ�ͼ��ʵ��Сè�ι켣���Ի���"), wxYES},
	{wxT("�ж��⣬���ѡ��"), -1},
	{wxT("�ж��⣬��ʵ����и����صĹ��ܡ�"), wxYES},
	{wxT("�ж��⣬��һ������ع����������Ұ�����ͨ��"), wxNO},
	{wxT("�ж��⣬Сè�ι켣��Loli��"), wxNO},
	{wxT("�ж��⣬����֮������ֲ����������д��ľ��"), wxNO},
};

typedef int (__stdcall *DECODEUCI) (const void *src, // ����UCI����ָ��(����Ϊnull)
									int srclen,      // ����UCI���ݳ���(����<0)
									void *dst,       // ���RAW����ָ��(BGR��BGRA��ʽ,����Ϊnull,��ʾֻ�������3������)
									int dstlen,      // ���RAW���ݻ������ĳ���(����<0)
									int *w,          // ���ͼ��Ŀ��ֵ(����Ϊnull)
									int *h,          // ���ͼ��ĸ߶�ֵ(����Ϊnull)
									int *b);         // ���ͼ���bppֵ(ÿ����λ��,����Ϊnull)

class MyFrame;

class About : public wxPanel
{
public:
	About(wxNotebook *notebook, long ID, MyFrame *parent);
	virtual ~About();
	wxPanel *GetPanel();
	void HideTestBox();
	void OnButtonTest(wxCommandEvent &WXUNUSED(event));
private:
	MyFrame *m_parent;
	bool m_bShowTestBox;
	SHORT m_sQuesNum;
	wxString thank, title;
	wxSizer *grid, *LSizer, *RSizer, *boxSizer, *boxLeftSizer, *boxRightSizer;
	wxStaticBitmap *TestResultImage;
	DECODEUCI DecodeUCI;

	void OnImageLeftDown(wxMouseEvent &event);
//	DECLARE_EVENT_TABLE()
};

#endif	/* _ABOUT_H_ */