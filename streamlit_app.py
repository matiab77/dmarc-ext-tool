import re
import streamlit as st

def extract_external_domains(domain, dmarc_record):
    tags = dict(re.findall(r'([\w]+)=([^;]+)', dmarc_record))
    rua = tags.get('rua', '')
    ruf = tags.get('ruf', '')

    external_domains = set()

    for tag_value in [rua, ruf]:
        emails = tag_value.split(',')
        for email_uri in emails:
            if email_uri.startswith('mailto:'):
                email = email_uri[len('mailto:'):]
                if '@' in email:
                    _, email_domain = email.split('@', 1)
                    email_domain = email_domain.strip().lower()
                    if 'dmarcian.com' in email_domain:
                        continue
                    if email_domain != domain:
                        external_domains.add(email_domain)
    return external_domains

def generate_verification_record(requesting_domain, external_domain):
    name = f"{requesting_domain}._report._dmarc.{external_domain}"
    value = "\"v=DMARC1;\""
    return name, value

st.title("DMARC External Reporting DNS Generator")

domain = st.text_input("Your Domain (e.g., mydomain.net)")
dmarc_record = st.text_area("DMARC Record")

if st.button("Generate DNS Records for external validation") and domain and dmarc_record:
    ext_domains = extract_external_domains(domain.lower(), dmarc_record.strip())
    if not ext_domains:
        st.success("✅ No external domains found (excluding dmarcian). No DNS records needed.")
    else:
        st.subheader("📌 DNS Records to Publish:")
        for ext_domain in ext_domains:
            name, value = generate_verification_record(domain, ext_domain)
            st.markdown(f"**Domain:** {ext_domain}")
            st.code(f"Name: {name}\nType: TXT\nValue: {value}")
