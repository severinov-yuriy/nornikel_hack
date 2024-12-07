from src.text import process_pdf, process_doc


def test_process_pdf():
    res = process_pdf("./server/example_docs_for_test/1.pdf")
    assert "ПЕРСПЕКТИВЫ УГОЛЬНОЙ ПРОМЫШЛЕННОСТИ РОССИИ" in res["text"]


def test_process_doc():
    res = process_doc("./server/example_docs_for_test/2.docx")
    assert "разъяснения о порядке применения Положения" in res["text"]
