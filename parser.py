from pathway.xpacks.llm.parsers import DoclingParser
import asyncio
from dotenv import load_dotenv
from pathway.xpacks.llm.llms import OpenAIChat
from pathway.internals import udfs

load_dotenv()
doc = []
llm = OpenAIChat(model="gpt-5-mini", cache_strategy=udfs.DefaultCache(),retry_strategy=udfs.ExponentialBackoffRetryStrategy(max_retries=3),)
parser = DoclingParser(image_parsing_strategy="llm", multimodal_llm=llm)

with open("../data/13e6981b-95ed-4aac-a602-ebc5865d0590.pdf", "rb") as f:
    content = f.read();
    doc = asyncio.run(parser.parse(content))


