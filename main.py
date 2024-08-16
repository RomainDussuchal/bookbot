def main():
    count = count_words(book)
    text= character_count(book)
    create_report(count, text )
  

book = "books/frankenstein.txt"
def count_words(book):
     with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = 0
        for _ in words:
            count +=1
        return count
       


def character_count(book):
    dict = {}

    with open(book) as f:

        file_contents = f.read()
        lowered_string = file_contents.lower()
        
        for char in lowered_string:
            if char.isalpha():

                if char not in dict:
                    dict[char] =  1
                dict[char] += 1

        return dict


def create_report(count, result):
    print("")
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document")

    sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_result:
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

main()


   
