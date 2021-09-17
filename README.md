<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Geothermal NLP Tools 
    (WebApp: http://steaming-geothermal-analytics.info)</h3>

  <p align="center">
With the globally growing volume of geothermal literature, data analysis has become useful to advance professional and academic research and development efforts. Furthermore, it is essential to leverage state-of-the-art algorithms to develop useful tools based on existing databases. This work utilized statistical and deep learning techniques to draw insights based on the geothermal literature. We retrieved papers from the International Geothermal Association (IGA) database using the Stanford University search engine. As of 23 December 2020, we gathered and preprocessed all 18,873 publications archived in this database, where headers included publication title, authors, year, keywords, abstract, language, conference, and session type.

Analysis shows that the three geothermal events with the largest volume of publications historically are the Geothermal Resources Council Transactions, World Geothermal Congress, and Stanford Geothermal Workshop. Using natural language processing (NLP) techniques, we “geoparsed” each abstract to figure out what location in geographical coordinates it is concerned about. This allowed for developing an interactive world heatmap showing the focus of geothermal research efforts historically. Latent Dirichlet Allocation (LDA) was used to cluster the geothermal literature into a total of nine topics. we also developed a geothermal literature intelligent search engine using term frequency -- inverse document frequency (TF-IDF) and cosine similarity. Preprocessing the “authors” data, we developed a coauthorship graphical network encompassing researchers within the geothermal community and reflecting the level of collaboration between them. Finally, a deep learning model was developed to perform text generation and auto-completion using the state-of-the-art generative pretrained transformers (GPT-2) fine-tuned to the geothermal literature. We made these tools available on an open-source application programming interface (API) for public use. You may access this API at http://steaming-geothermal-analytics.info.
    <br />
    <a href="https://github.com/aljubrmj/Geothermal-NLP"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/aljubrmj/Geothermal-NLP/issues">Report Bug</a>
    ·
    <a href="https://github.com/aljubrmj/Geothermal-NLP/issues">Request Feature</a>
  </p>
</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Name: [@MJAljubran](https://twitter.com/twitter_handle) - m.j.aljubran@gmail.com

Project Link: [https://github.com/aljubrmj/Geothermal-NLP](https://github.com/aljubrmj/Geothermal-NLP)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/aljubrmj/Geothermal-NLP.svg?style=for-the-badge
[contributors-url]: https://github.com/aljubrmj/Geothermal-NLP/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/aljubrmj/Geothermal-NLP.svg?style=for-the-badge
[forks-url]: https://github.com/aljubrmj/Geothermal-NLP/network/members
[stars-shield]: https://img.shields.io/github/stars/aljubrmj/Geothermal-NLP.svg?style=for-the-badge
[stars-url]: https://github.com/aljubrmj/Geothermal-NLP/stargazers
[issues-shield]: https://img.shields.io/github/issues/aljubrmj/Geothermal-NLP.svg?style=for-the-badge
[issues-url]: https://github.com/aljubrmj/Geothermal-NLP/issues
[license-shield]: https://img.shields.io/github/license/aljubrmj/Geothermal-NLP.svg?style=for-the-badge
[license-url]: https://github.com/aljubrmj/Geothermal-NLP/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mohammad-jabs/
[product-screenshot]: images/screenshot.png

