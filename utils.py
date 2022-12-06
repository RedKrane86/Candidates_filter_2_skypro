import json


def load_candidates_from_json(path):
    """Загружает данные из файла json"""
    with open(path, "r", encoding="utf8") as file:
        return json.load(file)


def get_all():
    return load_candidates_from_json("candidates.json")


def get_candidate(candidate_id):
    """Возвращает кондидата по id"""
    for candidate in get_all():
        if candidate['id'] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name):
    """Возвращает кондидата по имени"""
    candidates_list = []
    for candidate in get_all():
        if candidate_name.lower() in candidate['name'].lower():
            candidates_list.append(candidate)
    return candidates_list


def get_candidates_by_skill(skill_name):
    """Возвращаетт кандидатов по навыку"""
    candidates_list = []
    for candidate in get_all():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates_list.append(candidate)
    return candidates_list

