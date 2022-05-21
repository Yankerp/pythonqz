cj = int(input("请您输入您的成绩："))

if cj >= 90:
    print("您是一个非常优秀的学员")
elif cj >= 80:
    print("您在努力一下就突破90了，继续努力哦")
elif cj >= 70:
    print("你还需要继续努力，才可以成为你想要成为的人，成绩有些差哦")
elif cj >= 60:
    print("你刚刚突破及格，还需要继续努力")
else:
    print("你是最差的学生，再见！！！")


shengao = float(input("请您输入您的身高：").strip())
xueli = input("请您输入您的学历['大学'｜'高中'｜'初中'|'小学']：").strip()
tizhong = float(input("请您输入您的体重「单位g」：").strip())

if shengao >= 1.65 and xueli == "大学" and tizhong <= 130:
    print("你是一个非常美丽的人")
elif shengao >= 1.65 or xueli == "大学" or tizhong <= 110:
    if shengao >= 1.65 and xueli == "大学":
        print("您的身高和学历都很完美哦")
    elif shengao >= 1.65 and tizhong <= 110:
        print("你的身材简直太完美了。")
    else:
        print("你还要继续努力保持三项完美哦！！！")
    print("您的身高为：{sg}, 学历为：{xl}, 体重为：{tz},继续加油！".format(sg=shengao, xl=xueli, tz=tizhong))
else:
    print("不合格，滚蛋")
