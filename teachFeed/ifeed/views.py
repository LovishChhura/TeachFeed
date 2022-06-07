from django.shortcuts import render, HttpResponse, redirect
from .models import Taccess
from django.contrib import messages
from feed.models import Department, Teacher, Subject, Feed
from statistics import mean


# Create your views here.
def ifeed(request):
    return render(request, 'ifeed/ifeedHome.html')


def tlogin(request):
    if request.method == "POST":
        acscode = request.POST['acscode']
        access = Taccess.objects.all()
        for i in access:
            if acscode == i.accesscd:
                stDepartment = {'stDepartment': acscode}
                return redirect('feedPanel')
            if acscode != i.accesscd:
                messages.error(request, "Invalid Credentials")

    return redirect('ifeed')


def feedPanel(request):
    dep = Department.objects.all()
    teach = Teacher.objects.all()
    sub = Subject.objects.all()
    params = {'dep': dep, 'teach': teach, 'sub': sub}
    # print(params)

    if request.method == "POST":
        teacherName3 = request.POST.get('teacherName')
        branch3 = request.POST.get('branch')
        subject3 = request.POST.get('subject')
        sem3 = request.POST.get('sem')

        queryset = Feed.objects.filter(teacherName=teacherName3, branch=branch3, subject=subject3, sem=sem3)
        # print(queryset)
        n = len(queryset)
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
            if 0 < int(e.interact) < 11:
                interact1 = interact1 + int(e.interact)
            if 0 < int(e.softSkill) < 11:
                softSkill1 = softSkill1 + int(e.softSkill)
            if 0 < int(e.notes) < 11:
                notes1 = notes1 + int(e.notes)
            if 0 < int(e.ans) < 11:
                ans1 = ans1 + int(e.ans)
            if 0 < int(e.pInteract) < 11:
                pInteract1 = pInteract1 + int(e.pInteract)
            if 0 < int(e.quality) < 11:
                quality1 = quality1 + int(e.quality)
            if 0 < int(e.extra) < 11:
                extra1 = extra1 + int(e.extra)
            if 0 < int(e.assignment) < 11:
                assignment1 = assignment1 + int(e.assignment)
            if 0 < int(e.interrupt) < 11:
                interrupt1 = interrupt1 + int(e.interrupt)
            if 0 < int(e.mst) < 11:
                mst1 = mst1 + int(e.mst)
            if 0 < int(e.lecture) < 11:
                lecture1 = lecture1 + int(e.lecture)
            if 0 < int(e.mooc) < 11:
                mooc1 = mooc1 + int(e.mooc)
            if 0 < int(e.virtualLab) < 11:
                virtualLab1 = virtualLab1 + int(e.virtualLab)
            if 0 < int(e.curriculum) < 11:
                curriculum1 = curriculum1 + int(e.curriculum)
            if 0 < int(e.topic) < 11:
                topic1 = topic1 + int(e.topic)

            bless1 = bless1 + int(e.bless)
            cooperative1 = cooperative1 + int(e.cooperative)
            helpful1 = helpful1 + int(e.helpful)

        interact2 = round(interact1 / n, 2)
        softSkill2 = round(softSkill1 / n, 2)
        notes2 = round(notes1 / n, 2)
        ans2 = round(ans1 / n, 2)
        pInteract2 = round(pInteract1 / n, 2)
        quality2 = round(quality1 / n, 2)
        extra2 = round(extra1 / n, 2)
        assignment2 = round(assignment1 / n, 2)
        interrupt2 = round(interrupt1 / n, 2)
        mst2 = round(mst1 / n, 2)
        lecture2 = round(lecture1 / n, 2)
        mooc2 = round(mooc1 / n, 2)
        virtualLab2 = round(virtualLab1 / n, 2)
        curriculum2 = round(curriculum1 / n, 2)
        topic2 = round(topic1 / n, 2)
        bless2 = bless1
        cooperative2 = cooperative1
        helpful2 = helpful1

        overall2=interact2+softSkill2+notes2+ans2+pInteract2+quality2+extra2+assignment2+interrupt2+mst2+lecture2+mooc2+virtualLab2+curriculum2+topic2
        overallPerformance = round(overall2/15, 2)

        params1 = {'branch': branch3, 'teacherName': teacherName3, 'subject': subject3, 'sem': sem3,
                   'interact': interact2, 'softSkill': softSkill2, 'notes': notes2, 'ans': ans2,
                   'pInteract': pInteract2, 'quality': quality2, 'extra': extra2, 'assignment': assignment2,
                   'interrupt': interrupt2, 'mst': mst2, 'lecture': lecture2, 'mooc': mooc2, 'virtualLab': virtualLab2,
                   'curriculum': curriculum2, 'topic': topic2, 'n': n, 'bless': bless2, 'cooperative': cooperative2,
                   'helpful': helpful2,'overallPerformance':overallPerformance}

        return render(request, 'ifeed/ifeed.html', params1)
    return render(request, 'ifeed/feedPanel.html', params)


def tlogout(request):
    return redirect('ifeed')
