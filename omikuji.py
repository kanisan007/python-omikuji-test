
import random

kaitou = input('おみくじをしますか？するなら[y]、しないなら[n]を入力してください。')

if kaitou=='y':
    print('それではおみくじをを引きます。')
    print('・・・抽選中・・・')
    kekka = random.randint(1,5)

    if kekka==1:
        print('結果は大吉です！おめでとうございます！')
    elif kekka==2:
        print('結果は小吉です！ちょっとした幸せがあるかも？')
    elif kekka==3:
        print('結果は吉です！いつも通りの一年になりそうかも！')
    elif kekka==4:
        print('結果は凶です！今年はちょっと微妙かも！')
    else: 
        print('結果は大凶です！ドンマイ！')
    
elif kaitou=='n':
    print('わかりました。')
else:
    print('入力が違います。[y]か[n]で回答してください')


