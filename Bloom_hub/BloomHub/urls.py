from django.urls import path
from . import views  # views 모듈을 임포트하여 사용

urlpatterns = [
    path('', views.home, name='home'), 
    path('kor/', views.home_kor, name='homekor'),

    path('guide/', views.guide, name='guide'),
    path('guide/kor/', views.guide_kor, name='guidekor'),

    path('learning/', views.learning, name='learning'),
    path('learning/kor/', views.learning_kor, name='learningkor'),

    path('learned/', views.learned, name='learned'),
    path('learned/kor/', views.learned_kor, name='learnedkor'),


    #############로그인 관련 urls###############
    path('login/', views.login_view, name='login'),
    path('login/kor/', views.login_kor, name='loginkor'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup_view, name='signup'),
    path('signup/kor/', views.signup_kor, name='signupkor'),
    path('check-duplicate/', views.check_duplicate, name='check_duplicate'),
    path('check-login/', views.check_login, name='check_login'),

    #################### 아이디 찾기, 비번찾기, 이메일 인증필요 ###################

    path('find-id/', views.find_id, name='findID'),
    path('find-id/kor/', views.find_id_kor, name='findIDkor'),
    path('find-pwd/', views.find_pwd, name='findpwd'),
    path('find-pwd/kor/', views.find_pwd_kor, name='findpwdkor'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('verify_code_and_find_id/', views.verify_code_and_find_id, name='verify_code_and_find_id'),
    path('send_verification_code_for_password_reset/', views.send_verification_code_for_password_reset, name='send_verification_code_for_password_reset'),
    path('verify_code_for_password_reset/', views.verify_code_for_password_reset, name='verify_code_for_password_reset'),
    path('reset_password/', views.reset_password, name='reset_password'),

    #############################마이페이지,비번변경,닉넴변경,이메일변경처리 할것######################################

    path('mypage/', views.mypage, name='mypage'),
    path('mypage/kor/', views.mypage_kor, name='mypagekor'),
    path('mypage/manager/', views.mypage_manager, name='mypage_manager'),
    path('change_email/', views.change_email, name='change_email'),
    path('mypage/password/change/', views.mypage_reset_password, name='mypage_reset_password'),

    ########################### 검색 및 검색 결과 ########################################
    path('search', views.search, name='search'),
    path('searchkor', views.search_kor, name='searchkor'), # 슬래시 없이 URL 작성
    path('search/result', views.search_result, name='searchresult'),
    path('search/result/kor', views.search_result_kor, name='searchresultkor'),
    ##################비디오 저장 및 추출 분석#################################
    path('study/<str:video_id>', views.study, name='study'),  # video_id를 인자로 받는 study URL
    path('study/kor/<str:video_id>', views.study_kor, name='studykor'),
    path('save_learning_video/', views.save_learning_video, name='save_learning_video'),
    path('run_extractor_and_save_to_db/', views.run_extractor_and_save_to_db,name='run_extractor_and_save_to_db'),
    path('run_analysis/<str:video_id>/', views.run_analysis, name='run_analysis'), 
    path('save_analysis_result/', views.save_analysis_result, name='save_analysis_result'),
    path('get_analysis_result/<str:video_id>/',views.get_analysis_result, name='get_analysis_result'),

    path('analysis/', views.analysis, name='analysis'),

    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('change_email/', views.change_email, name='change_email'),
    path('check_old_password/', views.check_old_password, name='check_old_password'),
]
