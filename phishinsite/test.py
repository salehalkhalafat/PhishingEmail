from PhishingEmailDetection import PhishingEmailClassifier
email ={
        "sender": "Stella Lowry <rookcuduq@yahoo.com>",
        "receiver": "Brian <bernice@groucho.cs.psu.edu>",
        "date": "Sat, 03 Apr 1993 10:34:36 -0500",
        "subject": "re[12]:",
        "body": "           \n                                            \n LUXURY  WATCHES - BUY YOUR OWN ROLEX  FOR ONLY  $219!                                                        \n                                               \n  Rolex :: Cartier ::  Bvlgari  ::  Frank Muller  ::  Patek  Philippe :: Vacheron Constantin                   \n   A.  Lange  & Sohne  ::  Audemars  Piguet  :: Jaeger-Lecoultre  ::  IWC  :: Officine  Panerai                                                    \n Breitling ::  Omega ::  Tag  Heuer                                   \n                       \n   Exapmle:                 \n ROLEX  Full 18K Gold  Daytona  for MEN -  only  $269!                                      \n                                                 \n    - Fast delivery                       \n     -  The lowest prices  in the world                                                 \n -  Worldwide shipping                                                                      \n                                                            \n Visit  our shop at:                                                                   \n                        \nhttp://vvhvjk130.sewandeatone.com\n                                                                       \n                                              \n                                                   \n                                   \n                    \n",
        "label": "1",
        "urls": "1"
    }
text = email['body']
classifier = PhishingEmailClassifier()
truncated_text = classifier.truncate_text(text)
result = classifier.predict_phishing(truncated_text)
print(result)