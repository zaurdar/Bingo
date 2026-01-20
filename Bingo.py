import streamlit as st
import random
import cv2

event_types = ["mich fait pipi \ndans un endroit \ninapte a recevoir \ndu pipi",
               "flash fait pipi \ndans un endroit \ninapte a recevoir \ndu pipi",
               "leopold mets \npatate",
               "leopold emballe \nune mono de ski",
               "vincent apprend \na sam a jouer a lol",
               "Arnaud obtient \nla palme de l'autisme \nplanetaire suite a \nun vote du peuple",
               "Tout le monde \ndans l'appart \na part  vincent \nest tout nu",
               "Arnaud raconte \nsa blague et \npersonne s'en \nsouviens",
               "Arnaud raconte \nsa blague et \nelle est pas \ndrole au final",
               "Arnaud et Mich \ndorment en cuillere",
               "Mus2 et Mich \ndorment en cuillere",
               "Arnaud et Mus2 \ndorment en cuillere",
               "vincent choppe \nau ski",
               "Baptiste choppe \nmich",
               "sam trouve une \njolie rousse",
               "mich touche un \nzob qui n'est \npas le sien",
               "Arnaud choppe \nlea robinet (encore)",
               "Arnaud se fait \nprendre palate \npar des fucam \n(encore)",
               "flash choppe \nquelqu'un",
               "flash choppe \nvincent",
               "flash se leve \na 8h pour aller skier",
               "plus de deux \nhommes dorment en \nmeme temps sur \nles enormes pecs \nde samuel",
               "leopold a \nde la neige sur \nson zob",
               "Mus2 se fait \nappeler par \njeff en panique",
               "quelqu'un compare \nle zob de mus2 a un \nobjet contendant",
               "mich perd/casse \nses lunettes",
               "Mus2 prend une \ndouche avec au \nmoins une autre \npersonne",
               "la chambre adopte \nun neo et le \nmurge",
               "Arnaud parle \nde Gazelle",
               "leopold raconte \ncomment il a casse \nun micro onde \nau Bar CP",
               "Sam redrague une \nlouna (encore)",
               "baptiste et leo \nfont un bras \nde zob"
               ]
def put_multiline_text(img, text, org, font, font_scale, color, thickness=1, line_type=cv2.LINE_AA, line_spacing=1.2):
    x, y = org
    for line in text.split("\n"):
        cv2.putText(img, line, (x, y), font, font_scale, color, thickness, line_type)
        (w, h), baseline = cv2.getTextSize(line, font, font_scale, thickness)
        y += int((h + baseline) * line_spacing)
st.set_page_config(
    page_title="Bingo",
    page_icon="<UNK>",
)

st.title("Bingo")
img = cv2.imread("Bingo.png")
if st.button("generate"):
    events = random.sample(event_types, k=16)
    event_list = [events[i:i+4] for i in range(0, len(events), 4)]
    for i in range(4):
        for j in range(4):
            put_multiline_text(img,event_list[i][j],(100+i*320,430+j*380),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2)
    st.image(img)



ok, buffer = cv2.imencode(".png", img)   # ou ".jpg"
if ok:
    st.download_button(
        label="📥 Télécharger l'image",
        data=buffer.tobytes(),
        file_name="bingo.png",
        mime="image/png"
    )
else:
    st.error("Impossible d'encoder l'image.")