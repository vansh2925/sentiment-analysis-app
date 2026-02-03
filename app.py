import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main():
    st.set_page_config(page_title="Sentiment Analysis")
    st.title("Sentiment Analysis App")

    text = st.text_area("Enter your text here:")

    if st.button("Analyze Sentiment"):
        if not text or not text.strip():
            st.warning("Please enter some text to analyze.")
            return

        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)

        if score['compound'] >= 0.05:
            sentiment = "Positive 😊"
        elif score['compound'] <= -0.05:
            sentiment = "Negative 😠"
        else:
            sentiment = "Neutral 😐"

        st.subheader("Result:")
        st.write(sentiment)
        st.json(score)


if __name__ == "__main__":
    main()
