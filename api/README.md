# atlas-back-end

By Suntha Lucas

API:
Application Programming Interface.  What is it?  Well, when I read it in english I understood it better.  So I will explain it to you how I read it.
Every page on the internet is stored somewhere on a remote server.  it’s just a part of a remotely located computer that is optimized to process requests.  To put things in perspective, you can spin up a server on your laptop capable of serving an entire website to the Web (in fact, a local server is what engineers use to develop websites before releasing them to the public).  Once you type you the address on www., your browser, a request goes out to the remote server.  Once your browser receives the response, it interprets the code and displays the page.  The browser,  also known as the client, makes whatever www.(like FACEBOOK)the server is an API. Meaning every time you visit a page on the Web, you interact with some remote server's API.  Just remember, an API isn't the same as the remoter server- rather it is the part of the server that receives requests and send reponse!

REST API:
Representational State Transfer--means nothing to me without a full explanation.  A REST API is a way for two computer systems to communicate using the HTTP technologies found in web browsers and servers.  Sharing data between two or more systems is fundamental requirement of software development.  APIs help this type of communication between systems by providing an interface for them to talk to each other.  REST is simply a widely adopted style of API that we use to communicate with internal and external parties in a consistent and predictable way.  For people on the web systems to interact with each  sharing real-time data.  example, retrieving and updating account information in a social media application.  Here's an example of a REST API:

{
  "response_code": 0,
  "results": [
    {
      "category": "Science: Computers",
      "type": "multiple",
      "difficulty": "easy",
      "question": "What does GHz stand for?",
      "correct_answer": "Gigahertz",
      "incorrect_answers": [
        "Gigahotz",
        "Gigahetz",
        "Gigahatz"
      ]
    }
  ]

As you can see it follows a REST convention.  
You could request the same URL and get a response using any HTTP client, such as curl.

MICROSERVICES:
Microservice architecture is a method of developing software systems that tries to focus on building single-functio modules with well-defined interfaces and operations.  Microservices have many benefits for Agile and DevOps teams - as Martin Fowler points out, Netflix, eBay, Amazon, Twitter, PayPal, and other tech stars have all evolved from monolithic to microservices architecture.  Unlike microservices, a monolith application is built as a single, autonomous unit. So any changes to the application are slow, as it affects the entire system. Microservices solve the challenges of monolithic systems by being as modular as possible. In the simplest form, they help build an application as a suite of small services, each running in its own process and being independently deployable. These services may be written in different programming languages and may even use different data storage techniques. Microservices are often connected via APIs and can leverage many of the same tools and solutions that have grown in the RESTful and web service ecosystem. Testing these APIs is now non-negotiable to ensure quality software deployments. It works by validating the communication paths and flow of data throughout your microservice deployment.

Benefits Of Microservices
Simpler to deploy

Deploy in literal pieces without affecting other services.
Simpler to understand

Code is easier to follow since the function is isolated and less dependent.
Reusable across business

Share small services like payment or login systems across the business.
Faster defect isolation

When a test fails or service goes down, isolate it quickly.
Minimized risk from change

Avoid locking in technologies or languages - change on the fly with minimal risk.
There are six characteristics of Microservices:
1. Multiple Components
2. Built For Business
3. Simple Routing
4. Decentralized
5. Failure Resistant
6. Evolutionary
