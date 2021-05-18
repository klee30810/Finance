import dart_fss as dart

api_key='998bebe5acc23a9e8321f35d52181529440718e8'
dart.set_api_key(api_key=api_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
filename = '삼성전자'
samsung = corp_list.find_by_corp_name(filename, exactly=True)[0]

# 2012년부터 연간&분기 연결재무제표 불러오기
fs = samsung.extract_fs(bgn_de='20120101', report_tp='quarter')

# 재무제표 일괄저장 (default: 실행폴더/fsdata/{corp_code}_{report_tp}.xlsx)
#fs.save()

# 재무제표 일괄저장
path = '/User/klee30810/Documents/Career/Finance/halto/fsdata'
fs.save(filename=filename, path=path)
