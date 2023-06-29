import pdfid
import yara

def detect_malicious_code(pdf_file):
    # Analyze the PDF structure using pdfid
    pdf_info = pdfid.PDFiD(open(pdf_file, 'rb'))
    pdf_info.parse()

    if pdf_info.js and pdf_info.js_objects:
        print("Potential malicious JavaScript code found.")

    # Define YARA rules to detect known malicious code signatures
    rules = """
    rule MaliciousCode {
        meta:
            description = "Detects potential malicious code in PDF files"
        strings:
            $eval = /[\s\(]+eval\s*\(/ nocase
            $base64_decode = /base64_decode\s*\(/ nocase
            $shellcode = { 33 C0 50 68 }
        condition:
            any of ($eval, $base64_decode) or $shellcode
    }
    """
   

    # Create a YARA compiler and load the rules
    compiler = yara.compile(source=rules)

    # Scan the PDF file using the YARA rules
    matches = compiler.match(pdf_file)

    if matches:
        print("Malicious code signatures found:")
        for match in matches:
            print(f" - Rule: {match.rule}, Offset: {match.offset}")

    if not pdf_info.js and not matches:
        print("No malicious code detected.")