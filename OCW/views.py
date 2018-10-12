from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def test_response(request):
    return HttpResponse("OCW4IQ1")

def toppage(request):
    d = {'default_input_value' : '授業名'}
    return render(request,'topPage.html',d)

def search_and_result(request):
    # テーブルヘッダ
    result_head = {'quarter': 'クォーター', 'lecname': '講義名', 'teacher': '教員名'}

    # リクエストから取れる情報
    lecname = request.GET.get("lectureName")    # 講義名


    # リクエストに応じてDBから情報を取得
    # TODO 
    content = [('1Q', '講義名1', '教員名3','lecture'), ('2Q', '講義名2', '教員名2','lecture'), ('1Q', '講義名3', '教員名3','lecture')]
    result_content = []
    for item in content:
        result_content.append({'quarter': item[0], 'lecname': item[1], 'teacher': item[2] })

    d = {
        'result_head': result_head,
        'result_content': result_content,
        'lectureName' : lecname,
    }
    return render(request, 'searchAndResult.html', d)


def lecture(request):
    # クエリから得られる情報
    #lecname = request.GET.get("lecname")    # 講義名

    # 情報からのデータ構築
    d = {
            'name' : "文系エッセンス1 : 人間力を育む Essence of Humanities and Social",
            'quarter' : '2Q',
            'teacher' : '中野 民夫',
            'department' : '文系教養科目',
            }
    return render(request,'lecture.html',d)


def department_page(request):
    print(request)
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

    department_name = param2name(request_param)

    d = {
        'department_name' : department_name,
        }
    print(d)
    return render(request,'department.html',d)
