from .ai_state import get_cookie, store_cookie

max_length=606
time_limit=55

def AI_answer(model, tokenizer, ai_state, boot_prompt, init_prompt, activity_prompt, max_tokens):
    in_string = boot_prompt + init_prompt + activity_prompt
    inputs = tokenizer.encode(in_string, return_tensors='pt', truncation=True, max_length=512)
    inputs = inputs.cuda()
    attention_mask = inputs.ne(tokenizer.pad_token_id).float()
    outputs = model.generate(inputs, max_length=max_tokens, do_sample=True, max_time=time_limit, attention_mask=attention_mask)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    stripped_text = text[len(in_string):]

    # Check if the model wants to retrieve specific cookies
    if "[GET_COOKIE]" in stripped_text:
        get_cookie_prompt = input("Please enter the name of the cookie you want to retrieve: ")
        cookie_data = get_cookie(ai_state, get_cookie_prompt)
        if cookie_data:
            stripped_text = stripped_text.replace("[GET_COOKIE]", cookie_data)
        else:
            print("Cookie not found. Please try again.")
            return

    # Check if the model wants to store a cookie
    if "[STORE_COOKIE]" in stripped_text:
        store_cookie_prompt = input("Please enter the name of the cookie you want to store: ")
        store_cookie(ai_state, store_cookie_prompt, stripped_text)
        stripped_text = stripped_text.replace("[STORE_COOKIE]", "")

    return stripped_text
