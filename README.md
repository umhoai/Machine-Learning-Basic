# split words and perform stemming
            words = item.split()
            stemmed_words = []
            for word in words:
                stemmed_words.append(stemmer.stem(word))

            # join stemmed words back into a string
            item = ' '.join(stemmed_words)
            
            # remove consecutive equal signs
            item = re.sub(r'==+', '=', item)
