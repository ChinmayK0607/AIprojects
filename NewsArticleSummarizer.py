import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Define the function that will be called when the "Summarize" button is clicked
def summarize():
    # Get the URL entered by the user from the text box
    url=utext.get('1.0',"end").strip()

    # Download and parse the article using the newspaper library
    article=Article(url)
    article.download()
    article.parse()
    article.nlp() # Use the natural language processing features of the article

    # Enable the text boxes for displaying the article's information
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear the text boxes before updating them with new information
    title.delete('1.0','end')
    author.delete('1.0','end')
    publication.delete('1.0','end')
    summary.delete('1.0','end')
    sentiment.delete('1.0','end')

    # Update the text boxes with the article's information
    title.insert('1.0',article.title)
    author.insert('1.0',article.authors)
    publication.insert('1.0',article.publish_date)
    summary.insert('1.0',article.summary)

    # Analyze the sentiment of the article using the textblob library
    analysis=TextBlob(article.text)
    sentiment.insert('1.0',f'Polarity:{analysis.priority},Sentiment :{"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')

    # Disable the text boxes again once the information has been displayed
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# Create the tkinter window and set its title and size
root=tk.Tk()
root.title("News Article Summariser")
root.geometry('1200x700')

# Create the labels and text boxes for displaying the article's information
tLabel=tk.Label(root,text='Title')
tLabel.pack()
title=tk.Text(root,height=1,width=150)
title.config(state='disabled',bg='#f4fdff')
title.pack()

aLabel=tk.Label(root,text='Author')
aLabel.pack()
author=tk.Text(root,height=1,width=150)
author.config(state='disabled',bg='#f4fdff')
author.pack()

pLabel=tk.Label(root,text='Date of Publishing')
pLabel.pack()
publication=tk.Text(root,height=1,width=150)
publication.config(state='disabled',bg='#f4fdff')
publication.pack()

sLabel=tk.Label(root,text='Summary of the Article')
sLabel.pack()
summary=tk.Text(root,height=20,width=150)
summary.config(state='disabled',bg='#f4fdff')
summary.pack()

seLabel=tk.Label(root,text='Sentiment of the Article')
seLabel.pack()
sentiment=tk.Text(root,height=1,width=150)
sentiment.config(state='disabled',bg='#f4fdff')
sentiment.pack()

# Create the label and text box for the user to enter the URL
uLabel=tk.Label(root,text='URL')
uLabel.pack()
utext=tk.Text(root,height=1,width=150)
utext.pack()

# Create the "Summarize" button and link it to the summarize() function
butto=tk.Button(root,text="Summarize",command=summarize)
butto.pack()

# Start the tkinter event loop
root.mainloop()
