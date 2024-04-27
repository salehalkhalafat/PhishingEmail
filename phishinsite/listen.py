import email_listener
from data.models import EMAILS
from .PhishingEmailDetection import PhishingEmailClassifier


def massagelisten():
    email = "ramaalzain44@gmail.com"
    app_password = "yeld avgm nnwv wxay"
    folder = "Inbox"
    attachment_dir = "static\\attachments"
    el = email_listener.EmailListener(email, app_password, folder, attachment_dir)
    el.login()
    messages = el.scrape()

    if len(messages) > 0:
        sender = list(messages.keys())[0]
        subject = messages[sender]['Subject']
        planText = messages[sender]['Plain_Text']
        planHTML = messages[sender]['Plain_HTML']
        html = messages[sender]['HTML']

        classifier = PhishingEmailClassifier()
        truncated_text = classifier.truncate_text(planText)
        result = classifier.predict_phishing(truncated_text)

        new_record = EMAILS(
            email=sender, subject=subject,
            body=planHTML,
            isfishing=True if result["label"] == 'PHISHING EMAIL' else False
        )
        new_record.save()

        return {"sender": sender,
                "Subject": subject,
                "Plain_Text": planText,
                "Plain_HTML": planHTML,
                "HTML": html}
    else:
        return {}


print(massagelisten())
