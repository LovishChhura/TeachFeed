from django.shortcuts import render, HttpResponse, redirect
from .models import Department, Teacher, Subject, Feed
# Create your views here.
def feed(request):
    dep=Department.objects.all().order_by('department')
    teach=Teacher.objects.all().order_by('name')
    sub=Subject.objects.all().order_by('name')
    params={'dep':dep, 'teach': teach, 'sub': sub}
    #print(params)
    if request.method=="POST":
        branch = request.POST.get('branch')
        depTeach = request.POST.get('depTeach')
        teacherName = request.POST.get('teacherName')
        sem = request.POST.get('sem')
        subject = request.POST.get('subject')
        interact = request.POST.get('interact')
        softSkill = request.POST.get('softSkill')
        notes = request.POST.get('notes')
        ans = request.POST.get('ans')
        pInteract = request.POST.get('pInteract')
        quality = request.POST.get('quality')
        extra = request.POST.get('extra')
        assignment = request.POST.get('assignment')
        interrupt = request.POST.get('interrupt')
        mst = request.POST.get('mst')
        lecture = request.POST.get('lecture')
        mooc = request.POST.get('mooc')
        virtualLab = request.POST.get('virtualLab')
        curriculum = request.POST.get('curriculum')
        topic = request.POST.get('topic')
        bless = request.POST.get('bless')
        cooperative = request.POST.get('cooperative')
        helpful = request.POST.get('topic')
        feed=Feed(branch=branch, depTeach=depTeach, teacherName=teacherName,  sem=sem,subject=subject, interact=interact, softSkill=softSkill,notes=notes, ans=ans, pInteract=pInteract, quality=quality, extra=extra, assignment=assignment, interrupt=interrupt, mst=mst, lecture=lecture, mooc=mooc, virtualLab=virtualLab, curriculum=curriculum, topic=topic, bless=bless, cooperative=cooperative, helpful=helpful)

        feed.save()
        return redirect("thanks")

    return render(request,"feed/feed.html",params)

def thanks(request):
    return render(request,"feed/thanks.html")