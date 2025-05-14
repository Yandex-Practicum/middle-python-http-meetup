import asyncio
import random
import typing

import fastapi


app = fastapi.FastAPI()


async def stream(size_bytes: int, chunk_size: int = 1024) -> typing.AsyncGenerator[bytes, None]:
    for _ in range(size_bytes):
        yield random.randbytes(chunk_size)
        await asyncio.sleep(0.0001)


@app.get("/")
async def streaming_view() -> fastapi.responses.StreamingResponse:
    return fastapi.responses.StreamingResponse(
        stream(1024 * 1024 * 1),
        media_type="application/octet-stream",
        headers={"Content-Disposition": 'attachment; filename="large_file.bin"'},
    )
