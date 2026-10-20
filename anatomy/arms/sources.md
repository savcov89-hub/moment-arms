# Источники: плечевой пояс и руки

Номера соответствуют полю `refs` в `muscles.json` и `ref` в `validation.json`.
Пометка [R]: выходные данные (страницы, том) вспомнены, а не сверены с источником в этой сессии. Остальное прочитано на странице статьи, в аннотации или в открытом файле модели.

## Модели и параметры мышц

1. Holzbaur KRS, Murray WM, Delp SL. A model of the upper extremity for simulating musculoskeletal surgery and analyzing neuromuscular control. Ann Biomed Eng 2005;33(6):829–840. doi:10.1007/s10439-005-3320-7 — геометрия путей MoBL-ARMS, архитектура мышц
2. Saul KR, Hu X, Goehler CM, Vidt ME, Daly M, Velisar A, Murray WM. Benchmarking of dynamic simulation predictions in two software platforms using an upper limb musculoskeletal model. Comput Methods Biomech Biomed Engin 2015;18(13):1445–1458. doi:10.1080/10255842.2014.916698 — силы мышц MoBL-ARMS (σ = 50,8 Н/см²)
3. Wang H, Caggiano V, Durandau G, Sartori M, Kumar V. MyoSim: fast and physiologically realistic MuJoCo models for musculoskeletal and exoskeletal studies. ICRA 2022; модель MyoArm, github.com/MyoHub/myo_sim — реализация MoBL-ARMS, на которой считались пути и плечи [страницы R]
4. Seth A, Dong M, Matias R, Delp S. Muscle contributions to upper-extremity movement and work from a musculoskeletal model of the human shoulder. Front Neurorobot 2019;13:90. doi:10.3389/fnbot.2019.00090; файл ThoracoscapularShoulderModel.osim (opensim-core) — мышцы лопатки
5. Seth A, Matias R, Veloso AP, Delp SL. A biomechanical model of the scapulothoracic joint to accurately capture scapular kinematics during shoulder movements. PLoS ONE 2016;11:e0141028 [R]
6. Klein Breteler MD, Spoor CW, van der Helm FCT. Measuring muscle and joint geometry parameters of a shoulder for modeling purposes. J Biomech 1999;32(11):1191–1197 [R; данные через DAS3 и Seth 2019]
7. Chadwick EK, Blana D, Kirsch RF, van den Bogert AJ. Real-time simulation of three-dimensional shoulder girdle and arm dynamics. IEEE Trans Biomed Eng 2014;61(7):1947–1956 (модель DAS3)

## Ритм лопатки

8. de Groot JH, Brand R. A three-dimensional regression model of the shoulder rhythm. Clin Biomech 2001;16(9):735–743 [R] — основа ритма MoBL-ARMS
9. McClure PW, Michener LA, Sennett BJ, Karduna AR. Direct 3-dimensional measurement of scapular kinematics during dynamic movements in vivo. J Shoulder Elbow Surg 2001;10:269–277
10. Ludewig PM, Phadke V, Braman JP, Hassett DR, Cieminski CJ, LaPrade RF. Motion of the shoulder complex during multiplanar humeral elevation. J Bone Joint Surg Am 2009;91(2):378–389 [страницы R]
11. Inman VT, Saunders JB, Abbott LC. Observations on the function of the shoulder joint. J Bone Joint Surg 1944;26:1–30 [R]

## Объёмы мышц и сила

12. Holzbaur KRS, Murray WM, Gold GE, Delp SL. Upper limb muscle volumes in adult subjects. J Biomech 2007;40(4):742–749. doi:10.1016/j.jbiomech.2006.11.011 — доли объёма мышц (МРТ)
13. Holzbaur KRS, Delp SL, Gold GE, Murray WM. Moment-generating capacity of upper limb muscles in healthy adults. J Biomech 2007;40(11):2442–2449. doi:10.1016/j.jbiomech.2006.11.013

## Плечи сил: эксперимент

14. Murray WM, Delp SL, Buchanan TS. Variation of muscle moment arms with elbow and forearm position. J Biomech 1995;28(5):513–525
15. Murray WM, Buchanan TS, Delp SL. The isometric functional capacity of muscles that cross the elbow. J Biomech 2000;33(8):943–952
16. Murray WM, Buchanan TS, Delp SL. Scaling of peak moment arms of elbow muscles with upper extremity bone dimensions. J Biomech 2002;35(1):19–26 — масштабирование плеч локтя
17. Ackland DC, Pak P, Richardson M, Pandy MG. Moment arms of the muscles crossing the anatomical shoulder. J Anat 2008;213(4):383–390. doi:10.1111/j.1469-7580.2008.00965.x
18. Hik F, Ackland DC. The moment arms of the muscles spanning the glenohumeral joint: a systematic review. J Anat 2019;234(1):1–15. doi:10.1111/joa.12903
19. Kuechle DK, Newman SR, Itoi E, Morrey BF, An KN. Shoulder muscle moment arms during horizontal flexion and elevation. J Shoulder Elbow Surg 1997;6(5):429–439
20. Kuechle DK, Newman SR, Itoi E, Niebur GL, Morrey BF, An KN. The relevance of the moment arm of shoulder muscles with respect to axial rotation of the glenohumeral joint in four positions. Clin Biomech 2000;15(5):322–329
21. Otis JC, Jiang CC, Wickiewicz TL, Peterson MG, Warren RF, Santner TJ. Changes in the moment arms of the rotator cuff and deltoid muscles with abduction and rotation. J Bone Joint Surg Am 1994;76(5):667–676
22. Liu J, Hughes RE, Smutz WP, Niebur G, An KN. Roles of deltoid and rotator cuff muscles in shoulder elevation. Clin Biomech 1997;12(1):32–38
23. Hoffmann M, Begon M, Assila N, et al., Sobczak S. Moment arms of the deltoid, infraspinatus and teres minor muscles for movements with high range of motion: a cadaveric study. Clin Biomech 2022;105685. doi:10.1016/j.clinbiomech.2022.105685
24. Ward SR, Hentzen ER, Smallwood LH, et al., Lieber RL. Rotator cuff muscle architecture: implications for glenohumeral stability. Clin Orthop Relat Res 2006;448:157–163
25. Mathewson MA, Kwan A, Eng CM, Lieber RL, Ward SR. Comparison of rotator cuff muscle architecture between humans and other selected vertebrate species. J Exp Biol 2014;217(2):261–273
26. Langenderfer J, Jerabek SA, Thangamani VB, Kuhn JE, Hughes RE. Musculoskeletal parameters of muscles crossing the shoulder and elbow and the effect of sarcomere length sample size on estimation of optimal muscle length. Clin Biomech 2004;19(7):664–670 [R; через Holzbaur 2005]
27. Lieber RL, Fazeli BM, Botte MJ. Architecture of selected wrist flexor and extensor muscles. J Hand Surg Am 1990;15(2):244–250 [R]
28. Lieber RL, Jacobson MD, Fazeli BM, Abrams RA, Botte MJ. Architecture of selected muscles of the arm and forearm. J Hand Surg Am 1992;17(5):787–798 [R]
29. An KN, Hui FC, Morrey BF, Linscheid RL, Chao EY. Muscles across the elbow joint: a biomechanical analysis. J Biomech 1981;14(10):659–669
30. Ettema GJC, Styles G, Kippers V. The moment arms of 23 muscle segments of the upper limb with varying elbow and forearm positions. Hum Mov Sci 1998;17:201–220
31. Akagi R, Iwanuma S, Hashizume S, Kanehisa H, Yanai T, Kawakami Y. In vivo measurements of moment arm lengths of three elbow flexors at rest and during isometric contractions. J Appl Biomech 2012;28(1):63–69
32. Ramsay JW, Hunter BV, Gonzalez RV. Muscle moment arm and normalized moment contributions as reference data for musculoskeletal elbow and wrist joint models. J Biomech 2009;42(4):463–473 — готовые полиномы плеча от угла

## Мышцы лопатки: анатомия

33. Webb AL, O’Sullivan E, Stokes M, Mottram S. A novel cadaveric study of the morphometry of the serratus anterior muscle. Anat Sci Int 2018;93(1):98–107
34. Johnson G, Bogduk N, Nowitzke A, House D. Anatomy and actions of the trapezius muscle. Clin Biomech 1994;9(1):44–50 [R]

## Другие наборы параметров

35. Garner BA, Pandy MG. Estimation of musculotendon properties in the human upper limb. Ann Biomed Eng 2003;31(2):207–220
36. Wu W, Lee PVS, Bryant AL, Galea M, Ackland DC. Subject-specific musculoskeletal modeling in the evaluation of shoulder muscle and joint function. J Biomech 2016;49(15):3626–3634 [R; параметры из файла модели]

## Масштабирование

37. Delp SL, Anderson FC, Arnold AS, et al., Thelen DG. OpenSim: open-source software to create and analyze dynamic simulations of movement. IEEE Trans Biomed Eng 2007;54(11):1940–1950 — правило масштабирования Lopt/Lts
38. Modenese L, Ceseracciu E, Reggiani M, Lloyd DG. Estimation of musculotendon parameters for scaled and subject specific musculoskeletal models using an optimization technique. J Biomech 2016;49(2):141–148
39. Correa TA, Pandy MG. A mass–length scaling law for modeling muscle strength in the lower limb. J Biomech 2011;44(16):2782–2789
40. Handsfield GG, Meyer CH, Hart JM, Abel MF, Blemker SS. Relationships of 35 lower limb muscles to height and body mass quantified using MRI. J Biomech 2014;47(3):631–638
41. Klemt C, Nolte D, Ding Z, et al., Bull AMJ. Anthropometric scaling of anatomical datasets for subject-specific musculoskeletal modelling of the shoulder. Ann Biomed Eng 2019;47(4):924–936
42. Kainz H, Goudriaan M, Falisse A, et al., Jonkers I. The influence of maximum isometric muscle force scaling on estimated muscle forces from musculoskeletal models of children with cerebral palsy. Gait Posture 2018;65:213–220
43. Winby CR, Lloyd DG, Kirk TB, Besier TF. Evaluation of different analytical methods for subject-specific scaling of musculotendon parameters. J Biomech 2008;41(8):1682–1688

## Сверка: упражнения и сила

44. Mausehund L, Werkhausen A, Bartsch J, Krosshaug T. Understanding bench press biomechanics — the necessity of measuring lateral barbell forces. J Strength Cond Res 2022;36(10):2685–2695
45. Schütz P, Zimmer P, Zeidler F, et al., Lorenzetti SR. Chest exercises: movement and loading of shoulder, elbow and wrist joints. Sports 2022;10(2):19
46. Larsen S, Gomo O, van den Tillaar R. A biomechanical analysis of wide, medium, and narrow grip width effects on kinematics, horizontal kinetics, and muscle activity on the sticking region in recreationally trained males during 1-RM bench pressing. Front Sports Act Living 2021;2:637066
47. Duffey MJ, Challis JH. Vertical and lateral forces applied to the bar during the bench press in novice lifters. J Strength Cond Res 2011;25(9):2442–2447
48. Van Every DW, Coleman M, Plotkin DL, et al., Schoenfeld BJ. Biomechanical, anthropometric and psychological determinants of barbell bench press strength. Sports 2022;10(12):199
49. Lorenzetti S, Dayer R, Plüss M, List R. Pulling exercises for strength training and rehabilitation: movements and loading conditions. J Funct Morphol Kinesiol 2017;2(3):33
50. Urbanczyk CA, Prinold JAI, Reilly P, Bull AMJ. Avoiding high-risk rotator cuff loading: muscle force during three pull-up techniques. Scand J Med Sci Sports 2020;30(11):2205–2214
51. Saul KR, Vidt ME, Gold GE, Murray WM. Upper limb strength and muscle volume in healthy middle-aged adults. J Appl Biomech 2015;31:484–491
52. Harbo T, Brincks J, Andersen H. Maximal isokinetic and isometric muscle strength of major muscle groups related to age, body mass, height, and sex in 178 healthy subjects. Eur J Appl Physiol 2012;112:267–275
53. Pinter IJ, Bobbert MF, van Soest AJK, Smeets JBJ. Isometric torque–angle relationships of the elbow flexors and extensors in the transverse plane. J Electromyogr Kinesiol 2010;20:923–931
54. Aronis G, Kurz M, Wimmer F, Hackl H, Angeli T, Gföhler M. Maximum shoulder torque and muscle activation during standing arm flexion. J Funct Morphol Kinesiol 2026;11(1):20
55. Cavuoto LA, Pajoutan M, Mehta RK. Reliability analyses and values of isometric shoulder flexion and trunk extension strengths stratified by body mass index. PLoS ONE 2019;14(7):e0219090
56. Roy JS, MacDermid JC, Usher Boyd K, et al., Athwal GS. Rotational strength, range of motion, and function in people with unaffected shoulders from various stages of life. Sports Med Arthrosc Rehabil Ther Technol 2009;1:4
57. Vidt ME, Daly M, Miller ME, Davis CC, Marsh AP, Saul KR. Characterizing upper limb muscle volume and strength in older adults. J Biomech 2012;45(2):334–341
58. Chaffin DB, Andersson GBJ, Martin BJ. Occupational Biomechanics, 3rd ed. Wiley, 1999 (формулы силы по Stobbe 1982; приведены в arXiv:1503.06391)
59. Noteboom L, Belli I, Hoozemans MJM, Seth A, Veeger HEJ, van der Helm FCT. Effects of bench press technique variations on musculoskeletal shoulder loads and potential injury risk. Front Physiol 2024;15:1393235
60. Ekstrom RA, Donatelli RA, Soderberg GL. Surface electromyographic analysis of exercises for the trapezius and serratus anterior muscles. J Orthop Sports Phys Ther 2003;33(5):247–258 [R]
61. Pizzari T, Wickham J, Balster S, Ganderton C, Watson L. Modifying a shrug exercise can facilitate the upward rotator muscles of the scapula. Clin Biomech 2014;29(2):201–205

## Учебники и атласы

62. Standring S (ed.). Gray’s Anatomy: The Anatomical Basis of Clinical Practice, 42nd ed. Elsevier, 2020 — места начала и прикрепления
63. Neumann DA. Kinesiology of the Musculoskeletal System, 3rd ed. Elsevier, 2017 — функции мышц, пары сил лопатки
64. Kapandji IA. The Physiology of the Joints, Vol. 1: The Upper Limb, 7th ed. Handspring, 2019
65. Netter FH. Atlas of Human Anatomy, 8th ed. Elsevier, 2022

## Прочее

66. Sugisaki N, Wakahara T, Murata K, et al., Fukunaga T. Influence of muscle hypertrophy on the moment arm of the triceps brachii muscle. J Appl Biomech 2015;31(2) — рост мышцы почти не меняет плечо
67. Lavaill M, Martelli S, Gilliland L, et al., Pivonka P. The effects of anatomical errors on shoulder kinematics computed using multi-body models. Biomech Model Mechanobiol 2022
68. Bergmann G, Graichen F, Bender A, et al. In vivo gleno-humeral joint loads during forward flexion and abduction. J Biomech 2011;44:1543–1552 [R; число по вторичному источнику]
69. Axford DT, Potra R, Appleyard R, et al., Ferreira LM. Three-dimensional continuous muscle moment arm maps for the anatomical shoulder. J Biomech 2025;182:112561 — лучшие современные карты плеч по плоскостям
