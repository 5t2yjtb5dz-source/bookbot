def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
  return items["num"]

def chars_report(chars_dict):

  list_chars = []
  for i in chars_dict:
    tmp = {}
    if i.isalpha():
      tmp["char"] = tmp
      tmp["char"] = i
      tmp["num"] = tmp
      tmp["num"] = chars_dict[i]
      list_chars.append(tmp)
  list_chars.sort(key=sort_on, reverse=True)
  # print(list_chars)
  tmp_sorted = ''
  for i in list_chars:
    tmp_sorted = f"\n{i["char"]}: {i["num"]}"
    print(tmp_sorted)