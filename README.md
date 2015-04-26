# Restling

My RESTful API built on Python Flask. Try it out at restling.co!

## Version
1.0

## Usage

To ping the restling server, use the /ping endpoint.

To use the public lyrics endpoint, hit the /lyrics endpoint, which supports the parameters 'artist' and 'track'. For example, http://restling.co/lyrics?artist=Taylor_Swift&track=Blank_Space will give you the following JSON response:

```
{"status": "success", "message": null, "data": {"hometown": "Nashville", "preview": "Nice to meet you, where you been?", "lyrics": "Nice to meet you, where you been?\nI could show you incredible things...And I'll write your name\n"}}
```

The full lyrics body is omitted by ```...``` since it's pretty long. Lines in the lyrics are separated by ```\n```, so you could easily parse it to use for your needs.

Use a REST Client to interact with the FAQ (frequently asked questions) endpoint at /faq. The supported resource parameters are ```question``` and ```answer```. 
