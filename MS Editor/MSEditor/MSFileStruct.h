#ifndef _MSFILESTRUCT_H_
#define _MSFILESTRUCT_H_

#if _MSC_VER > 1000
#pragma once
#endif

#pragma warning(disable:4305)
#pragma warning(disable:4309)

#define LEN_OF_AIDATA       0x18
#define LEN_OF_SKILLDATA    0x1C
#define MAX_CRAFT_NAME      0x20
#define MAX_CRAFT_DES       0x100
#define MAX_NAME            0x15
#define MAX_DESCRIPTION     0x53
#define MAX_SEPITH_KIND     0x7
#define MAX_SEPITH_DROP     0xFF
#define MAX_CONDITION       0xFF
#define MAX_MAGIC_NUM       0x80
#define MAX_CRAFT_NUM       0x10
#define MAX_SKILL_NUM       0x10
#define CUSTOM_SKILL_BASE   0x3E8
#define CUSTOM_SKILL_MAX    0x3F8

#pragma pack(1)

typedef struct _tagAIData
{
    BYTE byCondition;
    BYTE byProbability;
    BYTE byTarget;
    BYTE byTargetCondition;
    WORD wEffectIndex;
    WORD wSkillDataIndex;
    CHAR cParam1[8];
    CHAR cParam2[8];
} TAIData, *LPAIData;

typedef struct
{
    BYTE    Condition;
    BYTE    Probability;
    BYTE    Target;
    BYTE    TargetCondition;
    BYTE    MagicChantAsEffectIndex;
    BYTE    AsEffectIndex;
    WORD    SkillInfoIndex;
    ULONG   Param[4];
} ED6_CRAFT_AI_INFO;

typedef struct
{
    ULONG               ASFileIndex;            // 0x00     LOWORD = FileIndex, HIWORD = DAT Index
    USHORT              Level;                  // 0x04
    ULONG               HPMax;                  // 0x06
    ULONG               HPInitial;              // 0x0A
    USHORT              EPMax;                  // 0x0E
    USHORT              EPInitial;              // 0x10
    USHORT              CPMax;                  // 0x12
    USHORT              CPInitial;              // 0x14
    USHORT              SPD;                    // 0x16
    USHORT              MoveSPD;                // 0x18     �ƶ��ٶ�
    USHORT              MOV;                    // 0x1A
    USHORT              STR;                    // 0x1C
    USHORT              DEF;                    // 0x1E
    USHORT              ATS;                    // 0x20
    USHORT              ADF;                    // 0x22
    USHORT              DEX;                    // 0x24
    USHORT              AGL;                    // 0x26
    USHORT              RGN;                    // 0x28
    DUMMY_STRUCT(2);
    USHORT              EXP;                    // 0x2C     ����ֵ,(�з��ȼ�-�ѷ��ȼ�) * EXP
    DUMMY_STRUCT(2);
    USHORT              AIType;                 // 0x30     // 00 01 02 10 13 14
    DUMMY_STRUCT(6);
    BYTE                Flags;                  // 0x38     0x10: ���� 0x40: ����
    BYTE                DeathFlags;             // 0x39     0x04 ��������ս����
    BYTE                UnderAttackFlags;       // 0x3A     0x08 Risist ATDelay 0x02 �������� 0x01 ��������ת��(3D)
    DUMMY_STRUCT(5);
    BYTE                SEX;                    // 0x40     0: Ů 1: ��
    DUMMY_STRUCT(9);
    USHORT              CharSize;               // 0x4A     ռ CharSize / 2 / 400 ��
    DUMMY_STRUCT(0xA);
    ULONG               SymbolTextureFileIndex; // 0x56     AT��ͷ��
    ULONG               Resistance;             // 0x5A     �쳣״̬����
    DUMMY_STRUCT(0xB);
    ULONG               ConditionResistance[7]; // 0x69     ���Թ�������
    BYTE                Sepith[7];              // 0x77     ����ҫ��Ƭ
    DUMMY_STRUCT(6);
    WORD                Equip[5];               // 0x84     װ��
    WORD                Orb[4];                 // 0x8E     ��·

    ED6_CRAFT_AI_INFO   NormalAttack;           // 0x96     ??
    DUMMY_STRUCT(8);
    BYTE                MagicCount;
    ED6_CRAFT_AI_INFO   Magic[MagicCount];      // ħ��ʹ�ñ�, ���80��
    BYTE                CraftCount;
    ED6_CRAFT_AI_INFO   Craft[CraftCount];      // ս��ʹ�ñ�, ���10��
    BYTE                SCraftCount;
    ED6_CRAFT_AI_INFO   SCraft[SCraftCount];    // S��ʹ�ñ�, ���5��
    BYTE                MagicTableCount;        // ħ������
    // .........
} ED6_MONSTER_STATUS;

typedef struct
{
    DWORD   MsFileSize;             // MS�ļ���С
    DWORD   ASIndex;                // ʹ�õ�AS�ļ�
    WORD    Level;                  // �ȼ�
    DWORD   HPMax;                  // HP����
    DWORD   HPDefault;              // ȱʡHP
    WORD    EPMax;                  // EP����
    WORD    EPDefault;              // ȱʡEP
    WORD    CPMax;                  // CP����
    WORD    CPDefault;              // ȱʡCP
    WORD    SPD;                    // �ٶ�
    WORD    MoveSPD;                // �ƶ��ٶ�
    WORD    MOV;                    // �ƶ�����
    WORD    STR;                    // ��������
    WORD    DEF;                    // ���������
    WORD    ATS;                    // ħ��������
    WORD    ADF;                    // ħ��������
    WORD    DEX;                    // ����
    WORD    AGL;                    // �ر�
    WORD    RNG;                    // ��������
    WORD    EXP;                    // ����ֵ,(�з��ȼ�-�ѷ��ȼ�) * Exp
    BYTE    DeathFlag;              // 0x04 ��������ս����
    BYTE    UnderAttackFlag;        // 0x08 Risist ATDelay 0x02 �������� 0x01 ��������ת��(3D)
    DWORD   Resistance;             // �쳣״̬����
    WORD    ConditionGuard[7];      // ������Ч��
    BYTE    Sepith[7];              // ����ҫ��Ƭ
    WORD    Equip[5];               // װ��
    WORD    Orb[4];                 // ��·
    BYTE    MagicCount;             // ħ����
    PBYTE   pbMagic;                // ħ��������ʼ��ַ
    BYTE    CraftCount;             // ��ͨս����
    PBYTE   pbCraft;                // ��ͨս��������ʼ��ַ
    BYTE    SCraftCount;            // S����
    PBYTE   pbSCraft;               // S��������ʼ��ַ
    BYTE    SkillDataCount;         // ħ��&ս��(>0x3E8)��
    PBYTE  *pbSKillData;            // ħ��&ս��(>0x3E8)���ݵ�ַ
    LPSTR  *lpSkillName;            // ħ��&ս��(>0x3E8)��������
    LPSTR  *lpSkillDescription;     // ħ��&ս��(>0x3E8)˵������
    LPSTR   lpName;                 // ��������
    LPSTR   lpDescription;          // ����˵��
} MSFileInfo, *LPMSFileInfo;

#pragma pack()

typedef struct _tagAI_Item
{
    CHAR   *szDescription;
    BYTE    nBytesOfParam;
    DWORD   dwParam1;
    DWORD   dwParam2;
} TAI_Item;

static TAI_Item condition[] =
{
    {"0%�ĸ���",                            0, 0, 0},
    {"100%�ĸ���",                            0, 0, 0},
    {"������",                                0, 0, 0},
    {"����HP����(%)",                        1, 0, 0},
    {"���ܵ��˺�",                            4, 0x040000, 0},
    {"�ϴγɹ�����˺�",                    4, 0, 0},
    {"��������Ŀ��",                        2, 0, 0},
    {"��������Ŀ��",                        2, 0, 0},
    {"��ʱ����ʱ��ʹ��",                    8, 0, 0},
    {"δ֪",                                0, 0, 0},
    {"CP��С��",                            1, 0, 0},
    {"��",                                    4, 0, 0},
    {"��",                                    4, 0, 0},
    {"��Ŀ��HPС��(%)",                        1, 0, 0},
    {"ս��������������",                    1, 0, 0},
    {"��Ŀ����������",                        0, 0, 0},
    {"��",                                    4, 0, 0},
    {"��",                                    4, 0, 0},
    {"��",                                    4, 0, 0},
    {"��Ŀ�������ض�״̬",                    4, 0, 0},
    {"��Ŀ��û���ض�״̬",                    4, 0, 0},
    {"ָ��Ŀ��û���ض�״̬",                8, 0, 0},
    {"(ħ��ר��)����HP����(%)",                1, 0, 0},
    {"(ħ��ר��)ʹ��ָ�����ܺ�����ʹ��",    2, 0, 0},
    {"δ֪",                                0, 0, 0},
    {"��Ŀ����������ħ��",                    0, 0, 0},
    {"����֣�������������",                0, 0, 0},
    {"��Ŀ��cp�ﵽָ��ֵ",                    1, 0, 0},
};

static TAI_Item target[] =
{
    {"�����",                        0, 0, 0},
    {"������",                        0, 0, 0},
    {"Ů��",                        0, 0, 0},
    {"�����",                        0, 0, 0},
    {"���������",                    0, 0, 0},
    {"������HP����",                0, 0, 0},
    {"HP���",                        0, 0, 0},
    {"��Χ��Ŀ�겻����",            1, 0, 0},
    {"���",                        0, 0, 0},
    {"��Զ��",                        0, 0, 0},
    {"AT����ǰ",                    0, 0, 0},
    {"������",                        0, 0, 0},
    {"�Լ�",                        0, 0, 0},
    {"HP�ٷֱ���͵�",                8, 0, 0},
    {"���Լ�ΪԲ��Ŀ�겻����",        1, 0, 0},
    {"AT�����",                    0, 0, 0},
    {"δ֪",                        0, 0, 0},
    {"ս�����ܵ�",                    0, 0, 0},
    {"������",                        0, 0, 0},
    {"�����ض�״̬��",                4, 0, 0},
    {"CP����",                    0, 0, 0},
    {"ָ���������",                4, 0, 0},
    {"�Ŵ������ר��",                1, 0, 0},
    {"����ص�",                    0, 0, 0},
    {"û���ض�״̬��",                4, 0, 0},
    {"��Χ��Ŀ�겻����(ֱ��)",        1, 0, 0},
};

#endif /* _MSFILESTRUCT_H_ */