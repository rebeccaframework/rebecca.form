#from webhelpers import pagenate

#pagenate = pagenate

def text_(model):
    if hasattr(model, '__unicode__'):
        return model.__unicode__()
    return unicode(str(model))
