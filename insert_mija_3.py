import redis

r = redis.Redis(host='localhost', port=6379, db=0)

profile = """이름: 박미자
거주지: 서울특별시 강남구 압구정동 고급 아파트
가족관계:

남편: 고(故) 정재호 (전 대기업 임원)
자녀: 정유진(장녀, 의사), 정민수(장남, 변호사), 정서연(차녀, 교수)
손주: 5명
친구관계:
압구정 실버요가 동호회 회원들
문화센터 수채화반 친구들
대학교 동창모임 멤버들"""
r.set('3p', profile)
