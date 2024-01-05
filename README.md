# SentimentAnalysis
## Objetivos
En este proyecto se quiere llevar a cabo un análisis de sentimientos de las reseñas de una determinada tienda online en la plataforma Trustpilot.
Trustpilot es una página web fundada en 2007 en Dinamarca que permite a los usuarios publicar sus experiencias y opiniones con determinados servicios. Hoy en día, son las propios comercios electrónicos quienes incentivan el uso de esta plataforma a sus clientes tras realizar un pedido y recibirlo.

Se ha decidido que el análisis se centre en las opiniones de los clientes de la tienda online San Saru, puesto que se conoce que esta empresa es activa en Trustpilot y piden a sus clientes que publiquen en esta plataforma qué tal les ha ido la experiencia con su pedido.
Su URL en Trustpilot es https://es.trustpilot.com/review/sansarushop.com, la cual cuenta actualmente con 11149 opiniones, de las cuales 9959 están en castellano. A pesar de que se puede ver la puntuación que ha otorgado cada cliente, así como una calificación media, en este proyecto se quiere extraer cuál es el sentimiento general de todos los clientes, así como conocer qué aspectos positivos destacan y qué aspectos negativos podrían mejorar.

En primer lugar se deben recopilar las reseñas (script _1. recopilacion.py_).

Una vez se han recopilado las reseñas en castellano, se deben tratar para que la tarea de análisis sea lo más sencilla y precisa posible (script _2. preprocesamiento.py_).
En esta fase, lo primero que se debe hacer es traducir las opiniones al inglés mediante la API del traductor DeepL, que proporciona una suscripción gratuita con 500.000 caracteres al mes.
Con las reseñas traducidas, se debe realizar la tarea de limpieza y normalización. 

En cuanto a la limpieza, se deben eliminan los caracteres especiales y los emojis, los cuales se ha observado que utilizan los usuarios con frecuencia. Por otro lado, también se pasa cada reseña a minúscula. Tras esto, se deben quitar las palabras vacías _(stop words)_, que son aquellas que no aportan ningún significado a la oración. Para ello, se ha usado el paquete Corpus de NLTK. 

**Ejemplo de procesado de una reseña**:
- Original: “El reparto ha sido nefasto pero me encanta San Saru El reparto ha sido nefasto. Tuve que cambiar mi dirección porque por defecto sale otra dirección de un piso en el que ya no vivo. A pesar de contactar con san saru en seguida y de llamar a DHL 20 veces, se intentó entregar en esa dirección y luego tuve que ir a recogerlo a una oficina de recogida de paquetes a 35 min de mi casa. Es una pena que el delivery en casa haya sido tan horrible porque me encanta la marca, pero me daría pereza volver a comprar en San Saru sólo por no volver a tener la misma experiencia” - 113 palabras.
- Traducida: “The delivery was terrible but I love San Saru The delivery was terrible. I had to change my address because it defaulted to another address for an apartment I no longer live in. Despite contacting san saru right away and calling DHL 20 times, they tried to deliver to that address and then I had to go pick it up at a parcel pickup office 35 min from my house. It’s a shame that the delivery at home was so horrible because I love the brand, but I would be lazy to shop at san saru again just to not have the same experience again.” - 105 palabras.
- Procesada: “delivery terrible love san saru delivery terrible change address defaulted another address apartment longer live despite contacting san saru right away calling dhl 20 times tried deliver address go pick parcel pickup office 35 min house shame delivery home horrible love brand would lazy shop san saru experience” - 48 palabras.

Por último se pasa a la fase de análisis (script _3. analisis.py_), para lo cual se utiliza la librería TextBlob, la cual tiene tiene WordNet integrado, que es una base de datos léxica de palabras en inglés.
