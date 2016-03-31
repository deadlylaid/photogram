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
