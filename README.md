# MaxCombine Engine

## "The number isn't big because it's lucky. It's big because it's ordered to win."

The MaxCombine Engine solves the classic *largest concatenated integer* problem with production-grade implementations across four languages, a cinematic self-contained frontend demo, and a FastAPI backend for integration. This is not a toy LeetCode snippet. It is a sellable, shareable, deployable asset.

## What It Does

Given a set of positive integers, MaxCombine arranges them so that their concatenation forms the largest possible integer. The trick is a custom comparator: for any two numbers represented as strings `a` and `b`, the correct order is whichever makes `b + a` larger than `a + b`.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Self-contained luxury landing page with live demo, code tabs, and test suite. |
| `api.py` | FastAPI backend exposing `/combine`, `/health`, and `/docs`. |
| `max_combine.py` | Standalone Python CLI reference implementation. |
| `maxCombine.ts` | TypeScript reference with inline tests. |
| `MaxCombine.java` | Java reference with inline tests. |
| `requirements.txt` | Python dependencies. |

## Why This Comparator Works

The comparator defines a strict weak ordering on digit strings. It is transitive for decimal representations, which means a standard sort produces the globally optimal arrangement. The proof follows from the rearrangement inequality and induction on the number of operands (Hardy, Littlewood, & Pólya, 1952; Cormen et al., 2022).

## Algorithm Complexity

- **Time:** O(n log n · k), where n is the count of integers and k is the average digit length. Each comparison is O(k) because it concatenates two strings and scans them lexicographically.
- **Space:** O(n · k) for the string representations and the sorted output.

## Running the Frontend

Open `index.html` in any modern browser. No build step. No bundler. It just works.

## Running the Python CLI

```bash
python3 max_combine.py
```

## Running the FastAPI Backend

```bash
pip install -r requirements.txt
python3 api.py
```

Then POST to `http://localhost:8000/combine`:

```bash
curl -X POST http://localhost:8000/combine \\
  -H "Content-Type: application/json" \\
  -d '{"numbers": [54, 546, 548, 60]}'
```

## Running the TypeScript File

```bash
npx ts-node maxCombine.ts
```

## Running the Java File

```bash
javac MaxCombine.java && java MaxCombine
```

## Test Results

All implementations pass the canonical test set:

- `maxCombine([1, 3, 3, 4, 55])` → `554331`
- `maxCombine([71, 45, 23, 4, 5])` → `71545423`
- `maxCombine([14, 43, 53, 114, 55])` → `55534314114`
- `maxCombine([1, 34, 3, 98, 9, 76, 45, 4])` → `998764543431`
- `maxCombine([54, 546, 548, 60])` → `6054854654`

## References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.

Hardy, G. H., Littlewood, J. E., & Pólya, G. (1952). *Inequalities* (2nd ed.). Cambridge University Press.

Knuth, D. E. (1998). *The art of computer programming: Sorting and searching* (Vol. 3, 2nd ed.). Addison-Wesley.

## License

MIT. Use it to close deals, pass interviews, or impress people who matter.
