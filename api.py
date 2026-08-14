from functools import cmp_to_key
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MaxCombine API", version="1.0.0")


class CombineRequest(BaseModel):
    numbers: List[int]


class CombineResponse(BaseModel):
    input_numbers: List[int]
    max_integer: int
    optimal_order: List[str]
    comparator_calls: int


def _comparator(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def max_combine(numbers: List[int]) -> CombineResponse:
    if not numbers:
        return CombineResponse(
            input_numbers=[], max_integer=0, optimal_order=[], comparator_calls=0
        )

    nums = [x for x in numbers if isinstance(x, int) and x >= 0]
    if not nums:
        return CombineResponse(
            input_numbers=numbers, max_integer=0, optimal_order=[], comparator_calls=0
        )

    calls = 0

    def counted_comparator(a: str, b: str) -> int:
        nonlocal calls
        calls += 1
        return _comparator(a, b)

    ordered = sorted(map(str, nums), key=cmp_to_key(counted_comparator))
    joined = ''.join(ordered)
    max_int = 0 if joined[0] == '0' else int(joined)

    return CombineResponse(
        input_numbers=nums,
        max_integer=max_int,
        optimal_order=ordered,
        comparator_calls=calls,
    )


@app.get("/")
def root():
    return {"status": "MaxCombine API is live", "docs": "/docs"}


@app.post("/combine", response_model=CombineResponse)
def combine(payload: CombineRequest):
    return max_combine(payload.numbers)


@app.get("/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
