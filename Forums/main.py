########################################
# Main
########################################

import models

name1 = 'Ahmed'
age1  = 32
name2 = 'Mohammed'
age2  = '22'

title1 = 'title 1'
content1 = 'content 1'

title2 = 'title 2'
content2 = 'content 2'

title3 = 'title 3'
content3 = 'content3'

member1 = models.member(name1,age1)
member2 = models.member(name2,age2)

post1 = models.post(title1,content1)
post2 = models.post(title2,content2)
post3 = models.post(title3,content3)

print(member1.name)
print(member2.age)
