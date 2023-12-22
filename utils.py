import openai
import logging
import config

openai.api_key = config.OPENAI_TOKEN

async def generate_schedule(df_parse, df_rest) -> str:
    try:
        prompt = f"На основе этих данных составь расписание на день:\n{df_parse}\n{df_rest}"
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("Ошибка во время взаимодействия с ChatGPT:", e)
        return "Извините, произошла ошибка при составлении расписания."

async def generate_text(prompt) -> dict:
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"user","content": prompt}
            ]

        )
        return response ['choices'][0]['message']['content'],response['usage']['total_tokens']
    except Exception as e:
        logging.error(e)

async def generate_image(prompt, n=1, size="1024x1024") -> list[str]:
    try:
        response = await openai.image.acreate(
            prompt=prompt,
            n=n,
            size=size
        )
        urls = []
        for i in response['data']:
            urls.append(i['url'])
    except Exception as e:
        logging.error(e)
        return []
    else:
        return urls
    

    
