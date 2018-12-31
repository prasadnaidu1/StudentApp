def handle_uploaded_file(f):
    with open("app/static/upload/"+f.name,'wb+') as des:
        for x in f:
            des.write(x)