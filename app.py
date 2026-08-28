import streamlit as st
import wikipedia
import google.generativeai as genai
import plotly.express as px

# =====================================================================
# 1. LIVE WEB EXTRACTION LAYER (WIKIPEDIA API WRAPPER)
# =====================================================================
# Real-time extraction via Wikipedia API

def get_wiki_clues(topic):
    """Queries the live web via API to provide structural cultural context to the engine."""
    if not topic or topic.strip() == "":
        return "No specific topic provided for background scraping."
    try:
        page = wikipedia.page(topic)
        return page.summary[:1000]  # First 1000 characters of clean string context
    except wikipedia.exceptions.DisambiguationError:
        return f"Multiple entries found for '{topic}'. Please be more specific."
    except wikipedia.exceptions.PageError:
        return f"No verified web context discovered for the entry: '{topic}'."
    except Exception:
        return "Network timeout while fetching live web metrics."

# =====================================================================
# 2. DEDUCTIVE REASONING SYSTEM (GEMINI API CONNECTIVITY)
# =====================================================================
def ask_sherlock(api_key, user_data, web_context, include_astro):
    """Invokes the AI processing layer to dynamically execute behavioral logic mapping."""
    
    # If no API key provided, use demo mode
    if not api_key:
        return generate_demo_analysis(user_data, include_astro)
    
    try:
        genai.configure(api_key=api_key)
        # Using the standard modern text-focused operational model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Branch operational logic based on user belief toggles
        if include_astro:
            astro_instruction = f"""
            - Factor in their Astrological Sign: {user_data['zodiac']}.
            - Cross-reference it with classical mythological archetypes to parse core behavioral instincts.
            - Synthesize how cosmic profiling maps onto their psychological makeup.
            """
            system_tag = "Cosmic-Psychometric Analysis Model"
        else:
            astro_instruction = """
            - CRITICAL: Bypassed by user demand. DO NOT include any astrology, zodiac, or mythological frameworks.
            - Evaluate the profile purely through empirical psychometrics, cognitive structures, and structural consumption dynamics.
            """
            system_tag = "Pure Scientific Psychometric Model"
            
        # Heavy programmatic prompt structuring to control boundaries
        prompt = f"""
        You are Sherlock Holmes acting as an expert, razor-sharp psychometric behavioral analyst.
        Your task is to strip away social masking and expose the unvarnished, authentic 'hidden face' of this subject.
        
        [SUBJECT PORTFOLIO PROFILE]
        - Operational Model: {system_tag}
        - Region / Cultural Base: {user_data['region']}
        - MBTI Cognitive Type: {user_data['mbti']}
        - Target Fictional Character: {user_data['char']}
        - Visual Aesthetic / Identity Subculture: {user_data['style']}
        - Stated Vulnerabilities / Core Insecurities: {user_data['insecurities']}
        
        [WEB-SCRAPED CONTEXT FROM OPEN CHANNELS REGARDING FACTION: {user_data['char']}]
        """
        {web_context}
        """
        
        [OPERATIONAL DIRECTIVES]
        {astro_instruction}
        
        Provide your comprehensive deduction in your iconic, cold, clinical, and hyper-articulate analytical prose.
        You must structure your response exactly under these three distinct headers:
        
        ### 🧠 1. Core Psychological Archetype & Social Camouflage
        (Analyze how their subculture, style, and persona choices act as defensive masks to protect their vulnerabilities.)
        
        ### 🚨 2. Unmasked Behavioral 'Red Flags' & Relational Friction Points
        (Expose hidden behavioral risks, toxic tendencies, emotional deflection strategies, or communication traps.)
        
        ### ⚡ 3. Crisis Response & Projected Growth Arc 
        (Predict exactly how they break down under a high-stress crisis scenario, and detail their ultimate personal evolution arc.)
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ **Operational Interruption**: Failed to bridge communication to the AI matrix. Details: {str(e)}"

def generate_demo_analysis(user_data, include_astro):
    """Generate a demo analysis without API key (demonstration mode)."""
    mbti = user_data.get('mbti', 'INTJ')
    char = user_data.get('char', 'Sherlock Holmes')
    style = user_data.get('style', 'Minimalist')
    insecurities = user_data.get('insecurities', 'performance anxiety')
    zodiac = user_data.get('zodiac', 'Aries')
    
    astrological_note = f"\n\n**Astrological Overlay**: As a {zodiac}, this profile reveals inherent tension between your cosmic predisposition toward independence and your stated need for structural validation." if include_astro else ""
    
    demo_output = f"""
### 🧠 1. Core Psychological Archetype & Social Camouflage

Your identification with **{char}** paired with your **{mbti}** cognitive architecture reveals a classic "Intellectual Fortress" personality pattern. The **{style}** aesthetic choice functions as behavioral armor—projecting competence, control, and emotional distance to compensate for deeper vulnerabilities around inadequacy and relational disconnection.

Your personality operates through systematic abstraction: you process emotional situations as logical puzzles, converting feelings into solvable problems. This allows you to feel "safe" through intellectual dominance, but creates a paradox—the more you retreat into logic, the more you reinforce the very isolation you secretly fear.{astrological_note}

### 🚨 2. Unmasked Behavioral 'Red Flags' & Relational Friction Points

**Critical Vulnerabilities:**
- **Perfectionism Spiral**: Your standards are weaponized self-sabotage. When you inevitably fail to meet your impossible expectations, you interpret this as personal unworthiness rather than human limitation.
- **Emotional Avoidance Architecture**: You dismiss emotions in others as "weakness" while simultaneously being hypersensitive to perceived rejection. This creates a push-pull dynamic in relationships.
- **Superiority Masking Inferiority**: Behind the intellectual posturing lives deep-seated comparison anxiety. You compulsively measure yourself against others, experiencing every setback as evidence of fundamental inadequacy.

**Relational Red Flags:**
- You attract similar "broken geniuses" who mirror your isolation patterns, creating toxically codependent intellectual partnerships
- Your communication style reads as dismissive or condescending when anxious, pushing away the very people you secretly want to connect with
- You have a pattern of abrupt relationship termination when emotional vulnerability becomes unavoidable

### ⚡ 3. Crisis Response & Projected Growth Arc

**Under High-Stress Crisis:**
When your intellectual control systems fail (professional setback, romantic rejection, health crisis), you experience catastrophic psychological collapse. Your carefully constructed identity shatters because it was built entirely on external validation, not internal resilience. You become either paralyzingly depressed or compulsively overactive, seeking to rebuild the sense of control through obsessive work or self-isolation.

**Projected Evolution Path:**
Your breakthrough comes when you recognize that vulnerability is not weakness but depth. Real strength lies not in never failing, but in continuing despite failure. Your {char}-like deductive capabilities are gifts, but only when grounded in genuine human connection rather than intellectual superiority.

**Transformation Milestone**: Learning to say "I don't know" or "I was wrong" without experiencing existential threat. This single shift unlocks access to authentic relationships, genuine creativity, and psychological freedom.

---

💡 **DEMO MODE NOTE**: This analysis was generated using pattern-based demonstration logic. For personalized AI-powered analysis, please add a valid Gemini API key in the sidebar.
"""
    
    return demo_output

def analyze_situation(situation_description, your_typical_response, user_profile, api_key):
    """Analyzes a specific situation and provides strategic recommendations."""
    
    if not situation_description.strip():
        return "⚠️ Please provide a detailed description of the situation to analyze."
    
    # Demo mode if no API key
    if not api_key:
        return generate_demo_situation_analysis(situation_description, your_typical_response, user_profile)
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        You are Sherlock Holmes analyzing a complex interpersonal or professional situation.
        
        SITUATION DESCRIPTION:
        {situation_description}
        
        HOW THE PERSON TYPICALLY RESPONDS:
        {your_typical_response if your_typical_response else "Not specified"}
        
        PERSON'S PSYCHOLOGICAL PROFILE:
        - MBTI Type: {user_profile.get('mbti', 'Unknown')}
        - Region/Background: {user_profile.get('region', 'Unknown')}
        - Visual Identity: {user_profile.get('style', 'Unknown')}
        
        Provide your strategic analysis with these exact sections:
        
        ### 🔍 1. Hidden Dynamics & Unspoken Tensions
        (Analyze what's really going on beneath the surface that isn't being stated)
        
        ### ⚠️ 2. Behavioral Trap Analysis
        (Identify the psychological patterns and automatic reactions that might make things worse)
        
        ### ✅ 3. Strategic Counter-Moves & Optimal Response Path
        (Provide specific, actionable steps to navigate this situation effectively given your personality type)
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def generate_demo_situation_analysis(situation, response, user_profile):
    """Generate demo situation analysis without API key."""
    mbti = user_profile.get('mbti', 'Unknown')
    
    return f"""
### 🔍 1. Hidden Dynamics & Unspoken Tensions

The stated situation on the surface appears straightforward, but as a {mbti} personality type, you're likely missing the emotional subtext. People around you are often communicating on multiple levels simultaneously—their words mask deeper needs, fears, and unspoken expectations that your logical framework tends to dismiss as "irrational."

In this specific scenario, there are likely power dynamics at play that someone with your cognitive style might overlook. Others are reading the emotional temperature of the room while you're processing facts and logic. This creates a gap where misunderstandings fester.

### ⚠️ 2. Behavioral Trap Analysis

Your typical response pattern—{response if response else "to retreat into analysis mode"}—is actually reinforcing the conflict rather than resolving it. Here's why:

**The Trap**: As a {mbti}, you likely default to either:
- **Logic bombardment** (explaining why you're right, which makes others feel unheard)
- **Withdrawal** (retreating to process independently, which others interpret as coldness or rejection)
- **Perfectionism pressure** (demanding flawless solutions, which paralyzes the situation)

This response style works against you in emotionally-charged situations because people need to feel *understood* before they'll accept your logic. Your pattern validates their fear that you don't care about their feelings, creating a negative feedback loop.

### ✅ 3. Strategic Counter-Moves & Optimal Response Path

**Immediate Action (Next 24-48 hours):**
1. **Pause the urge to "fix it"** - Set aside your need to analyze or problem-solve immediately
2. **Validate first** - Use phrases like: "I hear that this is frustrating for you" or "That makes sense given your perspective"
3. **Ask clarifying questions about feelings, not facts** - "What matters most to you in this situation?" not "Why did you make that choice?"

**Medium-term Strategy:**
- Acknowledge your limitation explicitly: "I'm wired to think logically first, but I recognize emotions are important here too"
- Suggest a structured conversation time rather than reactive exchanges
- Commit to listening for understanding, not for finding flaws in their argument

**Long-term Pattern Shift:**
The real breakthrough for your personality type is learning that emotional validation and logical problem-solving aren't mutually exclusive. You can do both. The key is *sequencing*—validate emotions first, then problem-solve together.

This situation is actually an opportunity to build trust by proving you can adapt your natural style to meet others halfway.

---
💡 **DEMO MODE**: This analysis was generated using pattern-based demonstration logic. For personalized AI analysis with your Gemini API key, results will be customized to your specific situation.
"""

def assess_mbti_from_profile(fav_char, style, insecurities, zodiac):
    """Infer MBTI type from profile characteristics using pattern matching."""
    
    mbti_map = {
        "Sherlock Holmes": ["INTJ", "INTP"],
        "Tony Stark": ["ENTP", "ENTJ"],
        "Hermione Granger": ["ISTJ", "INTJ"],
        "Harley Quinn": ["ENFP", "ESFP"],
        "Batman": ["INTJ", "ISTP"],
        "Katniss Everdeen": ["ISTP", "ISTJ"],
        "Aang": ["ENFP", "ESFJ"],
        "Loki": ["ENTP", "INTJ"]
    }
    
    # Start with character-based inference
    primary_mbti = mbti_map.get(fav_char, ["INTJ", "INTP"])
    
    # Adjust based on style preference
    style_lower = style.lower()
    if "dark" in style_lower or "isolated" in style_lower:
        if primary_mbti[0].startswith("E"):
            primary_mbti = [primary_mbti[0].replace("E", "I")] + primary_mbti
    
    if "social" in style_lower or "tribe" in style_lower:
        if primary_mbti[0].startswith("I"):
            primary_mbti = [primary_mbti[0].replace("I", "E")] + primary_mbti
    
    # Check for F (feeling) indicators
    if any(word in insecurities.lower() for word in ["emotional", "connection", "love", "care", "support"]):
        primary_mbti = [mbti.replace("T", "F") if "T" in mbti else mbti for mbti in primary_mbti]
    
    return primary_mbti[0]

def decode_mystery_person(person_name, clues, style, interaction, response, api_key):
    """Analyze a person you don't know well based on limited signals."""
    
    if not clues.strip():
        return "⚠️ Please provide at least some clues or observations about this person."
    
    if not api_key:
        return generate_demo_stranger_analysis(person_name, clues, style, interaction, response)
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        You are Sherlock Holmes making initial deductions about a person based on limited first impressions.
        
        PERSON: {person_name}
        
        CLUES & OBSERVATIONS:
        {clues}
        
        AESTHETIC/STYLE:
        {style}
        
        A SPECIFIC INTERACTION OR MOMENT:
        {interaction}
        
        HOW THEY RESPONDED:
        {response}
        
        Based on these limited signals, provide your initial profile assessment with these sections:
        
        ### 🔍 1. First Impression Deduction
        (What do these signals reveal about their personality, motivations, and core values?)
        
        ### 🚩 2. Red Flags & Patterns to Watch
        (What behavioral tendencies or potential issues do you detect?)
        
        ### 💡 3. How to Engage With This Person
        (Specific strategies for building rapport or understanding them better)
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def generate_demo_stranger_analysis(person_name, clues, style, interaction, response):
    """Generate demo analysis of a stranger without API key."""
    
    return f"""
### 🔍 1. First Impression Deduction

From the limited signals you've provided, **{person_name}** appears to operate from a particular psychological baseline. Their aesthetic choice ({style}) combined with how they responded to your interaction ({response.lower()[:50]}...) suggests someone who:

- Is navigating social situations with a specific defensive or adaptive strategy
- Uses their physical presentation as communication (whether intentional or not)
- Has particular values or concerns that emerged in your interaction
- May be presenting a curated version of themselves in first meetings

The clues you've noted ({clues[:60]}...) are meaningful data points that suggest interest in certain ideas, characters, or values—these often reflect deeper psychological needs or aspirations.

### 🚩 2. Red Flags & Patterns to Watch

**Initial Patterns:**
- **Information Scarcity**: Based on brief interaction, watch for consistency between their words and actions over time
- **Mirror Effect**: People often adjust their behavior in first meetings—what you saw may be a modified version of their typical self
- **Selective Sharing**: The clues they volunteered may indicate what they want you to know, not necessarily what's most important about them
- **Communication Style**: How they responded ({response}) in that moment could indicate: comfort level, authenticity, or social performance

**What To Investigate Further:**
- Do their stated interests (favorite character, etc.) align with their actual behavior?
- How do they respond to mild disagreement or challenge?
- What do they avoid talking about?

### 💡 3. How to Engage With This Person

**Initial Strategy:**
1. **Validate their interests** - They volunteered information about {clues.split()[0:3]}; this suggests these topics matter to them
2. **Observe consistency** - Note whether their behavior matches their stated preferences over multiple interactions
3. **Create low-pressure situations** - People reveal more when they're not feeling evaluated
4. **Ask open questions** - Instead of assumptions, dig deeper: "What draws you to that?" rather than making conclusions

**Long-term Understanding:**
- Build a hypothesis and test it gradually
- Look for patterns across contexts (how they act with different people, in different settings)
- Pay attention to what they're *not* saying—silence and avoidance reveal as much as words

---
💡 **DEMO MODE**: This is a preliminary assessment based on limited data. Real understanding develops over time through consistent interaction.
"""

# =====================================================================
# 3. INTERACTIVE WEB USER INTERFACE (STREAMLIT DASHBOARD)
# =====================================================================
st.set_page_config(
    page_title="Project Sherlock Live",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# Mobile-friendly CSS styling
st.markdown("""
    <style>
        /* Mobile optimization */
        @media (max-width: 640px) {
            .stTabs [role="tablist"] {
                gap: 0.5rem;
            }
            .stTabs [role="tab"] {
                padding: 0.5rem 0.75rem;
                font-size: 0.85rem;
            }
            .main .block-container {
                padding: 1rem 0.5rem;
            }
            input, textarea, select {
                font-size: 16px !important;
                padding: 0.75rem !important;
            }
        }
        
        /* Responsive form layout */
        @media (max-width: 768px) {
            .stColumn {
                min-width: 100% !important;
            }
        }
        
        /* Better spacing on all devices */
        .stForm {
            padding: 1rem;
            border-radius: 8px;
            background-color: #f8f9fa;
        }
        
        /* Improve button sizing for mobile */
        button {
            min-height: 44px;
        }
        
        /* Better text sizing */
        h1, h2, h3 {
            word-break: break-word;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #1E3A8A; word-break: break-word;'>🕵️‍♂️ Project Sherlock: Deductive Behavioral Engine</h1>
    <h4 style='text-align: center; color: #4B5563; word-break: break-word;'>MIT WPU B.Tech CSE Core Credit — Prototype Matrix</h4>
    <hr style='border-top: 2px solid #3B82F6;'>
""", unsafe_allow_html=True)

# Operational Sidebar Setup
st.sidebar.markdown("### 🔧 Operations Control")
GOOGLE_API_KEY = st.sidebar.text_input(
    "Gemini API Token Key", 
    type="password", 
    help="Acquire your development sandbox token key for free from Google AI Studio."
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Execution Note**: This architecture aggregates user subcultures, demographics, and media metrics, "
    "pulls real-time Wikipedia context tables, and maps psychological profiles while exposing relational red flags."
)

# Application Navigation Form Architecture
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👤 Profile Dossier Intake", 
    "📊 Structural Compatibility Weights", 
    "🎭 Situation Analysis",
    "📋 MBTI Assessment",
    "🔎 Mystery Person Decoder"
])

with tab1:
    st.markdown("### 🔍 Subject Intake Dossier Formulation")
    st.write("Fill out the demographic and behavioral markers below to construct the processing pipeline.")
    
    with st.form("dossier_form"):
        name = st.text_input("Subject Codename / Real Name", "Aarav")
        region = st.text_input("Region / Nationality Context", "Pune, India")
        
        col1, col2 = st.columns((1, 1), gap="small")
        
        with col1:
            mbti = st.selectbox(
                "MBTI Personality Matrix Block", 
                ["INTJ (Architect)", "INTP (Logician)", "INFJ (Advocate)", "INFP (Mediator)", 
                 "ENTJ (Commander)", "ENFP (Campaigner)", "ISTP (Virtuoso)", "ESTP (Entrepreneur)"]
            )
            
        with col2:
            zodiac = st.selectbox(
                "Astrological Zodiac Constellation", 
                ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
            )
        
        fav_char = st.text_input("Favorite Character (Exact text for Web Search connectivity)", "Sherlock Holmes")
        
        col3, col4 = st.columns((1, 1), gap="small")
        
        with col3:
            style = st.selectbox(
                "Visual Subculture Identity / Aesthetic", 
                ["Minimalist (Structured/Efficient)", "Dark Academia (Intellectual/Isolated)", 
                 "Grunge (Raw/Non-conformist)", "Streetwear (Social/Tribe-focused)", "Techwear (Utilitarian/Shielded)"]
            )
            
        with col4:
            pass
            
        insecurities = st.text_area(
            "Stated Internal Insecurities / Core Fears", 
            "Fear of structural failure, performance anxiety, deep-seated emotional isolation",
            height=80
        )
            
        st.markdown("#### 🎛️ Operational Paradigm Modifiers")
        include_astro = st.checkbox(
            "Activate Astrological & Mythological Core Interpretation Layer", 
            value=True,
            help="Uncheck this parameter to completely remove astrology and run a pure, empirical scientific evaluation pipeline."
        )
        
        submit = st.form_submit_button("🧠 Execute Critical Mind Palace Induction Analysis", use_container_width=True)
        
    if submit:
        with st.spinner("🕵️‍♂️ Holmes is deploying automated scrapers to gather web metadata vectors..."):
            # Step A: Scrape live web clues
            web_clues = get_wiki_clues(fav_char)
            st.toast(f"✓ Packets retrieved from Wikipedia servers regarding query '{fav_char}'")
            
            # Step B: Consolidate data packets
            user_profile = {
                "region": region, 
                "mbti": mbti.split(" ")[0], 
                "zodiac": zodiac, 
                "char": fav_char, 
                "style": style.split(" ")[0], 
                "insecurities": insecurities
            }
            
            # Step C: Process results via the API engine logic layer
            deduction_result = ask_sherlock(GOOGLE_API_KEY, user_profile, web_clues, include_astro)
            
            # Render Clean Deliverable Visuals
            st.markdown("---")
            st.markdown(f"### 📋 Analytical Output Case File Folder: **Subject {name}**")
            st.markdown(deduction_result)

with tab2:
    st.markdown("### 📊 Algorithmic Scoring Mechanics Breakdown")
    st.write(
        "This window simulates how the system dynamically adjusts mathematical scoring weight importance matrices "
        "when users shift filtering protocols (such as toggling off Astrology for pure psychometric evaluation)."
    )
    
    # Calculate responsive dynamic graphs based on toggle positioning
    if include_astro:
        metrics_labels = ["MBTI Layer Score", "Media Scraped Overlap", "Astrological Overlap Matrix", "Subculture Camouflage"]
        metrics_values = [40, 30, 20, 10]
        matrix_title = "Active Architecture Matrix: Composite Cosmic & Psychological Blueprint Weights"
    else:
        metrics_labels = ["MBTI Layer Score", "Media Scraped Overlap", "Astrological Overlap Matrix", "Subculture Camouflage"]
        metrics_values = [50, 35, 0, 15]
        matrix_title = "Active Architecture Matrix: Pure Scientific Empirical Profiling Metric Weights"
        
    fig = px.bar(
        x=metrics_labels, 
        y=metrics_values,
        labels={'x': 'System Analytical Metric Components', 'y': 'Weight Percentage Distribution (%)'},
        title=matrix_title,
        color=metrics_values,
        color_continuous_scale=px.colors.sequential.Blues
    )
    fig.update_yaxes(range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("### 🎭 Real-Time Situation Decoder")
    st.write("Facing a complex interpersonal or professional situation? Get Sherlock-style strategic analysis.")
    
    with st.form("situation_form"):
        st.markdown("#### 📍 Situation Details")
        situation = st.text_area(
            "Describe the situation you're navigating",
            placeholder="E.g., My team lead gave me critical feedback in front of the group, and I froze up instead of responding...",
            height=120
        )
        
        st.markdown("#### 🧠 Your Typical Response")
        response = st.text_area(
            "How do you typically respond to situations like this?",
            placeholder="E.g., I usually withdraw and process internally, then prepare a logical counter-argument...",
            height=100
        )
        
        include_profile = st.checkbox(
            "Use my profile data for analysis",
            value=True,
            help="This will incorporate your MBTI, region, and style for more personalized insights"
        )
        
        analyze_btn = st.form_submit_button("🔍 Execute Situation Decoder", use_container_width=True)
    
    if analyze_btn:
        if not situation.strip():
            st.error("❌ Please describe the situation first")
        else:
            with st.spinner("🕵️‍♂️ Holmes is analyzing the psychological architecture of this situation..."):
                # Prepare profile data if user wants it
                if include_profile:
                    profile_data = {
                        "mbti": "INTJ",  # Default, could be made dynamic
                        "region": "India",
                        "style": "Minimalist"
                    }
                else:
                    profile_data = {"mbti": "Unknown", "region": "Unknown", "style": "Unknown"}
                
                # Get analysis
                analysis_result = analyze_situation(situation, response, profile_data, GOOGLE_API_KEY)
                
                # Display results
                st.markdown("---")
                st.markdown("### 📋 Strategic Analysis Report")
                st.markdown(analysis_result)

with tab4:
    st.markdown("### 📋 Discover Your MBTI Type")
    st.write("Haven't taken an official MBTI test? Let's infer your personality type from your preferences and how you operate.")
    
    with st.form("mbti_assessment_form"):
        st.markdown("#### 🎬 Quick Assessment Questions")
        
        char = st.text_input(
            "Who's a character/person you deeply relate to?",
            "Sherlock Holmes",
            help="This reveals your aspirational self and value system"
        )
        
        style = st.selectbox(
            "How would you describe your personal aesthetic?",
            ["Minimalist (Structured/Efficient)", "Dark Academia (Intellectual/Isolated)", 
             "Grunge (Raw/Non-conformist)", "Streetwear (Social/Tribe-focused)", 
             "Techwear (Utilitarian/Shielded)", "Bohemian (Creative/Expressive)"]
        )
        
        col1, col2 = st.columns((1, 1), gap="small")
        
        with col1:
            insecurities = st.text_area(
                "What are your core insecurities or fears?",
                "Performance anxiety, inadequacy, emotional isolation",
                height=80,
                help="This helps us identify your F/T and J/P preferences"
            )
            
        with col2:
            zodiac = st.selectbox(
                "Your zodiac sign (optional)",
                ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", 
                 "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
            )
        
        assess_btn = st.form_submit_button("🧠 Reveal Your MBTI Type", use_container_width=True)
    
    if assess_btn:
        detected_mbti = assess_mbti_from_profile(char, style, insecurities, zodiac)
        st.success(f"### 🎯 Detected MBTI Type: **{detected_mbti}**")
        
        st.markdown(f"""
        Based on your preferences and psychological markers, you appear to be an **{detected_mbti}**.

        **Key Indicators:**
        - Your character affinity ({char}) suggests your cognitive processing style
        - Your aesthetic preference ({style.split()[0]}) reveals how you present to the world
        - Your stated insecurities indicate which functions are most activated
        
        **Note**: This is an inference, not a clinical assessment. For a definitive result, take the official 16Personalities or MBTI test.
        You can now use this type in the Profile Dossier tab for full analysis!
        """)

with tab5:
    st.markdown("### 🔎 Decode Someone You Just Met")
    st.write("Based on minimal information from a brief encounter, make initial psychological deductions about a new person.")
    
    with st.form("stranger_analysis_form"):
        st.markdown("#### 👤 Mystery Person Profile")
        
        person_name = st.text_input("What's their name/nickname?", "Alex")
        
        st.markdown("#### 📍 Clues About This Person")
        clues = st.text_area(
            "What clues have you picked up? (favorite character, interests, phrases they used, etc.)",
            "Mentioned they love sci-fi, quiet in group settings, wore vintage band t-shirt",
            height=100,
            help="The more specific, the better"
        )
        
        style = st.text_input(
            "Their aesthetic/style",
            "Alternative/vintage",
            help="How do they present themselves visually?"
        )
        
        col1, col2 = st.columns((1, 1), gap="small")
        
        with col1:
            interaction = st.text_area(
                "Describe one specific interaction or moment",
                "When I asked about their favorite movie, they gave a detailed answer but seemed uncomfortable with eye contact",
                height=80
            )
        
        with col2:
            response = st.text_area(
                "How did they respond/behave?",
                "Thoughtful but guarded, opened up a bit when talking about interests, avoided personal questions",
                height=80
            )
        
        decode_btn = st.form_submit_button("🔍 Decode This Person", use_container_width=True)
    
    if decode_btn:
        if not clues.strip():
            st.error("❌ Please provide at least some clues")
        else:
            with st.spinner("🕵️‍♂️ Holmes is observing the micro-expressions and patterns..."):
                analysis = decode_mystery_person(person_name, clues, style, interaction, response, GOOGLE_API_KEY)
                
                st.markdown("---")
                st.markdown(f"### 📋 First Impression Analysis: {person_name}")
                st.markdown(analysis)


