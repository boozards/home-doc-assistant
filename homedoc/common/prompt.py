import pathway as pw
from datetime import datetime
from common.openaiapi_helper import openai_chat_completion


def prompt(index, embedded_query, user_query):

    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        print(docs_str)
        prompt = f"Given the following data: \n {docs_str} \nanswer this query.if you dont have enough information for a given question it is preferred that you say i dont have enough information then recommend a professional medical assisstance.you are a home-doctor so if you have enough information be confident in your response .try to be precise and accurate in recommending treatments: {query}"
        return prompt
    
    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_list=pw.this.chunk).promise_universe_is_equal_to(embedded_query)

    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=openai_chat_completion(pw.this.prompt),
    )
