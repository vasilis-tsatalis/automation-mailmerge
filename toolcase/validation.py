def allowed_file(ALLOWED_EXTENSIONS, filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
