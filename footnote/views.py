from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Idea, Medley
from .forms import FootNoteForm

class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by("-created_on")
    template_name  = 'index.html'
    paginate_by = 2

#class MedleyList(generic.ListView):
#    model = Idea
#    queryset = Idea.objects.filter(status=1).order_by("-created_on")
#    template_name  = 'medley_detail.html'
#    paginate_by = 2

class IdeaDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, slug=slug)
        footnotes = idea.footnotes.filter(approved=True).order_by('created_on')
        liked = False
        if idea.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "idea_detail.html",
            {
                "idea": idea,
                "footnotes": footnotes,
                "footnoted":False,
                "liked": liked,
                "footnote_form": FootNoteForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
            queryset = Idea.objects.filter(status=1)
            idea = get_object_or_404(queryset, slug=slug)
            footnotes = idea.footnotes.filter(approved=True).order_by('created_on')
            liked = False
            if idea.likes.filter(id=self.request.user.id).exists():
                liked = True

            footnote_form = FootNoteForm(data=request.POST)

            if footnote_form.is_valid():
                footnote_form.instance.email = request.user.email 
                footnote_form.instance.name = request.user.username
                footnote = footnote_form.save(commit=False)
                footnote.idea = idea
                footnote.save()
            else:
                footnote_form = FootNoteForm()

            return render(
                request,
                "idea_detail.html",
                {
                    "idea": idea,
                    "footnotes": footnotes,
                    "footnoted":True,
                    "liked": liked,
                    "footnote_form": FootNoteForm()
                },
            )

class MedleyDetail(View):

    def get(self, request, *args, **kwargs):
#                queryset = Idea.objects.filter(status=1)
            medley = get_object_or_404(queryset)
#            footnotes = idea.footnotes.filter(approved=True).order_by('created_on')
#                liked = False
#                if idea.likes.filter(id=self.request.user.id).exists():
#                    liked = True

#           return render_template("medley_detail.html", medley=medley)
            return render(
            request,
            "medley_detail.html",
            {
            },
        )        

        
class IdeaLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Idea, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))
            

class FootnoteLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Footnote, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))
                        

#
    