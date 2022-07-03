from polls.models import Choice, Question

Question.objects.all()

from django.utils import timezone
q = Question(question_text = 'who is nolan',pub_date = timezone.now())

current_year = timezone.now().year
question.objects.get(pub_date__year=current_year)
 