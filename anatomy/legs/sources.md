# Источники: мышцы ног и таза

Номера — те, на которые ссылаются `refs` в `muscles.json` и `ref` в `validation.json`.

## Модели и параметры мышц

1. Rajagopal A, Dembia CL, DeMers MS, Delp DD, Hicks JL, Delp SL. Full-body musculoskeletal model for muscle-driven simulation of human gait. IEEE Trans Biomed Eng. 2016;63(10):2068–2079. doi:10.1109/TBME.2016.2586891 — Основная модель: точки прикрепления, Fmax (объёмы по МРТ × 60 Н/см²), волокна, сухожилия.
2. Lai AKM, Arnold AS, Wakeling JM. Why are antagonist muscles co-activated in my simulation? A musculoskeletal model for analysing human locomotor tasks. Ann Biomed Eng. 2017;45(12):2762–2774. doi:10.1007/s10439-017-1920-7 — Пути четырёхглавой и обходы для сгибания колена до 140° и бедра до 120°.
3. Uhlrich SD, Jackson RW, Seth A, Kolesar JA, Delp SL. Muscle coordination retraining inspired by musculoskeletal simulations reduces knee contact force. Sci Rep. 2022;12:9842. doi:10.1038/s41598-022-13386-9 — Версия RajagopalLaiUhlrich2023: пассивные силы, пути отводящих бедра.
4. Delp SL, Loan JP, Hoy MG, Zajac FE, Topp EL, Rosen JM. An interactive graphics-based model of the lower extremity to study orthopaedic surgical procedures. IEEE Trans Biomed Eng. 1990;37(8):757–767. doi:10.1109/10.102791 — Модель gait2392: гребенчатая, квадратная мышца бедра, близнецовые.
5. Arnold EM, Ward SR, Lieber RL, Delp SL. A model of the lower limb for analysis of human movement. Ann Biomed Eng. 2010;38(2):269–279. doi:10.1007/s10439-009-9852-5 — Основа путей мышц в модели Rajagopal; архитектура по 21 кадавру.
6. Handsfield GG, Meyer CH, Hart JM, Abel MF, Blemker SS. Relationships of 35 lower limb muscles to height and body mass quantified using MRI. J Biomech. 2014;47(3):631–638. doi:10.1016/j.jbiomech.2013.12.002 — Объёмы мышц по МРТ; регрессии объёма от массы и роста (масштабирование PCSA).
7. Ward SR, Eng CM, Smallwood LH, Lieber RL. Are current measurements of lower extremity muscle architecture accurate? Clin Orthop Relat Res. 2009;467(4):1074–1082. doi:10.1007/s11999-008-0594-8 — Длины волокон, перистость, кадаверные PCSA 27 мышц (21 кадавр).
8. Delp SL, Anderson FC, Arnold AS, et al. OpenSim: open-source software to create and analyze dynamic simulations of movement. IEEE Trans Biomed Eng. 2007;54(11):1940–1950. doi:10.1109/TBME.2007.901024; Seth A, Hicks JL, Uchida TK, et al. OpenSim: simulating musculoskeletal dynamics and neuromuscular control to study human and animal movement. PLoS Comput Biol. 2018;14(7):e1006223. doi:10.1371/journal.pcbi.1006223 — OpenSim 4.6: расчёт плеч (computeMomentArm), Scale Tool.
9. Millard M, Uchida T, Seth A, Delp SL. Flexing computational muscle: modeling and simulation of musculotendon dynamics. J Biomech Eng. 2013;135(2):021005. doi:10.1115/1.4023390 — Модель мышцы в файлах OpenSim (оптимальная длина волокна, длина сухожилия, перистость).
10. opensim-org/opensim-models, GitHub: Models/Rajagopal/RajagopalLaiUhlrich2023.osim, Models/Gait2392_Simbody/gait2392_millard2012muscle.osim; коммит d9b05d4 (5 ноября 2025). https://github.com/opensim-org/opensim-models — Файлы моделей, из которых взяты числа.
11. Crowninshield RD, Brand RA. A physiologically based criterion of muscle force prediction in locomotion. J Biomech. 1981;14(11):793–801. doi:10.1016/0021-9290(81)90035-X — Критерий деления момента между мышцами: минимум суммы кубов напряжений.

## Моменты и силы в упражнениях (validation.json)

12. Wretenberg P, Feng Y, Arborelius UP. High- and low-bar squatting techniques during weight-training. Medicine and Science in Sports and Exercise. 1996;28(2):218-224. https://read.qxmd.com/read/8775157/high-and-low-bar-squatting-techniques-during-weight-training
13. Swinton PA, Lloyd R, Keogh JWL, Agouris I, Stewart AD. A biomechanical comparison of the traditional squat, powerlifting squat, and box squat. Journal of Strength and Conditioning Research. 2012;26(7):1805-1816. doi:10.1519/JSC.0b013e3182577067
14. Swinton PA, Stewart A, Agouris I, Keogh JWL, Lloyd R. A biomechanical analysis of straight and hexagonal barbell deadlifts using submaximal loads. Journal of Strength and Conditioning Research. 2011;25(7):2000-2009. doi:10.1519/JSC.0b013e3181e73f87
15. Lahti J, Hegyi A, Vigotsky AD, Ahtiainen JP. Effects of barbell back squat stance width on sagittal and frontal hip and knee kinetics. Scandinavian Journal of Medicine & Science in Sports. 2019;29(1):44-54. doi:10.1111/sms.13305
16. Fry AC, Smith JC, Schilling BK. Effect of knee position on hip and knee torques during the barbell squat. Journal of Strength and Conditioning Research. 2003;17(4):629-633. https://oasis.library.unlv.edu/kns_fac_articles/69
17. Escamilla RF, Fleisig GS, Lowry TM, Barrentine SW, Andrews JR. A three-dimensional biomechanical analysis of the squat during varying stance widths. Medicine and Science in Sports and Exercise. 2001;33(6):984-998. doi:10.1097/00005768-200106000-00019
18. van den Tillaar R, Falch HN, Larsen S. Are Diminishing Potentiation and Large Extensor Moments the Cause for the Occurrence of the Sticking Region in Maximum Free-Weight Barbell Back Squats among Resistance-Trained Males?. Journal of Human Kinetics. 2024;91:105-119. doi:10.5114/jhk/185720
19. Larsen S, Kristiansen E, van den Tillaar R. New Insights About the Sticking Region in Back Squats: An Analysis of Kinematics, Kinetics, and Myoelectric Activity. Frontiers in Sports and Active Living. 2021;3:691459. doi:10.3389/fspor.2021.691459
20. Pürzel A, Kaufmann P, Koller W, Deimel D, Baca A, Kainz H. Hip moment increases while knee and ankle moments remain constant during squats with increasing loads in elite powerlifters. ISBS Proceedings Archive. 2024;42(1):776-779 (art. 17). https://commons.nmu.edu/cgi/viewcontent.cgi?article=2709&context=isbs
21. Lee S, Kim J, Han KH, Kim D, Hasan M, Kim J, Kwon Y-H. Effects of foot placement on resultant joint moments of lower extremity joints during squat. 33rd International Conference on Biomechanics in Sports (ISBS), Poitiers. 2015:1050-1053. https://ojs.ub.uni-konstanz.de/cpa/article/view/6590/5951
22. Sinclair J, Atkins S, Vincent H, Richards JD. Modelling Muscle Force Distributions during the Front and Back Squat in Trained Lifters. Central European Journal of Sport Sciences and Medicine. 2016;14(2):13-20. doi:10.18276/cej.2016.2-02
23. Sjöberg M, Berg HE, Norrbrand L, Andersen MS, Gutierrez-Farewik EM, Sundblad P, Eiken O. Comparison of Joint and Muscle Biomechanics in Maximal Flywheel Squat and Leg Press. Frontiers in Sports and Active Living. 2021;3:686335. doi:10.3389/fspor.2021.686335
24. Beardsley C, Contreras B. The Increasing Role of the Hip Extensor Musculature With Heavier Compound Lower-Body Movements and More Explosive Sport Actions. Strength and Conditioning Journal. 2014;36(2):49-55. https://bretcontreras.com/wp-content/uploads/The-Increasing-Role-of-the-Hip-Extensor-Musculature-With-Heavier-Compound-Lower-Body-Movements-and-More-Explosive-Sport-Actions.pdf
25. Hanen NC, Ben Mansour K, Ertel GN, Duchene Y, Gauchard GC. Biomechanical analysis of conventional and sumo deadlift. Frontiers in Bioengineering and Biotechnology. 2025;13:1597209. doi:10.3389/fbioe.2025.1597209
26. Escamilla RF, Lowry TM, Osbahr DC, Speer KP. Biomechanical analysis of the deadlift during the 1999 Special Olympics World Games. ISBS Biomechanics Symposia 2001 (University of San Francisco). 2001:63-67. https://ojs.ub.uni-konstanz.de/cpa/article/view/3819/3538
27. Schellenberg F, Lindorfer J, List R, Taylor WR, Lorenzetti S. Kinetic and kinematic differences between deadlifts and goodmornings. BMC Sports Science, Medicine and Rehabilitation. 2013;5:27. doi:10.1186/2052-1847-5-27
28. Schellenberg F, Taylor WR, Lorenzetti S. Towards evidence based strength training: a comparison of muscle forces during deadlifts, goodmornings and split squats. BMC Sports Science, Medicine and Rehabilitation. 2017;9:13. doi:10.1186/s13102-017-0077-x
29. Lee S, Schultz J, Timgren J, Staelgraeve K, Miller M, Liu Y. An electromyographic and kinetic comparison of conventional and Romanian deadlifts. Journal of Exercise Science & Fitness. 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6323186/table/tbl2
30. Breed R, Hulm S, Hickey JT, Timmins RG, Opar D, Banyard HG, Maniar N. Hamstring force and stretch during progressively increasing running speeds and the eccentric phase of resistance training exercises commonly used for injury prevention and rehabilitation. British Journal of Sports Medicine. 2026;60:420-428. doi:10.1136/bjsports-2025-110847
31. Brazil A, Needham L, Palmer JL, Bezodis IN. A comprehensive biomechanical analysis of the barbell hip thrust. PLoS ONE. 2021;16(3):e0249307. doi:10.1371/journal.pone.0249307
32. Bezodis I, Brazil A, Palmer J, Needham L. Hip joint kinetics during the barbell hip thrust. ISBS Proceedings Archive. 2017;35(1):art. 184. https://commons.nmu.edu/cgi/viewcontent.cgi?article=1197&context=isbs
33. Hahn D, Tusker F, Schwirtz A. Knee and ankle joint moment-angle relationships of multi-joint leg extension. ISB 2009 congress abstract (media.isbweb.org, conf/2009, #201). 2009. https://media.isbweb.org/images/conf/2009/data/pdf/201.pdf
34. Šarabon N, Kozinc Ž, Perman M. Establishing Reference Values for Isometric Knee Extension and Flexion Strength. Frontiers in Physiology. 2021;12:767941. doi:10.3389/fphys.2021.767941

## Плечи сил: МРТ, рентген, УЗИ, кадавры (moment_arms_literature.json)

35. Arnold AS, Blemker SS, Asakawa DJ, Delp SL. Accuracy of muscle moment arms estimated from MRI-based musculoskeletal models of the lower extremity. Computer Aided Surgery. 2000;5(2):108-119. doi:10.3109/10929080009148877
36. Baxter JR, Piazza SJ. Plantarflexor moment arms estimated from tendon excursion in vivo are not strongly correlated with geometric measurements. Journal of Biomechanics (ScienceDirect pii S0021929018304512); preprint bioRxiv. 2018. doi:10.1101/290916
37. Blemker SS, Delp SL. Three-dimensional representation of complex muscle architectures and geometries. Annals of Biomedical Engineering. 2005;33(5):661-673. doi:10.1007/s10439-005-1433-7
38. Brookbush Institute. Research Review: Contributions of Lower Leg Muscles to Movement at the Ankle (review of Klein et al. 1996). Brookbush Institute (web). https://brookbushinstitute.com/articles/research-review-contributions-of-lower-leg-muscles-to-movement-at-the-ankle
39. Buffey AJ, Onambele-Pearson GL, Erskine RM, Tomlinson DJ. The validity and reliability of the Achilles tendon moment arm assessed with dual-energy X-ray absorptiometry, relative to MRI and ultrasound assessments. Journal of Biomechanics (ScienceDirect pii S002192902030628X). 2021. https://researchonline.ljmu.ac.uk/14289/1/Buffey_AT_MA_2021_Repository.pdf
40. Buford WL Jr, et al. Muscle balance at the knee - moment arms for the normal knee and the ACL-minus knee. IEEE Transactions on Rehabilitation Engineering. 1997;5(4):367-379. doi:10.1109/86.650292
41. Chen Z, Franklin DW. Muscle moment arm-joint angle relations in the hip, knee, and ankle: a visualization of datasets. Annals of Biomedical Engineering. 2025;53(8):1757-1776. doi:10.1007/s10439-025-03735-w
42. Dandridge O, Garner A, Amis A, Cobb J, van Arkel RJ. Variation in the patellar tendon moment arm identified with an improved measurement framework. Journal of Orthopaedic Research. 2022;40(4):799-807. doi:10.1002/jor.25124
43. Delp SL, Hess WE, Hungerford DS, Jones LC. Variation of rotation moment arms with hip flexion. Journal of Biomechanics. 1999;32(5):493-501. doi:10.1016/S0021-9290(99)00032-9
44. Dostal WF, Soderberg GL, Andrews JG. Actions of hip muscles. Physical Therapy. 1986;66(3):351-359. doi:10.1093/ptj/66.3.351
45. Fath F, Blazevich AJ, Waugh CM, Miller SC, Korff T. Direct comparison of in vivo Achilles tendon moment arms obtained from ultrasound and MR scans. Journal of Applied Physiology. 2010;109(6):1644-1652. doi:10.1152/japplphysiol.00656.2010
46. Fath F, Blazevich AJ, Waugh CM, Miller SC, Korff T. Interactive effects of joint angle, contraction state and method on estimates of Achilles tendon moment arms. Journal of Applied Biomechanics. 2013;29:241-244. https://bura.brunel.ac.uk/bitstream/2438/7757/2/Fulltext.pdf
47. Herzog W, Read LJ. Lines of action and moment arms of the major force-carrying structures crossing the human knee joint. Journal of Anatomy. 1993;182(Pt 2):213-230. https://pmc.ncbi.nlm.nih.gov/articles/PMC1259832
48. Hosseinzadeh S, Barzegari A, Taghipour M, Mehr Aein R, Gholinia H. Changes of the patellar tendon moment arm length in different knee angles: a biomechanical in vivo study. Archives of Bone and Joint Surgery. 2020;8(5). doi:10.22038/abjs.2020.42551.2158
49. Kellis E, Baltzopoulos V. In vivo determination of the patella tendon and hamstrings moment arms in adult males using videofluoroscopy during submaximal knee extension and flexion. Clinical Biomechanics. 1999;14(2):118-124. doi:10.1016/S0268-0033(98)00055-2
50. Klein P, Mattys S, Rooze M. Moment arm length variations of selected muscles acting on talocrural and subtalar joints during movement: an in vitro study. Journal of Biomechanics. 1996;29(1):21-30. doi:10.1016/0021-9290(95)00025-9
51. Krevolin JL, Pandy MG, Pearce JC. Moment arm of the patellar tendon in the human knee. Journal of Biomechanics. 2004;37(5):785-788. doi:10.1016/j.jbiomech.2003.09.010
52. Lee SSM, Piazza SJ. Built for speed: musculoskeletal structure and sprinting ability. Journal of Experimental Biology. 2009;212(22):3700-3707. https://cob.silverchair.com/jeb/article-split/212/22/3700/19059/Built-for-speed-musculoskeletal-structure-and
53. Maganaris CN, Baltzopoulos V, Sargeant AJ. Changes in Achilles tendon moment arm from rest to maximum isometric plantarflexion: in vivo observations in man. Journal of Physiology. 1998;510(3):977-985. doi:10.1111/j.1469-7793.1998.977bj.x
54. Maganaris CN, Baltzopoulos V, Sargeant AJ. Changes in the tibialis anterior tendon moment arm from rest to maximum isometric dorsiflexion: in vivo observations in man. Clinical Biomechanics. 1999;14(9):661-666. doi:10.1016/S0268-0033(99)00018-2
55. Maganaris CN, Baltzopoulos V, Sargeant AJ. In vivo measurement-based estimations of the human Achilles tendon moment arm. European Journal of Applied Physiology. 2000;83(4-5):363-369. https://e-space.mmu.ac.uk/2416
56. Maganaris CN. Imaging-based estimates of moment arm length in intact human muscle-tendons. European Journal of Applied Physiology. 2004;91(2-3):130-139. https://e-space.mmu.ac.uk/2411
57. Maganaris CN, Baltzopoulos V, Tsaopoulos DE. Muscle fibre length-to-moment arm ratios in the human lower limb determined in vivo. Journal of Biomechanics. 2006;39(9):1663-1668. https://e-space.mmu.ac.uk/2408
58. Nemeth G, Ohlsen H. In vivo moment arm lengths for hip extensor muscles at different angles of hip flexion. Journal of Biomechanics. 1985;18(2):129-140. doi:10.1016/0021-9290(85)90005-3
59. Nemeth G, Ohlsen H. Moment arms of hip abductor and adductor muscles measured in vivo by computed tomography. Clinical Biomechanics. 1989;4(3):133-136. doi:10.1016/0268-0033(89)90015-6
60. O'Brien TD, Reeves ND, Baltzopoulos V, Jones DA, Maganaris CN. Moment arms of the knee extensor mechanism in children and adults. Journal of Anatomy. 2009;215(2):198-205. doi:10.1111/j.1469-7580.2009.01088.x
61. Spoor CW, van Leeuwen JL, Meskers CGM, Titulaer AF, Huson A. Estimation of instantaneous moment arms of lower-leg muscles. Journal of Biomechanics. 1990;23(12):1247-1259. doi:10.1016/0021-9290(90)90382-D
62. Takahashi K, Tozawa H, Kawama R, Wakahara T. Redefining muscular action: human "adductor" magnus is designed to act primarily for hip "extension" rather than adduction in living young individuals. Journal of Applied Physiology. 2025. doi:10.1152/japplphysiol.00600.2024
63. Tsaopoulos DE, Baltzopoulos V, Maganaris CN. Human patellar tendon moment arm length: measurement considerations and clinical implications for joint loading assessment. Clinical Biomechanics. 2006;21(7):657-667. https://smithengineering.queensu.ca/mme/faculty/deluzio/jam/files/6.26.2009_Stacey.pdf
64. Tsaopoulos DE, Baltzopoulos V, Richards PJ, et al. A comparison of different two-dimensional approaches for the determination of the patellar tendon moment arm length. European Journal of Applied Physiology. 2009;105:809-814. doi:10.1007/s00421-008-0968-3
65. Wretenberg P, Nemeth G, Lamontagne M, Lundin B. Passive knee muscle moment arms measured in vivo with MRI. Clinical Biomechanics. 1996;11(8):439-446. doi:10.1016/S0268-0033(96)00030-7

## Архитектура мышц и масштабирование

66. OpenSim 3.3 documentation. How Scaling Works. https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim33/pages/53674051 — Правила Scale Tool: точки и обходы — по коэффициентам своего тела.
67. opensim-core, OpenSim/Actuators/Millard2012EquilibriumMuscle.cpp, extendPostScale. https://github.com/opensim-org/opensim-core — Оптимальная длина волокна и длина сухожилия × отношение длины пути после/до масштабирования.
68. Correa TA, Pandy MG. A mass–length scaling law for modeling muscle strength in the lower limb. J Biomech. 2011;44(16):2782–2789. — Fmax ∝ масса мышцы / длина волокна.
69. Hainisch R, Kranzl A, Lin Y-C, Pandy MG, Gfoehler M. A generic musculoskeletal model of the juvenile lower limb for biomechanical analyses of gait. Comput Methods Biomech Biomed Engin. 2021;24(4):349–357. doi:10.1080/10255842.2020.1817405 — Форма закона Correa & Pandy (ур. 4).
70. Son J, Ward SR, Lieber RL. Scaling relationships between human leg muscle architectural properties and body size. J Exp Biol. 2024;227(6):jeb246567. doi:10.1242/jeb.246567 — PCSA ∝ масса тела^1,17, длина волокна почти не растёт.
71. Jaric S. Muscle strength testing: use of normalisation for body size. Sports Med. 2002;32(10):615–631. — Сила ∝ m^0,67, момент ∝ m^1.
72. Yeung S, Fernandez JW, Handsfield GG, et al. Biomech Model Mechanobiol. 2020;19:1239–1249. doi:10.1007/s10237-019-01243-0 — Объём мышц ноги по обхвату голени, полу и длине ноги.
73. Waugh C, Blazevich AJ, Fath F, Korff T. J Biomech. 2011;44(10):1839–1844. doi:10.1016/j.jbiomech.2011.03.023 — Плечо ахиллова сухожилия по длине стопы (дети).
74. Foster AD, Block B, Capobianco F, et al. Sci Rep. 2021;11:9360. doi:10.1038/s41598-021-88774-8 — Длина пятки и масса тела.
75. Scholz MN, Bobbert MF, van Soest AJ, Clark JR, van Heerden J. J Exp Biol. 2008;211(20):3266–3271. — Плечо ахиллова сухожилия у бегунов.
76. Tsaopoulos DE, Maganaris CN, Baltzopoulos V. Can the patellar tendon moment arm be predicted from anthropometric measurements? J Biomech. 2007;40(3):645–651. — Плечо связки надколенника почти не связано с ростом.
77. Tsaopoulos DE et al. ISB XXth Congress / ASB 2005, abstract p. 712. https://media.isbweb.org/images/conf/2005/abstracts/0712.pdf
78. Hu X, et al. Front Bioeng Biotechnol. 2021;9:645019. doi:10.3389/fbioe.2021.645019 — Офсет бедра и плечи отводящих.
79. Kramer PA, Sylvester AD. PLoS ONE. 2023;18(4):e0284450. doi:10.1371/journal.pone.0284450 — Ширина таза и фронтальный момент в бедре.
80. de Leva P. Adjustments to Zatsiorsky-Seluyanov's segment inertia parameters. J Biomech. 1996;29(9):1223–1230. — Длины, массы и центры масс сегментов.
81. Сторонний код, только для перекрёстной проверки: johnjdavisiv/scale-muscle-strength; israelluis/MetabolicRateWalking; basgoncalves/powerlifing_model; stanfordnmbl/coupled-exo-sim (GitHub). — Коэффициенты 47,05 и 1289,6 в формуле объёма.

## Книги

82. Neumann DA. Neumann's Kinesiology of the Musculoskeletal System. 4th ed. Elsevier; 2024. ISBN 9780323718592 (3-е изд.: 2017) — Действия мышц, линии сил и плечи по суставам; места прикрепления.
83. Winter DA. Biomechanics and Motor Control of Human Movement. 4th ed. Wiley; 2009. ISBN 9780470398180 — Пропорции сегментов к росту, обратная динамика.
84. Zatsiorsky VM. Kinetics of Human Motion. Human Kinetics; 2002. ISBN 9780736037785 — Инерционные параметры сегментов, моменты в суставах, кривые силы.
85. Zatsiorsky VM, Prilutsky BI. Biomechanics of Skeletal Muscles. Human Kinetics; 2012. ISBN 9780736080200 — Архитектура, плечи, двусуставные мышцы, распределение сил.
86. Зациорский В.М., Аруин А.С., Селуянов В.Н. Биомеханика двигательного аппарата человека. М.: Физкультура и спорт; 1981 — Массы и центры масс сегментов (основа таблиц de Leva).
87. Lieber RL. Skeletal Muscle Structure, Function, and Plasticity. 3rd ed. Lippincott Williams & Wilkins; 2009. ISBN 9780781775939 — PCSA, длина волокна, перистость.
88. Kapandji AI. The Physiology of the Joints. Vol. 2: The Lower Limb. 7th ed. Handspring; 2019. ISBN 9781912085606 — Оси суставов и логика действий мышц.
89. Standring S, ed. Gray's Anatomy: The Anatomical Basis of Clinical Practice. 42nd ed. Elsevier; 2020. ISBN 9780702077050 (43-е изд.: 2025) — Места прикрепления и варианты.
90. Yamaguchi GT, Sawa AGU, Moran DW, Fessler MJ, Winters JM. A survey of human musculotendon actuator parameters. In: Winters JM, Woo SL-Y, eds. Multiple Muscle Systems. Springer; 1990. doi:10.1007/978-1-4613-9030-5 — Сводные таблицы PCSA, волокон, сухожилий по кадаврам.
91. Zajac FE. Muscle and tendon: properties, models, scaling, and application to biomechanics and motor control. Crit Rev Biomed Eng. 1989;17(4):359–411 — Безразмерная модель мышцы, масштабирование по Fmax и длинам.
