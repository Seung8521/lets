from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import Feed
#현재폴더의 models 라는 파일에서 Feed라는 이름의 class를 가져오세요.

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        feeds = Feed.objects.all()

        return render(request, self.template_name,
                      {'feed_list' : feeds})
    
class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        #content 정보를 전달받는다
        param = request.POST.get('content', '')
        param2 = request.FILES.get('up_photo', False)
        #화면에서 확인 하기위해 출력
        print(f"param:{param}")
        feed = Feed(content = param, photo = param2)
        feed.save()
        #받는게 완료되면 /edu/tag 로 이동
        return redirect('edu:tag_study')
        