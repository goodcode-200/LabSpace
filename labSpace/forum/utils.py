from .models import Title

def get_pre_obj(pk):
    earliest = Title.objects.earliest("id").id
    while(True):
        pk = pk-1
        if(pk < earliest):
            return False
        try:
            title = Title.objects.get(pk = pk)
            return title
        except:
            continue

def get_next_obj(pk):
    latest = Title.objects.latest("id").id
    while (True):
        pk = pk + 1
        if (pk > latest):
            return False
        try:
            title = Title.objects.get(pk=pk)
            return title
        except:
            continue