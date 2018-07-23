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
    content = [('1Q', '講義名1', '教員名3'), ('2Q', '講義名2', '教員名2'), ('1Q', '講義名3', '教員名3')]
    result_content = []
    for item in content:
        result_content.append({'quarter': item[0], 'lecname': item[1], 'teacher': item[2]})

    d = {
        'result_head': result_head,
        'result_content': result_content,
        'lectureName' : lecname,
    }
    return render(request, 'searchAndResult.html', d)


def lecture(request):
	d = {
			'name' : '講義名1',
			'quarter' : '1Q',
			'teacher' : '教員A',
			'department' : '情報理工学院',
			}
	return render(request,'lecture.html',d)
