# Sahih-Bukhari-JSON

Using beautifulSoup, I wrote this web scraper python script to get data from **sahih bukhari** website https://sunnah.com/bukhari/
It traverses through books and chapters of the Sahih Bukhari and extracts the data and saves to a organozed Directory based JSON files
BUKHARI
|_____BOOK_1
      |_______Book_1.json
     
This is the folder structure and file format
{
  Book: 'Revelation',
  Ahadith:[
  {
    narrator: "",
    hadith: ""
  }
  ]
}

Also used a progress bar in the console for a better view :)
