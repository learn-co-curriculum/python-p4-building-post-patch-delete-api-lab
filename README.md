# Building a POST/PATCH/DELETE API Lab

## Learning Goals

- Build an API to handle GET, POST, PATCH, and DELETE requests.

---

## Key Vocab

- **Application Programming Interface (API)**: a software application that
  allows two or more software applications to communicate with one another. Can
  be standalone or incorporated into a larger product.
- **HTTP Request Method**: assets of HTTP requests that tell the server which
  actions the client is attempting to perform on the located resource.
- **`GET`**: the most common HTTP request method. Signifies that the client is
  attempting to view the located resource.
- **`POST`**: the second most common HTTP request method. Signifies that the
  client is attempting to submit a form to create a new resource.
- **`PATCH`**: an HTTP request method that signifies that the client is
  attempting to update a resource with new information.
- **`DELETE`**: an HTTP request method that signifies that the client is
  attempting to delete a resource.

---

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `server/` folder. Make sure to test your
routes in Postman as you progress.

```console
$ pipenv install
$ pipenv shell
```

In this application, we'll be working on a familiar JSON API to get a list of
bakeries and their baked goods. We have two models, bakeries and baked goods, in
a one-to-many relationship. The migrations are already set up. Here's a reminder
of what the ERD for these tables looks like:

![Bakeries ERD](https://curriculum-content.s3.amazonaws.com/phase-3/sinatra-with-active-record-get-lab/bakeries-baked_goods-erd.png)

You can pick up where we left off by entering the following commands:

```console
$ cd server
$ flask db upgrade
$ python seed.py
$ python app.py
```

Edit `server/app.py` to support the following requests:

- Define a `POST` block inside of a `/baked_goods` route that creates a new
  baked good in the database and returns its data as JSON. The request will send
  data in a form.
- Define a `PATCH` block inside of the `/bakeries/<int:id>` route that updates
  the name of the bakery in the database and returns its data as JSON. As with
  the previous `POST` block, the request will send data in a form. The form does
  not need to include values for all of the bakery's attributes.
- Define a `DELETE` block inside of a `/baked_goods/<int:id>` route that deletes
  the baked good from the database and returns a JSON message confirming that
  the record was successfully deleted.

Once all of your tests are passing, commit and push your work using `git` to
submit.

### Examples

#### `POST /baked_goods`

![POST request with form data for a baked good's name, price, and bakery_id](https://curriculum-content.s3.amazonaws.com/6130/python-p4-v2-flask/post.png)

#### `PATCH /bakeries/<int:id>`

![PATCH request with form data for a bakery's name](https://curriculum-content.s3.amazonaws.com/6130/python-p4-v2-flask/ppd_lab_patch.png)

#### `DELETE /baked_goods/<int:id>`

![DELETE request for baked good by ID](https://curriculum-content.s3.amazonaws.com/6130/python-p4-v2-flask/ppd_lab_delete.png)

NOTE: You can use Postman to make get requests for bakeries and baked_goods
before and after your post, patch, and delete requests to ensure the correct
record is being added, updated, or deleted.

---

## Resources

- [Flask - Pallets](https://flask.palletsprojects.com/en/2.2.x/)
- [POST - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
- [PATCH - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)
- [DELETE - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)
- [SQLAlchemy-serializer - PyPI](https://pypi.org/project/SQLAlchemy-serializer/)
