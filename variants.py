class VariantForRiskRatio:
    def __init__(self):
        self.var_service = [
            # service
            'has_visited_hospital',
            'had_NOT_had_exam',
            # 'had_been_cared',
            # 'need_support',
            # 'need_care',

            # 'is_subject_to_program',
            # 'is_NOT_any_subject_to_program',
            # 'had_attended_to_program',
            # 'had_NOT_any_attended_to_program',
            #
            # 'is_NOT_any_determined_program_level',
            # 'is_to_take_intervention',
            # 'is_to_be_motivated',
            # 'is_to_be_given_info',
            # 'is_to_be_given_info(have_drug)',
            # 'had_to_be_motivated',
            # 'had_motivated',
            # 'had_to_take_intervention',
            # 'had_taken_intervention',
        ]

        self.var_exam_result = [
            # NCD risk
            'has_DM_risk',
            'has_HT_risk',
            'has_DL_risk',

            # blood glu lv
            'is_Glu_controlled',
            'is_(HbA1c_5.6to6.5_OR_Glu_fasting_100to126)',
            'is_(HbA1c_6.5to7.0_OR_Glu_fasting_126to130)',
            'is_(HbA1c_7.0to8.0_OR_Glu_fasting_130to140)',

            'is_Glu_GE_HbA1c5.6_OR_Glu100',
            'is_Glu_GE_HbA1c6.5_OR_Glu126',
            'is_Glu_GE_HbA1c7.0_OR_Glu130',
            'is_Glu_GE_HbA1c8.0_OR_Glu140',

            'is_HbA1c_controlled',
            'is_(HbA1c_5.6to6.5)',
            'is_(HbA1c_6.5to7.0)',
            'is_(HbA1c_7.0to8.0)',

            'is_(HbA1c_GE_5.6)',
            'is_(HbA1c_GE_6.5)',
            'is_(HbA1c_GE_7.0)',
            'is_(HbA1c_GE_8.0)',

            # blood pressure lv
            'is_BP_controlled',
            'is_BP_slightly_high',
            'is_hypertension_lv1',
            'is_hypertension_lv2',
            'is_hypertension_lv3',

            'is_BP_higher',
            'is_hypertension_lv_GE1',
            'is_hypertension_lv_GE2',
            'is_hypertension_lv_GE3',

            # blood lipid lv
            'is_Lipid_controlled',
            'is_(LDL_120to140_OR_TG_150to300)',
            'is_(LDL_140to180_OR_TG_300to500)',

            'is_(LDL_GE_120_OR_TG_GE_150)',
            'is_(LDL_GE_140_OR_TG_GE_300)',
            'is_(LDL_GE_180_OR_TG_GE_500)',

            'is_LDL_GE_140_OR_TG_GE_150_OR_HDL_LT_40',

            # kidney function
            '(is_eGFR_LT_60)&(is_UP_GE_3)',

            'is_eGFR_controlled',
            'is_eGFR_60to90',
            'is_eGFR_30to60',
            'is_eGFR_15to30',

            'is_(eGFR_LT_90)',
            'is_(eGFR_LT_60)',
            'is_(eGFR_LT_30)',
            'is_(eGFR_LT_15)',

            # from single variant
            'is_BMI_GE_25',
            'is_BMI_GE_30',

            f'is_waist_circumference_GE_male85_female90',

            'is_Glu_fasting_GE_100',
            'is_Glu_fasting_GE_126',

            'is_HbA1c_GE_5.6',
            'is_HbA1c_GE_6.5',
            'is_HbA1c_GE_7.0',
            'is_HbA1c_GE_8.0',

            'is_SBP_GE_130',
            'is_SBP_GE_140',
            'is_DBP_GE_85',
            'is_DBP_GE_90',

            'is_LDL_GE_120',
            'is_LDL_GE_140',

            'is_TG_GE_150',
            'is_TG_GE_300',

            'is_HDL_LT_40',
            'is_HDL_LT_35',

            'is_UP_GE_3',
            'is_US_GE_3',

            'is_eGFR_LT_90',
            'is_eGFR_LT_60',
            'is_eGFR_LT_30',
            'is_eGFR_LT_15',
        ]

        self.var_intv_presc = [
            'has_presc_HT',
            'has_presc_DM',
            'has_presc_DL',
        ]

        self.var_intv_history = [
            'has_history_stroke',
            'has_history_CVD',
            'has_history_CKD',
            'has_story_anemia',
        ]

        self.var_intv_lifestyle = [

            'has_habit_smoke',
            'had_gained_weight',
            'has_NOT_exercise_habit',
            'has_NOT_walk_habit',
            'is_slow',
            'had_changed_weight',
            'is_hardly_to_chew',
            'is_fast_to_eat',
            'has_supper_late_often',
            'has_late_night_snack_often',
            'has_snack_often',
            'has_breakfast_skipped_often',
            'has_alcohol_every_day',
            'has_alcohol_heavily',
            'has_not_enough_sleep',
            'is_lazy',
            'is_not_likely_to_be_assigned_to_program',

            'has_been_drunk',
            'has_NOT_any_exercise_habit',
        ]

        self.var_disease = [
            # from receipt
            'is_diagnosed_as_diabetes_kdb',
            'is_diagnosed_as_hypertension_kdb',
            'is_diagnosed_as_dyslipidemia_kdb',
            'is_diagnosed_as_hyperuricemia_kdb',
            'is_diagnosed_as_IHD_kdb',
            # 'has_bypass_or_stent_operation_kdb',
            'is_diagnosed_as_aortic_disease_kdb',
            'is_diagnosed_as_CeVD_kdb',
            'is_diagnosed_as_AOD_kdb',
            # 'is_diagnosed_as_CKD_kdb',
            # 'is_diagnosed_as_musculoskeletal_disease_kdb',
            # 'is_diagnosed_as_SZ_kdb',

            'is_diagnosed_as_AnyMalignancy',
            'is_diagnosed_as_Arteriosclerosis',
            'is_diagnosed_as_COPD',
            'is_diagnosed_as_Diabetes',
            'is_diagnosed_as_Fracture',
            'is_diagnosed_as_Ossification',
            'is_diagnosed_as_Osteoarthritis_Knee',
            'is_diagnosed_as_RheumatoidArthritis',
            'is_diagnosed_as_SpinalStenosis',
            'is_diagnosed_as_Stroke',
        ]

        # from health check
        self.var_exam = self.var_exam_result + self.var_intv_presc + self.var_intv_history + self.var_intv_lifestyle

        self.var_all = self.var_service + self.var_exam + self.var_disease

        self.var_combi_NCD_risk_and_lifestyles = [
            '(has_DM_risk)&(has_NOT_any_exercise_habit)',
            '(has_HT_risk)&(has_NOT_any_exercise_habit)',
            '(has_DL_risk)&(has_NOT_any_exercise_habit)',
            '(is_BMI_GE_25)&(has_NOT_any_exercise_habit)',

            '(has_DM_risk)&(has_been_drunk)',
            '(has_HT_risk)&(has_been_drunk)',
            '(has_DL_risk)&(has_been_drunk)',
            '(is_BMI_GE_25)&(has_been_drunk)',

            '(has_DM_risk)&(has_habit_smoke)',
            '(has_HT_risk)&(has_habit_smoke)',
            '(has_DL_risk)&(has_habit_smoke)',
            '(is_BMI_GE_25)&(has_habit_smoke)',

            '(has_DM_risk)&(has_NOT_any_exercise_habit)&(has_been_drunk)',
            '(has_HT_risk)&(has_NOT_any_exercise_habit)&(has_been_drunk)',
            '(has_DL_risk)&(has_NOT_any_exercise_habit)&(has_been_drunk)',
            '(is_BMI_GE_25)&(has_NOT_any_exercise_habit)&(has_been_drunk)',

            '(has_DM_risk)&(has_NOT_any_exercise_habit)&(has_habit_smoke)',
            '(has_HT_risk)&(has_NOT_any_exercise_habit)&(has_habit_smoke)',
            '(has_DL_risk)&(has_NOT_any_exercise_habit)&(has_habit_smoke)',
            '(is_BMI_GE_25)&(has_NOT_any_exercise_habit)&(has_habit_smoke)',

            '(has_DM_risk)&(has_NOT_any_exercise_habit)&(has_been_drunk)&(has_habit_smoke)',
            '(has_HT_risk)&(has_NOT_any_exercise_habit)&(has_been_drunk)&(has_habit_smoke)',
            '(has_DL_risk)&(has_NOT_any_exercise_habit)&(has_been_drunk)&(has_habit_smoke)',
            '(is_BMI_GE_25)&(has_NOT_any_exercise_habit)&(has_been_drunk)&(has_habit_smoke)',

            '(has_DM_risk)&(has_been_drunk)&(has_habit_smoke)',
            '(has_HT_risk)&(has_been_drunk)&(has_habit_smoke)',
            '(has_DL_risk)&(has_been_drunk)&(has_habit_smoke)',
            '(is_BMI_GE_25)&(has_been_drunk)&(has_habit_smoke)',
        ]

        self.var_combi_NCD_risks = [
            '(has_DM_risk)&(has_HT_risk)',
            '(has_DL_risk)&(has_DM_risk)',
            '(has_DM_risk)&(is_BMI_GE_25)',
            '(has_DL_risk)&(has_HT_risk)',
            '(has_HT_risk)&(is_BMI_GE_25)',
            '(has_DL_risk)&(is_BMI_GE_25)',

            '(has_DL_risk)&(has_DM_risk)&(has_HT_risk)',
            '(has_DM_risk)&(has_HT_risk)&(is_BMI_GE_25)',
            '(has_DL_risk)&(has_DM_risk)&(is_BMI_GE_25)',
            '(has_DL_risk)&(has_HT_risk)&(is_BMI_GE_25)',

            '(has_DL_risk)&(has_DM_risk)&(has_HT_risk)&(is_BMI_GE_25)',
        ]

        self.dict_translate = {
            'has_visited_hospital': '医療機関受診あり',
            'had_NOT_had_exam': '健診未受診',
            # 'had_been_cared': '介護保険給付あり',
            # 'need_support': '介護保険給付あり（要支援）',
            # 'need_care': '介護保険給付あり（要介護）',

            # 'is_subject_to_program',
            # 'is_NOT_any_subject_to_program',
            # 'had_attended_to_program',
            # 'had_NOT_any_attended_to_program',
            #
            # 'is_NOT_any_determined_program_level',
            # 'is_to_take_intervention',
            # 'is_to_be_motivated',
            # 'is_to_be_given_info',
            # 'is_to_be_given_info(have_drug)',
            # 'had_to_be_motivated',
            # 'had_motivated',
            # 'had_to_take_intervention',
            # 'had_taken_intervention',

            # from health check

            # NCD risk
            'has_DM_risk': '血糖有所見',
            'has_HT_risk': '血圧有所見',
            'has_DL_risk': '血中脂質有所見',

            # blood glu lv
            'is_Glu_controlled': '血糖正常',
            'is_(HbA1c_5.6to6.5_OR_Glu_fasting_100to126)': 'HbA1c 5.6-6.5% または 空腹時血糖 100-126 mg/dL',
            'is_(HbA1c_6.5to7.0_OR_Glu_fasting_126to130)': 'HbA1c 6.5-7.0% または 空腹時血糖 126-130 mg/dL',
            'is_(HbA1c_7.0to8.0_OR_Glu_fasting_130to140)': 'HbA1c 7.0-8.0% または 空腹時血糖 130-140 mg/dL',

            'is_Glu_GE_HbA1c5.6_OR_Glu100': 'HbA1c 5.6%以上 または 空腹時血糖 100 mg/dL以上',
            'is_Glu_GE_HbA1c6.5_OR_Glu126': 'HbA1c 6.5%以上 または 空腹時血糖 126 mg/dL以上',
            'is_Glu_GE_HbA1c7.0_OR_Glu130': 'HbA1c 7.0%以上 または 空腹時血糖 130 mg/dL以上',
            'is_Glu_GE_HbA1c8.0_OR_Glu140': 'HbA1c 8.0%以上 または 空腹時血糖 140 mg/dL以上',

            'is_HbA1c_controlled': 'HbA1c正常',
            'is_(HbA1c_5.6to6.5)': 'HbA1c 5.6-6.5%',
            'is_(HbA1c_6.5to7.0)': 'HbA1c 6.5-7.0%',
            'is_(HbA1c_7.0to8.0)': 'HbA1c 7.0-8.0%',

            'is_(HbA1c_GE_5.6)': 'HbA1c 5.6%-',
            'is_(HbA1c_GE_6.5)': 'HbA1c 6.5%-',
            'is_(HbA1c_GE_7.0)': 'HbA1c 7.0%-',
            'is_(HbA1c_GE_8.0)': 'HbA1c 8.0%-',

            # blood pressure lv
            'is_BP_controlled': '至適血圧',
            'is_BP_slightly_high': '正常高値血圧',
            'is_hypertension_lv1': 'Ⅰ度高血圧',
            'is_hypertension_lv2': 'Ⅱ度高血圧',
            'is_hypertension_lv3': 'Ⅲ度高血圧',

            'is_BP_higher': '正常高値血圧以上',
            'is_hypertension_lv_GE1': 'I度高血圧以上',
            'is_hypertension_lv_GE2': 'Ⅱ度高血圧以上',
            'is_hypertension_lv_GE3': 'Ⅲ度高血圧以上',

            # blood lipid lv
            'is_Lipid_controlled': '血中脂質正常（LDL, TG）',

            'is_(LDL_120to140_OR_TG_150to300)': 'LDL 120-140 mg/dL または TG 150-300 mg/dL',
            'is_(LDL_140to180_OR_TG_300to500)': 'LDL 140-180 mg/dL または TG 300-500 mg/dL',

            'is_(LDL_GE_120_OR_TG_GE_150)': 'LDL 120 mg/dL以上 または TG 150 mg/dL以上',
            'is_(LDL_GE_140_OR_TG_GE_300)': 'LDL 140 mg/dL以上 または TG 300 mg/dL以上',
            'is_(LDL_GE_180_OR_TG_GE_500)': 'LDL 180 mg/dL以上 または TG 500 mg/dL以上',

            'is_LDL_GE_140_OR_TG_GE_150_OR_HDL_LT_40': 'LDL 140 mg/dL以上 または TG 150 mg/dL以上 または HDL 40 mg/dL未満',

            # kidney function
            '(is_eGFR_LT_60)&(is_UP_GE_3)': 'eGFR 60未満かつ尿蛋白陽性',

            'is_eGFR_controlled': 'eGFR正常',
            'is_eGFR_60to90': 'eGFR 60-90',
            'is_eGFR_30to60': 'eGFR 30-60',
            'is_eGFR_15to30': 'eGFR 15-30',

            'is_(eGFR_LT_90)': 'eGFR -90',
            'is_(eGFR_LT_60)': 'eGFR -60',
            'is_(eGFR_LT_30)': 'eGFR -30',
            'is_(eGFR_LT_15)': 'eGFR -15',

            # from single variant
            'is_BMI_GE_25': 'BMI 25以上',
            'is_BMI_GE_30': 'BMI 30以上',

            'is_waist_circumference_GE_male85_female90': '腹囲基準値（男性85 cm, 女性90 cm）以上',

            'is_Glu_fasting_GE_100': '空腹時血糖100 mg/dL以上',
            'is_Glu_fasting_GE_126': '空腹時血糖126 mg/dL以上',

            'is_HbA1c_GE_5.6': 'HbA1c 5.6%以上',
            'is_HbA1c_GE_6.5': 'HbA1c 6.5%以上',
            'is_HbA1c_GE_7.0': 'HbA1c 7.0%以上',
            'is_HbA1c_GE_8.0': 'HbA1c 8.0%以上',

            'is_SBP_GE_130': '収縮期血圧130 mmHg以上',
            'is_SBP_GE_140': '収縮期血圧140 mmHg以上',
            'is_DBP_GE_85': '拡張期血圧85 mmHg以上',
            'is_DBP_GE_90': '拡張期血圧90 mmHg以上',

            'is_LDL_GE_120': 'LDL 120 mg/dL以上',
            'is_LDL_GE_140': 'LDL 140 mg/dL以上',

            'is_TG_GE_150': '中性脂肪150 mg/dL以上',
            'is_TG_GE_300': '中性脂肪300 mg/dL以上',

            'is_HDL_LT_40': 'HDL40 mg/dL未満',
            'is_HDL_LT_35': 'HDL35 mg/dL未満',

            'is_UP_GE_3': '尿蛋白陽性',
            'is_US_GE_3': '尿糖陽性',

            'is_eGFR_LT_90': 'eGFR 90未満',
            'is_eGFR_LT_60': 'eGFR 60未満',
            'is_eGFR_LT_30': 'eGFR 30未満',
            'is_eGFR_LT_15': 'eGFR 15未満',

            'has_presc_DM': '問診_服薬あり（血糖）',
            'has_presc_HT': '問診_服薬あり（血圧）',
            'has_presc_DL': '問診_服薬あり（血中脂質）',

            'has_history_stroke': '問診_既往歴（脳卒中）',
            'has_history_CVD': '問診_既往歴（心臓病）',
            'has_history_CKD': '問診_既往歴（腎臓病）',
            'has_story_anemia': '問診_既往歴（貧血）',
            'has_habit_smoke': '問診_喫煙',
            'had_gained_weight': '問診_20代からの体重増加あり',
            'has_NOT_exercise_habit': '問診_運動習慣（30分以上の運動）なし',
            'has_NOT_walk_habit': '問診_運動習慣（1時間以上の歩行）なし',
            'is_slow': '問診_歩行速度が遅い',
            'had_changed_weight': '問診_直近1年間で3 kg以上の体重増減あり',
            'is_hardly_to_chew': '問診_咀嚼が困難',
            'is_fast_to_eat': '問診_食べる速度が速い',
            'has_supper_late_often': '問診_就寝直前に夕食をとる',
            'has_late_night_snack_often': '問診_夜食をとる',
            'has_snack_often': '問診_間食を取る',
            'has_breakfast_skipped_often': '問診_朝食を抜く',
            'has_alcohol_every_day': '問診_毎日飲酒する',
            'has_alcohol_heavily': '問診_３合以上飲酒する',
            'has_not_enough_sleep': '問診_睡眠で十分な休息が取れていない',
            'is_lazy': '問診_生活習慣改善の意欲がない',
            'is_not_likely_to_be_assigned_to_program': '問診_保健指導利用の意欲がない',

            'has_been_drunk': '問診_飲酒習慣がある',
            'has_NOT_any_exercise_habit': '問診_運動習慣（30分以上の運動または1時間以上の歩行）なし',

            # from receipt
            'is_diagnosed_as_diabetes_kdb': 'KDBレセ_受療あり（糖尿病）',
            'is_diagnosed_as_hypertension_kdb': 'KDBレセ_受療あり（高血圧症）',
            'is_diagnosed_as_dyslipidemia_kdb': 'KDBレセ_受療あり（脂質異常症）',
            'is_diagnosed_as_hyperuricemia_kdb': 'KDBレセ_受療あり（高尿酸血症）',
            'is_diagnosed_as_IHD_kdb': 'KDBレセ_受療あり（虚血性心疾患）',
            # 'has_bypass_or_stent_operation_kdb': 'KDBレセ_受療あり（ステント・バイパス手術）',
            'is_diagnosed_as_aortic_disease_kdb': 'KDBレセ_受療あり（大動脈疾患）',
            'is_diagnosed_as_CeVD_kdb': 'KDBレセ_受療あり（脳血管疾患）',
            'is_diagnosed_as_AOD_kdb': 'KDBレセ_受療あり（動脈閉塞性疾患）',
            # 'is_diagnosed_as_CKD_kdb': 'KDBレセ_受療あり（慢性腎臓病）',
            # 'is_diagnosed_as_musculoskeletal_disease_kdb': 'KDBレセ_受療あり（筋・骨格疾患）',
            # 'is_diagnosed_as_SZ_kdb': 'KDBレセ_受療あり（統合失調症）',
            'is_diagnosed_as_AnyMalignancy': 'レセあり（がん）',
            'is_diagnosed_as_Arteriosclerosis': 'レセあり（閉塞性動脈硬化症）',
            'is_diagnosed_as_COPD': 'レセあり（COPD）',
            'is_diagnosed_as_Diabetes': 'レセあり（合併症あり糖尿病）',
            'is_diagnosed_as_Fracture': 'レセあり（骨折）',
            'is_diagnosed_as_Ossification': 'レセあり（後縦靭帯骨化症）',
            'is_diagnosed_as_Osteoarthritis_Knee': 'レセあり（変形性膝・股関節症）',
            'is_diagnosed_as_RheumatoidArthritis': 'レセあり（関節リウマチ）',
            'is_diagnosed_as_SpinalStenosis': 'レセあり（脊柱管狭窄症）',
            'is_diagnosed_as_Stroke': 'レセあり（脳卒中）',

        }


__variant__ = VariantForRiskRatio()