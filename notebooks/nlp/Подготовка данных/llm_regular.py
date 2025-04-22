import time
import json
from sources_db import runQuery, execQuery, generateUpdateQuery
from openai import OpenAI

def get_reviews(count=10):
    reviews = runQuery(f"""
    SELECT
        review_id, review_id as id, message
    FROM
        public.analysis_nlp_reviews
    where message_ru is null and LENGTH(message) > 1
    limit {count}
    ;
    """)
    return reviews

# Формирует запрос на обработку одного комментария
def create_message_item(i:int, id: str, message: str):
    return f'''Комментарий в отзыве №{i}: "{message}". Переведи его c бразильского португальского на русский и положи в поле "message" объекта, который будем добавлять в массив.
    В поле "id" положи значение "{id}". Далее заполни поля "q1"–"q11" объекта следующим образом:
    Вопросы к комментарию и мнению автора:
q1: Товар соответствует описанию? "да"/"нет"/"не указано".  
q2: В каком состоянии товар? "в хорошем"/"в плохом"/"в замечательном"/"в ужасном"/"не указано".  
q3: Клиент порекомендует сервис? "да"/"нет"/"не указано".  
q4: Заказ доставлен? "да"/"нет"/"не указано".  
q5: Доставлен вовремя? "да"/"нет"/"не указано".  
q6: Какое настроение клиента? "хорошее"/"плохое"/"замечательное"/"ужасное"/"не указано".  
q7: Клиент будет покупать снова? "да"/"нет"/"не указано".  
q8: Клиент угрожает уйти и больше не далать покупки? "да"/"нет"/"не указано".  
q9: Количество товара (число цифрами или "не указано").  
q10: У клиента были неожиданные проблемы? "да"/"нет"/"не указано".  
q11: Клиент доволен качеством? "да"/"нет"/"не указано".  

Не додумывай, если нет ответа – "не указано".
У тебя получился json объект, добавь его в массив.
'''

def create_message_items(reviews):
    request =[f'Верни ответ в формате JSON. Комментарий должен быть переведён с португальского на русский. Это должен быть массив с {len(reviews)} элементами. Каждый элемент массива это объект с полями с полями: "id", "message", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11". ']
    i = 0
    for review in reviews:
        i += 1
        id = review['id']
        message = review['message']
        message_item = create_message_item(i, id, message)
        request.append(message_item)
    request.append('У тебя должен был получиться json массив. Отдай его мне без лишнего, json должен быть валидный. Верни мне именно плоский массив элементов вида: [\{\}, \{\}, \{\}, ...].')
    return '\n'.join(request)

def send_gpt_request(request_message):
    client = OpenAI(
        api_key="sk-aitunnel-zuQCGqt0pRofcbh9PsfDFgrHbSgIRokH",
        base_url="https://api.aitunnel.ru/v1/",
    )
    results = []
    try:
        chat_result = client.chat.completions.create(
            messages=[{"role": "user", "content": request_message}],
            model="llama-3.2-11b-vision-instruct",
            # model="llama-3.2-3b-instruct",
            max_tokens=50000,
        )
        time.sleep(0.1)
        # print(111)
        response_message = chat_result.choices[0].message.content.replace('\n{', '{').replace('}\n', '}').replace('```json\n', '').replace('```', '').strip()
        start_index = response_message.find('[')
        if start_index > 0:
            response_message = response_message[start_index:]
        end_index = response_message.rfind(']')
        if end_index + 1 < len(response_message):
            response_message = response_message[:end_index + 1]
        print('response_message:', response_message)
        if not response_message.strip():
            return []
        # print(2)
        results = json.loads(response_message)
        # print(3)
        for result in results:
            for key in result:
                # print(414)
                if result[key] == 'да':
                    result[key] = True
                # print(415)
                if result[key] == 'нет':
                    result[key] = False
                # print(416)
                if result[key] == 'не указано':
                    result[key] = None
                # print(417)
                if result[key] in ('ужасное', 'в ужасном'):
                    result[key] = -2
                # print(418)
                if result[key] in ('плохое', 'в плохом'):
                    result[key] = -1
                # print(419)
                if result[key] in ('хорошее', 'в хорошем'):
                    result[key] = 1
                # print(4110)
                if result[key] in ('замечательное', 'в замечательном'):
                    result[key] = 2
                # print(4111)
                if type(result[key]) == str and key not in ['id', 'message']:
                    result[key] = None
                # print(4112)
    except Exception as e:
        print(f"Ошибка при выполнении запроса к GPT: {e}")
    return results

def updateReview(review):
    try:
        id = review['id']
        review['message_ru'] = review['message'].replace("'", '`').replace('"', '`')
        update_q = generateUpdateQuery(review, ['message_ru', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'])
        query = f'''update public.analysis_nlp_reviews SET
        {update_q}
        where review_id='{id}';
        '''
        execQuery(query)
    except Exception as e:
        print(f"Ошибка при выполнении транзакции: {e}")
    finally:
        print("Обновление базы данных завершено.")


# clientGPT = OpenAI(
#     api_key="sk-aitunnel-zuQCGqt0pRofcbh9PsfDFgrHbSgIRokH",
#     base_url="https://api.aitunnel.ru/v1/",
# )
while True:
    reviews = get_reviews(5)
    if not len(reviews):
        print('Обработка завершена')
        break
    request_message = create_message_items(reviews)
    results = send_gpt_request(request_message)
    # results = send_gpt_request(clientGPT, request_message)
    for result in results:
        updateReview(result)
    time.sleep(1)
