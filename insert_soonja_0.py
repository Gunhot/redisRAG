import redis

r = redis.Redis(host='localhost', port=6379, db=0)

profile = """이름: 김순자 (81세)
거주지: 부산 남구 대연동
가족관계:
- 남편 고(故) 박정호 (15년 전 작고)
- 장녀 박미연 (53세, 초등학교 교사)
- 차녀 박미숙 (51세, 간호사)
- 장남 박준호 (48세, 회사원)
- 손주 5명
친구관계:
- 이명숙 (81세, 40년지기 친구, 같은 아파트 거주)
- 박영자 (79세, 교회 친구)
- 황정희 (82세, 복지관 댄스 동아리 친구)"""
r.set('0p', profile)
