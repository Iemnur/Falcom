diff --git a/scp_jp_conv/map/0/EV00120.txt b/scp_conv/map/0/EV00120.txt
index a5df571..64a3fa7 100644
--- a/scp_jp_conv/map/0/EV00120.txt
+++ b/scp_conv/map/0/EV00120.txt
@@ -216,8 +216,9 @@ INIT
 		{
 		//	set_chr( MEI,49,		-1,-1,	763,-290,0,		52,90,20,"<TK_MEI>")		//�޾ƈ����ڥ󥮥��ǰ���ᥤ
 			set_chr( MEI,49,	-1,-1,  800,-850,1,  	50,30, 20,"<TK_MEI>")			//�޾ƈ��������󥿩`���ᥤ
-			set_chr( PENGUIN,81,	-1,-1,	734,-542,0,		2,190,20,"<TK_PENGUIN>")	//�����z�ߥڥ󥮥�
-			
+//			set_chr( PENGUIN,81,	-1,-1,	734,-542,0,		2,190,20,"<TK_PENGUIN>")	//�����z�ߥڥ󥮥�
+			set_chr( PENGUIN,81,	-1,-1,	840,-542,0,		2,190,20,"<TK_PENGUIN>")	//�����z�ߥڥ󥮥�	//�ѥå� 2008/09/22
+
 			//��`�����
 			MOT_SET(MEI,150,-1,476,476,-1,15)		//�ᥤ
 			MOT(MEI,150,0)
@@ -237,7 +238,8 @@ INIT
 		//��`�����
 		MOT_SET(SHESTOR,150,-1,260,319,-1,0)	//���������`����M
 		MOT(SHESTOR,150,0)
-		MOT_SET(CEPHEILA,150,-1,560,560,-1,0)	//���ե��`�顡�٥åɤ�����
+	//	MOT_SET(CEPHEILA,150,-1,560,560,-1,0)	//���ե��`�顡�٥åɤ�����
+		MOT_SET(CEPHEILA,150,-1,554,554,-1,0)	//���ե��`�顡�٥åɤ�����0922��`�������
 		MOT(CEPHEILA,150,0)
 		MOT_SET(TEO,150,-1,577,577,-1,0)		//�ƥ�������
 		MOT(TEO,150,0)
@@ -613,7 +615,7 @@ ROOT_MOVE_MEI
 MOVE_MEI
 {
 //	һ��Ŀ�ΥƩ`�֥��
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1,	257,-1152,0, 0)
 	wait_move( MEI )
 //	rot(MEI,60,72)
@@ -622,21 +624,21 @@ MOVE_MEI
 	
 //	rot(MEI,60,351)
 
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, 327,-1012,1,	0)
 	wait_move( MEI )
 	
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, 271,-948,0,	0)
 	wait_move( MEI )
 //	rot(MEI,60,90)
 	
 //	2��Ŀ�ΥƩ`�֥��
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -398,-1015,0,	0)
 	wait_move( MEI )
 //	rot(MEI,60,353)
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -492,-941,1,	0)
 	wait_move( MEI )
 
@@ -644,11 +646,11 @@ MOVE_MEI
 
 //	3��Ŀ�ΥƩ`�֥��
 //	rot(MEI,60,146)
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -598,-1180,1,	0)	
 	wait_move( MEI )
 //	rot(MEI,60,97)
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -756,-1175,0,	0)
 	wait_move( MEI )
 
@@ -656,14 +658,14 @@ MOVE_MEI
 
 //	����λ�ä�
 //	rot(MEI,60,247)							
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -405,-1209,1,	0)
 	wait_move( MEI )
 //	rot(MEI,60,239)							
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -181,-1431,1,	0)
 	wait_move( MEI )
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, 298,-1505,1,		0)
 	wait_move( MEI )
 //	rot(MEI,60,351)
diff --git a/scp_jp_conv/map/0/EV00145.txt b/scp_conv/map/0/EV00145.txt
index e88a230..399301a 100644
--- a/scp_jp_conv/map/0/EV00145.txt
+++ b/scp_conv/map/0/EV00145.txt
@@ -102,46 +102,46 @@ INIT
 
 
 	//�ƥ���Τ����`��
-	set_chr(300, 716, 	2,4,	0,40,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(301, 716, 	2,4,	-340,-330,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(302, 716, 	2,4,	340,-330,0,		0,	270,0,";")	//�����^��`��		obx0500
-	set_chr(303, 716, 	2,4,	-250,-70,0,		0,	45,	0,";")	//�����^��`��		obx0500
-	set_chr(304, 716, 	2,4,	250,-70,0,		0,	315,0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,4,	0,40,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,4,	-340,-330,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,4,	340,-330,0,		0,	270,0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,4,	-250,-70,0,		0,	45,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,4,	250,-70,0,		0,	315,0,";")	//�����^��`��		obx0500
 
 	//���ƥ������`��
-	set_chr(305, 716, 	3,2,	0,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(306, 716, 	3,2,	350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(307, 716, 	3,2,	-350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,2,	0,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,2,	350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,2,	-350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
 
 	//�ȥꥱ������`��
-	set_chr(308, 716, 	1,2,	0,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(309, 716, 	1,2,	350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(310, 716, 	1,2,	-350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,2,	0,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,2,	350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,2,	-350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
   
   	//���L�o�����`��
-	set_chr(311, 716, 	2,2,	0,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(312, 716, 	2,2,	350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
-	set_chr(313, 716, 	2,2,	-350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,2,	0,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,2,	350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	2,2,	-350,110,0,			0,	0,	0,";")	//�����^��`��		obx0500
                               
 	//���`�饫�󥹡����Υޥ��ꥹ�����`��
-	set_chr(370, 716, 	3,3,	-30,-30,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(371, 716, 	3,3,	-30,320,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(372, 716, 	3,3,	-30,640,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(373, 716, 	3,3,	-30,960,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(374, 716, 	3,3,	-30,1280,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(375, 716, 	3,3,	-30,1600,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(376, 716, 	3,3,	-30,1920,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(377, 716, 	3,3,	100,-200,0,	0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,-30,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,320,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,640,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,960,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,1280,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,1600,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	-30,1920,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	3,3,	100,-200,0,	0,	0,	0,";")	//�����^��`��		obx0500
 	
 	//���`�ɥ饴�󡫥��奴������`��
-	set_chr(378, 716, 	1,3,	30,-30,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(379, 716, 	1,3,	30,320,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(380, 716, 	1,3,	30,640,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(381, 716, 	1,3,	30,960,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(382, 716, 	1,3,	30,1280,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(383, 716, 	1,3,	30,1600,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(384, 716, 	1,3,	30,1920,0,	0,	90,	0,";")	//�����^��`��		obx0500
-	set_chr(385, 716, 	1,3,	-100,-200,0,	0,	0,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,-30,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,320,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,640,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,960,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,1280,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,1600,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	30,1920,0,	0,	90,	0,";")	//�����^��`��		obx0500
+	set_chr(36, 716, 	1,3,	-100,-200,0,	0,	0,	0,";")	//�����^��`��		obx0500
 	
 	
 	                            
@@ -160,13 +160,13 @@ INIT
 //�Ω`������
 	//---------------------------���L---------------------------------
 	workL(5,SET,0)//��ٛ״�r
-	if(F2325)
+	if(F2425)
 		workL(5,ADD,1)
-	if(F2326)
+	if(F2426)
 		workL(5,ADD,1)
-	if(F2327)
+	if(F2427)
 		workL(5,ADD,1)
-	if(F2328)
+	if(F2428)
 		workL(5,ADD,1)
 
 	if(WK005<4)
@@ -189,13 +189,13 @@ INIT
 	}
 	//---------------------------�ƥ����---------------------------------
 	workL(5,SET,0)//��ٛ״�r
-	if(F2329)
+	if(F2429)
 		workL(5,ADD,1)
-	if(F2330)
+	if(F2430)
 		workL(5,ADD,1)
-	if(F2331)
+	if(F2431)
 		workL(5,ADD,1)
-	if(F2332)
+	if(F2432)
 		workL(5,ADD,1)
 
 	if(WK005<4)
@@ -218,13 +218,13 @@ INIT
 	}
 	//---------------------------���ƥ�---------------------------------
 	workL(5,SET,0)//��ٛ״�r
-	if(F2333)
+	if(F2433)
 		workL(5,ADD,1)
-	if(F2334)
+	if(F2434)
 		workL(5,ADD,1)
-	if(F2335)
+	if(F2435)
 		workL(5,ADD,1)
-	if(F2336)
+	if(F2436)
 		workL(5,ADD,1)
 
 	if(WK005<4)
@@ -247,13 +247,13 @@ INIT
 	}
 	//---------------------------�ȥꥱ��---------------------------------
 	workL(5,SET,0)//��ٛ״�r
-	if(F2337)
+	if(F2437)
 		workL(5,ADD,1)
-	if(F2338)
+	if(F2438)
 		workL(5,ADD,1)
-	if(F2339)
+	if(F2439)
 		workL(5,ADD,1)
-	if(F2340)
+	if(F2440)
 		workL(5,ADD,1)
 
 	if(WK005<4)
diff --git a/scp_jp_conv/map/0/EV00146.txt b/scp_conv/map/0/EV00146.txt
index a3f825a..2be209d 100644
--- a/scp_jp_conv/map/0/EV00146.txt
+++ b/scp_conv/map/0/EV00146.txt
@@ -313,7 +313,7 @@ INIT
 		F_set(NAZO)
 		
 		//�����å�Ҋ�Ϥ��������F
-		set_chr( 291,990,	3,2,     0, -200,  0,    0,   0,8,"(L7?99 <CAM_NAZO> WT?30 L7!99 <CAM_RESET>);")
+		set_chr( 81,990,	3,2,     0, -200,  0,    0,   0,8,"(L7?99 <CAM_NAZO> WT?30 L7!99 <CAM_RESET>);")
 		set_chr( 170,991,	3,2,     0, -80,  0,    0,0506,0,";")//������
 		set_chr( 170,991,	3,2,     0,    0,  0,    0,0603,0,";")//����������
 		set_chr( 170,991,	3,2,     0,   80,  0,    0,0303,0,";")//��������ǰ
@@ -322,13 +322,13 @@ INIT
 
 	//---------------------------��ܢ�---------------------------------
 	workL(6,SET,0)//��ٛ״�r
-	if(F2341)
+	if(F2441)
 		workL(6,ADD,1)
-	if(F2342)
+	if(F2442)
 		workL(6,ADD,1)
-	if(F2343)
+	if(F2443)
 		workL(6,ADD,1)
-	if(F2344)
+	if(F2444)
 		workL(6,ADD,1)
 
 	if(WK006<4)
@@ -350,7 +350,7 @@ INIT
 
 	if(WK006==4)
 	{	//���Ҋ�Ϥ��������F
-		set_chr( 292,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
+		set_chr( 82,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
 
 	}
 //	if(WK006==4)
@@ -364,13 +364,13 @@ INIT
 //	}
 	//---------------------------��ܢ�---------------------------------
 	workL(7,SET,0)//��ٛ״�r
-	if(F2345)
+	if(F2445)
 		workL(7,ADD,1)
-	if(F2346)
+	if(F2446)
 		workL(7,ADD,1)
-	if(F2347)
+	if(F2447)
 		workL(7,ADD,1)
-	if(F2348)
+	if(F2448)
 		workL(7,ADD,1)
 
 	if(WK007<4)
@@ -391,7 +391,7 @@ INIT
 	}
 	if(WK007==4)
 	{	//���Ҋ�Ϥ��������F
-		set_chr( 293,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
+		set_chr( 83,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
 	}
 //	else
 //	{
@@ -703,7 +703,7 @@ LP_ROBO1
 	if(WK006==4)
 	{
 //		MES(ROBO1_TXT,"C4W9����ץƥ󣲣��š��ã��������21��\n�D�D�إ����F��\n����Ϥɤ��ޤǤ⸶�����Ф�����\n�����Υ�äݤ��h����ļ���С�\n�ߤ�������֎���ľ�ʤɣ�",0)
-		MES(ROBO1_TXT,"C4W9����ץƥ󣲣��š��ã��������21��\n��ä���ɡ��Ť������֥ꥭ�Τ�����㡣\n�ڄӲ����٤ʤ����������ζ�����롣",0)
+		MES(ROBO1_TXT,"C4W9����ץƥ󣲣��š��ã��������21��\n��ä���ɡ��Ť������֥ꥭ�Τ�����㡣\n�ɄӲ����٤ʤ����������ζ�����롣",0)
 		MES(ROBO1_TXT,"C4W9�����䤡��������ϥ���ץƥ󣲣��ţ�\n늳ؤξA���ޤ�ɤ��ޤǤⲽ���裡\nС�������Ә����֤ν줫�ʤ��Ȥ���˱��ܤ��Ƥͣ�",0)
 		MES_close(ROBO1_TXT)
 		wait_MES(ROBO1_TXT)
@@ -717,7 +717,7 @@ LP_ROBO1
 	//	if(!FT_FF_TalkROBO1)
 		if(!FT_FF_TalkROBO1 && !F6_05_EndSixth)		//���ԥ�`���Ǥϰk�����ʤ�
 		{
-			delete(292)
+			delete(82)
 			wait(2)
 
 			cross_fade(20)
@@ -908,7 +908,7 @@ LP_ROBO1
 			F_set(FT_FF_TalkROBO1)
 
 			look_del(RAGNA)
-			set_chr( 292,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
+			set_chr( 82,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
 
 			fade_in(0,30,BLACK)
 			wait_fade()
@@ -1052,7 +1052,7 @@ LP_ROBO2
 	//	if(!FT_FF_TalkROBO2)
 		if(!FT_FF_TalkROBO2 && !F6_05_EndSixth)		//���ԥ�`���Ǥϰk�����ʤ�
 		{
-			delete(293)
+			delete(83)
 			wait(2)
 
 			cross_fade(20)
@@ -1190,7 +1190,7 @@ LP_ROBO2
 
 		//	name("�ե쥤��Х����`")
 			MES(ROBO2,"W9L711���ߤȤ��������x��ȭ��\nL711���x��ȭ�Ȥ����Х��åѩ`�ܥ����",0)
-			MES(ROBO2,"W9L711����ȭ��֤ä�\nL711�������x��؞���Ƥߤ��뤬����������",0)
+			MES(ROBO2,"W9L711����ȭ���ä�\nL711�������x��؞���Ƥߤ��뤬����������",0)
 			MES_close(ROBO2)
 
 
@@ -1202,7 +1202,7 @@ LP_ROBO2
 			F_set(FT_FF_TalkROBO2)
 
 			look_del(RAGNA)
-			set_chr( 293,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
+			set_chr( 83,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
 
 			fade_in(0,30,BLACK)
 			wait_fade()
diff --git a/scp_jp_conv/map/0/EV00301.txt b/scp_conv/map/0/EV00301.txt
index 7aff059..a0cebb8 100644
--- a/scp_jp_conv/map/0/EV00301.txt
+++ b/scp_conv/map/0/EV00301.txt
@@ -816,7 +816,9 @@ EV_3_01_MonsterVillage
 		get_item(003,-1,1)		// ����(���饤�ɥ���)
 	if(IT004>0)					// �֤äƤ�����
 		get_item(004,-1,1)		// ����(�֥�`�ɥ���)
-
+	if(IT005>0)					// �֤äƤ�����
+		get_item(005,-1,1)		// ����(�ޥå��륮��)
+		
 	wait(10)
 	SE(043,PLAYER1)
 //	MES(RAGNA,"C3S2�եå�������װ�䤷�ޤ�����\n���ˤ������ᤫ��եå������ǲ��ޤ���\n���륦�����Ԫ���\��Ǥ���������",2)
@@ -896,7 +898,9 @@ EV_3_01_MonsterOnly
 		get_item(003,-1,1)		// ����(���饤�ɥ���)
 	if(IT004>0)					// �֤äƤ�����
 		get_item(004,-1,1)		// ����(�֥�`�ɥ���)
-
+	if(IT005>0)					// �֤äƤ�����
+		get_item(005,-1,1)		// ����(�ޥå��륮��)
+		
 	set_chr(ALWEN,	1011,-1,-1, 1,1,1, 2,0,8, "<EV_JYOUKA>")
 	set_chr(LUE,	 1015,-1,-1, 1,1,1, 2,0,0, "")
 	set_chr(ZONBI_A,	384,-1,-1, 1,1,1, 2,0,9, "RF200 Z1?06 L4?12 SF200")
@@ -1069,7 +1073,9 @@ EV_3_02_DEBUG
 		get_item(003,-1,1)		// ����(���饤�ɥ���)
 	if(IT004>0)					// �֤äƤ�����
 		get_item(004,-1,1)		// ����(�֥�`�ɥ���)
-
+	if(IT005>0)					// �֤äƤ�����
+		get_item(005,-1,1)		// ����(�ޥå��륮��)
+		
 	set_chr(ALWEN,	1011,-1,-1, 1,1,1, 2,0,0, "")
 	set_chr(LUE,	 1015,-1,-1, 1,1,1, 2,0,0, "")
 	set_chr(ZONBI_A,	384,-1,-1, 1,1,1, 2,0,0, "")
@@ -1220,7 +1226,9 @@ EV_3_02_GoMoonCastle
 		get_item(003,1,1)		// ��������(���饤�ɥ���)
 	if(IT004==0)
 		get_item(004,1,1)		// ��������(�֥�`�ɥ���)
-
+	if(IT005==0)
+		get_item(005,1,1)		// ��������(�ޥå��륮��)
+		
 	set_chr(EVENT_RAGNA,	  1010,-1,-1, 180,3560,-22, 2,195,0, "")
 	chr_pos(ALWEN,	530,3920,-22,10,2)
 	chr_pos(LUE, 	690,3850,-22,70,2)
diff --git a/scp_jp_conv/map/0/EV00400.txt b/scp_conv/map/0/EV00400.txt
index 47ebe8d..44e370e 100644
--- a/scp_jp_conv/map/0/EV00400.txt
+++ b/scp_conv/map/0/EV00400.txt
@@ -299,7 +299,7 @@ INIT
 		set_chr( NINJYA_F,490,-1,-1, -157,-3460,1,	2,34, 20,"<TK_NINJYA_F>")		//�ǽ����������ΰ��ǵ���Ƥ��롡���ߣ�
 
 		
-		set_chr( 97,990,	-1,-1,  -359,-13227,1476,	   0,  0505, 6,"<EV_STOP_KARASU>")	//���ȥåѩ`��������
+		set_chr( 81,990,	-1,-1,  -359,-13227,1476,	   0,  0505, 6,"<EV_STOP_KARASU>")	//���ȥåѩ`��������
 
 		if(!FS_10_TalkKarasu)
 		{
@@ -355,7 +355,7 @@ INIT
 		F_set_chr(NINJYA_H_2,CF_NO_MOVE)
 		F_set_chr(NINJYA_H_3,CF_NO_MOVE)
 		F_set_chr(NINJYA_H_4,CF_NO_MOVE)
-		F_set_chr(KARASU,CF_NO_MOVE)
+	//	F_set_chr(KARASU,CF_NO_MOVE)	//0924�����Ȼ�
 	}
 	else
 	//������������������������������������������������������������
@@ -417,7 +417,8 @@ INIT
 		//�������ᡡ����4��Ŀ���F
 		if(FS_08_TalkLuri)
 		{
-			set_chr( LURI_4,77,		-1,-1,	7495,-9945,1399,	2,0, 20,"<TK_LURI_4>")					//�ǽ��������R�ɤ��������������4
+//			set_chr( LURI_4,77,		-1,-1,	7495,-9945,1399,	2,0, 20,"<TK_LURI_4>")					//�ǽ��������R�ɤ��������������4
+			set_chr( LURI_4,77,		-1,-1,	6530,-10404,1660,	2,0, 20,"<TK_LURI_4>")					//�ǽ������Ҥ��ϡ�������4���ѥå� 2008/09/22
 			MOT_SET(LURI_4,150,-1,552,552,-1,-1)
 			MOT(LURI_4,150,0)
 			EV("ROLING_LURI")
@@ -442,9 +443,9 @@ INIT
 		//��Υ�����һͨ��Ԓ���ȥ��٥�ȥ���ȥ�`�����F
 		if(F4_12_OkRoten && !F4_15_EndSatolook)
 		{
-			set_chr( 300,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//�A����
-			set_chr( 301,990,	-1,-1,   658,-10864,1400,	   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//�A����
-			set_chr( 302,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//�����
+			set_chr( 82,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//�A����
+			set_chr( 83,990,	-1,-1,   658,-10864,1400,	   2,083404, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//�A����
+			set_chr( 84,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//�����
 		}
 		
 		//��Υ�����һͨ��Ԓ���ȥ��饵��������
@@ -713,9 +714,9 @@ EV_F4_12_OkRoten
 	//�ҥ���Τ߄e�ޥåפʤΤ����z��Ǥ��ޤ���
 	if(FS_08_TalkHikome && FS_08_TalkKarasu && FS_08_TalkDaigoro && FS_08_TalkYasaku && FS_08_TalkKai && FS_08_TalkAkane && FS_08_TalkLuri && FS_08_TalkGen)
 	{
-		set_chr( 300,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//�A����
-		set_chr( 301,990,	-1,-1,   658,-10864,1400,	   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//�A����
-		set_chr( 302,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//�����
+		set_chr( 82,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//�A����
+		set_chr( 83,990,	-1,-1,   658,-10864,1400,	   2,083404, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//�A����
+		set_chr( 84,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//�����
 
 		F_set(F4_12_OkRoten)
 	
@@ -927,9 +928,9 @@ EV_4_15_EndSatolook
 		F_set(F4_15_EndSatolook)
 		
 		//����ȥ��3�ص㤫������
-		delete(300)
-		delete(301)
-		delete(302)
+		delete(82)
+		delete(83)
+		delete(84)
 
 		EV_end()
 		
diff --git a/scp_jp_conv/map/0/EV00401.txt b/scp_conv/map/0/EV00401.txt
index f685134..7ad6ea8 100644
--- a/scp_jp_conv/map/0/EV00401.txt
+++ b/scp_conv/map/0/EV00401.txt
@@ -354,7 +354,7 @@ INIT
 		{
 			//��ħ���Ⱥ��ˇ�ޤ�롫���륦����ǈ�
 			//								                 z x y
-			set_chr( 80,990,	-1,-1,   1075,-8300,-100,  0, 140802,6,"<EV_4_12_JoinAlwen>;")
+			set_chr( 80,990,	-1,-1,   1075,-8300,-100,  0, 201202,6,"<EV_4_12_JoinAlwen>;")		//�ѥå� 2008/09/22 �����ڤ���
 		}
 	}
 }
@@ -824,7 +824,8 @@ EV_4_10_AreYouSubaru3
 	F_set(F4_06_StopAttack)
 	
 	//��饰�ʡ�����ǰ��
-	F_set_note(RAGNA,2)
+	F_set_note(PLAYER1,2)				//�ѥå����� 20081010
+
 	//�凉�Х롾�g��Ů���ӡ�
 	F_set_note(-20,2)
 
diff --git a/scp_jp_conv/map/0/EV00431.txt b/scp_conv/map/0/EV00431.txt
index d261e99..6fb2cb1 100644
--- a/scp_jp_conv/map/0/EV00431.txt
+++ b/scp_conv/map/0/EV00431.txt
@@ -93,11 +93,13 @@ INIT
 
 		if( GW_ENTRY_EVENT==0 )
 		{
-			set_chr(EFFDUMMY1,749,	-1,-1,  -927,97,-49,55,0, 0,"")		//��ηۣ�
+			set_chr(EFFDUMMY1,749,	-1,-1,    680,0,0,55,0, 0,"")		//��ηۣ�	//�ѥå����� 2008/09/22
 			F_set_chr(EFFDUMMY1,CF_NO_CSP)
+			F_set_chr(EFFDUMMY1,CF_NO_HEIGHT)
+			F_set_chr(EFFDUMMY1,CF_NO_ZIMEN)
 			map_color(80,60,60,0);//R,G,B, time 100%
 		}
-		
+
 		//��`�����
 		MOT_SET(NINJYA_A, 150, -1, 523,523,-1,-1)	//����
 		MOT_SET(NINJYA_C, 150, -1, 523,523,-1,-1)	//����
@@ -690,8 +692,10 @@ EV_4_11_Save
 	//--- �ǥե���ȱ��� --------------------------------------------------
 	KAO(EVENT_RAGNA, "1","3","1")
 
-	set_chr(EFFDUMMY1,749,	-1,-1,  -927,97,-49,55,0, 0,"")		//��ηۣ�
-	F_set_chr(EFFDUMMY1,CF_NO_CSP)	
+	set_chr(EFFDUMMY1,749,	-1,-1,    680,0,0,55,0, 0,"")		//��ηۣ�	//�ѥå����� 2008/09/22
+	F_set_chr(EFFDUMMY1,CF_NO_CSP)
+	F_set_chr(EFFDUMMY1,CF_NO_HEIGHT)
+	F_set_chr(EFFDUMMY1,CF_NO_ZIMEN)
 	map_color(80,60,60,0);//R,G,B, time 100%
 
 	look(EVENT_RAGNA, "Bone_Head", 0,2,2,2, 0,0,-20)	
diff --git a/scp_jp_conv/map/0/EV00440.txt b/scp_conv/map/0/EV00440.txt
index ea40e01..235f2e2 100644
--- a/scp_jp_conv/map/0/EV00440.txt
+++ b/scp_conv/map/0/EV00440.txt
@@ -478,6 +478,8 @@ EV_4_09_WithSubaru
 	delete(SUBARU)
 	delete(EVENT_RAGNA)
 
+	F_set(F4_17_InTheEvening)		////��Ϧ���ˤʤä� �ѥå���2008/09/22 Ϧ���ե饰���Ƥ�
+
 //¶���L�Τ�
 	workG(GW_ENTRY_EVENT,SET,1)
 	new_map(10451)
diff --git a/scp_jp_conv/map/0/EV00480.txt b/scp_conv/map/0/EV00480.txt
index f03385a..2f4ce14 100644
--- a/scp_jp_conv/map/0/EV00480.txt
+++ b/scp_conv/map/0/EV00480.txt
@@ -169,7 +169,7 @@ LP_MON
 		if(GW_MAN==1)
 		{
 		//�������饰�����^
-			MES(RAGNA,"���ä������ʤ��ߤ�������\n�ޡ��¤�����Ƥʤ��ͤ����ʡ�",0)
+			MES(RAGNA,"���ä������ʤ��ߤ�������\n�ޡ��¤�����Ƥ����ͤ����ʡ�",0)
 			MES_close(RAGNA)
 		}
 		else
diff --git a/scp_jp_conv/map/0/EV00490.txt b/scp_conv/map/0/EV00490.txt
index 9cc452a..ac53a63 100644
--- a/scp_jp_conv/map/0/EV00490.txt
+++ b/scp_conv/map/0/EV00490.txt
@@ -97,6 +97,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,76)	//�����Х�`��
 		workL(WK_ROUTETIME_STOP,SET,1)	// ������Ӌ�yֹͣ
 
+		if(GW_SKI_COUNT1<255)
+		{
+			workG(GW_SKI_COUNT1,ADD,1)	//�ץ쥤����
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////�ȣ�0�Ǥ������ʤ��������0�������r��"EV_DEAD"������
 		//��`�׷⤸
 		workG(GW_WARP_FLAG,SET,0)//��`�׷⤸�롣
@@ -249,39 +254,155 @@ EV_GOAL
 //	move(PLAYER1,0,RUN2,138,63079,-1002,0)//	typ[0=����ָ�� 1=�����X��λ��+Z 2=�Է�����λ�� 3=�Է�λ�ã�xyz��-1�����ֱλ�á�5=�ե��� 99=��`�ֽ��]   Len=���_������x type��20���Ϥ��Ԅӷ����Q type��30���Ϥ��Ԅӥ�`������Ф��椨�ʤ�
 	CAM_Type(1)
 
-	if(GW_NOW_BREAK==28 && GW_NOW_DAM==0 && SP003<3600)
-	{
-		//�_�ɤǤ�����֥��
-		workG(GW_ENTRY_EVENT,SET,1)	//�֥��
-	}
-	else
-	if(SP003>3600)		//60��=60*60sec
-	{
-		//�r�g���`�Щ`
-		workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
-	}
-	else
-	if(GW_NOW_DAM!=0)
+	if(GW_SKI_DOWN==3)		// �y�׶ȥ�����
 	{
-		//����`��
-		workG(GW_ENTRY_EVENT,SET,9)	//9=�����`ʧ��(����`��)
+		if(GW_NOW_BREAK>=12 && GW_NOW_DAM<=5 && SP003<4800)
+		{
+			//�_�ɤǤ�����֥��
+			workG(GW_ENTRY_EVENT,SET,1)		//�֥��
+		}
+		else
+		if(SP003>4800)						//80��=80*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>5)					//����`��5 ��
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<9)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
+	if(GW_SKI_DOWN==2)		// �y�׶ȥ�����
 	{
-		//�������ʤ�������
-		workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		if(GW_NOW_BREAK>=20 && GW_NOW_DAM<=3 && SP003<4200)
+		{
+			//�_�ɤǤ�����֥��
+			workG(GW_ENTRY_EVENT,SET,1)		//�֥��
+		}
+		else
+		if(SP003>4200)						//70��=70*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>3)					//����`��3��
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<17)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<25)
+	if(GW_SKI_DOWN==1)		// �y�׶ȥ�����
 	{
-		//�������ʤ������ʤ�
-		workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		if(GW_NOW_BREAK>=24 && GW_NOW_DAM<=1 && SP003<3900)
+		{
+			//�_�ɤǤ�����֥��
+			workG(GW_ENTRY_EVENT,SET,1)		//�֥��
+		}
+		else
+		if(SP003>3900)						//65��=65*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>1)					//����`��1��
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<21)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
 	{
-		//�������ʤ���������
-		workG(GW_ENTRY_EVENT,SET,8)	//8=�����`ʧ��(�ĥܡ�������)
+		if(GW_NOW_BREAK==28 && GW_NOW_DAM==0 && SP003<3600)
+		{
+			//�_�ɤǤ�����֥��
+			workG(GW_ENTRY_EVENT,SET,1)		//�֥��
+		}
+		else
+		if(SP003>3600)						//60��=60*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM!=0)					//����`������
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<25)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 
 	//��ܞ
diff --git a/scp_jp_conv/map/0/EV00491.txt b/scp_conv/map/0/EV00491.txt
index b5898ca..8e1238c 100644
--- a/scp_jp_conv/map/0/EV00491.txt
+++ b/scp_conv/map/0/EV00491.txt
@@ -115,6 +115,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,77)	//�����Х�`��
 		workL(WK_ROUTETIME_STOP,SET,1)	// ������Ӌ�yֹͣ
 
+		if(GW_SKI_COUNT2<255)
+		{
+			workG(GW_SKI_COUNT2,ADD,1)	//�ץ쥤����
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////�ȣ�0�Ǥ������ʤ��������0�������r��"EV_DEAD"������
 		//��`�׷⤸
 		workG(GW_WARP_FLAG,SET,0)//��`�׷⤸�롣
@@ -261,39 +266,155 @@ EV_GOAL
 	SE(24,0)
 	CAM_Type(1)
 
-	if(GW_NOW_BREAK==36 && GW_NOW_DAM==0 && SP003<2700)		//45��=45*60sec
-	{
-		//�_�ɤǤ����饷��Щ`
-		workG(GW_ENTRY_EVENT,SET,2)	//����Щ`
-	}
-	else
-	if(SP003>2700)		//45��=45*60sec
-	{
-		//�r�g���`�Щ`
-		workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
-	}
-	else
-	if(GW_NOW_DAM!=0)
+	if(GW_SKI_DOWN==3)		// �y�׶ȥ�����
 	{
-		//����`��
-		workG(GW_ENTRY_EVENT,SET,9)	//9=�����`ʧ��(����`��)
+		if(GW_NOW_BREAK>=16 && GW_NOW_DAM<=5 && SP003<3900)		//65��=65*60sec
+		{
+			//�_�ɤǤ����饷��Щ`
+			workG(GW_ENTRY_EVENT,SET,2)		//����Щ`
+		}
+		else
+		if(SP003>3900)						//65��=65*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>5)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<12)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
+	if(GW_SKI_DOWN==2)		// �y�׶ȥ�����
 	{
-		//�������ʤ�������
-		workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		if(GW_NOW_BREAK>=26 && GW_NOW_DAM<=3 && SP003<3300)		//55��=55*60sec
+		{
+			//�_�ɤǤ����饷��Щ`
+			workG(GW_ENTRY_EVENT,SET,2)		//����Щ`
+		}
+		else
+		if(SP003>3300)						//55��=55*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>3)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<22)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<32)
+	if(GW_SKI_DOWN==1)		// �y�׶ȥ�����
 	{
-		//�������ʤ������ʤ�
-		workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		if(GW_NOW_BREAK>=31 && GW_NOW_DAM<=1 && SP003<3000)		//50��=50*60sec
+		{
+			//�_�ɤǤ����饷��Щ`
+			workG(GW_ENTRY_EVENT,SET,2)		//����Щ`
+		}
+		else
+		if(SP003>3000)						//50��=50*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>1)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<27)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
 	{
-		//�������ʤ���������
-		workG(GW_ENTRY_EVENT,SET,8)	//8=�����`ʧ��(�ĥܡ�������)
+		if(GW_NOW_BREAK==36 && GW_NOW_DAM==0 && SP003<2700)		//45��=45*60sec
+		{
+			//�_�ɤǤ����饷��Щ`
+			workG(GW_ENTRY_EVENT,SET,2)		//����Щ`
+		}
+		else
+		if(SP003>2700)						//45��=45*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM!=0)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<32)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 
 	//��ܞ
diff --git a/scp_jp_conv/map/0/EV00492.txt b/scp_conv/map/0/EV00492.txt
index 92c3133..e031221 100644
--- a/scp_jp_conv/map/0/EV00492.txt
+++ b/scp_conv/map/0/EV00492.txt
@@ -156,6 +156,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,78)	//�����Х�`��
 		workL(WK_ROUTETIME_STOP,SET,1)	// ������Ӌ�yֹͣ
 
+		if(GW_SKI_COUNT3<255)
+		{
+			workG(GW_SKI_COUNT3,ADD,1)	//�ץ쥤����
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////�ȣ�0�Ǥ������ʤ��������0�������r��"EV_DEAD"������
 		//��`�׷⤸
 		workG(GW_WARP_FLAG,SET,0)//��`�׷⤸�롣
@@ -303,41 +308,159 @@ EV_GOAL
 	SE(24,0)
 	CAM_Type(1)
 
-	if(GW_NOW_BREAK==21 && GW_NOW_DAM==0 && SP003<3600)
+	if(GW_SKI_DOWN==3)		// �y�׶ȥ�����
 	{
-		//�_�ɤǤ����饴�`���
-		workG(GW_ENTRY_EVENT,SET,3)	//���`���
+		if(GW_NOW_BREAK>=5 && GW_NOW_DAM<=5 && SP003<4200)
+		{
+			//�_�ɤǤ����饴�`���
+			workG(GW_ENTRY_EVENT,SET,3)		//���`���
+		}
+		else
+		if(SP003>4200)						//70��=70*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>5)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<3)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(SP003>3600)		//60��=60*60sec
+	if(GW_SKI_DOWN==2)		// �y�׶ȥ�����
 	{
-		//�r�g���`�Щ`
-		workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		if(GW_NOW_BREAK>=13 && GW_NOW_DAM<=3 && SP003<3600)
+		{
+			//�_�ɤǤ����饴�`���
+			workG(GW_ENTRY_EVENT,SET,3)		//���`���
+		}
+		else
+		if(SP003>3600)						//60��=60*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>3)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<11)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_DAM!=0)
+	if(GW_SKI_DOWN==1)		// �y�׶ȥ�����
 	{
-		//����`��
-		workG(GW_ENTRY_EVENT,SET,9)	//9=�����`ʧ��(����`��)
+		if(GW_NOW_BREAK>=17 && GW_NOW_DAM<=1 && SP003<3300)
+		{
+			//�_�ɤǤ����饴�`���
+			workG(GW_ENTRY_EVENT,SET,3)		//���`���
+		}
+		else
+		if(SP003>3300)						//55��=55*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>1)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<15)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
 	{
-		//�������ʤ�������
-		workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
-	}
-	else
-	if(GW_NOW_BREAK<19)
-	{
-		//�������ʤ������ʤ�
-		workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
-	}
-	else
-	{
-		//�������ʤ���������
-		workG(GW_ENTRY_EVENT,SET,8)	//8=�����`ʧ��(�ĥܡ�������)
+		if(GW_NOW_BREAK==21 && GW_NOW_DAM==0 && SP003<3000)
+		{
+			//�_�ɤǤ����饴�`���
+			workG(GW_ENTRY_EVENT,SET,3)		//���`���
+		}
+		else
+		if(SP003>3000)						//50��=60*50sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM!=0)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<19)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 
+
+
 	//��ܞ
 	fade_in(100,60,0)
 	wait_fade()
diff --git a/scp_jp_conv/map/0/EV00493.txt b/scp_conv/map/0/EV00493.txt
index 79becb5..8e83a54 100644
--- a/scp_jp_conv/map/0/EV00493.txt
+++ b/scp_conv/map/0/EV00493.txt
@@ -39,11 +39,14 @@ INIT
 //	set_chr( 92,990,	-1,-1,    -55, 44200, -1500,	 0,6050, 6,"K2_16000;")	//����ȥ� ����
 //	set_chr( 93,990,	-1,-1,    107, 48800, -2500,	 0,6050, 6,"K2_16000;")	//����ȥ� ����
 	set_chr( 91,990,	-1,-1,    159, 55239,  -800,	 0,4010, 6,"<EV_GOAL>;")	//����ȥ� ���`��
-	set_chr( 92,990,	-1,-1,    -55, 44200, -1500,	 0,6050, 6,"<EV_FALL>;")	//����ȥ� ����
-	set_chr( 93,990,	-1,-1,    107, 48800, -2500,	 0,6050, 6,"<EV_FALL>;")	//����ȥ� ����
+	set_chr( 92,990,	-1,-1,    -55, 44200, -1400,	 0,6050, 6,"<EV_FALL>;")	//����ȥ� ����
+	set_chr( 93,990,	-1,-1,    107, 48800, -2400,	 0,6050, 6,"<EV_FALL>;")	//����ȥ� ����
 
 	set_chr( 94,990,	 0, 0,      0,      0,    0,	  0, 0 , 8,"(<EV_Snow> WT?50)")	//���ե����ȥ�`��������
 
+	set_chr( 95,991,	-1,-1,    -55, 44200, -1500,	 0,6050, 0,";")	//������¤Τ�����
+	set_chr( 96,991,	-1,-1,    107, 48800, -2500,	 0,6050, 0,";")	//������¤Τ�����
+
 //	set_chr( 90,990,	-1,-1,   -450,3000,-300,   	180,  1201,	6,"K9_10000;")	//�٥���ȥ� �ե��`���
 //	set_chr( 91,990,	-1,-1,   -100,-1330,0,  	330,050202,	6,"K0_16010;")	//�٥���ȥ� ��ڷ��
 //	set_chr( 92,990,	-1,-1,   4950,-11700, 1850, 345,  1001,	6,"K0_16010;")	//�٥���ȥ� �����m��
@@ -128,6 +131,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,79)	//�����Х�`��
 		workL(WK_ROUTETIME_STOP,SET,1)	// ������Ӌ�yֹͣ
 
+		if(GW_SKI_COUNT4<255)
+		{
+			workG(GW_SKI_COUNT4,ADD,1)	//�ץ쥤����
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////�ȣ�0�Ǥ������ʤ��������0�������r��"EV_DEAD"������
 
 		//��`�׷⤸
@@ -327,7 +335,10 @@ EV_KappaWarp
 	SE(1016, KAPPA)	//���
 	EFF_chr(24560,KAPPA,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA,-92,40991,3634,360,2)
+	if(GW_SKI_DOWN>=1)		// �y�׶ȥ�����
+		chr_pos(KAPPA,1562,43701,3493,360,2)
+	else
+		chr_pos(KAPPA,-92,40991,3634,360,2)
 }
 
 EV_KappaWarp1
@@ -351,7 +362,10 @@ EV_KappaWarp1
 	SE(1016, KAPPA)	//���
 	EFF_chr(24560,KAPPA01,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA01,-406, 31210,  7999,360,2)
+	if(GW_SKI_DOWN>=1)		// �y�׶ȥ�����
+		chr_pos(KAPPA01,-1777,43442,3230,360,2)
+	else
+		chr_pos(KAPPA01,-406, 31210,7999,360,2)
 }
 
 EV_KappaWarp2
@@ -375,7 +389,10 @@ EV_KappaWarp2
 	SE(1016, KAPPA)	//���
 	EFF_chr(24560,KAPPA02,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA02,-200,35814,5619,360,2)
+	if(GW_SKI_DOWN>=2)		// �y�׶ȥ�����
+		chr_pos(KAPPA02,-1777,43442,3230,360,2)
+	else
+		chr_pos(KAPPA02,-200,35814,5619,360,2)
 }
 
 EV_KappaWarp3
@@ -399,7 +416,10 @@ EV_KappaWarp3
 	SE(1016, KAPPA)	//���
 	EFF_chr(24560,KAPPA03,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA03,91,34416,6413,360,2)
+	if(GW_SKI_DOWN>=2)		// �y�׶ȥ�����
+		chr_pos(KAPPA03,1562,43701,3493,360,2)
+	else
+		chr_pos(KAPPA03,91,34416,6413,360,2)
 }
 
 EV_KappaWarp4
@@ -430,7 +450,10 @@ EV_KappaWarp4
 	SE(1016, KAPPA)	//���
 	EFF_chr(24560,KAPPA04,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA04,-92,40991,3634,360,2)
+	if(GW_SKI_DOWN>=3)		// �y�׶ȥ�����
+		chr_pos(KAPPA04,-1777,43442,3230,360,2)
+	else
+		chr_pos(KAPPA04,-92,40991,3634,360,2)
 }
 
 //--------------------------------------------------------------------
@@ -447,47 +470,183 @@ EV_GOAL
 	CAM_Type(1)
 
 	//-- �ж� -----------------------------------------------------------
-	if(F201)		// ���åѥ��`��g�ߣ�
-	{
-		//���åѤΤۤ����٤��ä�
-		workG(GW_ENTRY_EVENT,SET,13)	//13=�����`ʧ��(���å�)
-	}
-	else
-	if(GW_NOW_BREAK==16 && GW_NOW_DAM==0 && SP003<3000)
-	{
-		//�_�ɤǤ�����ץ����
-		workG(GW_ENTRY_EVENT,SET,4)	//�ץ����
-	}
-	else
-	if(SP003>3000)		//50��=50*60sec
-	{
-		//�r�g���`�Щ`
-		workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
-	}
-	else
-	if(GW_NOW_DAM!=0)
+
+	if(GW_SKI_DOWN==3)		// �y�׶ȥ�����
 	{
-		//����`��
-		workG(GW_ENTRY_EVENT,SET,9)	//9=�����`ʧ��(����`��)
+		if(F201)							// ���åѥ��`��g�ߣ�
+		{
+			//���åѤΤۤ����٤��ä�
+			workG(GW_ENTRY_EVENT,SET,13)	//13=�����`ʧ��(���å�)
+		}
+		else
+		if(GW_NOW_BREAK>=6 && GW_NOW_DAM<=5 && SP003<4200)
+		{
+			//�_�ɤǤ�����ץ����
+			workG(GW_ENTRY_EVENT,SET,4)		//�ץ����
+		}
+		else
+		if(SP003>4200)						//70��=70*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>5)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<4)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
+	if(GW_SKI_DOWN==2)		// �y�׶ȥ�����
 	{
-		//�������ʤ�������
-		workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		if(F201)							// ���åѥ��`��g�ߣ�
+		{
+			//���åѤΤۤ����٤��ä�
+			workG(GW_ENTRY_EVENT,SET,13)	//13=�����`ʧ��(���å�)
+		}
+		else
+		if(GW_NOW_BREAK>=11 && GW_NOW_DAM<=3 && SP003<3600)
+		{
+			//�_�ɤǤ�����ץ����
+			workG(GW_ENTRY_EVENT,SET,4)		//�ץ����
+		}
+		else
+		if(SP003>3600)						//60��=60*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>3)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<9)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<14)
+	if(GW_SKI_DOWN==1)		// �y�׶ȥ�����
 	{
-		//�������ʤ������ʤ�
-		workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		if(F201)							// ���åѥ��`��g�ߣ�
+		{
+			//���åѤΤۤ����٤��ä�
+			workG(GW_ENTRY_EVENT,SET,13)	//13=�����`ʧ��(���å�)
+		}
+		else
+		if(GW_NOW_BREAK>=14 && GW_NOW_DAM<=1 && SP003<3300)
+		{
+			//�_�ɤǤ�����ץ����
+			workG(GW_ENTRY_EVENT,SET,4)		//�ץ����
+		}
+		else
+		if(SP003>3300)						//55��=55*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM>1)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<12)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 	else
 	{
-		//�������ʤ���������
-		workG(GW_ENTRY_EVENT,SET,8)	//8=�����`ʧ��(�ĥܡ�������)
+		if(F201)							// ���åѥ��`��g�ߣ�
+		{
+			//���åѤΤۤ����٤��ä�
+			workG(GW_ENTRY_EVENT,SET,13)	//13=�����`ʧ��(���å�)
+		}
+		else
+		if(GW_NOW_BREAK==16 && GW_NOW_DAM==0 && SP003<3000)
+		{
+			//�_�ɤǤ�����ץ����
+			workG(GW_ENTRY_EVENT,SET,4)		//�ץ����
+		}
+		else
+		if(SP003>3000)						//50��=50*60sec
+		{
+			//�r�g���`�Щ`
+			workG(GW_ENTRY_EVENT,SET,10)	//10=�����`ʧ��(������)
+		}
+		else
+		if(GW_NOW_DAM!=0)
+		{
+			//����`��
+			workG(GW_ENTRY_EVENT,SET,9)		//9=�����`ʧ��(����`��)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//�������ʤ�������
+			workG(GW_ENTRY_EVENT,SET,12)	//12=�����`ʧ��(�ĥܡ�����)
+		}
+		else
+		if(GW_NOW_BREAK<14)
+		{
+			//�������ʤ������ʤ�
+			workG(GW_ENTRY_EVENT,SET,11)	//11=�����`ʧ��(�ĥܡ����ʤ�)
+		}
+		else
+		{
+			//�������ʤ���������
+			workG(GW_ENTRY_EVENT,SET,8)		//8=�����`ʧ��(�ĥܡ�������)
+		}
 	}
 
+
 	//��ܞ
 	fade_in(100,60,0)
 	wait_fade()
diff --git a/scp_jp_conv/map/0/EV00510.txt b/scp_conv/map/0/EV00510.txt
index 5d072a9..a348d48 100644
--- a/scp_jp_conv/map/0/EV00510.txt
+++ b/scp_conv/map/0/EV00510.txt
@@ -45,6 +45,36 @@ INIT
 //	set_obj("@ob00082a", 4, 3,     0,   0,  0,		270)						//���A�Σ�Ĺ����
 	set_chr(192,1301,	 4, 3,     0,   0,  0,		  0,   270, 0,";")			//�A���ϣ����ߩ`��
 
+//�Y�ե����奢�^/�ѥå���
+	if(!F6_11_GameClear)
+	{
+		set_obj2("mp00442",   6, 5, -450,-450,  0,	 0) //
+		set_obj2("mp00452",   6, 5,  450,-450,  0,	 0) //
+		set_obj2("mp00222",   6, 5, -450, 450,  0,	 0) //
+		set_obj2("mp00232",   6, 5,  450, 450,  0,	 0) //
+	}
+	else
+	{
+		set_obj2("mp00442",   6, 5, -450,-450,  0,	 0) //
+		set_obj2("mp00252",   6, 5,  450,-450,  0,	 0) //
+		set_obj2("mp00222",   6, 5, -450, 450,  0,	 0) //
+		set_obj2("mp00512",   6, 5,  450, 450,  0,	 0) //
+
+		set_obj2("mp00082",   7, 5, -450,-450,  0,	 0) //
+		set_obj2("mp00012",   7, 5,  450,-450,  0,	 0) //
+		set_obj2("mp00102",   7, 5, -450, 450,  0,	 0) //
+		set_obj2("mp00032",   7, 5,  450, 450,  0,	 0) //
+
+		set_chr( 93,990,	 7, 5,     0,   0,  0,		90,  0102, 6,"K0_10540;")	//�ۥ���ȥ� �����^
+		set_obj("@ob00072a", 7, 5,     0,   0,  0,		90)						//���A�Σ��ǥ���
+		set_chr(193,1301,	 7, 5,     0,   0,  0,		  0,   270, 0,";")			//�A���ϣ����ߩ`��
+
+		set_chr(87, 804,	 6,5,	 425,-200,0,	0,	0,	8,"(L2?99 [9991���ե����奢�^ �e�ҡ���] WT?30 L2!99 [9903]);")	//����
+		set_chr(88, 445,	 6,5,    300,-350,82,		2,   0, 3,";")//������ɥ��ƽ���
+		set_chr(89, 991,	 6,5,    300,-350, 0,		0,0202, 0,";")//������ɥ��ƽ��񵱤���
+
+	}
+
 	set_chr(100,990,	-1,-1,   11518,5426,0,		 90,  0101, 6,"RF100")	//
 	set_chr(101,990,	-1,-1,   11506,6298,0,		 90,  0101, 6,"RF100")	//
 	set_chr(102,990,	-1,-1,   11570,5872,0,		 90,  0407, 6,"SF100")	//�ܸ�����å�
@@ -366,7 +396,32 @@ INIT
 
 	workG(GW_SKI_MODE,SET,0)	//���֥��åץ�˥�`�򥯥ꥢ
 
+	//NPC�ե����奢����k�����٥�Ȥ���
+	if(GW_ENTRY_EVENT==4)
+	{
+		workG(GW_ENTRY_EVENT,SET,0)
+		EV("EV_ALLGET_END")
+	}
+	else
 	//�L���������餷�Ƒ��äƤ����Ȥ��Υ��٥��
+	//�����Х��Х�K��
+	if(GW_ENTRY_EVENT==3)
+	{
+		workG(GW_ENTRY_EVENT,SET,0)
+		F_reset_chr(PLAYER1,CF_NO_DEAD)
+		set_hp(PLAYER1,100)//ȫ��
+
+		if(GW_WINLOSE==1)
+		{
+			EV("WIN_BATTLE3")
+		}
+		else
+		{
+			EV("LOSE_BATTLE")		//�L������ͬ�����������ݤ�ע��
+		}		
+	}
+	else
+	//���L����
 	//���Ǥ˥��ꥢ�g�ߤΥ��`�����ä�
 	if(GW_ENTRY_EVENT==2)
 	{
@@ -377,6 +432,7 @@ INIT
 		EV("WIN_BATTLE2")
 	}
 	else
+	//���L����	
 	//�����ꥢ���ä����⤷����ؓ��
 	if(GW_ENTRY_EVENT==1)
 	{
@@ -543,8 +599,9 @@ WIN_BATTLE
 	EV_end()
 }
 
-
+//������������������������������������������������������������
 //���`�����ꥢ����Ŀ�Խ��ǥ����ƥ���B���I��
+//������������������������������������������������������������
 WIN_BATTLE2
 {
 //�����L�����ܸ�����åƤ�ǰ�˥ե��`�ɥ��󤹤롣
@@ -572,6 +629,7 @@ WIN_BATTLE2
 	MES(LOTTE,"����ǤȤ��������ޤ�����",0)
 	MES(LOTTE,"�����餬��ؤ�\n�pƷ�ˤʤ�ޡ�����",0)
 	MES_close(LOTTE)
+	
 	EV("ITEMGET_SECOND")
 	wait_EV("ITEMGET_SECOND")
 
@@ -595,6 +653,60 @@ WIN_BATTLE2
 	EV_end()
 }
 
+//������������������������������������������������������������
+//���Х��Х�Ǆ���
+//������������������������������������������������������������
+WIN_BATTLE3
+{
+//�����L�����ܸ�����åƤ�ǰ�˥ե��`�ɥ��󤹤롣
+	EV_begin()
+
+	//��ܞ
+	fade_in(100,1,0)
+	wait_fade()
+	wait(10)
+	
+	chr_pos(PLAYER2,11230,5753,0,270,2)
+	chr_pos(PLAYER1,11230,6011,0,270,2)
+	chr_pos(PET,11100,5883,0,270,2)
+	rot_chr(LOTTE,-1,PLAYER1)
+
+	//�ե��`�ɥ���
+	fade_in(0,60,0)
+	wait_fade()
+	wait(10)
+
+	MES(LOTTE,"����ǤȤ��������ޤ�����",0)
+	if(IT022>0)						//�ڥåȡ��ڥ󥮥󡹤�Ȥ˳֤äƤ���
+	{
+		MES(LOTTE,"Ҋ�¤�����ޤ��Ф��ޤ����͡���\n�����餬��ؤ��pƷ�ˤʤ�ޡ�����",0)
+		MES_close(LOTTE)		
+		
+		SE(24,0)	//�����������ζ�ݤʤ�
+		MES(0,"C3������ڥ���ܤ�ȡ�ä���",2)
+		MES_close(0)
+		get_gold(500000,RAGNA)
+	}
+	else
+	{
+		MES(LOTTE,"Ҋ�¤�����ޤ��Ф��ޤ����͡���\n�����餬��ؤ��pƷ�ˤʤ�ޡ�����",0)
+		MES_close(LOTTE)
+	
+		get_item(22,1,0)				//�ڥåȡ��ڥ󥮥�
+		wait_key(0)
+		menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+		menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+	}
+		
+	MES(LOTTE,"�ҥޤʤ�\n�ޤ����餷�Ƥ��������͡���",0)
+	MES_close(LOTTE)
+
+	EV("EV_WARP_FLAG")
+	wait_EV("EV_WARP_FLAG")
+
+	rot(LOTTE,30,90)
+	EV_end()
+}
 
 //������������������������������������������������������������
 //���ܸ���������΄I��
@@ -1184,6 +1296,38 @@ EV_FIGURE_12
 	TK_end()
 }
 
+
+//---------------------------------------------------------------------
+//NPC�ե����奢����ץ�`��
+EV_ALLGET
+{
+	if(!F1_05_FigureCmp)	//NPC�ե����奢����ץ�`��
+	{
+		TK_begin()
+		wait(30)
+		F_set(F1_05_FigureCmp)
+		
+		fade_in(100,30,0)
+		wait_fade()
+		
+		workG(GW_ENTRY_EVENT,SET,4)
+		new_map(10540)
+	}
+}
+
+EV_ALLGET_END
+{	
+	chr_pos(RAGNA,   10194,5988,0,180,2)
+	chr_pos(PARTNER, 10105,6145,0,180,2)
+	chr_pos(PET,     10334,6145,0,180,2)
+
+	fade_in(0,30,0)
+	wait_fade()
+		
+	TK_end()
+}
+
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/0/EV00520.txt b/scp_conv/map/0/EV00520.txt
index 5f1934f..12cd719 100644
--- a/scp_jp_conv/map/0/EV00520.txt
+++ b/scp_conv/map/0/EV00520.txt
@@ -10,6 +10,8 @@
 
 #LOTTE		10
 
+//30��34�Ϸ���
+
 /*
 #MAURICE	11
 #ODESSA		12
@@ -54,6 +56,7 @@
 
 //����`�����`��
 // 001:��������������
+// 002:���Х��Х��`�ɤΤȤ�1
 
 INIT
 {
@@ -72,147 +75,186 @@ INIT
 	//�^�ڤˤ����̣ơ�
 	F_set(90)
 
+	//�����åѥ�`��
+/*	if(GW_ENTRY_EVENT==3)
+	{
+		set_chr( 1,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 2,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 3,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 4,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 5,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 6,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 7,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 8,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+		set_chr( 9,311,		0,0,10280,10210,0,	0,	0,		0,";")//��ͨ���饤��
+//		set_chr( 10,350,	0,0,10280,10210,800,-1,	0,		8,"!F10 F1 F2 F3 F4 F5 F6 F7 F8 F9 S0_1 WT?120 V0_99;")//�󥹥饤��
+	
+	
+		EV("PRE_KAPPA_BATTLE")										//���å�
+	}
+	else*/
+	
+	//�����Х��Х루���å��ᣩ
+	if(GW_ENTRY_EVENT==3)
+	{
+		workG(GW_ENTRY_EVENT,SET,3)							//�K����η�᪤�ʹ��
+		EV("PRE_SURVIVAL_LOOP")
+		wait_EV("PRE_SURVIVAL_LOOP")
+		
+		
+	}
+	else
+	//�����Х��Х�	
+	if(GW_ENTRY_EVENT==2)
+	{
+		workG(GW_ENTRY_EVENT,SET,3)							//�K����η�᪤�ʹ��
+		EV("PRE_SURVIVAL")									//���Х��Х�
+	}
 	//���L����
-	if(GW_ENTRY_EVENT==1)
+	else
 	{
-//�ؤ����餫��ʼ�ޤ�褦������ 2008.07.29. 18:40
-		workG(GW_SKI_MODE,SET,5)	//���֥��åץ�˥�`�򥻥å�
+	
+		if(GW_ENTRY_EVENT==1)
+		{
+	//�ؤ����餫��ʼ�ޤ�褦������ 2008.07.29. 18:40
+			workG(GW_SKI_MODE,SET,5)	//���֥��åץ�˥�`�򥻥å�
 
-		set_chr( LOTTE,1068,	-1,-1,  10388,10356,1,	0,0,0,"")	//����å�
-		MOT_SET( LOTTE,159,159,3001,3061,-1,-1 )
-		MOT(LOTTE,159,0)
+			set_chr( LOTTE,1068,	-1,-1,  10388,10356,1,	0,0,0,"")	//����å�
+			MOT_SET( LOTTE,159,159,3001,3061,-1,-1 )
+			MOT(LOTTE,159,0)
 
-		//�Хȥ�����餹��Τ����ؤΈ��ϡ��ݳ���Ҋ�������λ�ä�
-		if(GW_TRY_CUP==1)
-		{
-			if(!FV_FF_BAMaurice)
+			//�Хȥ�����餹��Τ����ؤΈ��ϡ��ݳ���Ҋ�������λ�ä�
+			if(GW_TRY_CUP==1)
 			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAMaurice)
+				if(!FV_FF_BAMaurice)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAMaurice)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==2)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==2)
-		{
-			if(!FV_FF_BAOdessa)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAOdessa)
+				if(!FV_FF_BAOdessa)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAOdessa)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==3)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==3)
-		{
-			if(!FV_FF_BAPockle)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAPockle)
+				if(!FV_FF_BAPockle)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAPockle)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==4)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==4)
-		{
-			if(!FV_FF_BAPipiro)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAPipiro)
+				if(!FV_FF_BAPipiro)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAPipiro)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==5)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==5)
-		{
-			if(!FV_FF_BASubaru)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BASubaru)
+				if(!FV_FF_BASubaru)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BASubaru)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==6)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==6)
-		{
-			if(!FV_FF_BAFiona)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAFiona)
+				if(!FV_FF_BAFiona)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAFiona)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==7)
 			{
-				F_reset(FV_FF_FarstBattle)
+				if(!FV_FF_BAKlode)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAKlode)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
-		}
-		else
-		if(GW_TRY_CUP==7)
-		{
-			if(!FV_FF_BAKlode)
+			else
+			if(GW_TRY_CUP==8)
 			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAKlode)
+				if(!FV_FF_BAGyarandow)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAGyarandow)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==9)
 			{
-				F_reset(FV_FF_FarstBattle)
+				if(!FV_FF_BAPenguin)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAPenguin)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 		}
-		else
-		if(GW_TRY_CUP==8)
+
+		if(FV_FF_FarstBattle)
 		{
-			if(!FV_FF_BAGyarandow)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAGyarandow)
-			}
-			else
-			{
-				F_reset(FV_FF_FarstBattle)
-			}
+			//���ؤ΄I��
+			EV("PRE_BATTLE")
 		}
+		//�����Ǥʤ����Ϥ�������锳���򤭺ϤäƤ���
 		else
-		if(GW_TRY_CUP==9)
 		{
-			if(!FV_FF_BAPenguin)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAPenguin)
-			}
-			else
-			{
-				F_reset(FV_FF_FarstBattle)
-			}
+		//2��Ŀ�Խ��΄I��
+			EV("PRE_BATTLE_2")
 		}
-	}
 
-	if(FV_FF_FarstBattle)
-	{
-		//���ؤ΄I��
-		EV("PRE_BATTLE")
 	}
-	//�����Ǥʤ����Ϥ�������锳���򤭺ϤäƤ���
-	else
-	{
-	//2��Ŀ�Խ��΄I��
-		EV("PRE_BATTLE_2")
-	}
-
 	map_color(85,80,80,0);//R,G,B, time 100%
 }
 
@@ -1026,8 +1068,10 @@ PRE_BATTLE
 
 			if(!F4_09_GoShrineMia)
 			{
-				KAO(ENEMY_CHARA, "B232BZ6", "1233321", "5")	
-				MES(ENEMY_CHARA,"�������΃W��\n������ե����ʤ����\n�m�ޤ�Ƥ��{�ˤ����äơ���",0)
+//				KAO(ENEMY_CHARA, "B232BZ6", "1233321", "5")		//�����ͨ�ä��ʤ������¤ȺϤ碌������0922��
+//				MES(ENEMY_CHARA,"�������΃W��\n������ե����ʤ����\n�m�ޤ�Ƥ��{�ˤ����äơ���",0)
+				KAO(ENEMY_CHARA, "B232BZ4", "1233321", "5")	
+				MES(ENEMY_CHARA,"�������΃W�����\n����ä�æ������Ǥ����ɤá���",0)
 				MES_close(ENEMY_CHARA)
 			}
 			else
@@ -1790,34 +1834,49 @@ EV_DEAD
 	wait_BGM()
 
 	//-- ؓ�����ܸ��ˑ��� ------------------------------------------------
-
-	if(GW_TRY_CHARA==0)
+	if(WK002==1)		//WK002��1�ʤ饵�Х��Х��`��
 	{
-		join_party(1)//ALWEN��ѩ`�ƥ��`�ˑ���
-		
-		//�ե����奢���å�
-		if(!F2857)
+		if(GW_TRY_CHARA==0)
 		{
-			SE(24,0)//���å�SE
-			MES(0,"L777�μ��p�Ȥ��ơ�\nL667�饰��L777�Υե����奢���֤���줿����",2)
-			MES_close(0)
-			F_set(2857)
+			join_party(1)//ALWEN��ѩ`�ƥ��`�ˑ���
 		}
+		else
+		{
+			join_party(0)//RAGNA��ѩ`�ƥ��`�ˑ���		
+		}	
+		workL(002,SET,0)
 	}
 	else
 	{
-		join_party(0)//RAGNA��ѩ`�ƥ��`�ˑ���
-		
-		//�ե����奢���å�
-		if(!F2858)
+	
+		if(GW_TRY_CHARA==0)
 		{
-			SE(24,0)//���å�SE
-			MES(0,"L777�μ��p�Ȥ��ơ�\nL667���륦����L777�Υե����奢���֤���줿����",2)
-			MES_close(0)
-			F_set(2858)
+			join_party(1)//ALWEN��ѩ`�ƥ��`�ˑ���
+			
+			//�ե����奢���å�
+			if(!F2857)
+			{
+				SE(24,0)//���å�SE
+				MES(0,"L777�μ��p�Ȥ��ơ�\nL667�饰��L777�Υե����奢���֤���줿����",2)
+				MES_close(0)
+				F_set(2857)
+			}
+		}
+		else
+		{
+			join_party(0)//RAGNA��ѩ`�ƥ��`�ˑ���
+			
+			//�ե����奢���å�
+			if(!F2858)
+			{
+				SE(24,0)//���å�SE
+				MES(0,"L777�μ��p�Ȥ��ơ�\nL667���륦����L777�Υե����奢���֤���줿����",2)
+				MES_close(0)
+				F_set(2858)
+			}
 		}
+	
 	}
-
 	wait(15)
 	CAM_return( 0 )
 	new_map(10510)
@@ -2988,7 +3047,7 @@ ITEMGET_FIRST	//
 		wait(20)
 		fade_in(30,10,BLACK)		//�٤���ܞ
 
-		if(IT113>0)
+		if(IT113>=0)
 			get_item(196,1,0)
 		else
 			get_item(113,1,0)
@@ -3108,7 +3167,7 @@ ITEMGET_FIRST	//
 		wait(20)
 		fade_in(30,10,BLACK)		//�٤���ܞ
 
-		if(IT116>0)
+		if(IT116>=0)
 		{
 			get_item(166,1,0)
 			wait(70)
@@ -3157,15 +3216,22 @@ ITEMGET_FIRST	//
 		fade_in(30,10,BLACK)		//�٤���ܞ
 
 		if(IT138>0)
-			get_item(182,1,0)
-		else
-			get_item(138,1,0)
+			get_item(182,1,0)		//�ѥ��ʥåץ�
+		else	
+			get_item(138,1,0)		//��٥�ץ�`�ȣ�
 		wait(70)
 		wait_key(0)
+		menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+		menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)		
+		
+		SE(043,PLAYER1)
+MES_pos(0,"C3����٥�ץ�`�ȣǡ��ϥ��󥸥���ڤˤ���\n��٥�ץ�`�Ȥ��{�٤뤳�Ȥ�ʹ�ä��ޤ���\n����ͨ����ꏊ���ʤ�ޤ�����\n�����ƥ�γ��F�_�ʤ�һ���α���������仯���ޤ���",2,120,200,400,100)	
+		wait_key(0)	
+		MES_close(0)		
+		
 		BGM_vol(100,30)				//BGM����
 		fade_in(0,10,BLACK)			//��ܞ���
-		menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
-		menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+
 		
 		//�ե����奢���å�
 		if(!F2848)
@@ -4142,5 +4208,390 @@ DELETE_ROPE
 }
 
 
+
+//������������������������������������������������������������
+//���Х��Х��`��
+//������������������������������������������������������������
+PRE_SURVIVAL
+{
+
+	workG(GW_TRY_CUP,SET,1)
+//	workG(GW_TRY_CUP,SET,6)
+	workL(002,SET,1)
+	set_hp(PLAYER1,100)//ȫ��	
+		
+	EV("PRE_SURVIVAL_LOOP")
+	wait_EV("PRE_SURVIVAL_LOOP")
+}
+
+//������������������������������������������������������������
+// ���Х��Х루���أ�
+//������������������������������������������������������������
+PRE_SURVIVAL_FIRST
+{
+	//�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D
+	//	���ڻ��I��
+	//�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D
+	//��ܞ
+//	fade_in(100,1,0)
+//	wait_fade()
+//	wait(1)
+
+//	EV("PRE_BATTLE_SET")
+//	wait_EV("PRE_BATTLE_SET")
+
+	chr_pos(PLAYER1,	10651,10772,1,90,2)
+	color(ENEMY_CHARA,	-1)	//͸�^
+	color(PLAYER1,		-1)		//͸�^
+	color(PLAYER2,		-1)		//͸�^
+	color(LOTTE,		1)		//
+
+	set_chr( LOTTE,1068,	-1,-1,  10388,10356,1,	0,0,0,"")	//����å�		
+	chr_equip2( LOTTE,"eq_062", "Bone_LeftHand", 100,	90,0,0,	-7,0,2);
+
+	wait(30)
+
+	//����饻�å�
+	CAM_move(10388,-10456,162,0,0)
+	CAM(-50,118,162,20,180,0,0)
+	CAM_move(10388,-10456,162,100,0)
+	CAM(-50,50,162,21,180,100,0)
+
+	fade_in( 0, 60, BLACK)	//�ե��`�ɥ���
+	wait_fade()
+
+
+	if( GW_TRY_CUP==6)
+	{
+		KAO(LOTTE,"52625Z4","5","6")	
+		MES(LOTTE,"P1S4�����������Фä����餤�äƤߤޤ��硫��",0)
+		MES_close(LOTTE)
+		wait_MES(LOTTE)			
+	}
+	else
+	{
+		CAM_quake("463746")
+		KAO(LOTTE,"52625Z4","5","6")
+		MES(LOTTE,"P1S4��ǥ��`����������ȥ�ᡫ��",0)
+		KAO(LOTTE,"52625Z3","321","6")
+		MES(LOTTE,"P1S4�����������ޤ�������",0)
+		KAO(LOTTE,"52625Z6","1","6")
+		MES(LOTTE,"P1S4�����ϥ��Х��Х���̤��Ф��ޡ�����",0)
+		KAO(LOTTE,"52625Z6","1236","6")		
+		MES(LOTTE,"P1S4�������Υ󥹥ȥåץХȥ��ʼ�ޤ�ǡ�������",0)
+		MES_close(LOTTE)
+		wait_MES(LOTTE)	
+	}
+
+
+	SE(591,0)//�Z��
+	
+	//��ܞ
+	fade_in(100,30,0)
+	wait_fade()
+
+}
+
+//������������������������������������������������������������
+// ���Х��Х루��`�ף�
+//������������������������������������������������������������
+PRE_SURVIVAL_LOOP
+{
+	EV_begin()
+
+	workG(GW_SKI_MODE,SET,5)	//���֥��åץ�˥�`�򥻥å�
+
+	//��ܞ
+	fade_in(100,1,0)
+	wait_fade()
+	wait(1)
+
+	if(GW_TRY_CUP==1 || GW_TRY_CUP==6)
+	{
+		//�����޶�
+		EV("PRE_SURVIVAL_FIRST")
+		wait_EV("PRE_SURVIVAL_FIRST")
+	}
+
+
+	//�������֤��O������
+	if(GW_TRY_CUP==1)
+	{
+		set_chr( ENEMY_CHARA,390,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣���`�ꥹ
+		workG(GW_TRY_CHARA,SET,0)										//�����ߡ����饰��
+		chr_state_LV( ENEMY_CHARA, 26 )									//����٥��O��(����4)	chr_state_LV �� ����
+		chr_state_LV( ENEMY_CHARA, 30)					
+	}
+	else
+	if(GW_TRY_CUP==2)
+	{
+		set_chr( ENEMY_CHARA,392,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣����ǥå�
+		workG(GW_TRY_CHARA,SET,1)										//�����ߡ������륦����
+		chr_state_LV( ENEMY_CHARA, 23 )									//����٥��O��(����7)		
+		chr_state_LV( ENEMY_CHARA, 30)					
+	}
+	else
+	if(GW_TRY_CUP==3)
+	{
+		set_chr( ENEMY_CHARA,396,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣��ݥå���
+		workG(GW_TRY_CHARA,SET,0)										//�����ߡ����饰��
+		chr_state_LV( ENEMY_CHARA, 28 )									//����٥��O��(����12)
+		chr_state_LV( ENEMY_CHARA, 20)			
+	}
+	else
+	if(GW_TRY_CUP==4)
+	{
+		set_chr( ENEMY_CHARA,397,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣��ԥԥ�
+		workG(GW_TRY_CHARA,SET,1)										//�����ߡ������륦����
+		chr_state_LV( ENEMY_CHARA, 17)									//����٥��O��(����13)
+		chr_state_LV( ENEMY_CHARA, 20)			
+	}	
+	else
+	if(GW_TRY_CUP==5)
+	{
+		set_chr( ENEMY_CHARA,391,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣����Х�
+		workG(GW_TRY_CHARA,SET,1)										//�����ߡ������륦����
+		chr_state_LV( ENEMY_CHARA, 13)									//����٥��O��(����17)
+		chr_state_LV( ENEMY_CHARA, 30)	
+	}
+	else	
+	if(GW_TRY_CUP==6)
+	{
+		set_chr( ENEMY_CHARA,393,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣��ե�����
+		workG(GW_TRY_CHARA,SET,1)										//�����ߡ������륦����
+		chr_state_LV( ENEMY_CHARA, 10 )									//����٥��O��(����20)
+		chr_state_LV( ENEMY_CHARA, 5 )									//
+	}	
+	else
+	if(GW_TRY_CUP==7)
+	{
+		set_chr( ENEMY_CHARA,394,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣�����`��
+		workG(GW_TRY_CHARA,SET,0)										//�����ߡ����饰��
+		chr_state_LV( ENEMY_CHARA, 7)									//����٥��O��(����23)
+		chr_state_LV( ENEMY_CHARA, 15 )			
+	}	
+	else
+	if(GW_TRY_CUP==8)
+	{
+		set_chr( ENEMY_CHARA,398,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣�������ɥ�
+		workG(GW_TRY_CHARA,SET,0)										//�����ߡ����饰��
+		chr_state_LV( ENEMY_CHARA, 3)									//����٥��O��(����27)
+		chr_state_LV( ENEMY_CHARA, 10 )			
+	}	
+	else
+	if(GW_TRY_CUP==9)
+	{
+		set_chr( ENEMY_CHARA,399,	-1,-1,  9501,8247,1,	2,0,0,"")	//�������֣��ڥ󥮥�
+		workG(GW_TRY_CHARA,SET,1)										//�����ߡ������륦����
+		chr_state_LV( ENEMY_CHARA, 10 )									//����٥��O��(����30)
+		chr_state_LV( ENEMY_CHARA, 10 )									//
+	}	
+
+
+
+	F_set_chr(PLAYER1,CF_NO_DEAD) ////�ȣ�0�Ǥ������ʤ��������0�������r��"EV_DEAD"������
+
+	set_chr( ZAKO_19,990,	-1,-1,  11388,9309,1,	10,0,8,"(F9 <EV_WIN_SURVIVAL> RF9)")
+	F_set_chr(ENEMY_CHARA,CF_NO_DEAD)
+	F_set_chr(ENEMY_CHARA,CF_NO_DROPITEM)
+	
+	color(ENEMY_CHARA,1)	//
+
+	//�ѩ`�ƥ���һ�ˤˤ��롣(���ѩ`�ƥ��ˣ��ˤ��뤳��ǰ��)
+	if(GW_TRY_CHARA==0)
+	{
+		clear_party(PARTNER)	//���륦������ȥ
+//		delete(PLAYER2)	
+		color(PLAYER2,-1)
+		color(PLAYER1, 1)
+	}
+	else
+	{
+		clear_party(99)			//���륦����Τߤβ�����`�ɤ�	
+//		delete(RAGNA)			//������ȡ����Х�η���r�˲��ߺϰk��
+		color(PLAYER2,-1)
+		color(PLAYER1, 1)
+	}
+
+	chr_pos(PLAYER1,	10651,10772,1,90,2)
+//	chr_pos(PLAYER2,	10651,10772,1,90,2)
+	chr_pos(PLAYER2,	0,0,1,90,2)
+	
+	KAO(PLAYER1, "1", "1", "1")
+	KAO(LOTTE, "1", "1", "1")
+
+
+	EV("SET_ROPE")												//��`�ץ��å�
+
+	//����λ�å��å� 2��Ŀ�Խ�
+	chr_pos(PLAYER1,	10651,10772,1,90,2)
+	chr_pos(ENEMY_CHARA,	10120,10772,1,270,2)
+
+
+	CAM_move(10388,-10676,102,0,0)
+	CAM(950,183,102,21,180,0,0)
+	CAM_move(10388,-10456,122,120,0)
+	CAM(-50,107,122,22,180,120,0)
+
+	SE(591,0)//�Z��
+	KAO(LOTTE,"1","1","3")
+
+
+
+	fade_in( 0, 60, BLACK)	//�ե��`�ɥ���
+	wait_CAM()
+	wait_CAM_move()
+	wait_fade()
+
+
+	//��ǰ����˱�ʾ
+	if(GW_TRY_CUP==1)
+		set_namebmp(34,0)	//���������`�ꥹ	�ǣ�����å���
+	if(GW_TRY_CUP==2)
+		set_namebmp(35,0)	//�I�����ꥪ�ǥå�		�ǣ�����å���
+	if(GW_TRY_CUP==3)
+		set_namebmp(37,0)	//��������ݥå���		�ǣ�����å���
+	if(GW_TRY_CUP==4)
+		set_namebmp(38,0)	//ħ����Ů�ԥԥ�		�ǣ�����å���
+	if(GW_TRY_CUP==5)
+		set_namebmp(36,0)	//Ҋ�������ߥ��Х�		�ǣ�����å���
+	if(GW_TRY_CUP==6)	
+		set_namebmp(39,0)	//�}��ʹ���ե�����		�ǣ�����å���
+	if(GW_TRY_CUP==7)
+		set_namebmp(40,0)	//���L���¥���`��		�ǣ�����å���
+	if(GW_TRY_CUP==8)
+		set_namebmp(41,0)	//���泬�˥�����ɥ�	�ǣ�����å���
+	if(GW_TRY_CUP==9)
+		set_namebmp(42,0)	//�~�����O�o���ڥ󥮥�	�ǣ�����å���
+	wait(90)
+
+//����ͬ�r�ˁI�ߣӣŤĤ��ǘ����롣
+	EV("KAMAE_SET")
+	wait_EV("KAMAE_SET")
+
+
+	EFF(21630,320,240,0,0,100,0)//FIGHT
+	wait(40)
+	SE(211,PLAYER1)
+	EV("PLAY_VOICE_Fight")
+
+	//���������
+	EV("KAMAE_RESET")
+	wait_EV("KAMAE_RESET")
+
+	//��åƤ�ɤ���
+	if(GW_TRY_CUP==1 || GW_TRY_CUP==6)
+	{
+		//�����޶�
+		MOT(LOTTE,153,2)
+		rot(LOTTE,60,360)
+		KAO(LOTTE,"5","5","6")
+		jump(LOTTE,0,20,9549,9099,0,400)
+	}
+
+	CAM_return( 30 )
+
+	workL(WK_BOSSHP,SET,ENEMY_CHARA)	//BOSS�ߣȣб�ʾ
+	BGM(45)
+	EV_end()
+
+	//�ڥå�����
+	color(PET,-1)
+
+	//���L�_ʼ
+
+
+}
+
+
+
+//������������������������������������������������������������
+//���Х��Х�ǣ��Ĥ�ԇ�Ϥ˄���
+EV_WIN_SURVIVAL
+{
+	delete(ZAKO_19)	// �ж��������ȥ
+	delete(30)	// ���������ȥ
+	delete(31)	// 
+	delete(32)	// 
+	delete(33)	// 
+	delete(34)	// 
+	
+	DelDropItem()	//�ɥ�åץ����ƥ�ȫ����
+	StopEffect()	//���ե�����ȫ����
+
+	map_color(100,100,100, 5);//R,G,B, time 100%
+	map_specular(80,80,80, 5);//R,G,B, time 100%
+
+	EV_begin()
+	wait(20)
+	map_specular(0,0,0,20);//R,G,B, time 100%
+	KAO(ENEMY_CHARA,"5","5","5")//�����åե��������å�0822
+	wait(30)
+	
+	EV("PLAY_VOICE_EnemyLose")
+	CAM_move_chr(ENEMY_CHARA,90,0)
+	rot_chr(PLAYER1,30,ENEMY_CHARA)	
+	
+	
+	EFF(21650,320,240,0,0,100,0)//WIN
+	wait(60)
+	rot_chr(PLAYER1,30,ENEMY_CHARA)
+
+	wait(30)
+
+	wait(30)
+	fade_in(100,60,0)
+	wait(60)
+	wait_CAM_move()
+//	wait_BGM()
+	wait_EV("PLAY_VOICE_EnemyLose")
+	wait_fade()
+
+	
+	delete(ENEMY_CHARA)
+	
+	
+	//���ʤ��ۤ��Υ�����Ӥ������˽M�ߤˑ���
+	if(GW_TRY_CHARA==0)
+	{
+		join_party(1)			//�饰��
+	}
+	else
+	{
+		join_party(0)			//���륦����
+	}	
+	
+	//�������ԇ�Ϥ��ä�
+	if(GW_TRY_CUP==9)
+	{
+		workG(GW_ENTRY_EVENT,SET,3)
+		workG(GW_WINLOSE,SET,1)		//�٤ä�GW�����Ƥ�
+		F_set(FV_FF_WinSurvival)	//���L�������Х��Х�˄٤ä�
+		stop_BGM(60)		
+		workL(002,SET,0)
+		new_map(10510)				//�ǥ���ˑ���
+	}
+	else
+	//�����åѤ�
+	if(GW_TRY_CUP==5)
+//	if(GW_TRY_CUP==1)				//���å�ֱǰ��ԇ�Ϥ��ä�
+	{
+		workG(GW_TRY_CUP,SET,6)		//�Τ�ԇ�Ϥء����å����ԇ�Ϸ���
+//		workG(GW_TRY_CUP,SET,9)		//�Τ�ԇ�Ϥء����å����ԇ�Ϸ���		
+		stop_BGM(60)	
+		new_map(10521)				
+	}
+	//���Τ�ԇ�Ϥ�
+	else
+	{
+		workG(GW_TRY_CUP,ADD,1)	//�Τ�ԇ�Ϥ�
+	
+//		workG(GW_TRY_CUP,SET,7)	//���ƥڥ󤮤�
+		EV("PRE_SURVIVAL_LOOP")
+	}
+
+}
+
+
 #EndScriptTable
 //====================================================================
diff --git a/scp_jp_conv/map/0/EV00530.txt b/scp_conv/map/0/EV00530.txt
index a776aa6..82d1721 100644
--- a/scp_jp_conv/map/0/EV00530.txt
+++ b/scp_conv/map/0/EV00530.txt
@@ -7,6 +7,9 @@
 
 #GATEROPE	1
 
+#TREASURE_CH	60
+#IT_TREASURE	32	//��ǥ�󥸥㥱�å�
+
 INIT
 {
 //  -------  no typ   	  tip      x    y   z       mot     �� ״  000+++++++010+++++++020+++++++030+++++++040+++++++050+++++++060+++++++070+++++++080+++++++090+++++++100+++++++110+++++++120+++++++130+++++++140+++++++150+++++++160+++++++170+++++++180+++++++190+++++++200+++++++210+++++++220+++++++230+++++++240+++++++250++
@@ -38,6 +41,9 @@ INIT
 	set_chr(99, 991,	-1,-1,6208,12678,0,		0,0202,0,";")//������ɥ��ƽ��񵱤���
 
 
+	if(F6_11_GameClear)
+		set_chr( 250,648,	 3, 7,     0,   0,  0,		0,	0, 0,";")	//�٥�٥�ץ�`��
+
 //�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D�D
 //	���ܥ��ّ顣
 //	�����r�����Ƥ�ե饰�����¤ΤȤ��ꡣ
@@ -70,7 +76,10 @@ INIT
 	}
 	else
 	{
-		set_chr(11, 760,  3,5,	-100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_01>")//760	�ܥ����`�����
+		if(F3100)//�ϩ`�ɥ��ꥢ
+			set_chr(11, 773,  3,5,	-100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_01>")//760	�ܥ����`�����
+		else
+			set_chr(11, 760,  3,5,	-100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_01>")//760	�ܥ����`�����
 	}
 
 	//ˮħ���ե���륬��	->Figure F2835
@@ -81,7 +90,10 @@ INIT
 	}
 	else
 	{
-		set_chr(12, 760,  3,5,	 300,  -350,	000,	0,0,2,"<EV_BOSS_GAME_02>")//760	�ܥ����`�����
+		if(F3101)//�ϩ`�ɥ��ꥢ
+			set_chr(12, 773,  3,5,	 300,  -350,	000,	0,0,2,"<EV_BOSS_GAME_02>")//760	�ܥ����`�����
+		else
+			set_chr(12, 760,  3,5,	 300,  -350,	000,	0,0,2,"<EV_BOSS_GAME_02>")//760	�ܥ����`�����
 	}
 	
 	//�������ӥ��ե��`��	->Figure F2834
@@ -92,7 +104,10 @@ INIT
 	}
 	else
 	{
-		set_chr(13, 760,  3,5,	 700,  -350,	000,	0,0,2,"<EV_BOSS_GAME_03>")//760	�ܥ����`�����
+		if(F3102)//�ϩ`�ɥ��ꥢ
+			set_chr(13, 773,  3,5,	 700,  -350,	000,	0,0,2,"<EV_BOSS_GAME_03>")//760	�ܥ����`�����
+		else
+			set_chr(13, 760,  3,5,	 700,  -350,	000,	0,0,2,"<EV_BOSS_GAME_03>")//760	�ܥ����`�����
 	}
 	
 	//��o�ե��֥˩`���	->Figure F2838	->Figure F2880
@@ -106,7 +121,10 @@ INIT
 	}
 	else
 	{
-		set_chr(14, 760,  3,5,	1125,  -350,	000,	0,0,2,"<EV_BOSS_GAME_04>")//760	�ܥ����`�����
+		if(F3103)//�ϩ`�ɥ��ꥢ
+			set_chr(14, 773,  3,5,	1125,  -350,	000,	0,0,2,"<EV_BOSS_GAME_04>")//760	�ܥ����`�����
+		else
+			set_chr(14, 760,  3,5,	1125,  -350,	000,	0,0,2,"<EV_BOSS_GAME_04>")//760	�ܥ����`�����
 
 		//------FIGURE------------
 		if(F2880)
@@ -135,7 +153,10 @@ INIT
 	}
 	else
 	{
-		set_chr(16, 765,  3,5,	1800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_06>")//760	�ܥ����`�����
+		if(F3104)//�ϩ`�ɥ��ꥢ
+			set_chr(16, 774,  3,5,	1800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_06>")//760	�ܥ����`�����
+		else
+			set_chr(16, 765,  3,5,	1800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_06>")//760	�ܥ����`�����
 
 		//------FIGURE------------
 		if(F2881)
@@ -157,7 +178,10 @@ INIT
 	}
 	else
 	{
-		set_chr(17, 765,  3,5,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_07>")//760	�ܥ����`�����
+		if(F3105)//�ϩ`�ɥ��ꥢ
+			set_chr(17, 774,  3,5,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_07>")//760	�ܥ����`�����
+		else
+			set_chr(17, 765,  3,5,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_07>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2882)
 		{
@@ -181,7 +205,10 @@ INIT
 	}
 	else
 	{
-		set_chr(18, 765,  3,5,	3100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_08>")//760	�ܥ����`�����
+		if(F3106)//�ϩ`�ɥ��ꥢ
+			set_chr(18, 774,  3,5,	3100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_08>")//760	�ܥ����`�����
+		else
+			set_chr(18, 765,  3,5,	3100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_08>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2883)
 		{
@@ -202,7 +229,10 @@ INIT
 	}
 	else
 	{
-		set_chr(15, 760,  3,5,	3750,  -350,	000,	0,0,2,"<EV_BOSS_GAME_05>")//760	�ܥ����`�����
+		if(F3107)//�ϩ`�ɥ��ꥢ
+			set_chr(15, 773,  3,5,	3750,  -350,	000,	0,0,2,"<EV_BOSS_GAME_05>")//760	�ܥ����`�����
+		else
+			set_chr(15, 760,  3,5,	3750,  -350,	000,	0,0,2,"<EV_BOSS_GAME_05>")//760	�ܥ����`�����
 	}
 
 	//���`�����륦�����	->Figure F2884
@@ -216,7 +246,10 @@ INIT
 	}
 	else
 	{
-		set_chr(19, 765,  3,6,	 550,  -350,	000,	0,0,2,"<EV_BOSS_GAME_09>")//760	�ܥ����`�����
+		if(F3108)//�ϩ`�ɥ��ꥢ
+			set_chr(19, 774,  3,6,	 550,  -350,	000,	0,0,2,"<EV_BOSS_GAME_09>")//760	�ܥ����`�����
+		else
+			set_chr(19, 765,  3,6,	 550,  -350,	000,	0,0,2,"<EV_BOSS_GAME_09>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2884)
 		{
@@ -242,7 +275,10 @@ INIT
 	}
 	else
 	{
-		set_chr(20, 760,  3,6,	1250,  -350,	000,	0,0,2,"<EV_BOSS_GAME_10>")//760	�ܥ����`�����
+		if(F3109)//�ϩ`�ɥ��ꥢ
+			set_chr(20, 773,  3,6,	1250,  -350,	000,	0,0,2,"<EV_BOSS_GAME_10>")//760	�ܥ����`�����
+		else
+			set_chr(20, 760,  3,6,	1250,  -350,	000,	0,0,2,"<EV_BOSS_GAME_10>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2885)
 		{
@@ -266,8 +302,14 @@ INIT
 	}
 	else
 	{
-		set_chr(21, 760,  3,6,	1950,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_01>")//760	�ܥ����`�����
-		set_chr(21, 760,  3,6,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_02>")//760	�ܥ����`�����
+		if(F3110)//�ϩ`�ɥ��ꥢ
+			set_chr(21, 773,  3,6,	1950,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_01>")//760	�ܥ����`�����
+		else
+			set_chr(21, 760,  3,6,	1950,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_01>")//760	�ܥ����`�����
+		if(F3111)//�ϩ`�ɥ��ꥢ
+			set_chr(21, 773,  3,6,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_02>")//760	�ܥ����`�����
+		else
+			set_chr(21, 760,  3,6,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_02>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2886)
 		{
@@ -291,7 +333,10 @@ INIT
 	}
 	else
 	{
-		set_chr(22, 760,  3,6,	2800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_12>")//760	�ܥ����`�����
+		if(F3112)//�ϩ`�ɥ��ꥢ
+			set_chr(22, 773,  3,6,	2800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_12>")//760	�ܥ����`�����
+		else
+			set_chr(22, 760,  3,6,	2800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_12>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2887)
 		{
@@ -310,8 +355,14 @@ INIT
 	}
 	else
 	{
-		set_chr(23, 760,  3,6,	5150,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_01>")//760	�ܥ����`�����
-		set_chr(23, 760,  3,6,	5650,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_02>")//760	�ܥ����`�����
+		if(F3113)//�ϩ`�ɥ��ꥢ
+			set_chr(23, 773,  3,6,	5150,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_01>")//760	�ܥ����`�����
+		else
+			set_chr(23, 760,  3,6,	5150,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_01>")//760	�ܥ����`�����
+		if(F3114)//�ϩ`�ɥ��ꥢ
+			set_chr(23, 773,  3,6,	5650,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_02>")//760	�ܥ����`�����
+		else
+			set_chr(23, 760,  3,6,	5650,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_02>")//760	�ܥ����`�����
 		//------FIGURE------------
 		if(F2888)
 		{
@@ -324,6 +375,26 @@ INIT
 		//------------------------
 	}
 
+
+//���������é�����������������������������������������������������������������������������������������������������������������������
+	workL(001,SET,0)
+	if(F3100 && F3101 && F3102 && F3103 && F3104 && F3105 && F3106 && F3107 )	
+		workL(001,ADD,1)
+	if(F3108 && F3109 && F3110 && F3111 && F3112 && F3113 && F3114 )	
+		workL(001,ADD,1)
+
+	if(WK001==2)
+	{
+		if(IT_TREASURE<1)
+			set_chr( TREASURE_CH,563,	 3,7,    -400, 0,  0,	6,   270,20,"<TK_PARTGG>;")	//�ٱ��䣨�K��
+		else
+			set_chr( TREASURE_CH,563,    3,7,    -400, 0,  0,	7,   270, 0,";")			//�ٱ��䣨�K��
+	}
+//���������é�����������������������������������������������������������������������������������������������������������������������
+
+
+
+
 	//���`������
 	if(GW_ENTRY_EVENT==101)//���x���`��������֑鎢��
 	{
@@ -415,6 +486,46 @@ INIT
 		EV("EV_BOSS_GAME_13_02B")
 	}
 
+
+
+}
+
+
+//��������F���٥�ȩ�����������������������������������������������������������������������������������������������������������������������
+//���`���󥳥�ץ�`�Ȥ�����
+EV_SPAWN_TREASUREBOX
+{
+	if(!F1_04_GameCenCmp)
+	{
+			
+		if(WK001==2)
+		{
+			F_set(F1_04_GameCenCmp)			//�沈�`���󥳥�ץ�`�ȣ�������F
+			
+			color(TREASURE_CH,-1)
+				
+			cross_fade(30)
+			CAM_move_chr(TREASURE_CH,0,0)
+			wait_CAM_move()
+			wait_fade()
+			wait(20)
+			
+			SE( 1016, TREASURE_CH)
+
+			EFF_chr(24580, TREASURE_CH, 0, 100, -1, "root")
+			
+			color(TREASURE_CH,20)
+			wait(60)		
+			
+			fade_in(100,30,0)
+			wait_fade()
+			CAM_return(0)
+			CAM(670,112,80,23,180,0,0)
+			wait(15)
+			fade_in(0,30,0)
+			wait_fade()	
+		}	
+	}
 }
 
 
@@ -432,6 +543,10 @@ EV_BOSS_GAME_01B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+			
 	TK_end()
 }
 //ˮħ���ե���륬
@@ -446,6 +561,10 @@ EV_BOSS_GAME_02B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //�������ӥ��ե��`
@@ -460,6 +579,10 @@ EV_BOSS_GAME_03B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //��o�ե��֥˩`��
@@ -474,6 +597,10 @@ EV_BOSS_GAME_04B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //���������륬�ꥪ��
@@ -488,6 +615,10 @@ EV_BOSS_GAME_05B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //èħ�˥��֥��
@@ -502,6 +633,10 @@ EV_BOSS_GAME_06B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //���Ǒ�ʿ���������
@@ -516,6 +651,10 @@ EV_BOSS_GAME_07B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+		
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //ħ��ʹ���ƥ�ߥɩ`��
@@ -530,6 +669,10 @@ EV_BOSS_GAME_08B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //���`�����륦����
@@ -541,10 +684,13 @@ EV_BOSS_GAME_09B
 	chr_pos(RAGNA,		6300,11150,0,210,	2)
 	chr_pos(PARTNER, 	6500,11150,0,120,	2)
 	chr_pos(PET,	 	6400,11300,0,180,	2)
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //�¤Α����������
@@ -559,6 +705,10 @@ EV_BOSS_GAME_10B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //��Ѫ������ϩ`��
@@ -573,6 +723,10 @@ EV_BOSS_GAME_11_01B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //���楶�ϩ`��
@@ -587,6 +741,10 @@ EV_BOSS_GAME_11_02B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //�}ӑ��܊�ƥ�ߥɩ`��
@@ -601,6 +759,10 @@ EV_BOSS_GAME_12B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //��륻�ǥ�������
@@ -615,6 +777,10 @@ EV_BOSS_GAME_13_01B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //ħ���륷����
@@ -629,6 +795,10 @@ EV_BOSS_GAME_13_02B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 
@@ -639,6 +809,14 @@ EV_BOSS_GAME_13_02B
 //ʹ��ʤ������ߥ󥰤⤢�뤱��һ��������
 SET_WARP_FLAG
 {
+	//0924׷��
+	if(!F6_00_GoToMeru)
+	{
+		SCORE(-2,92,0);//�����磮�о@��	���`�����륦����
+		SCORE(-2,93,0);//�����磮�о@��	����������
+		SCORE(-2,94,0);//�����磮�K��	���ϩ`�룯�楶�ϩ`��
+	}
+
 	//����
 	if(F6_00_GoToMeru)
 		workG(GW_WARP_FLAG,SET,1)//��`���S��
diff --git a/scp_jp_conv/map/0/EV00533.txt b/scp_conv/map/0/EV00533.txt
index 66874fe..1fbce5c 100644
--- a/scp_jp_conv/map/0/EV00533.txt
+++ b/scp_conv/map/0/EV00533.txt
@@ -130,7 +130,7 @@ INIT
 		set_chr(19, 365,  5,6,	2800,-300,	140,	-115,0,0,";");
 	if(F2827)
 		set_chr(20, 366,  5,6,	3200,-300,	140,	-150,0,0,";");
-	if(F2811)
+	if(F2711)
 		set_chr(21, 126,  5,6,	3600,-300,	140,	-100,0,0,";");
 	if(F2817)
 		set_chr(22, 353,  5,6,	4000,-300,	140,	-100,0,0,";");
@@ -275,7 +275,7 @@ INIT
 		workL(001,ADD,1)
 	if(F2827)
 		workL(001,ADD,1)
-	if(F2811)
+	if(F2711)
 		workL(001,ADD,1)
 	if(F2817)
 		workL(001,ADD,1)
diff --git a/scp_jp_conv/map/0/EV00535.txt b/scp_conv/map/0/EV00535.txt
index 5949d61..b93313e 100644
--- a/scp_jp_conv/map/0/EV00535.txt
+++ b/scp_conv/map/0/EV00535.txt
@@ -121,7 +121,7 @@ INIT
 		set_chr(17, 136,  3,6,	4100,-300,	140,	-100,0,0,";");
 	if(F2773)
 		set_chr(18, 229,  3,6,	4375,-300,	140,	-100,0,0,";");
-	if(F2790)
+	if(F2791)
 		set_chr(19, 269,  3,6,	4650,-300,	140,	-100,0,0,";");
 	if(F2796)
 		set_chr(20, 277,  3,6,	4925,-300,	140,	-100,0,0,";");
@@ -223,7 +223,7 @@ INIT
 		workL(001,ADD,1)
 	if(F2773)
 		workL(001,ADD,1)
-	if(F2790)
+	if(F2791)
 		workL(001,ADD,1)
 	if(F2796)
 		workL(001,ADD,1)
diff --git a/scp_jp_conv/map/0/EV00536.txt b/scp_conv/map/0/EV00536.txt
index f8edd8d..57ca197 100644
--- a/scp_jp_conv/map/0/EV00536.txt
+++ b/scp_conv/map/0/EV00536.txt
@@ -101,9 +101,9 @@ INIT
 		set_chr(7, 	231,  3,6,	1600,-300,	140,	-100,0,0,";");
 	if(F2757)                  
 		set_chr(8, 	213,  3,6,	1900,-300,	140,	-100,0,0,";");
-	if(F2721)                  
-		set_chr(9, 	282,  3,6,	2200,-300,	140,	-100,0,0,";");
 	if(F2833)                  
+		set_chr(9, 	282,  3,6,	2200,-300,	140,	-100,0,0,";");
+	if(F2830)                  
 		set_chr(10,	372,  3,6,	2500,-300,	140,	-100,0,0,";");
 
 	if(F2716)
@@ -117,9 +117,9 @@ INIT
 	if(F2800)
 		set_chr(15, 281,  3,6,	6200,-300,	140,	-100,0,0,";");
 
-	if(F2701)
+	if(F2831)
 		set_chr(16, 370,  5,6,	3100,-300,	140,	-100,0,0,";");
-	if(F2701)
+	if(F2832)
 		set_chr(17, 371,  5,6,	3700,-300,	140,	-100,0,0,";");
 
 
@@ -139,6 +139,7 @@ INIT
 	F_set_chr(14,CF_NO_MINIMAP)
 	F_set_chr(15,CF_NO_MINIMAP)
 	F_set_chr(16,CF_NO_MINIMAP)
+	F_set_chr(17,CF_NO_MINIMAP)
 	
 //�ե����奢̨������������������������������������������������������������������������������������������������������������������������
 
@@ -199,10 +200,10 @@ INIT
 		workL(001,ADD,1)
 	if(F2757)                  
 		workL(001,ADD,1)
-	if(F2721)                  
-		workL(001,ADD,1)
 	if(F2833)                  
 		workL(001,ADD,1)
+	if(F2830)                  
+		workL(001,ADD,1)
 
 	if(F2716)
 		workL(001,ADD,1)
@@ -215,9 +216,9 @@ INIT
 	if(F2800)
 		workL(001,ADD,1)
 
-	if(F2701)
+	if(F2831)
 		workL(001,ADD,1)
-	if(F2701)
+	if(F2832)
 		workL(001,ADD,1)
 	if(F2837)
 		workL(001,ADD,1)
diff --git a/scp_jp_conv/map/0/EV00600.txt b/scp_conv/map/0/EV00600.txt
index d6de88e..b9653be 100644
--- a/scp_jp_conv/map/0/EV00600.txt
+++ b/scp_conv/map/0/EV00600.txt
@@ -68,6 +68,9 @@ INIT
 
 	set_chr(100,990,	-1,-1,     0,-5300,  200,    0, 0813, 6,"<EV_SeeFirst>")	//��Ҋ���٥����
 
+	//������
+	set_chr( 81,991,	-1,-1,	 -1520,3830,-1450,   0,  0202,	0,";")		//0922׷��
+
 	//NPC
 	
 
@@ -619,7 +622,11 @@ EV_Meets_Cleese
 	look_off(RAGNA)
 	look_off(PET)
 	look_off(PARTNER)
-
+	
+	KAO(RAGNA,   "1","1","1")
+	KAO(PARTNER, "9","1","7")
+	KAO(PET,     "1","1","1")
+	
 	//����������O����
 	CAM_return( 0 )
 	wait(30)
@@ -885,15 +892,15 @@ EV_Survant_Cleese
 	fade_in(100,30,BLACK)
 	wait_fade()
 
+	KAO(RAGNA,   "1","1","1")
+	KAO(PARTNER, "9","1","7")
+	KAO(PET,     "1","1","1")
+
 	//����������O����
 	CAM_return( 0 )
 	wait(30)
 
 	F_reset_chr(CLEESE,CF_NO_CSP)
-
-	KAO(RAGNA,"1","1","1")
-	KAO(PET,"1","1","1")
-	KAO(PARTNER,"1","1","1")
 	
 	F_set_chr(S_MONTBLANC,CF_NO_MOVE)
 	F_set_chr(CLEESE,CF_NO_MOVE)
diff --git a/scp_jp_conv/map/0/EV00601.txt b/scp_conv/map/0/EV00601.txt
index 9d05543..f2d729d 100644
--- a/scp_jp_conv/map/0/EV00601.txt
+++ b/scp_conv/map/0/EV00601.txt
@@ -450,7 +450,7 @@ EV_5_22_ReturnCrystal
 	F_set_chr(LUE,CF_NO_CSP)
 
 	wait(1)
-	chr_equip( ALWEN,"wp_004", "Bone_RightSword", 100)	//�Ȥ�װ�䤵����ΤϤ����顣
+	chr_equip( ALWEN,"wp_004b", "Bone_RightSword", 100)	//�Ȥ�װ�䤵����ΤϤ����顣
 //	MOT(AWEN,53,1)										//���륦��������֤��_�����롣
 
 	//��������λ��
diff --git a/scp_jp_conv/map/0/EV00602.txt b/scp_conv/map/0/EV00602.txt
index 6b875ce..6ef4c03 100644
--- a/scp_jp_conv/map/0/EV00602.txt
+++ b/scp_conv/map/0/EV00602.txt
@@ -82,12 +82,12 @@ EV_LocateZacos
 
 
 	set_chr(MONSTER_D1,	  144,-1,-1,   -200,10000,4680,		 2,   0, 0, "D0_36;")	// ���ޤ��֤��`
-		set_chr( 36,		  808,-1,-1,      0, 8000,5480,		 3,   0, 0, "")	// �ȥ���
+		set_chr( 36,		  808,-1,-1,      0, 8000,5480,		 4,   0, 0, "")	// �ȥ���
 		chr_equip_chr(36,MONSTER_D1,"Bone_Hips", 125,  0, 0,0,	 0,50,25);
 
 
 	set_chr(MONSTER_D2,	  144,-1,-1,    200, 9000,5080,		 2,   0, 0, "D0_37;")	// ���ޤ��֤��`
-		set_chr( 37,		  808,-1,-1,      0, 8000,5480,		 3,   0, 0, "")	// �ȥ���
+		set_chr( 37,		  808,-1,-1,      0, 8000,5480,		 4,   0, 0, "")	// �ȥ���
 		chr_equip_chr(37,MONSTER_D2,"Bone_Hips", 125,  0, 0,0,	 0,50,25);
 
 
diff --git a/scp_jp_conv/map/0/EV00800.txt b/scp_conv/map/0/EV00800.txt
index ba51247..aa245c3 100644
--- a/scp_jp_conv/map/0/EV00800.txt
+++ b/scp_conv/map/0/EV00800.txt
@@ -2039,7 +2039,7 @@ EV_6_17_GameClear_to2
 		get_item(201,1,1)
 	}
 	else
-	if(GW_TREASURE<47)
+	if(GW_TREASURE<48)				//�ѥå� 2008/09/22 47 -> 48 ���
 	{
 		get_item(162,1,1)
 		get_item(166,1,1)
@@ -2155,6 +2155,9 @@ EV_6_17_GameClear_to2
 	menuTXT(3,	"�����`�֤��ʤ�",	20,GREEN)
 	menuEVENT(3,"EV_SAVE_OFF","EV_SAVE_OFF","")
 
+//	name("�����ƥ��å��`��")
+	MES_pos(0,"C3���Υ��ꥢ�ǩ`�����`�ɤ��뤳�Ȥˤ�ꡢ\nһ���Υǩ`���������@����״�B�ǡ�\n���Z��ʼ�ᤫ��ץ�`�����¤��Ǥ��ޤ���\n�ޤ����N׷��Ҫ�ؤ��[�٤�褦�ˤʤ�ޤ���",2,172,296,300,100)
+
 	wait_W(WK_YESNO)
 
 	menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
@@ -2162,6 +2165,8 @@ EV_6_17_GameClear_to2
 	menu(3,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
 	wait_menu(1)
 
+	MES_close(0)
+
 	if(WK_YESNO==2)
 	{
 	}
diff --git a/scp_jp_conv/map/0/EV10902.txt b/scp_conv/map/0/EV10902.txt
index 772e482..68f3513 100644
--- a/scp_jp_conv/map/0/EV10902.txt
+++ b/scp_conv/map/0/EV10902.txt
@@ -81,6 +81,10 @@ INIT
 	//set_chr( 1,622,	1,4,    0800, 0500,  0,    2, 0,	0,"") //ʯ�����t��
 	set_chr( 1,623,	1,4,    1200, 0500,  0,    2, 0,	0,"") //���������
 	set_chr( 1,624,	1,4,    1600, 0500,  0,    2, 0,	0,"") //��ܞ��
+	//set_chr( 1,760,	1,4,    0000, 1000,  0,    2, 0,	0,"") //�ܥ����`�����1
+	set_chr( 1,773,	1,4,    0000, 1000,  0,    2, 0,	0,"") //�ܥ����饦��1
+	//set_chr( 1,765,	1,4,    0400, 1000,  0,    2, 0,	0,"") //�ܥ����`�����2
+	set_chr( 1,774,	1,4,    0400, 1000,  0,    2, 0,	0,"") //�ܥ����饦��2
 
 	set_chr( 1,633,	3,1,   -600,0,  0,      2,  270,	0,"") //�ҥӱ�
 	set_chr( 1,633,	3,1,   -1000,0,  0,      2,  90,	0,"") //�ҥӱ�
diff --git a/scp_jp_conv/map/0/EV20901.txt b/scp_conv/map/0/EV20901.txt
index da7571e..eb7e7ab 100644
--- a/scp_jp_conv/map/0/EV20901.txt
+++ b/scp_conv/map/0/EV20901.txt
@@ -99,6 +99,10 @@ INIT
 	set_chr( 60,097,	3,4,   0700,1000,  0,  	 2,  0,	20,"") //�������߷�
 	set_chr( 61,062,	3,4,   1200,1000,  0,  	 2,  0,	20,"") //��������
 
+	set_chr( 61,081,	3,4,   -300,1500,  0,  	 2,  0,	20,"") //�ڥ󥮥�
+	set_chr( 61,1006,	3,4,   -100,1500,  0,  	 2,  0,	20,"") //�ڥ󥮥����g��
+	set_chr( 61,1106,	3,4,   0200,1500,  0,  	 2,  0,	20,"") //����ȥӥڥ󥮥�
+
 
 }
 
diff --git a/scp_jp_conv/map/0/EV52902.txt b/scp_conv/map/0/EV52902.txt
index 5c28095..d1ad5d9 100644
--- a/scp_jp_conv/map/0/EV52902.txt
+++ b/scp_conv/map/0/EV52902.txt
@@ -69,9 +69,7 @@ INIT
 	set_chr( 1,99,1,4,     2000,1000,  0,  	 2,  0,	0,"") //Ů�Ӹ��Ʒ����륦����
 
 	set_chr( 1,1064,1,4,   -400,1500,  0,  	 2,  0,	0,"") //���ԥ��ƥ�ߥɩ`��
-
-
-
+	set_chr( 1,1069,1,4,    000,1500,  0,  	 2,  0,	0,"") //�ѥ󥯥�å�
 }
 
 #EndScriptTable
diff --git a/scp_jp_conv/map/0/MC00012.bmp b/scp_conv/map/0/MC00012.bmp
index 9faba38..7215eff 100644
Binary files a/scp_jp_conv/map/0/MC00012.bmp and b/scp_conv/map/0/MC00012.bmp differ
diff --git a/scp_jp_conv/map/0/MC00042.bmp b/scp_conv/map/0/MC00042.bmp
index ac7a942..558f2ee 100644
Binary files a/scp_jp_conv/map/0/MC00042.bmp and b/scp_conv/map/0/MC00042.bmp differ
diff --git a/scp_jp_conv/map/0/MC00052.bmp b/scp_conv/map/0/MC00052.bmp
index ac7a942..94b9bba 100644
Binary files a/scp_jp_conv/map/0/MC00052.bmp and b/scp_conv/map/0/MC00052.bmp differ
