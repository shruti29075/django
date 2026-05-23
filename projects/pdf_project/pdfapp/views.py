from django.shortcuts import render, redirect
from .models import Document
from urllib.parse import urlencode


def pdf_search(request):

    # If POST: handle optional upload, then redirect to GET with keyword
    if request.method == "POST":
        pdf_file = request.FILES.get("document")
        keyword = request.POST.get("keyword") or ""
        selected_id = request.POST.get("doc_id") or ""

        new_doc_id = None
        if pdf_file:
            doc = Document.objects.create(file=pdf_file)
            new_doc_id = str(doc.id)

        # If user selected an existing document and didn't upload a new one,
        # prefer that id; otherwise, use newly created id if present.
        doc_id = new_doc_id or selected_id

        # Redirect to GET with keyword and optional doc_id so the page is
        # bookmarkable and rendering runs from a clean URL.
        params = {"keyword": keyword}
        if doc_id:
            params["doc_id"] = doc_id
        qs = urlencode(params)
        return redirect(f"/?{qs}")

    # For GET: read keyword from querystring and find the latest PDF to display
    pdf_url = None
    keyword = request.GET.get("keyword")
    doc_id = request.GET.get("doc_id")

    # Choose document by id if provided, otherwise the latest
    if doc_id:
        try:
            doc = Document.objects.get(id=doc_id)
            pdf_url = doc.file.url
        except Document.DoesNotExist:
            pdf_url = None
    elif keyword:
        last = Document.objects.order_by("-uploaded_at").first()
        if last:
            pdf_url = last.file.url

    # Provide list of uploaded documents for the chooser
    documents = Document.objects.order_by("-uploaded_at")[:20]

    return render(
        request,
        "pdfapp/pdf_search.html",
        {"pdf_url": pdf_url, "keyword": keyword, "documents": documents, "selected_id": doc_id},
    )
