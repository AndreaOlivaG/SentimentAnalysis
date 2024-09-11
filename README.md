# Sentiment Analysis of Trustpilot Reviews

## Objectives

This project aims to perform sentiment analysis on reviews of the online store San Saru on Trustpilot. Trustpilot is a website founded in 2007 in Denmark that allows users to post their experiences and opinions about various services. Nowadays, e-commerce businesses encourage customers to use this platform after placing and receiving an order.

The focus is on analyzing reviews from San Saru, which is active on Trustpilot and requests customers to share their experiences. Their Trustpilot page can be found at [this link](https://es.trustpilot.com/review/sansarushop.com), currently containing 11,149 reviews, of which 9,959 are in Spanish. Although the ratings and average score are visible, the goal is to extract the overall sentiment, highlight positive aspects, and identify areas for improvement.

### Steps

1. **Data Collection**: Collect reviews in Spanish using the script `collect_reviews.py`.

2. **Data Preprocessing**: Process the collected reviews to facilitate the analysis task using the script `preprocess_reviews.py`.
   - **Translation**: Translate reviews to English using the DeepL API, which offers a free subscription with 500,000 characters per month.
   - **Cleaning and Normalization**: Remove special characters, emojis, and convert text to lowercase. Eliminate stop words using the NLTK Corpus package.

   **Example of review processing**:
   - **Original**: “El reparto ha sido nefasto pero me encanta San Saru. El reparto ha sido nefasto. Tuve que cambiar mi dirección porque por defecto sale otra dirección de un piso en el que ya no vivo. A pesar de contactar con San Saru enseguida y de llamar a DHL 20 veces, se intentó entregar en esa dirección y luego tuve que ir a recogerlo a una oficina de recogida de paquetes a 35 min de mi casa. Es una pena que el delivery en casa haya sido tan horrible porque me encanta la marca, pero me daría pereza volver a comprar en San Saru sólo por no volver a tener la misma experiencia.”
   - **Translated**: “The delivery was terrible but I love San Saru. The delivery was terrible. I had to change my address because it defaulted to another address for an apartment I no longer live in. Despite contacting San Saru right away and calling DHL 20 times, they tried to deliver to that address and then I had to go pick it up at a parcel pickup office 35 minutes from my house. It’s a shame that the delivery at home was so horrible because I love the brand, but I would be reluctant to shop at San Saru again just to avoid having the same experience.”
   - **Processed**: “delivery terrible love san saru delivery terrible change address defaulted another address apartment longer live despite contacting san saru right away calling dhl 20 times tried deliver address go pick parcel pickup office 35 min house shame delivery home horrible love brand would reluctant shop san saru experience”


3. **Sentiment Analysis**: Perform sentiment analysis using the TextBlob library, which includes WordNet for lexical data. This is done with the script `analyze_sentiment.py`.