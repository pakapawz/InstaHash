import operator


def retrieve_hashtag():
    file_input = open('file_captions', 'r')
    file_output = open('file_hashtags_duplicate', 'w')

    for line in file_input:
        words = line.split()
        for word in words:
            if '#' in word:
                if len(word) > 2:
                    hashtags = word.split('#')
                    for hashtag in hashtags:
                        if len(hashtag) > 1:
                            # print(hashtag)
                            file_output.write('#' + hashtag + '\n')
    file_input.close()
    file_output.close()


def filter_and_tally_hashtag(hashtags):
    final_hashtags: dict[str, int] = {}  # final container; ready to show to user

    for hashtag in hashtags:
        if hashtag in final_hashtags:
            final_hashtags[hashtag] = final_hashtags[hashtag] + 1
        else:
            final_hashtags[hashtag] = 1

    return final_hashtags


def sort_final_hashtags(the_hashtags):
    the_hashtags = dict(sorted(the_hashtags.items(), key=operator.itemgetter(1), reverse=True))
    return the_hashtags


def get_hashtag_list():
    file_input = open('file_hashtags_duplicate', 'r')
    hashtag_list = []
    for hashtag in file_input:
        hashtag = hashtag.rstrip('\n')
        hashtag_list.append(hashtag)
    return hashtag_list


def get_final_sorted_hashtag():
    file_output = open('file_hashtags_final_sorted', 'w')

    retrieve_hashtag()
    hashtags = get_hashtag_list()
    final_hashtags = filter_and_tally_hashtag(hashtags)
    final_hashtags = sort_final_hashtags(final_hashtags)

    number = 1
    for result in final_hashtags:
        test = 'hashtag #' + str(number) + ' - '
        number += 1
        test += str(final_hashtags[result]) + ' : ' + str(result)
        print(test)
        file_output.write(str(result) + '\n')


