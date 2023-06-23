from utils import ChunkSegments, split_text_to_chunks


DOCUMENT = """
Идейные соображения высшего порядка, а также постоянный количественный рост и сфера нашей активности требуют определения и уточнения дальнейших направлений развития.
Повседневная практика показывает, что рамки и место обучения кадров представляет собой интересный эксперимент проверки новых предложений.
С другой стороны новая модель организационной деятельности позволяет оценить значение позиций, занимаемых участниками в отношении поставленных задач.
Задача организации, в особенности же начало повседневной работы по формированию позиции требуют от нас анализа форм развития.
С другой стороны консультация с широким активом требуют от нас анализа направлений прогрессивного развития.

Задача организации, в особенности же постоянный количественный рост и сфера нашей активности в значительной степени обуславливает создание системы обучения кадров, соответствует насущным потребностям.
Не следует, однако забывать, что реализация намеченных плановых заданий влечет за собой процесс внедрения и модернизации существенных финансовых и административных условий.
Не следует, однако забывать, что дальнейшее развитие различных форм деятельности играет важную роль в формировании систем массового участия.
Не следует, однако забывать, что новая модель организационной деятельности способствует подготовки и реализации форм развития.
Разнообразный и богатый опыт рамки и место обучения кадров обеспечивает широкому кругу (специалистов) участие в формировании дальнейших направлений развития.
Таким образом новая модель организационной деятельности в значительной степени обуславливает создание систем массового участия.
"""


def test_split_text_to_chunks():
    chunks = split_text_to_chunks(
        DOCUMENT,
        100,
        "Продолжаю ответ на вопрос.",
        "Продолжить?",
        "Отвечаю на вопрос.",
    )
    for chunk in chunks:
        assert len(chunk) <= 100
    assert len(chunks) == 34
    assert chunks[0] == 'Отвечаю на вопрос. Идейные соображения высшего порядка, а также постоянный Продолжить?'
    assert chunks[1] == 'Продолжаю ответ на вопрос. количественный рост и сфера нашей активности требуют Продолжить?'
    assert chunks[2] == 'Продолжаю ответ на вопрос. определения и уточнения дальнейших направлений развития. Продолжить?'
    assert chunks[3] == 'Продолжаю ответ на вопрос. Повседневная практика показывает, что рамки и место обучения Продолжить?'
    assert chunks[33] == 'Продолжаю ответ на вопрос. участия.'



def test_split_text_to_chunks__long_text():
    chunks = split_text_to_chunks(
        DOCUMENT,
        2000,
        "Продолжаю ответ на вопрос.",
        "Продолжить?",
        "Отвечаю на вопрос.",
    )
    assert len(chunks) == 1
    assert chunks == [
        "Отвечаю на вопрос. " + DOCUMENT,

    ]



def test_split_text_to_chunks__test_split():
    chunks = split_text_to_chunks(
        DOCUMENT,
        180,
        "Продолжаю ответ на вопрос.",
        "Продолжить?",
        "Отвечаю на вопрос.",
    )
    for chunk in chunks:
        assert len(chunk) <= 180
    assert chunks == [
        'Отвечаю на вопрос. Идейные соображения высшего порядка, а также постоянный количественный рост и сфера нашей активности требуют определения и уточнения дальнейших Продолжить?',
        'Продолжаю ответ на вопрос. направлений развития. Продолжить?',
        'Продолжаю ответ на вопрос. Повседневная практика показывает, что рамки и место обучения кадров представляет собой интересный эксперимент проверки новых предложений. Продолжить?',
        'Продолжаю ответ на вопрос. С другой стороны новая модель организационной деятельности позволяет оценить значение позиций, занимаемых участниками в отношении Продолжить?',
        'Продолжаю ответ на вопрос. поставленных задач. Продолжить?',
        'Продолжаю ответ на вопрос. Задача организации, в особенности же начало повседневной работы по формированию позиции требуют от нас анализа форм развития. Продолжить?',
        'Продолжаю ответ на вопрос. С другой стороны консультация с широким активом требуют от нас анализа направлений прогрессивного развития. Продолжить?',
        'Продолжаю ответ на вопрос. Задача организации, в особенности же постоянный количественный рост и сфера нашей активности в значительной степени обуславливает создание Продолжить?',
        'Продолжаю ответ на вопрос. системы обучения кадров, соответствует насущным потребностям. Продолжить?',
        'Продолжаю ответ на вопрос. Не следует, однако забывать, что реализация намеченных плановых заданий влечет за собой процесс внедрения и модернизации существенных Продолжить?',
        'Продолжаю ответ на вопрос. финансовых и административных условий. Продолжить?',
        'Продолжаю ответ на вопрос. Не следует, однако забывать, что дальнейшее развитие различных форм деятельности играет важную роль в формировании систем массового участия. Продолжить?',
        'Продолжаю ответ на вопрос. Не следует, однако забывать, что новая модель организационной деятельности способствует подготовки и реализации форм развития. Продолжить?',
        'Продолжаю ответ на вопрос. Разнообразный и богатый опыт рамки и место обучения кадров обеспечивает широкому кругу (специалистов) участие в формировании дальнейших Продолжить?',
        'Продолжаю ответ на вопрос. направлений развития. Продолжить?', 'Продолжаю ответ на вопрос. Таким образом новая модель организационной деятельности в значительной степени обуславливает создание систем массового участия.'
    ]


def test_split_text_to_chunks__exact_size():
    chunks = split_text_to_chunks(
        'а бв влдв', #9
        28,
        "Продолжаю ответ на вопрос.",
        "Продолжить?",
        "Отвечаю на вопрос.",
    )
    # 18 + 1 + 9
    assert len(chunks) == 1
    assert chunks[0] == 'Отвечаю на вопрос. а бв влдв'

def test_chunk_segments():
    s = ChunkSegments(prefix='a', sentenses=['c c', 'd d  d', 'e'], postfix='b')
    assert str(s) == 'a c c d d  d e b'
    assert s.str_len() == 16


def test_chunk_segments__no_postfix():
    s = ChunkSegments(prefix='prefix', sentenses=['sentense1', 'sentense2 is here'], postfix=None)
    assert str(s) == 'prefix sentense1 sentense2 is here'
    assert s.str_len() == 34