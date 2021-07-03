#include "CWindow.h"

TMenuItem Menu_Lock[] =
{
    { ID_LOCK_HP,   MF_ENABLED, "����HP\tF5",   NULL },
    { ID_LOCK_MP,   MF_ENABLED, "����MP\tF6",   NULL },
    { ID_LOCK_OUGI, MF_ENABLED, "��������\tF5", NULL },
};

TMenuItem Menu_Modify_Ski[] =
{
    { ID_SKI_LV1, MF_ENABLED, "Lv.1 ͨ��", NULL },
    { ID_SKI_LV2, MF_ENABLED, "Lv.2 ͨ��", NULL },
    { ID_SKI_LV3, MF_ENABLED, "Lv.3 ͨ��", NULL },
    { ID_SKI_LV4, MF_ENABLED, "Lv.4 ͨ��", NULL },
};

TMenuItem Menu_Max_EventItem[] =
{
    { ID_MAX_EVENTITEM, MF_ENABLED, "�¼�����", NULL },
    { ID_MAX_CD,        MF_ENABLED, "CD����",   NULL },
    { ID_MAX_TREASURE,  MF_ENABLED, "��֮����", NULL },
};

TMenuItem Menu_Modify[] =
{
    { ID_GOLD,  MF_ENABLED, "��Ǯ",     NULL,     0 },
    { ID_STEP,  MF_ENABLED, "�ܲ���",   NULL,     0 },
    { ID_POPUP, MF_POPUP,   "��ѩ���", Menu_Modify_Ski, countof(Menu_Modify_Ski) },
};

TMenuItem Menu_Maximum[] =
{
    { ID_MAX_GOLD,            MF_ENABLED, "��Ǯ\tCtrl+A",   NULL },
    { ID_POPUP,               MF_POPUP,   "�¼�����",       Menu_Max_EventItem, countof(Menu_Max_EventItem) },
    { ID_MAX_ITEM,            MF_ENABLED, "����\tCtrl+E",   NULL },
    { ID_MAX_FOOD,            MF_ENABLED, "ʳ��\tCtrl+F",   NULL },
    { ID_MAX_EQUIPMENT,       MF_ENABLED, "����\tCtrl+G",   NULL },
    { ID_MAX_ACCESSORYSOCKET, MF_ENABLED, "��Ʒ��\tCtrl+A", NULL },
    { ID_MAX_OUGI,            MF_ENABLED, "����\tCtrl+H",   NULL },
    { ID_MAX_CLOTHES,         MF_ENABLED, "�·�\tCtrl+I",   NULL },
    { ID_MAX_ACCESSORY,       MF_ENABLED, "��Ʒ\tCtrl+J",   NULL },
    { ID_MAX_GADGET,          MF_ENABLED, "�Ҽ�\tCtrl+K",   NULL },
    { ID_MAX_PET,             MF_ENABLED, "����\tCtrl+L",   NULL },
    { ID_MAX_CHAR,            MF_ENABLED, "����\tCtrl+M",   NULL },
    { ID_MAX_MONSTER,         MF_ENABLED, "ħ��\tCtrl+N",   NULL },
};

TMenuItem Menu_Joy_Ragna[] =
{
    { ID_JOY_RAGNA_ORIGIN,          MF_ENABLED, "�����ǡ�ԭ����\tCtrl+F1", NULL },
    { ID_JOY_RAGNA_BLUEHAIR,        MF_ENABLED, "�����ǡ�������",          NULL },
    { ID_JOY_RAGNA_NOEYEPATCH,      MF_ENABLED, "�����ǡ�������",          NULL },
    { ID_JOY_RAGNA_EYEPATCH,        MF_ENABLED, "�����ǡ�������",          NULL },
    { ID_JOY_RAGNA_HOTSPRING,       MF_ENABLED, "�����ǡ���Ȫװ",          NULL },
    { ID_JOY_RAGNA_TAPEUP,          MF_ENABLED, "�����ǡ�������",          NULL },
    { ID_JOY_RAGNA_ERMINE,          MF_ENABLED, "�����ǡ�������",          NULL },
    { ID_JOY_RAGNA_ALWENORIGIN,     MF_ENABLED, "������ԭ����",            NULL },
    { ID_JOY_RAGNA_ALWENREDHAIR,    MF_ENABLED, "�������췢��",            NULL },
    { ID_JOY_RAGNA_ALWENHOTSPRING,  MF_ENABLED, "��������Ȫװ",            NULL },
    { ID_JOY_RAGNA_ALWENSAILORSUIT, MF_ENABLED, "������ˮ�ַ�",            NULL },
    { ID_JOY_RAGNA_SUBARUORIGIN,    MF_ENABLED, "����·��ԭ����",          NULL },
    { ID_JOY_RAGNA_SUBARUNOSHOE,    MF_ENABLED, "����·����Ь��",          NULL },
    { ID_JOY_RAGNA_SUBARUHOTSPRING, MF_ENABLED, "����·����Ȫװ",          NULL },
    { ID_JOY_RAGNA_SUBARUTAPEUP,    MF_ENABLED, "����·��������",          NULL },
};

TMenuItem Menu_Joy_Alwen[] =
{
    { ID_JOY_ALWEN_ORIGIN,          MF_ENABLED, "������ԭ����\tCtrl+F2", NULL },
    { ID_JOY_ALWEN_REDHAIR,         MF_ENABLED, "�������췢��",          NULL },
    { ID_JOY_ALWEN_HOTSPRING,       MF_ENABLED, "��������Ȫװ",          NULL },
    { ID_JOY_ALWEN_SAILORSUIT,      MF_ENABLED, "������ˮ�ַ�",          NULL },
    { ID_JOY_ALWEN_RAGNAORIGIN,     MF_ENABLED, "�����ǡ�ԭ����",        NULL },
    { ID_JOY_ALWEN_RAGNABLUEHAIR,   MF_ENABLED, "�����ǡ�������",        NULL },
    { ID_JOY_ALWEN_RAGNANOEYEPATCH, MF_ENABLED, "�����ǡ�������",        NULL },
    { ID_JOY_ALWEN_RAGNAEYEPATCH,   MF_ENABLED, "�����ǡ�������",        NULL },
    { ID_JOY_ALWEN_RAGNAHOTSPRING,  MF_ENABLED, "�����ǡ���Ȫװ",        NULL },
    { ID_JOY_ALWEN_RAGNATAPEUP,     MF_ENABLED, "�����ǡ�������",        NULL },
    { ID_JOY_ALWEN_RAGNAERMINE,     MF_ENABLED, "�����ǡ�������",        NULL },
    { ID_JOY_ALWEN_SUBARUORIGIN,    MF_ENABLED, "����·��ԭ����",        NULL },
    { ID_JOY_ALWEN_SUBARUNOSHOE,    MF_ENABLED, "����·����Ь��",        NULL },
    { ID_JOY_ALWEN_SUBARUHOTSPRING, MF_ENABLED, "����·����Ȫװ",        NULL },
    { ID_JOY_ALWEN_SUBARUTAPEUP,    MF_ENABLED, "����·��������",        NULL },
};

TMenuItem Menu_Joy_Servant[] =
{
    { ID_JOY_FOLLOW_NONE, MF_ENABLED, "��",   NULL },
    { ID_JOY_FOLLOW_LUE,  MF_ENABLED, "¶",   NULL },
    { ID_JOY_FOLLOW_MIA,  MF_ENABLED, "���", NULL },
};

TMenuItem Menu_Joy[] =
{
    { ID_POPUP, MF_POPUP, "������", Menu_Joy_Ragna,   countof(Menu_Joy_Ragna) },
    { ID_POPUP, MF_POPUP, "����",   Menu_Joy_Alwen,   countof(Menu_Joy_Alwen) },
    { ID_POPUP, MF_POPUP, "����",   Menu_Joy_Servant, countof(Menu_Joy_Servant) },
};

TMenuItem Menu_Other[] =
{
    { ID_OTHER_UNDEAD,        MF_ENABLED, "�޵�\tShift+F1",             NULL },
    { ID_OTHER_ONEFOODLVUP,   MF_ENABLED, "��һ��ʳ�������\tShift+F2", NULL },
    { ID_OTHER_ONEHIT,        MF_ENABLED, "һ����ɱ\tShift+F3",         NULL },
    { ID_OTHER_QSPS,          MF_ENABLED, "��������\tShift+F4",         NULL },
    { ID_OTHER_UNLIMITEDJUMP, MF_ENABLED, "������Ծ\tShift+F5",         NULL },
    { ID_OTHER_FASTMOVE,      MF_ENABLED, "�����ƶ�\tShift+F6",         NULL },
    { ID_OTHER_EVAPLAT,       MF_ENABLED, "����Ϊ�׽�\tShift+F7",       NULL },
    { ID_OTHER_FIGURE,        MF_ENABLED, "�ص��ְ�\tShift+F8",         NULL },
};

TMenuItem Menu_Item[] =
{
    { ID_POPUP, MF_POPUP, "����",   Menu_Lock,    countof(Menu_Lock)    },
    { ID_POPUP, MF_POPUP, "�޸�",   Menu_Modify,  countof(Menu_Modify)  },
    { ID_POPUP, MF_POPUP, "���", Menu_Maximum, countof(Menu_Maximum) },
    { ID_POPUP, MF_POPUP, "����",   Menu_Joy,     countof(Menu_Joy)     },
    { ID_POPUP, MF_POPUP, "����",   Menu_Other,   countof(Menu_Other)   },
};

TMenuItem Menu_File[] =
{
    { ID_REFRESHDATA,    MF_ENABLED, "ˢ������\tF5" },
    { ID_OPENSAVEFOLDER, MF_ENABLED, "�򿪴浵�ļ���" },
    { ID_EXIT,           MF_ENABLED, "�˳�\tEsc" },
};

TMenuItem Menu_Main[] =
{
    { ID_POPUP, MF_POPUP,   "�ļ�(&F)", Menu_File, countof(Menu_File) },
    { ID_POPUP, MF_POPUP,   "��Ŀ(&I)", Menu_Item, countof(Menu_Item) },
    { ID_ABOUT, MF_ENABLED, "����(&A)", NULL,      0 },
};

DWORD dwMenuCount = countof(Menu_Main);