# Источники: мышцы корпуса

Номера совпадают с `refs` в `muscles.json` и `ref` в `validation.json`. «Через X» — число взято из вторичного источника X, который цитирует оригинал.

1. Christophy M, Faruk Senan NA, Lotz JC, O'Reilly OM (2012). A musculoskeletal model for the lumbar spine. Biomech Model Mechanobiol 11:19–34. https://link.springer.com/article/10.1007/s10237-011-0290-6  
   Что взято: Исходная модель: 238 пучков, кинематика поясницы (доли L1/L2…L5/S1 = 0,255/0,231/0,204/0,185/0,125, табл. 3 по Wong 2006).
2. Christophy M (2010). A detailed open-source musculoskeletal model of the human lumbar spine. MS thesis, UC Berkeley. https://spine.berkeley.edu/papers/Miguel-Masters.pdf  
   Что взято: PCSA групп (табл. 4.1), удельное напряжение 46 Н/см², обзор значений 22–100 Н/см² (табл. 4.2).
3. Walia R, Garzon K, Billot M et al. (2025). MyoBack: A Musculoskeletal Model of the Human Back with Integrated Exoskeleton. IROS 2025; модель MyoTorso в репозитории MyoHub/myo_sim (Apache-2.0), конвертация Constrained Lumbar Spine model-210 (SimTK). https://github.com/MyoHub/myo_sim  
   Что взято: Геометрия всех точек и Fmax пучков (myotorso_chain/tendon/muscle.xml); плечи пересчитаны нами в MuJoCo 3.x.
4. Bogduk N, Macintosh JE, Pearcy MJ (1992). A universal model of the lumbar back muscles in the upright position. Spine 17:897–913. https://wbldb.lievers.net/10376021.html  
   Что взято: На L4–L5 грудные пучки ES дают 50% разгибающего момента, многораздельная ~20%; 46 Н/см².
5. Bogduk N, Johnson G, Spalding D (1998). The morphology and biomechanics of latissimus dorsi. Clin Biomech 13:377–385. https://www.academia.edu/28883625  
   Что взято: PCSA пучков широчайшей, плечи ~7 см (грудные) и ~4 см (шов фасции и подвздошные), вклад в разгибание поясницы ≤6–12 Н·м.
6. Delp SL, Suryanarayanan S, Murray WM, Uhlir J, Triolo RJ (2001). Architecture of the rectus abdominis, quadratus lumborum, and erector spinae. J Biomech 34:371–375. https://nmbl.stanford.edu/publications/pdf/Vasavada2010.pdf  
   Что взято: Оптимальная длина волокон, перистость, PCSA (таблица перепечатана в Vasavada 2010).
7. Ward SR, Kim CW, Eng CM et al. (2009). Architectural analysis and intraoperative measurements demonstrate the unique design of the multifidus muscle for lumbar spine stability. J Bone Joint Surg Am 91:176–185. https://muscle.ucsd.edu/pubs/pdf/Ward_JBJSA_2009.pdf  
   Что взято: Многораздельная: длина волокна 5,66 см, PCSA 23,9 см².
8. Ward SR, Eng CM, Smallwood LH, Lieber RL (2009). Are current measurements of lower extremity muscle architecture accurate? Clin Orthop Relat Res 467:1074–1082. https://muscle.ucsd.edu/pubs/pdf/Ward_CORR_2009.pdf  
   Что взято: Большая поясничная: волокно 11,69 см, перистость 10,6°, PCSA 7,7 см².
9. Brown SHM, Ward SR, Cook MS, Lieber RL (2011). Architectural analysis of human abdominal wall muscles: implications for mechanical function. Spine 36:355–362. https://muscle.ucsd.edu/pubs/pdf/Brown_Spine_2011.pdf  
   Что взято: Прямая/наружная/внутренняя косая/поперечная: длина волокон 26,7/14,6/7,8/9,7 см, PCSA 3,3/6,6/8,6/4,7 см².
10. Stokes IAF, Gardner-Morse M (1999). Quantitative anatomy of the lumbar musculature. J Biomech 32:311–316. https://www.uvm.edu/~istokes/pdfs/qanatomy.pdf  
   Что взято: PCSA косых по пучкам (сумма 1575 и 1345 мм²), прямой 567 мм².
11. McGill SM, Patt N, Norman RW (1988). Measurement of the trunk musculature of active males using CT scan radiography: implications for force and moment generating capacity about the L4/L5 joint. J Biomech 21:329–341. https://wbldb.lievers.net/10368736.html  
   Что взято: КТ L4/L5, 13 мужчин: плечи ES 5,90, RA 10,28, психас 0,58 см; PCSA.
12. Anderson DE, D'Agostino JM, Bruno AG, Manoharan RK, Bouxsein ML (2012). Regressions for estimating muscle parameters in the thoracic and lumbar trunk for use in musculoskeletal modeling. J Biomech 45:66–75. https://dash.harvard.edu/server/api/core/bitstreams/7312037e-caba-6bd4-e053-0100007fdf3b/content  
   Что взято: Регрессии CSA и положения мышц по полу, возрасту, росту, массе (КТ, 100 человек 36–87 лет). Коэффициенты взяты из текста PDF, сверить с таблицами 3–4.
13. Jorgensen MJ, Marras WS, Gupta P, Waters TR (2003). Effect of torso flexion on the lumbar torso extensor muscle sagittal plane moment arms. Spine J 3:363–369. https://www.science.gov/topicpages/s/sagittal+plane+lumbar  
   Что взято: Плечо ES на L5/S1 от 0° до 45° сгибания уменьшается на 9,7% (мужчины).
14. Jorgensen MJ, Marras WS, Waters TR (2002). Proc HFES 46:1061 — плечи, зависящие от сгибания, в ЭМГ-модели. https://stacks.cdc.gov/view/cdc/195803/cdc_195803_DS1.pdf  
   Что взято: Учёт уменьшения плеча повышает расчётное сжатие L5/S1 на 6,6%, сдвиг на 11%.
15. McGill SM, Hughson RL, Parks K (2000). Changes in lumbar lordosis modify the role of the extensor muscles. Clin Biomech 15:777–780 (с данными Macintosh, Bogduk, Pearcy 1993, Spine 18:884). https://paulogentil.com/pdf/Changes%20in%20lumbar%20lordosis%20modify%20the%20role%20of%20the%20extensor%20muscles.pdf  
   Что взято: Угол волокон длиннейшей на L3: 26° стоя, 11° при полном сгибании; при полном сгибании плечо и сдвиговая составляющая меняются.
16. Tveit P, Daggfeldt K, Hetland S, Thorstensson A (1994). Erector spinae lever arm length variations with changes in spinal curvature. Spine 19:199–204 (через Mawston & Boocock 2012). https://nzjp.otago.ac.nz/nzjp/article/download/40/39/149  
   Что взято: Плечо апоневроза ES при полном сгибании на 10–20% меньше, чем в лордозе.
17. Rajagopal A, Dembia CL, DeMers MS et al. (2016). Full-body musculoskeletal model for muscle-driven simulation of human gait. IEEE Trans Biomed Eng 63:2068–2079 (MyoLeg в MyoHub/myo_sim). https://github.com/MyoHub/myo_sim  
   Что взято: Дистальная часть пути большой поясничной (край таза, малый вертел).
18. Delp SL et al. (1990). An interactive graphics-based model of the lower extremity. IEEE Trans Biomed Eng 37:757–767; модель OpenSim gait2392. https://simtk.org/projects/opensim  
   Что взято: Положение центра тазобедренного сустава в системе таза (−0,0707; −0,0661; ±0,0835 м), к которой привязана модель Christophy.
19. Holzbaur KRS, Murray WM, Delp SL (2005). A model of the upper extremity for simulating musculoskeletal surgery and analyzing neuromuscular control. Ann Biomed Eng 33:829–840 (MyoArm в MyoHub/myo_sim). https://github.com/MyoHub/myo_sim  
   Что взято: Плечевой сустав, точки широчайшей на плечевой кости, лопатке и грудной клетке.
20. Cholewicki J, McGill SM, Norman RW (1991). Lumbar spine loads during the lifting of extremely heavy weights. Med Sci Sports Exerc 23:1179–1186. https://pubmed.ncbi.nlm.nih.gov/1758295/  
   Что взято: Становая тяга на соревнованиях: момент L4/L5 до 988 Н·м, сжатие до 17 192 Н.
21. Ramirez VJ et al. (2022). IISE Trans Occup Ergon Hum Factors 10:34 (обзор нагрузок при тяжёлой атлетике). https://stacks.cdc.gov/view/cdc/123816/cdc_123816_DS1.pdf  
   Что взято: Диапазоны по Cholewicki 1991: мужчины 445–1071 Н·м, сжатие 7942–18 449 Н.
22. Granhed H, Jonson R, Hansson T (1987). The loads on the lumbar spine during extreme weight lifting. Spine 12:146–149 (через Hartmann 2016). https://www.mdpi.com/2411-5142/1/2/254  
   Что взято: Тяга 212–335 кг: сжатие L3 18,8–36,4 кН.
23. Hartmann H, Wirth K, Klusemann M et al. (2016). J Funct Morphol Kinesiol 1:254 (обзор нагрузок на позвоночник в приседе и тяге). https://www.mdpi.com/2411-5142/1/2/254  
   Что взято: Вторичный источник для Granhed 1987, Cappozzo 1985, Lander 1990.
24. Cappozzo A, Felici F, Figura F, Gazzani F (1985). Lumbar spine loading during half-squat exercises. Med Sci Sports Exerc 17:613–620 (через Hartmann 2016). https://www.mdpi.com/2411-5142/1/2/254  
   Что взято: Полуприсед со штангой 0,8–1,6 веса тела: сжатие L3/L4 6–10 весов тела.
25. Lander JE, Simonton RL, Giacobbe JKF (1990). The effectiveness of weight-belts during the squat exercise. Med Sci Sports Exerc 22:117–126 (через Hartmann 2016). https://www.mdpi.com/2411-5142/1/2/254  
   Что взято: Параллельный присед 70–90% 1ПМ: среднее сжатие L5/S1 9983 Н.
26. Swinton PA, Stewart A, Agouris I, Keogh JWL, Lloyd R (2011). A biomechanical analysis of straight and hexagonal barbell deadlifts using submaximal loads. J Strength Cond Res 25:2000–2009. https://rgu-repository.worktribe.com/OutputFile/295851  
   Что взято: Пиковый момент L5/S1 по %1ПМ, расстояние гриф–L5/S1.
27. Swinton PA, Lloyd R, Keogh JWL, Agouris I, Stewart AD (2012). A biomechanical comparison of the traditional squat, powerlifting squat, and box squat. J Strength Cond Res 26:1805–1816. https://rgu-repository.worktribe.com/OutputFile/295848  
   Что взято: Пиковый момент L5/S1 в трёх вариантах приседа при 30/50/70% 1ПМ.
28. Wilke HJ, Neef P, Caimi M, Hoogland T, Claes LE (1999). New in vivo measurements of pressures in the intervertebral disc in daily life. Spine 24:755–762. https://wbldb.lievers.net/10209298.html  
   Что взято: Внутридисковое давление L4/L5 (МПа) в позах и при подъёме 20 кг.
29. Dreischarf M, Rohlmann A, Zhu R, Schmidt H, Zander T (2013). Is it possible to estimate the compressive force in the lumbar spine from intradiscal pressure measurements? Med Eng Phys 35:1385–1390. https://www.bisp-surf.de/Record/PU201503002411  
   Что взято: Перевод давления в силу F = P × A × 0,66 (A ≈ 18 см²); сила L4/L5 стоя 430–600 Н.
30. Malakoutian M et al. (2022). Front Bioeng Biotechnol 10:852201 (модель на основе Christophy, σ = 100 Н/см²). https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2022.852201/pdf  
   Что взято: Сжатие L4/L5 и L5/S1 в позах Wilke.
31. Lerchl T et al. (2024). Front Bioeng Biotechnol 12:1363081. https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2024.1363081/full  
   Что взято: Сжатие L4/L5 у 93 человек: стоя 605 Н, наклон 30° 1651 Н.
32. Gallagher S, Marras WS (2012). Tolerance of the lumbar spine to shear: a review and recommended exposure limits. Clin Biomech 27:973–978. https://spine.osu.edu/sites/default/files/uploads/Publications/2012/ClinicalBiomechanics_2012_27_973-978.pdf  
   Что взято: Пределы сдвига 1000 Н (редко) и 700 Н (часто).
33. Waters TR, Putz-Anderson V, Garg A, Fine LJ (1993). Revised NIOSH equation for the design and evaluation of manual lifting tasks. Ergonomics 36:749–776. https://stacks.cdc.gov/view/cdc/205542  
   Что взято: Критерий сжатия L5/S1 3,4 кН (6,4 кН — опасный уровень, NIOSH 1981).
34. Jäger M (2018). Extended compilation of autopsy-material measurements on lumbar ultimate compressive strength for deriving reference values in ergonomic work design: The Revised Dortmund Recommendations. EXCLI J 17:362–385. https://www.excli.de/excli/article/view/463  
   Что взято: Прочность на сжатие: мужчины 6,09 ± 2,69 кН; рекомендуемые пределы 5,4 кН (20 лет) … 2,2 кН (60+).
35. Ghezelbash F, Shirazi-Adl A, Arjmand N et al. (2018). J Biomech 70:124 / IRSST — максимальное разгибание 236 Н·м (мужчины), 190 Н·м (женщины); максимальное напряжение мышц 0,8 МПа в среднем. https://pharesst.irsst.qc.ca/etudes-primaires/180  
   Что взято: Максимальный произвольный момент разгибания.
36. Anders C et al. (2026). Standing trunk extension MVC (preprint, JFMK 11:212). https://www.preprints.org/manuscript/202604.1462/v1  
   Что взято: Мужчины 241 Н·м, женщины 162 Н·м (n = 124 мужчин).
37. Favier CD, Finnegan ME, Quest RA et al. (2021). An open-source musculoskeletal model of the lumbar spine and lower limbs: a validation for movements of the lumbar spine. CMBBE 24:1310–1325. https://spiral.imperial.ac.uk/bitstreams/8cb28c2a-97c2-4333-941b-214a00b5c7b9/download  
   Что взято: London Lumbar Spine Model: σ = 100 Н/см², максимальное разгибание 175–310 Н·м при 0–60°.
38. Bruno AG, Bouxsein ML, Anderson DE (2015). Development and validation of a musculoskeletal model of the fully articulated thoracolumbar spine and rib cage. J Biomech Eng 137:081003. https://simtk.org/home/spine_ribcage  
   Что взято: Модель грудо-поясничного отдела с рёбрами, σ = 100 Н/см².
39. Ramirez VJ, Ghezelbash F, Shirazi-Adl A, Bazrgari B (2023). Trunk muscle forces and spinal loads during heavy deadlift. Int J Numer Method Biomed Eng 39:e3680. https://scholars.uky.edu/en/publications/trunk-muscle-forces-and-spinal-loads-during-heavy-deadlift-effect/  
   Что взято: Плечи мышц +40% → пиковое сжатие −32%: чувствительность к масштабированию.
40. Arjmand N, Shirazi-Adl A, Bazrgari B (2006). Wrapping of trunk thoracic extensor muscles influences muscle forces and spinal loads in lifting tasks. Clin Biomech 21:668–675. https://scholars.uky.edu/en/publications/wrapping-of-trunk-thoracic-extensor-muscles-influences-muscle-for/  
   Что взято: Уменьшение плеч при наклоне на 10% повышает силы мышц и сжатие.
41. Aiyangar A et al. (2015). J Biomech 48:3709 — доли уровней L2–S1 при подъёме груза. https://stacks.cdc.gov/view/cdc/203201  
   Что взято: L5/S1 22,6%, L4/L5 31%, L3/L4 25,8%, L2/L3 21,7%.
42. Huang (2019). BU thesis: регрессии плеч мышц корпуса с глубиной и шириной туловища. https://open.bu.edu/items/4a089ce1-2ba7-4ff2-a570-f14aacef6659  
   Что взято: Глубина туловища улучшает прогноз передне-задних плеч.
43. Delp SL, Anderson FC, Arnold AS et al. (2007). OpenSim: open-source software to create and analyze dynamic simulations of movement. IEEE Trans Biomed Eng 54:1940–1950 (инструмент Scale). https://simtk.org/projects/opensim  
   Что взято: Масштабирование по сегментам: точки крепления масштабируются с сегментом, длины волокна и сухожилия сохраняют долю от длины мышцы.

## Книги (для чтения; числа из них не брались, тексты не открывались)

- Bogduk N. Clinical and Radiological Anatomy of the Lumbar Spine, 5th ed. Churchill Livingstone, 2012. Главы о мышцах и фасциях поясницы.
- McGill S. Low Back Disorders: Evidence-Based Prevention and Rehabilitation, 3rd ed. Human Kinetics, 2016.
- Neumann DA. Kinesiology of the Musculoskeletal System, 3rd ed. Elsevier, 2017. Глава об осевом скелете: мышцы туловища и их плечи.
- Chaffin DB, Andersson GBJ, Martin BJ. Occupational Biomechanics, 4th ed. Wiley, 2006. Модели нагрузки на L5/S1 с фиксированным плечом 5 см.
- Kapandji IA. The Physiology of the Joints, vol. 3: The Spinal Column, Pelvic Girdle and Head.
- Bergmark A (1989). Stability of the lumbar spine. Acta Orthop Scand Suppl 230:1–54. Деление на «локальные» (многораздельная, поясничные пучки ES) и «глобальные» (грудные пучки ES, мышцы живота) мышцы.
- Cholewicki J, McGill SM (1996). Mechanical stability of the in vivo lumbar spine. Clin Biomech 11:1–15.
