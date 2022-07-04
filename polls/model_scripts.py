from polls.models import Choice, Question

Question.objects.all()

from django.utils import timezone
q = Question(question_text = 'who is nolan',pub_date = timezone.now())

current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
 
q = Question.objects.get(pk=4)

q.choice_set.create(choice_text = 'superman',votes = 0)
q.choice_set.create(choice_text = 'batman',votes = 0)
q.choice_set.create(choice_text = 'antman',votes = 0)

q.choice_set.all()
q.choice_set.count()