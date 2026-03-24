---
tags: [concept, api, web, tech]
created: 2026-03-21
related: [HTTP Methods, API Design, TypeScript]
---

# REST vs GraphQL

## What they are
Two approaches to building APIs — how clients request data from a server.

**REST** (Representational State Transfer): multiple fixed endpoints, each returns a specific shape of data. Industry standard.

**GraphQL**: single endpoint (`/graphql`), client specifies exactly what fields it wants in the query.

## How they work

### REST
```
GET  /users/123           → returns full user object
GET  /users/123/posts     → returns user's posts
POST /users               → creates user
PATCH /users/123          → updates user
```
Each URL = one resource. You get what the server decides to give.

### GraphQL
```graphql
query {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}
```
One endpoint. You ask for exactly the fields you need — nothing more.

## When to use each

| | REST | GraphQL |
|---|---|---|
| Simple CRUD API | ✅ | overkill |
| Mobile app (bandwidth sensitive) | ok | ✅ (fetch less) |
| Multiple clients needing different shapes | harder | ✅ |
| Public API for third parties | ✅ (familiar) | depends |
| Rapid iteration on frontend | slower | ✅ |
| Team already knows it | ✅ | learning curve |

## How we use it
EuroSide and most projects use REST via Next.js API routes. GraphQL makes sense when you have many different consumers (mobile app, web, partner API) that need different slices of the same data.

## Key terms
- **Over-fetching** (REST problem): getting more data than needed → GraphQL solves
- **Under-fetching** (REST problem): needing multiple requests for one view → GraphQL solves
- **N+1 problem** (GraphQL problem): resolving nested queries triggers many DB calls → use DataLoader

## Multi-Language Reference — Making API Requests (REST vs GraphQL)

```javascript
// JavaScript — REST
const res = await fetch('https://api.example.com/users/1');
const user = await res.json();

// JavaScript — GraphQL
const res = await fetch('https://api.example.com/graphql', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query: '{ user(id: "1") { name email } }' })
});
const { data } = await res.json();
```

```java
// Java — REST (HttpClient, Java 11+)
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create("https://api.example.com/users/1")).build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
// response.body() → JSON string, parse with Gson/Jackson

// Java — GraphQL
String query = "{\"query\":\"{ user(id: \\\"1\\\") { name email } }\"}";
HttpRequest gqlRequest = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/graphql"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(query)).build();
```

```python
# Python — REST (requests library)
import requests
user = requests.get('https://api.example.com/users/1').json()

# Python — GraphQL
query = '{ user(id: "1") { name email } }'
res = requests.post('https://api.example.com/graphql', json={'query': query})
data = res.json()['data']
```

```c
// C — REST with libcurl
#include <curl/curl.h>
CURL* curl = curl_easy_init();
curl_easy_setopt(curl, CURLOPT_URL, "https://api.example.com/users/1");
curl_easy_perform(curl);  // response written to stdout by default
curl_easy_cleanup(curl);
// GraphQL: same setup but POST with JSON body using CURLOPT_POSTFIELDS
```

```cpp
// C++ — REST with libcurl (same as C)
#include <curl/curl.h>
// REST GET:
CURL* curl = curl_easy_init();
curl_easy_setopt(curl, CURLOPT_URL, "https://api.example.com/users/1");
curl_easy_perform(curl);
// GraphQL POST: set CURLOPT_POSTFIELDS with JSON body
// Or use cpp-httplib / Beast (Boost.Asio) for modern C++
```

## Related
- [[HTTP Methods]] — foundational for REST
- [[API Design]] — principles that apply to both
