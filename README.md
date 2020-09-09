# ShakespeareComplimentsAndInsults
A program that randomly generates from a select list of words to create Shakespearean compliments or insults.

I had originally only intended for this to be a humorous compliment generator since a lot of words and phrases are no longer used from Shakespeare's time.
The results came out to be pretty funny, despite the phrases being compliments. So, I decided it would be funny to do an insult generator as well.

The compliment and insult generators are made basically the same way, with just some small differences here and there.
The main idea of how this is made:

- Create three separate lists of comma separated words for both the compliment and insult generators. I included the Excel file of the words I used.
- Use Python code to generate three separate random numbers, one number for each of the three lists in each of the two different generators.
- Each of the random numbers is then used to choose that numbered word in each of the respective lists.
- Lastly, each of the selected compliments or insults is joined together into one phrase that is displayed.
