import redis

r = redis.Redis(host='localhost', port=6379, db=0)

profile = """이름: 이춘자 (81세)
거주지: 광주 한옥마을
가족관계:
남편 고(故) (이른 나이에 작고)
장녀 윤미경 (패션디자이너)
장남 윤상철 (한의사)
차남 윤상현 (게스트하우스 운영)
친구관계:
최옥순 (50년지기 친구, 이웃 공방 운영)"""
r.set('4p', profile)
