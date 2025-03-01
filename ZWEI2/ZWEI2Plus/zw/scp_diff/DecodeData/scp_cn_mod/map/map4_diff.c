diff --git a/scp_jp_conv/map/4/EV40000.txt b/scp_conv/map/4/EV40000.txt
index 6f14557..0afb54f 100644
--- a/scp_jp_conv/map/4/EV40000.txt
+++ b/scp_conv/map/4/EV40000.txt
@@ -48,6 +48,15 @@ INIT
 	{
 		set_chr( 93,990,	-1,-1,   51,4849,-385,   180, 1601,11,"<LP_IronTower>")	//沈黙時ＬＰ
 	}
+	//0922追加
+	else
+	{
+		//アタリ
+		set_chr( 81,991,	-1,-1,	 -390,4840,-400,   0,  0202,	0,";")
+		set_chr( 82,991,	-1,-1,	 510,4840,-400,   0,  0202,	0,";")
+		set_chr( 83,991,	-1,-1,	340,1190,0,   0,  0206,	0,";")
+		set_chr( 84,991,	-1,-1,	-330,1190,0,   0,  0206,	0,";")
+	}
 
 	//NPC
 	//⑤３妖精
@@ -885,6 +894,11 @@ EV_2_05_IntoTower
 //ＧＦ『★大鉄塔に入れるようになった』を立てる。
 	F_set(F2_04_IntoTower)
 	delete(93)
+	//アタリ
+	set_chr( 81,991,	-1,-1,	 -390,4840,-400,   0,  0202,	0,";")
+	set_chr( 82,991,	-1,-1,	 510,4840,-400,   0,  0202,	0,";")
+	set_chr( 83,991,	-1,-1,	340,1190,0,   0,  0206,	0,";")
+	set_chr( 84,991,	-1,-1,	-330,1190,0,   0,  0206,	0,";")
 
 	fade_in(0,30,0)
 
diff --git a/scp_jp_conv/map/4/EV40100.txt b/scp_conv/map/4/EV40100.txt
index 38a8797..f9c245c 100644
--- a/scp_jp_conv/map/4/EV40100.txt
+++ b/scp_conv/map/4/EV40100.txt
@@ -13,6 +13,27 @@
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
 //環境SE
 	SE(63,0)
 	SE(65,0)
@@ -40,22 +61,77 @@ INIT
 	set_obj("@ob40020a", 3, 4,     0,   0,  0,		270)						//③アーチ（塔）
 	set_chr(192,1400,	 3, 4,	   0,   0,  0,		  0,   270, 0,";")			//アーチ（ダミー）
 
-	set_chr( 93,990,	 7, 4,     0,   0,  0,		 90,  0102, 6,"K0_14051;")	//④エントリ 無幻①
+	set_chr( 93,990,	 7, 4,     0,   0,  0,		 90,  0102, 6,"RF2060 K0_14051;")	//④エントリ 無幻①
 	set_obj("@ob40020a", 7, 4,     0,   0,  0,		 90)						//④アーチ（塔）
 	set_chr(193,1400,	 7, 4,	   0,   0,  0,		  0,    90, 0,";")			//アーチ（ダミー）
 
+	if( Fx_MUGEN2_OPENED )
+	{
+		set_chr( 94,990,	 6, 5,     0, 150,  0,		180,  0102, 6,"SF2060 K0_14051;")	//エントリ 無幻EX①
+		set_obj("@ob40020a", 6, 5,     0, 150,  0,		180)						//アーチ（塔）
+		set_chr(194,1400,	 6, 5,	   0, 150,  0,		  0,   180, 0,";")			//アーチ（ダミー）
+
+//x		set_chr( 60,648,	 6, 5,     0,-450,  0,		 99,   180, 0,";")	//レベルプレート
+//x		color2( 60, 100,88,91,0,0,0)
+		set_chr( 61,654,	 6, 5,  -250,-450,  0,		  6,   262, 0,";")	//順路案内（無限EX）
+		set_chr( 62,654,	 6, 5,  -250,-450,140,		  6,   278, 0,";")	//順路案内（無限EX）
+
+		set_obj2("mp40480",   6, 4, -450,-450,  0,	 0) //
+		set_obj2("mp40490",   6, 4,  450,-450,  0,	 0) //
+		set_obj2("mp40260",   6, 4, -450, 450,  0,	 0) //
+		set_obj2("mp40270",   6, 4,  450, 450,  0,	 0) //
+
+		set_obj2("mp40440",   6, 5, -450,-450,  0,	 0) //
+		set_obj2("mp40450",   6, 5,  450,-450,  0,	 0) //
+		set_obj2("mp40220",   6, 5, -450, 450,  0,	 0) //
+		set_obj2("mp40230",   6, 5,  450, 450,  0,	 0) //
+	}
+	else
+	{
+		set_obj2("mp40480",   6, 4, -450,-450,  0,	 0) //
+		set_obj2("mp40490",   6, 4,  450,-450,  0,	 0) //
+		set_obj2("mp40500",   6, 4, -450, 450,  0,	 0) //
+		set_obj2("mp40510",   6, 4,  450, 450,  0,	 0) //
+
+		set_obj("mp40160",    6, 5, -450,-450,  0,	 0) //
+	}
+
 	set_chr( 52,500,	 4, 4,  -900,   0,  0,		  3,    90, 6,";")			//⑤扉（塔）自由
 	set_chr( 53,500,	 6, 4,   900,   0,  0,		  7,   270, 6,";")			//⑥扉（塔）一通
+	if ( F6_11_GameClear )
+	{
+		set_chr( 51,500,	 6, 5,     0,-900,  0,		 7,      0, 6,";")			//扉（塔） 一通
+	}
 	if ( !F6_00_GoToMeru )
 	{
 		set_chr(149,769,	 6, 4,   900,   0,175,		  0,  270, 0,";")	//無限封印
 		set_chr(150,991,	 6, 4,   900,   0,  0,		  0, 0205, 0,";")	//無限封印アタリ
+		if ( F6_11_GameClear )
+		{
+			set_chr(147,769,	 6, 5,     0,-900,175,		  0,  180, 0,";")	//無限封印
+			set_chr(148,991,	 6, 5,     0,-900,  0,		180, 0502, 0,";")	//無限封印アタリ
+		}
 	}
 	else
 	{
 		MOT( 53, 6, 0 )
+		if( Fx_MUGEN2_OPENED )
+		{
+			MOT( 51, 6, 0 )
+		}
 	}
 
+//	set_chr( 51,500,	 6, 5,     0,-900,  0,		 7,      0, 6,";")			//扉（塔） 一通
+//	if ( !Fx_MUGEN2_OPENED )
+//	{
+//		set_chr(147,769,	 6, 5,     0,-900,175,		  0,  180, 0,";")	//無限封印
+//		set_chr(148,991,	 6, 5,     0,-900,  0,		180, 0502, 0,";")	//無限封印アタリ
+//	}
+//	else
+//	{
+//		MOT( 51, 6, 0 )
+//	}
+
 	set_chr(161,991,	 5, 3,  -650,   0,2000,		  0,200113, 0,";")	//空気壁 L┃
 	set_chr(162,991,	 5, 3,  -450, 600,2000,		  0,200501, 0,";")	//空気壁 L┗
 	set_chr(163,991,	 5, 3,   650,   0,2000,		  0,200113, 0,";")	//空気壁 R┃
@@ -74,6 +150,7 @@ INIT
 	color2( 56, 100,88,91,0,0,0)
 	set_chr( 59,654,	 6, 4,   600,-175,  0,		  6,     0, 0,";")	//③順路案内（無限）
 
+
 	set_chr( 65,660,	 5, 3,     0,-325,  0,		  2,     0, 8,"(M4?99 WT?15 Z1_50 Z2_1875 WT?60 Z3_-1875 M5_99 Z1_-50);")	//②プロペラ移動床
 	set_chr( 66,669,	 5, 3,  -425,-325,  0,		  2,   270, 0," ;")	//③扇風機
 	set_chr( 67,570,	 5, 3,     0   75,  0,		  6,     0, 5,"SF102")	//⑤ボタンスイッチ
diff --git a/scp_jp_conv/map/4/EV40130.txt b/scp_conv/map/4/EV40130.txt
index e4f0de0..a82e0c8 100644
--- a/scp_jp_conv/map/4/EV40130.txt
+++ b/scp_conv/map/4/EV40130.txt
@@ -142,24 +142,28 @@ INIT
 	{
 		set_chr( 75,810,	 3, 5,     0,   0,  0,		   2,    0, 0,"D1_40;"); //④大砲
 		set_chr(175,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F75 I_$$$2 SF2190;");
+		chr_equip_chr(175,75,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	if ( !F2191 )
 	{
 		set_chr( 76,810,	 5, 3,     0,   0,  0,		   2,    0, 0,"D1_41;"); //⑤大砲
 		set_chr(176,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F76 I_$$$2 SF2191;");
+		chr_equip_chr(176,76,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	if ( !F2192 )
 	{
 		set_chr( 77,810,	 7, 5,     0,   0,  0,		   2,    0, 0,"D1_42;"); //⑥大砲
 		set_chr(177,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F77 I_$$$2 SF2192;");
+		chr_equip_chr(177,77,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	if ( !F2193 )
 	{
 		set_chr( 78,810,	 5, 7,     0,   0,  0,		   2,    0, 0,"D1_43;"); //⑦大砲
 		set_chr(178,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F78 I_$$$2 SF2193;");
+		chr_equip_chr(178,78,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 
diff --git a/scp_jp_conv/map/4/EV40190.txt b/scp_conv/map/4/EV40190.txt
index 56be664..2822d66 100644
--- a/scp_jp_conv/map/4/EV40190.txt
+++ b/scp_conv/map/4/EV40190.txt
@@ -61,15 +61,45 @@ INIT
 //■スイッチ．看板
 	set_chr( 50,620,	-1,-1,    0,2400,-120,   0,180,	0,";")			//①セーブOBJ
 
-	set_chr( 55,648,	-1,-1, 1150,  50,880,   10,270,	0,";")	//レベルプレート
-	color2( 55, 100,88,81,0,0,0)
+//	set_chr( 55,648,	-1,-1, 1150,  50,880,   10,270,	0,";")	//レベルプレート
+//	color2( 55, 100,88,81,0,0,0)
 
 	set_chr( 57,654,	-1,-1,  750,-750,880,    4,305,	0,";")	//順路案内（武器）
 
-	set_chr( 56,648,	-1,-1,-1920, 160,880,   11, 50,	0,";")	//レベルプレート
-	color2( 56, 100,88,81,0,0,0)
+//	set_chr( 56,648,	-1,-1,-1920, 160,880,   11, 50,	0,";")	//レベルプレート
+//	color2( 56, 100,88,81,0,0,0)
 
 	set_chr( 58,654,	-1,-1,-1575, 350,880,    3, 80,	0,";")	//順路案内（ボス）
+	
+	//0924修正
+	if(F2_08_CancelBurn)
+	{
+		set_chr( 55,648,	-1,-1, 1150,  50,880,   10,270,	0,";")	//レベルプレート
+		color2( 55, 100,88,81,0,0,0)
+	}
+	else
+	{
+		set_chr( 55,648,	-1,-1, 6150,  50,880,   10,270,	0,";")	//レベルプレート
+		color2( 55, 100,88,81,0,0,0)
+		color( 55, -1)
+		
+		set_chr( 83,772,	-1,-1, 1150,  50,880,   10,270,	0,";")	//ダミープレート
+		color2( 83, 100,88,81,0,0,0)
+	}
+	if(F2_15_CancelWind)
+	{
+		set_chr( 56,648,	-1,-1,-1920, 160,880,   11, 50,	0,";")	//レベルプレート
+		color2( 56, 100,88,81,0,0,0)
+	}
+	else
+	{
+		set_chr( 56,648,	-1,-1,-6920, 160,880,   11, 50,	0,";")	//レベルプレート
+		color2( 56, 100,88,81,0,0,0)
+		color( 56, -1)
+
+		set_chr( 84,772,	-1,-1,-1920, 160,880,   11, 50,	0,";")	//ダミープレート
+		color2( 84, 100,88,81,0,0,0)
+	}
 
 //■イベント
 	//ＧＦ『★大鉄塔：燃える扉を水魔法で解除した』立ってない
@@ -77,7 +107,7 @@ INIT
 	{
 		set_chr( 60,704,	-1,-1,  755, 520,1210,   2,  0, 8,"M1?60 SF100 <EV_F_R_SwitchON> D0_160;") //
 		set_chr( 61,704,	-1,-1,  805,-470,1210,   2,  0, 8,"M1?61 SF101 <EV_F_L_SwitchON> D0_161;") //
-		set_chr( 80,990,	-1,-1,    0,   0,  0,    0,  0, 8,"F100 F101 WT?20 O1_18 WT?40 <EV_2_09_CancelBurn>;") //火-達成
+		set_chr( 82,990,	-1,-1,    0,   0,  0,    0,  0, 8,"F100 F101 WT?20 O1_18 WT?40 <EV_2_09_CancelBurn>;") //火-達成
 
 		set_chr(160,374,	-1,-1,  755, 520,1210,   0,  0, 0,";")
 		set_chr(161,374,	-1,-1,  805,-470,1210,   0,  0, 0,";")
@@ -181,6 +211,9 @@ EV_W_R_SwitchON
 	mot_obj("wind02","anim01")
 
 	SE(1064,0)
+	
+	if(F103)
+		workG(GW_WARP_FLAG,SET,0)//ワープ封じる0924
 }
 EV_W_L_SwitchON
 {
@@ -188,6 +221,9 @@ EV_W_L_SwitchON
 	mot_obj("wind01","anim01")
 
 	SE(1064,0)
+	
+	if(F102)
+		workG(GW_WARP_FLAG,SET,0)//ワープ封じる0924
 }
 
 //──────────────────────────────
@@ -213,10 +249,10 @@ EV_2_07_OnTowerHalf
 	F_set_chr(53,CF_NO_CLIP2)
 	F_set_chr(54,CF_NO_CLIP)
 	F_set_chr(54,CF_NO_CLIP2)
-	F_set_chr(55,CF_NO_CLIP)
-	F_set_chr(55,CF_NO_CLIP2)
-	F_set_chr(56,CF_NO_CLIP)
-	F_set_chr(56,CF_NO_CLIP2)
+	F_set_chr(83,CF_NO_CLIP)
+	F_set_chr(83,CF_NO_CLIP2)
+	F_set_chr(84,CF_NO_CLIP)
+	F_set_chr(84,CF_NO_CLIP2)
 	F_set_chr(57,CF_NO_CLIP)
 	F_set_chr(57,CF_NO_CLIP2)
 	F_set_chr(58,CF_NO_CLIP)
@@ -332,10 +368,10 @@ EV_2_07_OnTowerHalf
 	F_reset_chr(53,CF_NO_CLIP2)
 	F_reset_chr(54,CF_NO_CLIP)
 	F_reset_chr(54,CF_NO_CLIP2)
-	F_reset_chr(55,CF_NO_CLIP)
-	F_reset_chr(55,CF_NO_CLIP2)
-	F_reset_chr(56,CF_NO_CLIP)
-	F_reset_chr(56,CF_NO_CLIP2)
+	F_reset_chr(83,CF_NO_CLIP)
+	F_reset_chr(83,CF_NO_CLIP2)
+	F_reset_chr(84,CF_NO_CLIP)
+	F_reset_chr(84,CF_NO_CLIP2)
 	F_reset_chr(57,CF_NO_CLIP)
 	F_reset_chr(57,CF_NO_CLIP2)
 	F_reset_chr(58,CF_NO_CLIP)
@@ -651,7 +687,7 @@ EV_2_09_CancelBurn
 	MES_close(PIPIRO)
 	EV_stop("TK_POCKLE")
 	MES_close(POCKLE)
-	wait(1)
+//	wait(1)
 
 	EV_begin()
 
@@ -998,6 +1034,13 @@ EV_2_09_CancelBurn
 	set_chr( 90,990,	-1,-1, -30, 950,-120,    0,0201,6,"K1_14013;")	//①エントリ メイン③
 	workG(GW_WARP_FLAG,SET,1)//ワープ解除。
 
+//プレートを本物に戻す0924
+	delete(83)
+//	set_chr( 55,648,	-1,-1, 1150,  50,880,   10,270,	0,";")	//レベルプレート
+//	color2( 55, 100,88,81,0,0,0)
+	chr_pos(55,1150,  50,880,270,-1)
+	color(55,1)
+
 	fade_in(0,30,0)
 
 	EV_end()
@@ -1216,6 +1259,15 @@ EV_2_20_CancelWind
 //ＧＦ『★大鉄塔：風車の扉を開いた』を立てる。
 	F_set(F2_15_CancelWind)
 
+	workG(GW_WARP_FLAG,SET,1)//ワープ解除。
+	
+//プレートを本物に戻す0924
+	delete(84)
+//	set_chr( 56,648,	-1,-1,-1920, 160,880,   11, 50,	0,";")	//レベルプレート
+//	color2( 56, 100,88,81,0,0,0)
+	chr_pos(56,-1920, 160,880,50,-1)
+	color(56,1)
+
 	fade_in(0,30,0)
 
 	EV_end()
diff --git a/scp_jp_conv/map/4/EV40420.txt b/scp_conv/map/4/EV40420.txt
index 524f90e..6d2faed 100644
--- a/scp_jp_conv/map/4/EV40420.txt
+++ b/scp_conv/map/4/EV40420.txt
@@ -122,7 +122,7 @@ INIT
 
 	if ( !F2185 )
 	{
-		set_chr( 69 641,	 6, 4,   100,   0,  0,		  4,     0, 0,"I_$$$1 SF2185;")	//①パラボラアンテナ
+		set_chr( 69 641,	 6, 4,   100,   0,  0,		  4,     0, 0,"I_$$$2 SF2185;")	//①パラボラアンテナ
 	}
 
 //■敵
diff --git a/scp_jp_conv/map/4/EV40430.txt b/scp_conv/map/4/EV40430.txt
index c54a8b2..625cbeb 100644
--- a/scp_jp_conv/map/4/EV40430.txt
+++ b/scp_conv/map/4/EV40430.txt
@@ -18,6 +18,8 @@
 // 106 メイドアニメ割り込み
 // 107 イベント終了待ちワーク
 
+// 108 メイドアクティブ
+
 #WOODBOX_CH	48
 #IT_WOODBOX	189		//∴189しいたけ
 
@@ -91,9 +93,16 @@ INIT
 	set_chr( 55,665,	 5, 4,   150, 900,  0,		  2,     0, 8,"M3?99 SF100 M5_50 #3_50;")		//①ゴング ①敵
 
 	set_chr( 56,650,	 5, 3,     0,-350,  0,		  2,     0, 0,";"); //②苗床
-	set_chr( 57,664,	 5, 3,     0,   0,  0,		  2,     0, 8,"(M2!99 WT?150 M2_99 O0_1324 WT?20);");  //②豆電球
+	if ( F6_00_GoToMeru )
+	{
+		set_chr( 57,664,	 5, 3,     0,   0,  0,		  3,     0, 8,"M3!99 M0_99 O1_18 <EV_MaidLiftOff> WT?40 M2_99 (M2!99 WT?150 M2_99 O0_1324 WT?20);");  //②豆電球
+	}
+	else
+	{
+		set_chr( 57,664,	 5, 3,     0,   0,  0,		  2,     0, 8,"(M2!99 WT?150 M2_99 O0_1324 WT?20);");  //②豆電球
+	}
 	set_chr( 58,991,	 5, 3,     0,-350,  0,		  0,010202, 0,";");  //
-	set_chr( 33,229,	 5, 3,     0,-350,  0,		  3,     0, 8,"WT?2 M3_99 (WT?20 M3!99 WT?20 !F106 <EV_MaidMotReset>);")	//③敵 ばんのうめいど
+	set_chr( 33,229,	 5, 3,     0,-350,  0,		  3,     0, 8,"WT?2 M3_99 (WT?20 M3!99 WT?20 !F106 !F108 <EV_MaidMotReset>);")	//③敵 ばんのうめいど
 		chr_equip_chr(57,56,"obx0264",  200,  0,0,0,	   0,0,0);
 		chr_equip_chr(33,56,"obx0264",  100,  0,0,0,	   0,15,300);
 		F_set_chr( 33, CF_NO_DAMAGE_C);
@@ -101,8 +110,17 @@ INIT
 		F_set_chr( 33, CF_NO_HPBAR);
 		F_set_chr( 33, CF_NO_MINIMAP);
 //		F_set_chr( 33, CF_NO_DEAD);
+		chr_equip2( 33,	"eq_048",	"Bone_Spine_Dummy",	100,		0,0,0,	0,0,0)
+		if ( F4_00_StartSolo )
+		{
+			chr_equip2( 33,	"eq_049",	"Bone_Head",	100,		0,0,0,	0,16,0)
+			chr_equip2( 33,"eq_062", "Bone_LeftHand", 100,	90,0,0,	-7,10,2);
+		}
+
 	set_chr( 59,655,	 4, 6,  -900,-250, 50,		  4,     0, 0,";")	//③順路案内
 
+//	set_chr(175,804,	 5, 3,	-350,-600, 50,		  0,     0, 8,"(L2?99 [9991バーチャルアイドル現実化装置] WT?30 L2!99 [9903] WT?30);")	//看板
+
 //■ハニワ．壷
 
 	if ( !F2170 )
@@ -304,15 +322,6 @@ EV_MaidMotReset
 }
 
 //--------------------------------------------------------------------
-EV_MaidAttack
-{
-	F_set(106)
-	MOT(57, 97, 5)
-	wait(45)
-	F_reset(106)
-}
-
-//--------------------------------------------------------------------
 EV_SlotDarken
 {
 	wait(15)
@@ -326,6 +335,20 @@ EV_WaitWoodBox107
 	F_set(107)
 }
 
+//--------------------------------------------------------------------
+EV_MaidLiftOff
+{
+	if ( !F33 )
+	{
+		chr_equip_off( 33 )
+		jump( 33, 2,	40,	0,-250,0, 100)
+		wait( 40 )
+		F_set(108)
+		wait( 10 )
+		MOT(33, 2, 0 )
+	}
+}
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/4/EV40510.txt b/scp_conv/map/4/EV40510.txt
index f8410fc..4a20829 100644
--- a/scp_jp_conv/map/4/EV40510.txt
+++ b/scp_conv/map/4/EV40510.txt
@@ -11,13 +11,13 @@
 #BOSS_CH	75
 #TAKARA_CH	76
 #KIBAKO_CH	79
+#CAMTGT_CH	69
 
 #IT_TAKARA	47		//チェックスカート
 
 #GF_BOSS10	3213	//Fx_MUGEN_KA_10B
 #GF_BOSS20	3215	//Fx_MUGEN_KA_20B
 
-
 //--------------------------------------------------------------------
 INIT
 {
@@ -110,7 +110,8 @@ EV_AppearBoss
 
 		cross_fade(30)
 
-		CAM_move_chr(BOSS_CH,0,0)
+		CAM_move_chr(CAMTGT_CH,0,0)	// camera_dummy
+//		CAM_move_chr(BOSS_CH,0,0)
 		wait_CAM_move()
 
 		wait(60)
@@ -129,6 +130,10 @@ EV_AppearBoss
 
 		MOT(75,80,0)
 
+		if(WK006==1)
+		{
+			MOT(71,80,0)
+		}
 		if(WK004==1)
 		{
 			MOT(77,80,0)
@@ -224,48 +229,93 @@ EV_DefeatBoss
 		//宝箱出現
 		if(WK003==1)
 		{
-			F_set(GF_BOSS20)		//２０階のボス倒した
-			
-			if(IT_TAKARA<1)
+			if( !Fx_MUGEN_EXTRA )
 			{
-				color(TAKARA_CH,-1)
+				F_set(GF_BOSS20)		//２０階のボス倒した
 				
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
+				if(!Fx_MUGEN2_KA_BOX)
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
-			F_set(GF_BOSS10)		//１０階のボス倒した
+			if( !Fx_MUGEN_EXTRA )
+			{
+				F_set(GF_BOSS10)		//１０階のボス倒した
+			}
 		}
 
 		SCORE(-1,-1,-1)		//スコア表示
@@ -279,6 +329,12 @@ EV_DefeatBoss
 	}
 }
 
+//──────────────────────────────
+EV_MM2_BoxOpened
+{
+	F_set( Fx_MUGEN2_KA_BOX )
+}
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/4/EV41210.txt b/scp_conv/map/4/EV41210.txt
index 3419f4a..42efc70 100644
--- a/scp_jp_conv/map/4/EV41210.txt
+++ b/scp_conv/map/4/EV41210.txt
@@ -213,24 +213,28 @@ INIT
 	{
 		set_chr( 65,810,	 6, 5,     0, 300,  0,		  2,     0, 0,";"); //③大砲
 		set_chr(165,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F65 I_$$$2 SF2180;");
+		chr_equip_chr(165,65,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	if ( !F2181 )
 	{
 		set_chr( 66,810,	 6, 5,     0,-300,  0,		  2,     0, 0,";"); //④大砲
 		set_chr(166,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F66 I_$$$2 SF2181;");
+		chr_equip_chr(166,66,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	if ( !F2182 )
 	{
 		set_chr( 67,810,	 4, 5,     0, 300,  0,		  2,     0, 0,";"); //⑤大砲
 		set_chr(167,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F67 I_$$$2 SF2182;");
+		chr_equip_chr(167,67,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	if ( !F2183 )
 	{
 		set_chr( 68,810,	 4, 5,     0,-300,  0,		  2,     0, 0,";"); //⑥大砲
 		set_chr(168,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F68 I_$$$2 SF2183;");
+		chr_equip_chr(168,68,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 
diff --git a/scp_jp_conv/map/4/EV41220.txt b/scp_conv/map/4/EV41220.txt
index b1b2155..4f48c12 100644
--- a/scp_jp_conv/map/4/EV41220.txt
+++ b/scp_conv/map/4/EV41220.txt
@@ -18,6 +18,9 @@
 #WOODBOX_CH		48
 #IT_WOODBOX		177		//∴177焼き鳥
 
+// 105 		ジャンプ台②の微妙な範囲選択
+// 106 		ジャンプ台②の微妙な範囲選択
+
 //--------------------------------------------------------------------
 INIT
 {
@@ -43,6 +46,8 @@ INIT
 	set_obj("obx0044",	 4, 3,     0,   0,   0,  	 0) //立体交差用橋
 	set_obj("obx0044",	 6, 4,     0,   0,   0,  	 0) //立体交差用橋
 
+	set_chr(161,991,	 5, 5,   250,-850,-2000,		  0,202701, 0,";")	//空気壁 
+
 //  -------  no typ   	  tip      x    y   z       mot     向 状  000+++++++010+++++++020+++++++030+++++++040+++++++050+++++++060+++++++070+++++++080+++++++090+++++++100+++++++110+++++++120+++++++130+++++++140+++++++150+++++++160+++++++170+++++++180+++++++190+++++++200+++++++210+++++++220+++++++230+++++++240+++++++250++
 //■階段．扉
 	set_chr( 90,990,	 5, 3,     0,-150,  0,		180,  0201, 6,"K0_1;")	//①エントリ 武器①
@@ -62,6 +67,10 @@ INIT
 	set_chr( 94,990,	 3, 4,   900,   0,  0,		 90,070206, 6,"k4_0")
 
 //■スイッチ．看板
+	set_chr(162,990,	 4, 4,     0, 800, 25,		  0,010301, 6,"SF105") //②ジャンプ台
+	set_chr(163,990,	 4, 4,     0, 675, 25,		  0,010301, 6,"SF106") //②ジャンプ台
+	set_chr(164,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"RF105 RF196")
+
 	set_chr( 61,672,	 4, 4,     0,-800,  0,		  0,   180, 6,"<EV_JUMP1>") //①ジャンプ台
 	set_chr( 62,672,	 4, 4,     0, 800,  0,		  0,     0, 6,"<EV_JUMP2>") //②ジャンプ台
 	set_chr( 63,672,	 5, 5,  -800,   0,  0,		  0,    90, 6,"<EV_JUMP3>") //③ジャンプ台
@@ -210,10 +219,27 @@ EV_JUMP1
 //--------------------------------------------------------------------
 EV_JUMP2
 {
-	//	ch,typ	tim,xyz		高さ
-	jump(PLAYER1,2,	30,	0,2000,0,	400)
-	jump(PLAYER2,2,	30,	0,2000,0,	400)
-	jump(PET,2,	30,	0,2000,0,	400)
+	if ( F106 )
+	{
+		//	ch,typ	tim,xyz		高さ
+		jump(PLAYER1,2,	30,	0,1800,200,	400)
+		jump(PLAYER2,2,	30,	0,1800,200,	400)
+		jump(PET,2,	30,	0,1600,0,	400)
+	}
+	else if ( F105 )
+	{
+		//	ch,typ	tim,xyz		高さ
+		jump(PLAYER1,2,	30,	0,1950,100,	400)
+		jump(PLAYER2,2,	30,	0,1950,100,	400)
+		jump(PET,2,	30,	0,1800,0,	400)
+	}
+	else
+	{
+		//	ch,typ	tim,xyz		高さ
+		jump(PLAYER1,2,	30,	0,2000,0,	400)
+		jump(PLAYER2,2,	30,	0,2000,0,	400)
+		jump(PET,2,	30,	0,2000,0,	400)
+	}
 }
 
 //--------------------------------------------------------------------
diff --git a/scp_jp_conv/map/4/EV41230.txt b/scp_conv/map/4/EV41230.txt
index ef590a9..05e5db6 100644
--- a/scp_jp_conv/map/4/EV41230.txt
+++ b/scp_conv/map/4/EV41230.txt
@@ -74,6 +74,7 @@ INIT
 	else
 	{
 		set_chr( 69,636,	 2, 4,   600,   0, 10,		  0,     0, 0,";")					//⑨風船 ⑩扉を開け③敵が出現
+		MOT( 53, 6, 0 )
 	}
 
 
@@ -189,6 +190,7 @@ INIT
 	{
 		set_chr( 65,810,	 7, 3,   200, 450,  0,		  2,     0, 0,";"); //①大砲
 		set_chr(165,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F65 I_$$$2 SF2190;");
+		chr_equip_chr(165,65,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	set_chr( 72,809,	 7, 3,   900, 800,  0,		  3,     0, 0,"") //②トゲ床
@@ -210,6 +212,7 @@ INIT
 	{
 		set_chr( 66,810,	 8, 5,  -200,-200,  0,		  2,     0, 0,";"); //□大砲
 		set_chr(166,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F66 I_$$$2 SF2191;");
+		chr_equip_chr(166,66,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
 	}
 
 	set_chr(114,623,	 5, 4,     0,   0,  0,		  2,     0, 0,"") //□ガスコンロa
diff --git a/scp_jp_conv/map/4/EV41290.txt b/scp_conv/map/4/EV41290.txt
index f4d4680..642a5eb 100644
--- a/scp_jp_conv/map/4/EV41290.txt
+++ b/scp_conv/map/4/EV41290.txt
@@ -5,6 +5,9 @@
 
 #ScriptTable
 
+#TREASURE_CH	49
+#IT_TREASURE	131		//Dパーツ
+
 //--------------------------------------------------------------------
 INIT
 {
@@ -49,9 +52,9 @@ INIT
 //■イベント
 	//ＧＦ『★炎のパーツを入手した』立ってない
 	if(!F2_10_GetFirePart)
-		set_chr( 80,563,	-1,-1, 7650, 7650,  0,		  2,   270, 5,"#8_99 WT?15 <EV_2_11_GetFirePart>;")//宝箱
+		set_chr( 49,563,	-1,-1, 7650, 7650,  0,		  6,   270, 2,"<EV_2_11_GetFirePart>;")//宝箱
 	else
-		set_chr( 80,563,	-1,-1, 7650, 7650,  0,		  7,   270, 0,"")//宝箱
+		set_chr( 49,563,	-1,-1, 7650, 7650,  0,		  7,   270, 0,"")//宝箱
 
 
 //■場面固有設定
@@ -69,6 +72,27 @@ INIT
 //　　アンカーギアの強化を頼んでいるのが前提の文章になる。
 EV_2_11_GetFirePart
 {
+	TK_begin()
+	rot_chr(0,60,TREASURE_CH)
+
+	//宝箱が開く
+	MOT(TREASURE_CH,1,0)
+
+	//宝演出
+	BGM_vol(50,15)				//BGMフェード
+	wait(20)
+	fade_in(30,10,BLACK)		//少し暗転
+
+	get_item(IT_TREASURE,1,0)	//パーツ入手テキスト
+	wait(70)
+	wait_key(0)
+	BGM_vol(100,30)				//BGM戻し
+	fade_in(0,10,BLACK)			//暗転解除
+	menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+	menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+
+	TK_end()
+
 	EV_begin()
 
 	cross_fade(30)
@@ -83,19 +107,6 @@ EV_2_11_GetFirePart
 
 	wait(30)
 
-//	name("アイテム入手テキスト")
-//	MES(RAGNA,"◆未入力項目\n炎のパーツ（仮）を手に入れた。",0)
-//	MES_close(RAGNA)
-	BGM_vol(50,15)				//BGMフェード
-	wait(20)
-	fade_in(30,10,BLACK)		//少し暗転
-	get_item( 131,1,0 )
-	wait(70)
-	wait_key(0)
-	BGM_vol(100,30)				//BGM戻し
-	fade_in(0,10,BLACK)			//暗転解除
-	menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
-	menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
 
 	rot_chr(PARTNER,30,RAGNA)
 	wait(15)
diff --git a/scp_jp_conv/map/4/EV42310.txt b/scp_conv/map/4/EV42310.txt
index 545fa22..a15aa0f 100644
--- a/scp_jp_conv/map/4/EV42310.txt
+++ b/scp_conv/map/4/EV42310.txt
@@ -54,6 +54,9 @@
 // 2186 ボス② □爆弾タル
 // 2187 ボス② □爆弾タル
 
+// 2190 ボス② ⑦大砲
+// 2191 ボス② ⑧大砲
+
 //■ローカルフラグ
 // 100 □扉のスイッチ
 // 101 ⑤敵が出現
diff --git a/scp_jp_conv/map/4/EV42320.txt b/scp_conv/map/4/EV42320.txt
index f456672..e0cab82 100644
--- a/scp_jp_conv/map/4/EV42320.txt
+++ b/scp_conv/map/4/EV42320.txt
@@ -63,6 +63,7 @@ INIT
 	else
 	{
 		MOT(31, 3, 0 )
+		MOT(53, 6, 0 )
 	}
 
 
@@ -73,6 +74,7 @@ INIT
 	else
 	{
 		MOT(32, 3, 0 )
+		MOT(54, 6, 0 )
 	}
 
 
@@ -83,6 +85,7 @@ INIT
 	else
 	{
 		MOT(33, 3, 0 )
+		MOT(55, 6, 0 )
 	}
 
 //	set_chr( 33,666,	 4, 3,  -190,-190,-25,		  2,   315, 0,"") //④的c
@@ -122,8 +125,18 @@ INIT
 	set_chr( 64,660,	 5, 3,  -700,   0,100,		  4,   180, 8,"F2102 (X4_4300 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_1100);") //④プロペラ移動床
 	set_chr( 65,660,	 5, 3, -1050,   0, 50,		  4,   180, 8,"F2102 (X4_4650 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_0750);") //⑤プロペラ移動床
 	set_chr( 66,660,	 5, 3, -1400,   0,100,		  4,   180, 8,"F2102 (X4_5000 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_0400);") //⑥プロペラ移動床
-	set_chr( 67,810,	 5, 3,     0,   0,190,		  2,   180, 8,"F2102 (X4_3600 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_1800);") //⑦大砲
-	set_chr( 68,810,	 5, 3, -1400,   0,190,		  2,   180, 8,"F2102 (X4_5000 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_0400);") //⑧大砲
+	if ( !F2190 )
+	{
+		set_chr( 67,810,	 5, 3,     0,   0,190,		  2,   180, 8,"F2102 (X4_3600 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_1800);") //⑦大砲
+		set_chr(167,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F67 I_$$$2 SF2190;");
+		chr_equip_chr(167,67,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
+	}
+	if ( !F2191 )
+	{
+		set_chr( 68,810,	 5, 3, -1400,   0,190,		  2,   180, 8,"F2102 (X4_5000 Y4_-3600 X4_-1800 Y4_1800 X4_-3600 Y4_-1800 X4_5400 Y4_3600 X4_-5400 Y4_-1800 X4_3600 Y4_-1800 X4_-3600 Y4_3600 X4_0400);") //⑧大砲
+		set_chr(168,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F68 I_$$$2 SF2191;");
+		chr_equip_chr(168,68,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
+	}
 
 	if ( !F2130 )
 		set_chr( 70,630,	 8, 4,  -900,   0,  0,		  2,    60, 0,"I_FFF1 SF2130;")	//⑩樽
@@ -169,7 +182,7 @@ INIT
 	if ( !F2102 )
 	{
 		set_chr(160,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"M2!60 WT?10 M4_52 WT?45 SF2102;")//発車 ⑤コング
-		set_chr(556,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2102 WT?08 O1_18;")	// ゴング初回
+		set_chr(161,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2102 WT?08 O1_18;")	// ゴング初回
 	}
 	else
 	{
diff --git a/scp_jp_conv/map/4/EV42390.txt b/scp_conv/map/4/EV42390.txt
index c92c420..7e6c0c8 100644
--- a/scp_jp_conv/map/4/EV42390.txt
+++ b/scp_conv/map/4/EV42390.txt
@@ -30,7 +30,7 @@ INIT
 //■スイッチ．看板
 	set_chr( 50,620,	 5, 4,  -350,   0,  0,		  0,   270, 0,";")	//①セーブOBJ
 
-	set_chr( 56,648,	 5, 3,     0,-700,  0,		 12,     0, 0,";")	//レベルプレート
+	set_chr( 56,772,	 5, 3,     0,-700,  0,		 12,     0, 0,";")	//レベルプレート
 	color2( 56, 100,88,91,0,0,0)
 
 	set_chr(120 627,	 4, 3,     0, 600,  0,		  0,     0, 0,";")	//柵小
diff --git a/scp_jp_conv/map/4/MC40100.bmp b/scp_conv/map/4/MC40100.bmp
index b441ac7..9e4a929 100644
Binary files a/scp_jp_conv/map/4/MC40100.bmp and b/scp_conv/map/4/MC40100.bmp differ
