def base (request):
    
    CANONICAL_PATH=request.build_absolute_uri(request.path),
    
    return  {'CANONICAL_PATH':CANONICAL_PATH}