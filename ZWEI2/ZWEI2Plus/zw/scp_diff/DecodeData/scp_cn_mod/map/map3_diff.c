diff --git a/scp_jp_conv/map/3/EV30003.txt b/scp_conv/map/3/EV30003.txt
index 89848c6..c4a8331 100644
--- a/scp_jp_conv/map/3/EV30003.txt
+++ b/scp_conv/map/3/EV30003.txt
@@ -730,6 +730,7 @@ EV_11_TalkCleese
 //�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D
 //	���ڻ��I��
 //�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D
+	move(CLEESE, 99, 0,0,0,0,0)//0924׷��
 	EV_stop("FREEMOVE_CLEESE")
 	TK_end()
 
diff --git a/scp_jp_conv/map/3/EV30103.txt b/scp_conv/map/3/EV30103.txt
index 3da9adb..4d75e33 100644
--- a/scp_jp_conv/map/3/EV30103.txt
+++ b/scp_conv/map/3/EV30103.txt
@@ -10,6 +10,27 @@
 //--------------------------------------------------------------------
 INIT
 {
+	/*
+	if (Fx_MUGEN_TI_20B )
+	{
+		if (Fx_MUGEN_SUI_20B )
+		{
+			if ( Fx_MUGEN_FUU_20B )
+			{
+				if ( Fx_MUGEN_KA_20B )
+				{
+					F_set(Fx_MUGEN2_OPENED)
+				}
+			}
+		}
+	}
+	*/
+
+	if ( F6_11_GameClear )
+	{
+		F_set(Fx_MUGEN2_OPENED)
+	}
+	
 	// ����
 	set_obj2("mp30003", 2,4,   450,-450,  0,	 0) //
 	set_obj2("mp30023", 2,4,   450, 450,  0,	 0) //
@@ -38,10 +59,40 @@ INIT
 	set_obj("@obx0033a", 3, 2,     0,   0,  0,		  0)						//�ۥ��`����ɭ�v��
 	set_chr(192,1400,	 3, 2,	   0,   0,  0,		  0,     0, 0,";")			//���`�������ߩ`��
 
-	set_chr( 93,990,	 5, 2,     0,   0,  0,		270,  0102, 6,"K0_13051;")	//�ܥ���ȥ� �o�â�
+	set_chr( 93,990,	 5, 2,     0,   0,  0,		270,  0102, 6,"RF2060 K0_13051;")	//�ܥ���ȥ� �o�â�
 	set_obj("@obx0033a", 5, 2,     0,   0,  0,		270)						//�ܥ��`����ɭ�v��
 	set_chr(193,1400,	 5, 2,	   0,   0,  0,		  0,   270, 0,";")			//���`�������ߩ`��
 
+	if( Fx_MUGEN2_OPENED )
+	{
+		set_chr( 94,990,	 5, 1,     0,   0,  0,		  0,  0201, 6,"SF2060 K0_13051;")	//����ȥ� �o��EX��
+		set_obj("@obx0033a", 5, 1,     0,   0,  0,		  0)						//���`����ɭ�v��
+		set_chr(194,1400,	 5, 1,	   0,   0,  0,		  0,     0, 0,";")			//���`�������ߩ`��
+
+//x		set_chr( 60,648,	 5, 1,     0, 450,  0,		 99,     0, 0,";")	//��٥�ץ�`��
+		set_chr( 61,654,	 5, 1,  -275, 450,  0,		  6,   278, 0,";")	//�·���ڣ��o�ޣ�
+		set_chr( 62,654,	 5, 1,  -275, 450,140,		  6,   262, 0,";")	//�·���ڣ��o�ޣ�
+
+		set_obj2("mp30203",   5, 1, -450,-450,  0,	 0) //
+		set_obj2("mp30213",   5, 1,  450,-450,  0,	 0) //
+		set_obj2("mp30463",   5, 1, -450, 450,  0,	 0) //
+		set_obj2("mp30473",   5, 1,  450, 450,  0,	 0) //
+
+		set_obj2("mp30443",   5, 2, -450,-450,  0,	 0) //
+		set_obj2("mp30253",   5, 2,  450,-450,  0,	 0) //
+		set_obj2("mp30223",   5, 2, -450, 450,  0,	 0) //
+		set_obj2("mp30513",   5, 2,  450, 450,  0,	 0) //
+	}
+	else
+	{
+		set_obj("mp30163",    5, 1, -450,-450,  0,	 0) //
+
+		set_obj2("mp30203",   5, 2, -450,-450,  0,	 0) //
+		set_obj2("mp30493",   5, 2,  450,-450,  0,	 0) //
+		set_obj2("mp30223",   5, 2, -450, 450,  0,	 0) //
+		set_obj2("mp30513",   5, 2,  450, 450,  0,	 0) //
+	}
+
 	set_chr( 52,501,	 6, 3,     0,-900,  0,		  7,   180, 6,";")			//���飨ɭ��һͨ
 	if ( !F6_00_GoToMeru )
 	{
@@ -53,6 +104,17 @@ INIT
 		MOT( 52, 6, 0 )
 	}
 
+//	set_chr( 51,501,	 5, 1,     0, 900,  0,		 7,    180, 6,";")			//�飨ɭ�� һͨ
+//	if ( !Fx_MUGEN2_OPENED )
+//	{
+//		set_chr(147,769,	 5, 1,     0, 900,175,		  0,    0, 0,";")	//�o�޷�ӡ
+//		set_chr(148,991,	 5, 1,     0, 900,  0,		  0, 0502, 0,";")	//�o�޷�ӡ������
+//	}
+//	else
+//	{
+//		MOT( 51, 6, 0 )
+//	}
+
 	set_chr( 53,501,	 3, 4,     0,-700,  0,		  3,     0, 6,";")			//���飨ɭ������
 
 //�������å�������
diff --git a/scp_jp_conv/map/3/EV30133.txt b/scp_conv/map/3/EV30133.txt
index 8e1348d..e3e28db 100644
--- a/scp_jp_conv/map/3/EV30133.txt
+++ b/scp_conv/map/3/EV30133.txt
@@ -176,6 +176,7 @@ INIT
 		// �Хܥ�BGM
 		set_chr(160,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"(F113 <EV_BossBGM> WT?90 !F101 !F113 <EV_NormalBGM> WT?90);");
 		set_chr(161,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"!F2100 F101 SF113");	// �ܥ��������Ƥ��ơ��ܥ����L�Фʤ��113�򥻥å�
+		set_chr(164,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"!F2100 F107 SF113");	// �ܥ��������Ƥ��ơ����å��ϕN�g�ߤʤ��113�򥻥å�
 		set_chr(162,990,	 5, 6,   900,-900,  0,		  0,072323, 6,"!F2100 F100 SF113");		// �ܥ��������Ƥ��ơ�����k���Фʤ��113�򥻥å�
 		set_chr(163,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"RF113");				// 103�򥯥ꥢ
 	}
diff --git a/scp_jp_conv/map/3/EV30413.txt b/scp_conv/map/3/EV30413.txt
index 79feb8f..b28b7fb 100644
--- a/scp_jp_conv/map/3/EV30413.txt
+++ b/scp_conv/map/3/EV30413.txt
@@ -142,14 +142,21 @@ INIT
 	set_chr( 70,643,	 6, 5,     0,   0,  0,		  6,     0, 6,";")	//�भ�Τ�a
 		// ���
 		if( !Fx_341Food1 )
-			set_chr( WOODBOX_CH,562,	 6, 5,     0,   0,  0,	  6,    90,20,"<TK_WOODBOX><EV_SetGetFood1>;")// ��ľ��
+		{
+			set_chr( WOODBOX_CH,562,	 6, 5,     0,   0,  0,	  6,    90,20,"<TK_WOODBOX><EV_SetGetFood1> #3_148;")// ��ľ��
+
+		}
 		else
+		{
 			set_chr( WOODBOX_CH,562,	 6, 5,     0,   0,  0,	  7,    90, 0,";")// ��ľ��
-
+		}
 		chr_equip_chr( 49, 70,"csp2", 100,	0,  0, 0,	0, 0, 90);
-		set_chr(148,990, 0, 0,     0,   0,  0,		  0,     0, 8,"(!F104 #3_49 F104 #2_49)")
-		set_chr(149,990, 0, 0,     0,   0,  0,		  0,     0, 9,"RF104 L3?4900 SF104")
 
+		if( !Fx_341Food1 )
+		{
+			set_chr(148,990, 0, 0,     0,   0,  0,		  0,     0, 8,"(!F104 #3_49 F104 #2_49)")
+			set_chr(149,990, 0, 0,     0,   0,  0,		  0,     0, 9,"RF104 L3?4900 SF104")
+		}
 
 //���F���Ϻ���
 	set_chr(110,627,	 6, 8,     0,-900,  0,		  0,     0, 0,";")	// ��С
diff --git a/scp_jp_conv/map/3/EV30433.txt b/scp_conv/map/3/EV30433.txt
index f5d2dcc..e127c98 100644
--- a/scp_jp_conv/map/3/EV30433.txt
+++ b/scp_conv/map/3/EV30433.txt
@@ -281,7 +281,8 @@ INIT
 		}
 		else
 		{
-			set_chr( TREASURE_CH,561,	 6, 3,   100,-175,-100,	   -1,     0, 3,";")	// �ܱ��䣨�ϣ�
+			set_chr( TREASURE_CH,561,	 6, 3,   100,-175,-100,	    7,     0, 3,";")	// �ܱ��䣨�ϣ�
+			color(TREASURE_CH,-1)
 			set_chr(171,990,			 6, 3,   100,-175,   0,	   -1,     0, 3,"#8_99 <EV_Kokohore> WT?30 O1_18 #3_48;");
 		}
 		F_set_chr(TREASURE_CH,CF_NO_CSP)
diff --git a/scp_jp_conv/map/3/EV30513.txt b/scp_conv/map/3/EV30513.txt
index a3ef9bf..f78d3dd 100644
--- a/scp_jp_conv/map/3/EV30513.txt
+++ b/scp_conv/map/3/EV30513.txt
@@ -11,13 +11,13 @@
 #BOSS_CH	75
 #TAKARA_CH	76
 #KIBAKO_CH	79
+#CAMTGT_CH	69
 
 #IT_TAKARA	31		//�������祹�`��
 
 #GF_BOSS10	3209	//Fx_MUGEN_FUU_10B
 #GF_BOSS20	3211	//Fx_MUGEN_FUU_20B
 
-
 //--------------------------------------------------------------------
 INIT
 {
@@ -111,7 +111,8 @@ EV_AppearBoss
 
 		cross_fade(30)
 
-		CAM_move_chr(BOSS_CH,0,0)
+		CAM_move_chr(CAMTGT_CH,0,0)	// camera_dummy
+//		CAM_move_chr(BOSS_CH,0,0)
 		wait_CAM_move()
 
 		wait(60)
@@ -130,6 +131,10 @@ EV_AppearBoss
 
 		MOT(75,80,0)
 
+		if(WK006==1)
+		{
+			MOT(71,80,0)
+		}
 		if(WK004==1)
 		{
 			MOT(77,80,0)
@@ -217,48 +222,93 @@ EV_DefeatBoss
 		//������F
 		if(WK003==1)
 		{
-			F_set(GF_BOSS20)		//�����A�Υܥ�������
-			
-			if(IT_TAKARA<1)
+			if( !Fx_MUGEN_EXTRA )
 			{
-				color(TAKARA_CH,-1)
+				F_set(GF_BOSS20)		//�����A�Υܥ�������
 				
-				chr_pos(TAKARA_CH,10350,10350,0,0,2)
-				
-				CAM_move_chr(TAKARA_CH,45,0)
-				wait_CAM_move()
-
-				SE( 1016, TAKARA_CH)
-
-				EFF_chr(24580, TAKARA_CH, 0, 100, -1, "csp1")
-
-				color(TAKARA_CH,20)
-				wait(20)
-
-				wait(15)
+				if(IT_TAKARA<1)
+				{
+					color(TAKARA_CH,-1)
+					
+					chr_pos(TAKARA_CH,10350,10350,0,0,-1)
+					
+					CAM_move_chr(TAKARA_CH,45,0)
+					wait_CAM_move()
+
+					SE( 1016, TAKARA_CH)
+
+					EFF_chr(24580, TAKARA_CH, 0, 100, -1, "csp1")
+
+					color(TAKARA_CH,20)
+					wait(20)
+
+					wait(15)
+				}
+				else
+				{
+					color(KIBAKO_CH,-1)
+					
+					chr_pos(KIBAKO_CH,10350,10350,0,0,-1)
+					
+					CAM_move_chr(KIBAKO_CH,45,0)
+					wait_CAM_move()
+
+					SE( 1016, KIBAKO_CH)
+
+					EFF_chr(24580, KIBAKO_CH, 0, 100, -1, "CA")
+
+					color(KIBAKO_CH,20)
+					wait(20)
+
+					wait(15)
+				}
 			}
 			else
 			{
-				color(KIBAKO_CH,-1)
-				
-				chr_pos(KIBAKO_CH,10350,10350,0,0,2)
-				
-				CAM_move_chr(KIBAKO_CH,45,0)
-				wait_CAM_move()
-
-				SE( 1016, KIBAKO_CH)
-
-				EFF_chr(24580, KIBAKO_CH, 0, 100, -1, "CA")
-
-				color(KIBAKO_CH,20)
-				wait(20)
-
-				wait(15)
+				if(!Fx_MUGEN2_HUU_BOX)
+				{
+					color(TAKARA_CH,-1)
+					
+					chr_pos(TAKARA_CH,10350,10350,0,0,-1)
+					
+					CAM_move_chr(TAKARA_CH,45,0)
+					wait_CAM_move()
+
+					SE( 1016, TAKARA_CH)
+
+					EFF_chr(24580, TAKARA_CH, 0, 100, -1, "csp1")
+
+					color(TAKARA_CH,20)
+					wait(20)
+
+					wait(15)
+				}
+				else
+				{
+					color(KIBAKO_CH,-1)
+					
+					chr_pos(KIBAKO_CH,10350,10350,0,0,-1)
+					
+					CAM_move_chr(KIBAKO_CH,45,0)
+					wait_CAM_move()
+
+					SE( 1016, KIBAKO_CH)
+
+					EFF_chr(24580, KIBAKO_CH, 0, 100, -1, "CA")
+
+					color(KIBAKO_CH,20)
+					wait(20)
+
+					wait(15)
+				}
 			}
 		}
 		else
 		{
-			F_set(GF_BOSS10)		//�����A�Υܥ�������
+			if( !Fx_MUGEN_EXTRA )
+			{
+				F_set(GF_BOSS10)		//�����A�Υܥ�������
+			}
 		}
 
 		SCORE(-1,-1,-1)		//��������ʾ
@@ -272,6 +322,12 @@ EV_DefeatBoss
 	}
 }
 
+//������������������������������������������������������������
+EV_MM2_BoxOpened
+{
+	F_set( Fx_MUGEN2_HUU_BOX )
+}
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/3/EV31223.txt b/scp_conv/map/3/EV31223.txt
index cdad17c..81e772b 100644
--- a/scp_jp_conv/map/3/EV31223.txt
+++ b/scp_conv/map/3/EV31223.txt
@@ -130,6 +130,7 @@ INIT
 	{
 		set_chr( 66,810,	 7, 4,     0, 750, 15,		  2,     0, 0,";"); //�ڴ�h
 		set_chr(166,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F66 I_$$$2 SF2185;");
+		chr_equip_chr(166,66,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 	set_chr( 67,650,	 7, 4,     0, 750,  0,		  2,     0, 0,";"); //���紲
 
@@ -137,6 +138,7 @@ INIT
 	{
 		set_chr( 68,810,	 3, 3,     0, 900, 15,		  2,     0, 0,";"); //�۳h̨
 		set_chr(168,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F68 I_$$$2 SF2186;");
+		chr_equip_chr(168,68,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 	set_chr( 69,727,	 3, 3,     0, -50,-25,		  0,     0, 0,";")	//���ƄӴ���ɭ��
 	set_chr( 70,650,	 3, 3,     0, 900,  0,		  2,     0, 0,";"); //���紲 ��h
diff --git a/scp_jp_conv/map/3/EV31233.txt b/scp_conv/map/3/EV31233.txt
index 9b953bc..8254a5d 100644
--- a/scp_jp_conv/map/3/EV31233.txt
+++ b/scp_conv/map/3/EV31233.txt
@@ -101,7 +101,8 @@ INIT
 	set_chr(109,622,	 5, 7,     0,   0,  0,		  0,   270, 0,";")	//�ڥ��`������ʹ
 	set_chr( 55,501,	 3, 4,  -900,   0,  0,		  3,    90, 6,";")	//���飨ɭ�� ����
 	set_chr( 56,501,	 5, 6,   900,   0,  0,		  3,   270, 6,";")	//���飨ɭ�� ����
-	set_chr( 57,501,	 4, 5,     0,-900,  0,  	  8,   180, 6,";")	//���飨ɭ�� һͨ �Хܥ���
+	set_chr( 57,501,	 4, 5,     0,-900,  0,  	  7,   180, 0,";")	//���飨ɭ�� һͨ �Хܥ���
+//	set_chr( 57,501,	 4, 5,     0,-900,  0,  	  8,   180, 6,";")	//���飨ɭ�� һͨ �Хܥ���
 
 	set_chr( 60,502,	 9, 7,   600,   0,  0,		  3,   270, 6,";")	//���飨�ң� ����
 
@@ -170,8 +171,6 @@ INIT
 
 
 //���F���Ϻ���
-	set_chr( 65,644,	 3, 5,  -350,-100,  0,		  0,   225, 0,";") //�٥���`��Ů����
-	set_chr( 66,646,	 3, 5,  -150, 250,  0,		  0,   225, 0,";") //�ڥ��Ů����
 
 	set_chr(110,627,	 4, 5,  -400,-900,  0,		  0,     0, 0,";")	// ��Сa1
 	set_chr(111,627,	 4, 5,   400,-900,  0,		  0,     0, 0,";")	// ��Сa2
@@ -207,9 +206,10 @@ INIT
 	}
 
 	// �����ڤ���
+	// EV_SetupAna2�ڤ�2194�򥻥åȤ��Ƥ���
 	if ( !F2194 )
 	{
-		set_chr( 75,642,	10, 7,    0,   0,   0,		  2,     0, 0,"I_$$$2 SF2194 <EV_SetupAna2> E0_5100	;")	//����
+		set_chr( 75,642,	10, 7,    0,   0,   0,		  2,     0, 0,"I_$$$2 <EV_SetupAna2> E0_5100 O0_1024;")	//����
 		color( 99, -1)
 	}
 	else
@@ -224,11 +224,32 @@ INIT
 		set_chr( 74,630,	 5, 3,     0,   0,  0,		  2,   270, 0,"I_$$$1;")	//����
 
 //����
-	set_chr(  1,365,	 4, 5,  -200,-400,  0,		 -2,     0, 0,";") //�ٔ�a �����Ƥ��⤵�⤵
-	chr_equip2( 1,	"ac_0020",	"Bone_Head",	130,		0,0,180,	0,15,85);
+	if ( !F2105 )
+	{
+		set_chr( 82,990,	 0, 0,     0,   0,  0,		  0,     0, 0,"WT?10 C0_57 <EV_AdjPosMegami> WT?20 M4_57 WT?30 C0_0;")// ����
+		set_chr(167,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"L1?6567 L1?6668 SF2105 O1_18 #8_82;")
+
+		set_chr( 65,644,	 3, 5,  -350,-100,  0,		  0,   225, 0,";") //�٥���`��Ů����
+		set_chr( 66,646,	 3, 5,  -150, 250,  0,		  0,   225, 0,";") //�ڥ��Ů����
+
+		set_chr(  1,365,	 4, 5,  -200,-400,  0,		 -2,     0, 0,";") //�ٔ�a �����Ƥ��⤵�⤵
+		set_chr(  2,365,	 4, 5,   200,-400,  0,		 -2,     0, 0,";") //�ٔ�b �����Ƥ��⤵�⤵
+		chr_equip2( 1,	"ac_0020",	"Bone_Head",	130,		0,0,180,	0,15,85);
+		chr_equip2( 2,	"ac_0020",	"Bone_Head",	130,		0,0,180,	0,15,85);
+	}
+	else
+	{
+		MOT( 57, 6, 0)
+
+		set_chr( 65,644,	 4, 5,  -200,-400,  0,		  0,     0, 0,";") //�٥���`��Ů����
+		set_chr( 66,646,	 4, 5,   200,-400,  0,		  0,     0, 0,";") //�ڥ��Ů����
+
+		set_chr(  1,365,	 4, 5,  -200,-200,  0,		 -2,     0, 0,";") //�ٔ�a �����Ƥ��⤵�⤵
+		set_chr(  2,365,	 4, 5,   200,-200,  0,		 -2,     0, 0,";") //�ٔ�b �����Ƥ��⤵�⤵
+		chr_equip2( 1,	"ac_0020",	"Bone_Head",	130,		0,0,180,	0,15,85);
+		chr_equip2( 2,	"ac_0020",	"Bone_Head",	130,		0,0,180,	0,15,85);
+	}
 
-	set_chr(  2,365,	 4, 5,   200,-400,  0,		 -2,     0, 0,";") //�ٔ�b �����Ƥ��⤵�⤵
-	chr_equip2( 2,	"ac_0020",	"Bone_Head",	130,		0,0,180,	0,15,85);
 
 
 	set_chr(  4,303,	 4, 5,  -550, 150,  0,		  2,     0, 0,";") //�ڔ�a �⤵�⤵
@@ -246,15 +267,6 @@ INIT
 
 //�����٥��
 
-	if ( !F2105 )
-	{
-		set_chr( 82,990,	 0, 0,     0,   0,  0,		  0,     0, 0,"WT?10 C0_57 <EV_AdjPosMegami> WT?20 M4_57 WT?30 C0_0;")// ����
-		set_chr(167,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"L1?6567 L1?6668 SF2105 O1_18 #8_82;")
-	}
-	else
-	{
-		MOT( 6, 57, 1)
-	}
 
 //����������O��
 	map_color(100,100,100,0);//R,G,B, time 100%
@@ -277,7 +289,11 @@ EV_SetupAna2
 	delete(105)
 
 	wait(70)
-	SE(18,0)	// �ԥ�ݥ�
+	if ( !F2194 )
+	{
+		SE(18,0)	// �ԥ�ݥ�
+	}
+	F_set(2194)
 	jump( 99,3, 44,-1,-1,0,500)
 	wait(20)
 	color( 99, 30)
diff --git a/scp_jp_conv/map/3/EV32323.txt b/scp_conv/map/3/EV32323.txt
index 1e712cb..a1d33ef 100644
--- a/scp_jp_conv/map/3/EV32323.txt
+++ b/scp_conv/map/3/EV32323.txt
@@ -232,7 +232,7 @@ INIT
 //--------------------------------------------------------------------
 EV_BossItemSpawner
 {
-	set_chr(164,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2 I_FFF2 I_FFF2 I_FFF3;");
+	set_chr(164,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2 I_FFF3 I_FFF3 I_FFF3;");
 	chr_equip_chr(164, 2,"Bone_Spine1", 100,	0,0,0,	0,0,0);
 	F_set_chr(  2, CF_NO_CLIP2)
 }
diff --git a/scp_jp_conv/map/3/EV32393.txt b/scp_conv/map/3/EV32393.txt
index b60d2a3..5a741d5 100644
--- a/scp_jp_conv/map/3/EV32393.txt
+++ b/scp_conv/map/3/EV32393.txt
@@ -56,7 +56,7 @@ INIT
 //�������å�������
 	set_chr( 50,620,	 2, 7,  -350,   0,  0,		  0,   270, 0,";")			//�٥��`��OBJ
 
-	set_chr( 56,648,	 4, 4,     0,-450,  0,		 11,     0, 0,";")	//�ڥ�٥�ץ�`��
+	set_chr( 56,772,	 4, 4,     0,-450,  0,		 11,     0, 0,";")	//�ڥ�٥�ץ�`��
 	color2(56, 85,80,100, 0,0,0)
 	set_chr( 54,657,	 4, 6,  -425,-230,  0,		  0,     0, 0,";")	//�ۥϥƥʿ���
 
diff --git a/scp_jp_conv/map/3/MC30103.bmp b/scp_conv/map/3/MC30103.bmp
index e99a8d5..847a8a1 100644
Binary files a/scp_jp_conv/map/3/MC30103.bmp and b/scp_conv/map/3/MC30103.bmp differ
