def message(domain, uidb64, token, url_name):
    """Active를 담당하는 Endpoint URL 주소를 메시지로 Send"""
    return f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n" \
           f"회원가입 링크 : http://{domain}/{url_name}/activate/{uidb64}/{token}\n\n" \
           f"감사합니다."
