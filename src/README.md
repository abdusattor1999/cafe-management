# base url in localhost is: "http://127.0.0.1:8000/"
---
#User endpoints

###User registration endpoint
POST -> {{base_url}}/registration/
```
{
    "email":"test@mail.com",
    "password":"eee11111"
}

```

### Verification endpoint
POST -> {{base_url}}/verification/
```
{
    "token":"c24af255-6af1-4bff-b2ed-63275d323ece"
}
```

###Authentication (Login)
POST -> {{base_url}}/authentication/
```
{
    "email":"ali1@mail.com",
    "password":"eee11111"
}
```



---
#Card related endpoints

###Cart add // Authentication required
POST -> {{base_url}}/cart/
```
{
    "product_id":1,
    "quantity":5
}
```

###Delete all cart items // Authentication required
DELETE -> {{base_url}}/cart/

###CartItem delete // Authentication required
DELETE -> {{base_url}}/cart/<id>