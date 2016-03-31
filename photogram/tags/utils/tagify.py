from tags.models import Tag


def get_tag_list(content):

    tag_list = [
        word.replace("#", "")
        for word in content.split(" ")
        if word.startswith("#")]
    for tag_name in tag_list:
        tag, is_tag_created = Tag.objects.get_or_create(
            name=tag_name,
        )

    return tag_list


def get_tagify_content(content):
    tag_list = get_tag_list(content)
    word_list = [
        word
        for word
        in content.split(" ")
    ]

    tagify_list = []

    for word in word_list:
        if word in ["#{tag_name}".format(tag_name=tag) for tag in tag_list]:
            word = "<a href='{tag_url}'>{tag_name}</a> ".format(
                tag_name=word,
                tag_url=Tag.objects.get(name=word.replace("#", "")).get_absolute_url(),
            )
        tagify_list.append(word)

    return " ".join(tagify_list)
