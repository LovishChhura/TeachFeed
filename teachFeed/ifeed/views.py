from django.shortcuts import render, HttpResponse, redirect
from .models import Taccess
from django.contrib import messages
from feed.models import Department, Teacher, Subject, Feed
from statistics import mean
# Create your views here.
def ifeed(request):
    return render(request,'ifeed/ifeedHome.html')

def tlogin(request):
    if request.method == "POST":
        acscode = request.POST['acscode']
        access= Taccess.objects.all()
        for i in access:
            if acscode==i.accesscd:
                stDepartment={'stDepartment':acscode}
                return redirect('feedPanel')
            if acscode!=i.accesscd:
                messages.error(request, "Invalid Credentials")


    return redirect('ifeed')

def feedPanel(request):
    dep = Department.objects.all()
    teach = Teacher.objects.all()
    sub = Subject.objects.all()
    params = {'dep': dep, 'teach': teach, 'sub': sub}
    #print(params)

    if request.method=="POST":
        teacherName3 = request.POST.get('teacherName')
        depTeach3 = request.POST.get('depTeach')
        subject3 = request.POST.get('subject')
        sem3 = request.POST.get('sem')

        queryset=Feed.objects.filter(teacherName=teacherName3,depTeach=depTeach3,subject=subject3,sem=sem3)
        #print(queryset)
        n=len(queryset)
        interact1 = 0
        softSkill1 = 0
        notes1 = 0
        ans1 = 0
        pInteract1 = 0
        quality1 = 0
        extra1 = 0
        assignment1 = 0
        interrupt1 = 0
        mst1 = 0
        lecture1 = 0
        mooc1 = 0
        virtualLab1 = 0
        curriculum1 = 0
        topic1 = 0
        bless1 = 0
        cooperative1 = 0
        helpful1 = 0
        for e in queryset:
            interact1 = interact1+int(e.interact)
            softSkill1 = softSkill1+int(e.softSkill)
            notes1 = notes1+int(e.notes)
            ans1 = ans1+int(e.pInteract)
            pInteract1 = pInteract1+int(e.pInteract)
            quality1 = quality1+int(e.quality)
            extra1 = extra1+int(e.extra)
            assignment1 = assignment1+int(e.assignment)
            interrupt1 = interrupt1+int(e.interrupt)
            mst1 = mst1+int(e.mst)
            lecture1 = lecture1 + int(e.lecture)
            mooc1 = mooc1+int(e.mooc)
            virtualLab1 = virtualLab1+int(e.virtualLab)
            curriculum1 = curriculum1+int(e.curriculum)
            topic1 = topic1+int(e.topic)
            bless1=bless1+int(e.bless)
            cooperative1=cooperative1+int(e.cooperative)
            helpful1=helpful1+int(e.helpful)


        interact2 = round (interact1 / n, 2)
        softSkill2 =round(softSkill1/n,2)
        notes2=round(notes1/n,2)
        ans2=round(ans1/n,2)
        pInteract2=round(pInteract1/n,2)
        quality2=round(quality1/n,2)
        extra2=round(extra1/n,2)
        assignment2=round(assignment1/n,2)
        interrupt2=round(interrupt1/n,2)
        mst2=round(mst1/n,2)
        lecture2=round(lecture1/n,2)
        mooc2=round(mooc1/n,2)
        virtualLab2=round(virtualLab1/n,2)
        curriculum2=round(curriculum1/n,2)
        topic2=round(topic1/n,2)
        bless2=bless1
        cooperative2=cooperative1
        helpful2=helpful1

        params1 = {'depTeach': depTeach3, 'teacherName': teacherName3, 'subject': subject3, 'sem': sem3, 'interact': interact2, 'softSkill': softSkill2, 'notes': notes2, 'ans': ans2, 'pInteract': pInteract2, 'quality': quality2, 'extra': extra2, 'assignment': assignment2, 'interrupt': interrupt2, 'mst':mst2, 'lecture':lecture2, 'mooc': mooc2, 'virtualLab': virtualLab2, 'curriculum': curriculum2, 'topic': topic2, 'n':n, 'bless':bless2, 'cooperative':cooperative2, 'helpful':helpful2}

        return render(request,'ifeed/ifeed.html',params1)
    return render(request,'ifeed/feedPanel.html',params)

def tlogout(request):
    return redirect('ifeed')