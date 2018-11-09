from django.shortcuts import render
from django.http.response import HttpResponse
import pymysql
import ast

def db_connect():
    return pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='test_ocw',
                                 charset='utf8',
                                 # Selectの結果をdictionary形式で受け取る
                                 cursorclass=pymysql.cursors.DictCursor)

# column names in database
columns = [
        'LectureCode',
        'LectureName',
        'Department',
        'Professor',
        'DateRoom',
        'Quarter',
        ]

# テーブルヘッダ
result_head = {'series': '番台', 'lecname': '講義名', 'opening_department': '開講元', 'teacher': '教員名' , 'dateroom':'曜日・時間(講義室)' , 'quarter' : 'Q'}

# 教員名を整形する
def shape_teacher_list(teachers_str, n = 2): # n: 教員0,...,教員n-1 他
    l = teachers_str.split(', ', maxsplit=n + 1)
    if len(l) > n:
        return ', '.join(l[:n]) + ' ほか'
    return ', '.join(l)

# 曜日・講義室を整形する
def shape_dateroom(dateroom):
    return dateroom.replace('\xa0\xa0', '\xa0\xa0 ')


# Create your views here.
def test_response(request):
    return HttpResponse("OCW4IQ1")

def toppage(request):
    d = {'default_input_value' : '授業名'}
    return render(request,'topPage.html',d)

def search_and_result(request):
    # リクエストから取れる情報
    lecname = request.GET.get("lectureName")    # 講義名


    # リクエストに応じてDBから情報を取得
    # TODO

    #content = [('1Q', '講義名1', '教員名3','lecture'), ('2Q', '講義名2', '教員名2','lecture'), ('1Q', '講義名3', '教員名3','lecture')]
    content = []
    result_content = []

    #SQL kakeru baai
    with db_connect().cursor() as cursor:
        sql = "SELECT {} FROM lecture WHERE LectureName like %s".format(','.join(columns))
        cursor.execute(sql,("%{}%".format(lecname),))
        dbdata = cursor.fetchall()

        content = ((row["LectureName"],row["Department"],row["Professor"],row["LectureCode"],row["DateRoom"],row['Quarter']) for row in dbdata)

    result_content = list(
            {
                'lecname': item[0],
                'opening_department': item[1],
                'teacher': shape_teacher_list(item[2]),
                'code': item[3],
                'series': '%s00' % item[3][-3:-2:],
                'dateroom': shape_dateroom(item[4]),
                'quarter': item[5]
                } for item in content)
    series_list = sorted({row['series'] for row in result_content})
    opening_department_list = sorted({row['opening_department'] for row in result_content})

    d = {
        'result_head' : result_head,
        'result_content' : result_content,
        'series_list' : series_list,
        'opening_department_list' : opening_department_list,
        'lectureName' : lecname,
        }
    return render(request, 'searchAndResult.html', d)


def lecture(request):
    # クエリから得られる情報
    code = request.GET.get("code")    # 講義名


    with db_connect().cursor() as cursor:
        # 情報からのデータ構築
        sql = "SHOW COLUMNS FROM lecture"
        cursor.execute(sql)
        d = {col["Field"]:"" for col in cursor.fetchall()}

        sql = "SELECT * FROM lecture WHERE LectureCode like %s"
        cursor.execute(sql,(code,))
        dbdata = cursor.fetchall()
        if dbdata:
            d = dbdata[0]
            d["LecturePlan"] = [{"term":p[0],"plan":p[1],"task":p[2]} \
                for p in ast.literal_eval(d["LecturePlan"].replace("\'","\\\'")
                                                            .replace("\\\\'","\'")
                                                            .replace("\r","\\r")
                                                            .replace("\n","\\n"))]

    return render(request,'lecture.html',d)


def department_page(request):
    request_param = request.GET.get('dep')

    def param2name(param):
        if param == "rigakuin":
            return "理学院"
        elif param == "kougakuin":
            return "工学院"
        elif param == "bussitsu":
            return "物質理工学院"
        elif param == "jouhou":
            return "情報理工学院"
        elif param == "seimei":
            return "生命理工学院"
        elif param == "kankyo":
            return "環境・社会理工学院"
        elif param == "sonota":
            return "その他"
        return ""

    gakuin_name = param2name(request_param)

    with db_connect().cursor() as cursor:

        columns_str = ",".join('lecture.%s' % column for column in columns)
        if gakuin_name=="その他":
            sql = "SELECT {} \
                    FROM lecture JOIN LforG ON lecture.LectureCode = LforG.LectureCode WHERE LforG.Gakuin IN ('{}','{}')".format(columns_str, "教養科目群","類科目")
        else:
            sql = "SELECT {} \
                    FROM lecture JOIN LforG ON lecture.LectureCode = LforG.LectureCode WHERE LforG.Gakuin like '{}'".format(columns_str, gakuin_name)
        cursor.execute(sql)
        dbdata = cursor.fetchall()

        content = ((row["LectureName"],row["Department"],row["Professor"],row["LectureCode"],row["DateRoom"],row['Quarter']) for row in dbdata)

    result_content = list(
            {
                'lecname': item[0],
                'opening_department': item[1],
                'teacher': shape_teacher_list(item[2]),
                'code': item[3],
                'series': '%s00' % item[3][-3:-2:],
                'dateroom': shape_dateroom(item[4]),
                'quarter': item[5]
                } for item in content)
    series_list = sorted({row['series'] for row in result_content})
    opening_department_list = sorted({row['opening_department'] for row in result_content})

    d = {
        'result_head' : result_head,
        'result_content' : result_content,
        'series_list' : series_list,
        'opening_department_list' : opening_department_list,
        'gakuin_name' : gakuin_name,
        }
    return render(request,'department.html',d)

def manifest(request):
    return render(request, 'maniefst.json')

def base_layout(request):
    print('BASE LAYOUT')
    return render(request,'base.html')

def test(request):
    print("TEST")
    return render(request, 'test.html')
