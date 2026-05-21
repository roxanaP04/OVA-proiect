import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PetFlow România",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --mov-deep:    #4A1A6E;
    --mov-mid:     #7B3FA0;
    --mov-light:   #B27CC8;
    --lavanda:     #E8D5F5;
    --lavanda2:    #F3EAFB;
    --alb:         #FFFFFF;
    --gri:         #F7F3FA;
    --text-dark:   #1E0A2E;
    --text-mid:    #4A3060;
    --auriu:       #C9A84C;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--text-dark);
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--mov-deep) 0%, var(--mov-mid) 100%);
}
section[data-testid="stSidebar"] * {
    color: var(--alb) !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 1rem;
    padding: 6px 0;
    cursor: pointer;
}

/* Hero banner */
.hero {
    background: linear-gradient(135deg, var(--mov-deep) 0%, var(--mov-mid) 60%, var(--mov-light) 100%);
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "🐾";
    font-size: 180px;
    position: absolute;
    right: -20px;
    top: -20px;
    opacity: 0.08;
}
.hero h1 { font-size: 3.2rem; margin: 0; color: white; }
.hero p  { font-size: 1.25rem; opacity: 0.9; margin: 12px 0 0; }

/* Cards */
.card {
    background: var(--alb);
    border-radius: 16px;
    padding: 28px 24px;
    box-shadow: 0 4px 24px rgba(74,26,110,0.10);
    border-left: 5px solid var(--mov-mid);
    margin-bottom: 20px;
    transition: transform .2s;
}
.card:hover { transform: translateY(-3px); }
.card h3 { color: var(--mov-deep); margin-top: 0; }

/* Section title */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--mov-deep);
    border-bottom: 3px solid var(--mov-light);
    padding-bottom: 8px;
    margin-bottom: 24px;
}

/* Social buttons */
.social-btn {
    display: inline-block;
    padding: 10px 24px;
    border-radius: 50px;
    color: white !important;
    text-decoration: none;
    font-weight: 600;
    margin: 6px;
    font-size: 0.95rem;
}
.fb  { background: #1877F2; }
.ig  { background: linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); }

/* Blog card */
.blog-card {
    background: var(--lavanda2);
    border-radius: 14px;
    padding: 22px 20px;
    margin-bottom: 18px;
    border: 1px solid var(--lavanda);
}
.blog-card h4 { color: var(--mov-deep); margin-top: 0; }

/* Arbore */
.tree-node {
    background: var(--lavanda2);
    border-left: 4px solid var(--mov-mid);
    padding: 10px 16px;
    border-radius: 0 10px 10px 0;
    margin: 6px 0 6px 20px;
    font-size: 0.95rem;
}
.tree-root {
    background: var(--mov-deep);
    color: white;
    padding: 12px 20px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1.05rem;
    margin-bottom: 6px;
}

/* Price badge */
.price { 
    background: var(--mov-mid); 
    color: white; 
    padding: 4px 14px; 
    border-radius: 20px; 
    font-weight: 600;
    font-size: 0.9rem;
}

/* Footer */
.footer {
    background: var(--mov-deep);
    color: white;
    border-radius: 16px;
    padding: 30px 24px;
    text-align: center;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🐾 PetFlow")
    st.markdown("---")
    pagina = st.radio(
        "Navigare",
        [
            "🏠 Acasă",
            "ℹ️ Despre Noi",
            "🛎️ Servicii",
            "🖼️ Galerie",
            "📝 Blog",
            "📅 Programare Online",
            "⭐ Satisfacție Clienți",
            "💬 Feedback",
            "📞 Contact",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("**Urmărește-ne:**")
    st.markdown("""
    <a href="https://facebook.com/petflow.ro" target="_blank" class="social-btn fb">📘 Facebook</a><br><br>
    <a href="https://instagram.com/petflow.ro" target="_blank" class="social-btn ig">📸 Instagram</a>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: ACASĂ
# ══════════════════════════════════════════════════════════════════════════════
if pagina == "🏠 Acasă":
    st.markdown("""
    <div class="hero">
        <h1>🐾 PetFlow România</h1>
        <p>Îngrijire profesională pentru companionii tăi blănoși — cu dragoste, răbdare și dedicare</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, emoji, title, desc in [
        (c1, "🐕", "Plimbare Câini", "Plimbări zilnice în siguranță"),
        (c2, "✂️", "Toaletare", "Aspect îngrijit garantat"),
        (c3, "🏠", "Supraveghere", "Îngrijire la domiciliu"),
        (c4, "🏥", "Veterinar", "Programări rapide"),
    ]:
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center">
                <div style="font-size:2.5rem">{emoji}</div>
                <h3>{title}</h3>
                <p style="color:#4A3060;font-size:0.9rem">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('<div class="section-title">🎬 Videoclip de prezentare</div>', unsafe_allow_html=True)
    st.components.v1.iframe(
        "https://www.youtube.com/embed/loNTb5KPXek",
        height=500,
    )

    st.markdown("---")
    st.markdown('<div class="section-title">🎵 Audio — Mesaj de bun venit</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style='background:var(--lavanda2);border-radius:14px;padding:20px 24px;color:var(--text-mid)'>
        <p style='font-size:1rem;margin:0 0 12px 0'>🎵 <strong>Muzică ambient relaxantă</strong> — fundal sonor PetFlow</p>
        <audio controls style='width:100%'>
            <source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3" type="audio/mpeg">
        </audio>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">📣 Urmărește-ne pe social media</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;padding:20px">
        <a href="https://facebook.com/petflow.ro" target="_blank" class="social-btn fb">📘 Facebook — PetFlow România</a>
        <a href="https://instagram.com/petflow.ro" target="_blank" class="social-btn ig">📸 Instagram — @petcare.ro</a>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: DESPRE NOI
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "ℹ️ Despre Noi":
    st.markdown('<div class="section-title">ℹ️ Despre PetFlow</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>🌟 Povestea noastră</h3>
        <p>PetFlow a luat naștere din dragostea profundă față de animale și dorința de a oferi îngrijire de calitate 
        pentru companionii blănoși ai familiilor din România. Am observat că mulți proprietari de animale se confruntă 
        cu dificultăți în a găsi servicii de încredere atunci când sunt ocupați sau plecați. 
        Misiunea noastră este simplă: să tratăm fiecare animal ca și cum ar fi al nostru, cu grijă, răbdare și profesionalism.</p>
    </div>
    <div class="card">
        <h3>🎯 Misiunea noastră</h3>
        <p>Să oferim servicii de îngrijire animate de companie la cele mai înalte standarde de calitate, 
        asigurând confortul și siguranța fiecărui animal încredințat nouă, cu respect față de proprietari și față de natură.</p>
    </div>
    <div class="card">
        <h3>💜 Valorile noastre</h3>
        <ul>
            <li><strong>Dragoste</strong> — Tratăm fiecare animal cu afecțiune și grijă</li>
            <li><strong>Profesionalism</strong> — Servicii de înaltă calitate, personal calificat</li>
            <li><strong>Încredere</strong> — Transparență totală față de proprietari</li>
            <li><strong>Responsabilitate</strong> — Siguranța animalului pe primul loc</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">👥 Echipa noastră</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for col, name, role, emoji in [
        (c1, "Ana Popescu", "Fondator & Manager", "👩‍💼"),
        (c2, "Mihai Ionescu", "Specialist Toaletare", "✂️"),
        (c3, "Elena Radu", "Îngrijitor Animale", "🐾"),
        (c4, "Petrescu Roxana", "Specialist Relații Clienți", "🌟"),
    ]:
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center">
                <div style="font-size:3rem">{emoji}</div>
                <h3>{name}</h3>
                <p style="color:var(--mov-mid)">{role}</p>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: SERVICII — MODIFICAT (+ 2 servicii noi)
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "🛎️ Servicii":
    st.markdown('<div class="section-title">🛎️ Serviciile Noastre</div>', unsafe_allow_html=True)
    servicii = [
        ("🐕", "Plimbare Câini", "Plimbări zilnice de 30-60 minute în parcuri sigure, cu îngrijitor calificat. Raport foto după fiecare plimbare.", "50 RON / plimbare"),
        ("✂️", "Toaletare Animale", "Baie, tuns, pieptănat, tăiat unghii. Folosim produse 100% naturale, prietenoase cu animalele.", "120–200 RON"),
        ("🏠", "Supraveghere Animale", "Îngrijire la domiciliul tău sau al nostru. Hrănire, joacă, afecțiune și rapoarte zilnice.", "80 RON / zi"),
        ("🏥", "Programări Veterinar", "Organizăm și însoțim animalul tău la veterinar. Gestionăm dosarul medical și urmărim tratamentele.", "30 RON / programare"),
        # ── 2 servicii noi ──
        ("🎓", "Dresaj & Antrenament", "Sesiuni individuale de dresaj de bază sau avansat, adaptate vârstei și temperamentului câinelui tău. Lucrăm pe comenzi esențiale (șezi, stai, vino, la picior), gestionarea comportamentelor nedorite și socializare controlată. Fiecare sesiune include un raport de progres trimis proprietarului.", "150 RON / sesiune"),
        ("🚌", "Transport Animale", "Preluare și predare la domiciliu pentru orice serviciu PetFlow — toaletare, veterinar sau supraveghere. Vehicul dotat special pentru transportul în condiții de siguranță și confort: cuști omologate, ventilație, apă. Șofer cu experiență în manipularea animalelor.", "40 RON / cursă"),
    ]
    for emoji, titlu, desc, pret in servicii:
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <h3>{emoji} {titlu}</h3>
                <span class="price">{pret}</span>
            </div>
            <p style="color:var(--text-mid)">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: GALERIE
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "🖼️ Galerie":
    st.markdown('<div class="section-title">🖼️ Galerie Foto & Video</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    imagini = [
        ("https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400&auto=format&fit=crop", "Plimbare în parc 🐕"),
        ("https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&auto=format&fit=crop", "Prieteni la plimbare 🐾"),
        ("https://images.unsplash.com/photo-1552053831-71594a27632d?w=400&auto=format&fit=crop", "Golden Retriever fericit 🌟"),
        ("https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=400&auto=format&fit=crop", "Câine jucăuș 🎾"),
        ("https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?w=400&auto=format&fit=crop", "Toaletare profesională ✂️"),
        ("https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400&auto=format&fit=crop", "Îngrijire cu dragoste 💜"),
    ]
    for i, (url, cap) in enumerate(imagini):
        with cols[i % 3]:
            st.markdown(f'''<div style="margin-bottom:16px">
                <img src="{url}" style="width:100%;border-radius:12px;object-fit:cover;height:220px" />
                <p style="text-align:center;color:var(--text-mid);font-size:0.85rem;margin-top:6px">{cap}</p>
            </div>''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">🎬 Video Galerie</div>', unsafe_allow_html=True)
    st.components.v1.iframe(
        "https://www.youtube.com/embed/loNTb5KPXek",
        height=500,
    )

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: BLOG — MODIFICAT (4 articole lungi și îngrijite)
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "📝 Blog":
    st.markdown('<div class="section-title">📝 Blog PetFlow</div>', unsafe_allow_html=True)

    if "liked_posts" not in st.session_state:
        st.session_state.liked_posts = set()

    articole = [
        (
            "🐕 Ghidul complet pentru prima vizită la toaletare — cum să îți pregătești câinele pas cu pas",
            "12 Mai 2026", "Ana Popescu",
            """Pentru mulți câini, vizita la toaletare poate fi o experiență copleșitoare dacă nu sunt pregătiți din timp. 
            Zgomotul uscătorului, atingerea în zone sensibile precum lăbușele sau urechile, prezența altor animale — toate 
            acestea pot declanșa anxietate dacă câinele nu le-a experimentat anterior într-un context pozitiv.

            <strong>Cum începi pregătirea acasă?</strong> Cu cel puțin două săptămâni înainte de prima programare, 
            dedică zilnic câteva minute pentru a atinge blând lăbușele, urechile, coada și zona gurii. 
            Asociază fiecare atingere cu o recompensă — o gustare preferată sau câteva cuvinte de laudă. 
            Treptat, câinele va înțelege că aceste atingeri nu reprezintă un pericol.

            <strong>Alege toaletorul potrivit.</strong> Nu toți toalorii au aceeași abordare față de animale anxioase. 
            Caută un specialist care lucrează fără cuști de așteptare, care îți permite să fii prezent în primele vizite 
            și care are experiență cu rase sau temperamente similare câinelui tău. O primă vizită de „familiarizare", 
            fără tuns sau baie, poate face o diferență enormă.

            <strong>Ce să aduci la prima vizită?</strong> O jucărie sau o pătură cu mirosul casei poate ajuta câinele 
            să se simtă mai în siguranță. Informează toaletorul despre orice sensibilitate fizică, operație recentă 
            sau comportament specific al animalului. Cu cât comunicarea este mai clară, cu atât experiența va fi mai bună 
            pentru toată lumea — inclusiv pentru câinele tău."""
        ),
        (
            "🥗 Nutriție canină în 2026 — ce ar trebui să mănânce câinele tău cu adevărat",
            "5 Mai 2026", "Elena Radu",
            """Industria alimentației pentru animale de companie s-a schimbat enorm în ultimii ani. 
            Dacă acum un deceniu rafturile erau dominate de kibble-uri ultra-procesate cu ingrediente obscure, 
            astăzi proprietarii au acces la opțiuni mult mai variate și mai transparente. Dar cu atâtea alegeri, 
            confuzia este la fel de mare ca niciodată.

            <strong>Kibble vs. hrană proaspătă vs. raw — care este mai bun?</strong> Nu există un răspuns universal. 
            Kibble-ul de calitate superioară rămâne o opție practică și echilibrată pentru majoritatea câinilor, 
            cu condiția să verifici primele 3-5 ingrediente (ar trebui să fie surse de proteină animală, nu cereale). 
            Hrana proaspătă gătită blând sau dietele raw pot aduce beneficii reale — blană mai lucioasă, digestie mai bună, 
            energie crescută — dar necesită planificare atentă pentru a evita deficiențele nutriționale.

            <strong>Ce trebuie să eviți cu strictețe:</strong> ceapa și usturoiul (toxice chiar și în cantități mici), 
            strugurii și stafidele (pot provoca insuficiență renală), xilitolul din produsele fără zahăr, 
            ciocolata și macadamia. Multe dintre aceste alimente nu produc simptome imediat vizibile, 
            ceea ce le face cu atât mai periculoase.

            <strong>Hidratarea — elementul ignorat.</strong> Câinii hrăniți exclusiv cu kibble consumă mult mai puțină 
            apă decât au nevoie. Adaugă apă caldă peste mâncare, oferă o fântână cu apă curgătoare sau integrează 
            periodic hrană umedă în dietă. Un câine bine hidratat are rinichi sănătoși, articulații mai flexibile 
            și o piele mai echilibrată.

            Înainte de orice schimbare majoră în dietă, consultă medicul veterinar sau un nutriționist specializat în 
            animale de companie. Tranziția trebuie făcută gradual, pe parcursul a 7-10 zile, pentru a evita problemele digestive."""
        ),
        (
            "🧠 Sănătatea mintală a câinelui — cum recunoști anxietatea și ce poți face",
            "28 Aprilie 2026", "Mihai Ionescu",
            """Mult timp, comportamentele problematice ale câinilor au fost interpretate ca „răutate", „încăpățânare" 
            sau lipsă de dresaj. Astăzi știm că în spatele multor dintre ele se ascunde anxietatea — o stare reală, 
            cu baze neurologice, care afectează milioane de câini din întreaga lume.

            <strong>Cum arată anxietatea la câini?</strong> Semnele variază enorm în funcție de individ. 
            Unii câini latră excesiv sau distrug obiecte când sunt singuri acasă — aceasta este anxietatea de separare, 
            una dintre cele mai frecvente forme. Alții tremură, se ascund sau refuză să mănânce în situații noi. 
            Lingerea compulsivă a lăbelor, mișcările repetitive sau agresivitatea aparent inexplicabilă 
            pot fi, de asemenea, semne că ceva nu este în regulă la nivel emoțional.

            <strong>Ce declanșează anxietatea?</strong> Lipsa socializării în primele 3-14 săptămâni de viață 
            este unul dintre principalii factori de risc. La fel, traumele (abuz, abandon, accidente), 
            schimbările bruște de mediu sau rutină și — surprinzător — singurătatea cronică. 
            Câinii sunt animale sociale; un câine lăsat singur 10-12 ore pe zi, zi după zi, va dezvolta 
            aproape inevitabil probleme comportamentale.

            <strong>Ce poți face concret?</strong> Începe cu un consult la veterinar pentru a exclude cauze medicale. 
            Dacă originea este comportamentală, un specialist în comportament canin poate construi un plan de 
            desensibilizare și contracondiționare. Suplimentele naturale (L-teanina, ashwagandha pentru câini, 
            feromoni sintetici) pot oferi suport, dar nu înlocuiesc terapia comportamentală. 
            Mișcarea zilnică, rutina predictibilă și legătura emoțională cu proprietarul rămân cei mai puternici 
            „antidepresivi" naturali pentru câinele tău."""
        ),
        (
            "🏡 Cum pregătești casa și inima pentru un nou animal de companie — ghid pentru adopție responsabilă",
            "18 Aprilie 2026", "Petrescu Roxana",
            """Adoptarea unui animal de companie este una dintre cele mai frumoase decizii pe care le poate lua o familie. 
            Dar este și una dintre cele mai importante — pentru că în spatele acelei decizii stă o viață care depinde 
            în întregime de tine pentru următorii 10-15 ani sau chiar mai mult.

            <strong>Înainte de adopție — întrebările corecte.</strong> Ești pregătit pentru costurile reale? 
            Un câine de talie medie poate costa între 3.000 și 8.000 RON pe an, incluzând hrană de calitate, 
            vizite veterinare de rutină, toaletare și ocazional îngrijire de specialitate. 
            Ai timp pentru plimbări zilnice, joacă și socializare? 
            Toți membrii familiei sunt de acord și pregătiți? Există alergii sau fobii în casă?

            <strong>Pregătirea spațiului.</strong> Înainte să aduci animalul acasă, securizează mediul: 
            ascunde firele electrice accesibile, elimină plantele toxice (liliacul, ficus, aloe vera pot fi periculoase 
            pentru câini și pisici), asigură un spațiu dedicat pentru odihnă — o pătură sau un culcuș 
            în care animalul să se retragă când vrea liniște. Primele zile sunt critice pentru construirea 
            unui sentiment de siguranță.

            <strong>Primele săptămâni — răbdarea este totul.</strong> Un animal adoptat, mai ales unul din adăpost, 
            poate părea retras, confuz sau chiar agresiv în primele zile. Acesta este comportamentul normal de 
            adaptare — nu o reflecție a caracterului său permanent. Oferă-i spațiu, rutină și consistență. 
            Evită vizitele în masă, schimbările frecvente și stresul inutil. 
            Cu timp, grijă și răbdare, vei descoperi cu adevărat cine este animalul tău.

            <strong>Adoptă, nu cumpăra.</strong> România are mii de animale în adăposturi care așteaptă o familie. 
            Adoptând, nu doar că salvezi o viață — ci primești adesea un companion recunoscător, 
            sterilizat, vaccinat și cu un caracter format. PetFlow colaborează cu mai multe adăposturi partenere 
            din București și te poate ajuta să găsești perechea perfectă pentru stilul tău de viață."""
        ),
    ]

    st.info("Apasă pe inimioară ca să dai like sau apasă din nou ca să retragi like-ul.")

    for index, (titlu, data, autor, continut) in enumerate(articole):
        liked = index in st.session_state.liked_posts
        heart = "❤️" if liked else "🤍"
        like_text = "Retrage like" if liked else "Like"

        st.markdown(f"""
        <div class="blog-card">
            <h4>{titlu}</h4>
            <p style="color:var(--mov-light);font-size:0.85rem">📅 {data} &nbsp;|&nbsp; ✍️ {autor}</p>
            <div style="color:var(--text-mid); line-height:1.7; font-size:1rem;">
                {continut.strip().replace("\n", "<br>")}
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_like, col_spacer = st.columns([1, 5])
        with col_like:
            if st.button(f"{heart} {like_text}", key=f"like_blog_{index}"):
                if liked:
                    st.session_state.liked_posts.remove(index)
                else:
                    st.session_state.liked_posts.add(index)
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: PROGRAMARE ONLINE
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "📅 Programare Online":
    st.markdown('<div class="section-title">📅 Programare Online</div>', unsafe_allow_html=True)
    st.markdown("Completează formularul de mai jos și te vom contacta în cel mai scurt timp!")

    with st.form("form_programare"):
        c1, c2 = st.columns(2)
        with c1:
            nume = st.text_input("👤 Numele tău *")
            telefon = st.text_input("📞 Telefon *")
            email = st.text_input("📧 Email *")
        with c2:
            nume_animal = st.text_input("🐾 Numele animalului *")
            tip_animal = st.selectbox("🐶 Tipul animalului", ["Câine", "Pisică", "Alt animal"])
            rasa = st.text_input("Rasa animalului")

        serviciu = st.selectbox("🛎️ Serviciu dorit *", [
            "Plimbare Câini — 50 RON",
            "Toaletare Animale — 120-200 RON",
            "Supraveghere Animale — 80 RON/zi",
            "Programare Veterinar — 30 RON",
            "Dresaj & Antrenament — 150 RON/sesiune",
            "Transport Animale — 40 RON/cursă",
        ])
        data_prog = st.date_input("📅 Data dorită *")
        ora_prog = st.time_input("🕐 Ora dorită *")
        mentiuni = st.text_area("📝 Mențiuni speciale (alergii, comportament, etc.)")

        submitted = st.form_submit_button("✅ Trimite Programarea", use_container_width=True)
        if submitted:
            if nume and telefon and nume_animal:
                st.success(f"🎉 Mulțumim, **{nume}**! Programarea pentru **{nume_animal}** la **{serviciu.split('—')[0].strip()}** pe **{data_prog}** la ora **{ora_prog}** a fost înregistrată. Te vom contacta în curând!")
            else:
                st.error("⚠️ Te rugăm să completezi toate câmpurile obligatorii (*)")

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: SATISFACȚIE CLIENȚI
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "⭐ Satisfacție Clienți":
    st.markdown('<div class="section-title">⭐ Chestionar de Satisfacție</div>', unsafe_allow_html=True)
    st.markdown("Opinia ta contează! Ajută-ne să ne îmbunătățim serviciile.")

    with st.form("chestionar"):
        nume_client = st.text_input("👤 Numele tău (opțional)")
        serviciu_folosit = st.selectbox("🛎️ Ce serviciu ai folosit?", [
            "Plimbare Câini", "Toaletare", "Supraveghere", "Programare Veterinar",
            "Dresaj & Antrenament", "Transport Animale"
        ])

        st.markdown("**⭐ Evaluează serviciul primit (1 = Slab, 5 = Excelent)**")
        nota_generala = st.slider("Calitate generală", 1, 5, 5)
        nota_personal = st.slider("Amabilitatea personalului", 1, 5, 5)
        nota_pret = st.slider("Raport calitate/preț", 1, 5, 4)
        nota_curatenie = st.slider("Curățenie și igienă", 1, 5, 5)

        recomandat = st.radio("Ai recomanda PetFlow prietenilor?", ["Da, cu siguranță! 💜", "Probabil da", "Nu știu", "Nu"])
        comentariu = st.text_area("💬 Comentarii și sugestii")

        submitted = st.form_submit_button("📨 Trimite Evaluarea", use_container_width=True)
        if submitted:
            medie = (nota_generala + nota_personal + nota_pret + nota_curatenie) / 4
            st.success(f"🙏 Mulțumim pentru feedback! Nota medie acordată: **{medie:.1f}/5** ⭐")
            st.balloons()

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: FEEDBACK
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "💬 Feedback":
    st.markdown('<div class="section-title">💬 Feedback & Sugestii</div>', unsafe_allow_html=True)
    st.markdown("Avem o sugestie, o reclamație sau o idee? Scrie-ne direct!")

    with st.form("feedback_form"):
        c1, c2 = st.columns(2)
        with c1:
            nume_fb = st.text_input("👤 Numele tău")
            email_fb = st.text_input("📧 Email")
        with c2:
            tip_mesaj = st.selectbox("📌 Tipul mesajului", [
                "💡 Sugestie", "⭐ Compliment", "⚠️ Reclamație", "❓ Întrebare generală"
            ])
            urgent = st.checkbox("🚨 Mesaj urgent")

        subiect = st.text_input("📋 Subiect")
        mesaj = st.text_area("✍️ Mesajul tău *", height=150)
        acord_gdpr = st.checkbox("✅ Sunt de acord cu prelucrarea datelor personale conform GDPR")

        submitted = st.form_submit_button("📤 Trimite Mesajul", use_container_width=True)
        if submitted:
            if mesaj and acord_gdpr:
                st.success("✅ Mesajul tău a fost trimis cu succes! Îți vom răspunde în maxim 24 de ore.")
            elif not acord_gdpr:
                st.error("⚠️ Te rugăm să accepți prelucrarea datelor GDPR.")
            else:
                st.error("⚠️ Te rugăm să completezi câmpul mesaj.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGINA: CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif pagina == "📞 Contact":
    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card">
            <h3>📍 Date de Contact</h3>
            <p>📍 <strong>Adresă:</strong> Bd. Gheorghe Șincai nr. 5, București, România</p>
            <p>📞 <strong>Telefon:</strong> +40 712 345 678</p>
            <p>📧 <strong>Email:</strong> contact@petflow.ro</p>
            <p>🕐 <strong>Program:</strong> Luni–Sâmbătă, 08:00–20:00</p>
        </div>
        <div class="card">
            <h3>📣 Rețele Sociale</h3>
            <a href="https://facebook.com/petflow.ro" target="_blank" class="social-btn fb">📘 Facebook</a>
            <a href="https://instagram.com/petflow.ro" target="_blank" class="social-btn ig">📸 Instagram</a>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <h3>📝 Trimite-ne un Mesaj</h3>
        </div>
        """, unsafe_allow_html=True)
        with st.form("contact_form"):
            nume_c = st.text_input("Numele tău")
            email_c = st.text_input("Email")
            msg_c = st.text_area("Mesajul tău")
            if st.form_submit_button("Trimite ✉️", use_container_width=True):
                if nume_c and email_c and msg_c:
                    st.success("✅ Mesaj trimis! Te contactăm în curând.")
                else:
                    st.error("⚠️ Completează toate câmpurile.")

    st.markdown("---")
    st.markdown('<div class="section-title">🗺️ Locația Noastră</div>', unsafe_allow_html=True)
    st.components.v1.iframe(
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2848.5!2d26.0965!3d44.4195!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40b1ff3d3c8f4c3b%3A0x1a2b3c4d5e6f7890!2sBd.%20Gheorghe%20%C8%98incai%205%2C%20Bucure%C8%99ti!5e0!3m2!1sro!2sro!4v1716000000000",
        height=350,
    )

# ── Footer (always visible) ───────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <h3 style="color:white;margin:0">🐾 PetFlow România</h3>
    <p style="opacity:0.8">Îngrijire profesională pentru animalele tale de companie</p>
    <a href="https://facebook.com/petflow.ro" target="_blank" class="social-btn fb">📘 Facebook</a>
    <a href="https://instagram.com/petflow.ro" target="_blank" class="social-btn ig">📸 Instagram</a>
    <p style="opacity:0.5;font-size:0.8rem;margin-top:16px">© 2026 PetFlow România. Toate drepturile rezervate.</p>
</div>
""", unsafe_allow_html=True)
