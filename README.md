
# Sim Checker

Backend of sim checker application
- An app that helps you find and identify the network operator of a Nigerian Phone Number

## Run Locally

Clone the project

```bash
  git clone https://github.com/Bitee-cd/Sim_Checker_Backend
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install
```

Start the server

```bash
  python manage.py runserver
```


## Tech Stack

**Server Side** 
- Django
- Django RestAPI
- Selenium
- Python



## API Reference

#### Get all items

```http
  GET https://sim-checker.vercel.app/phone_number/
```

| URL | Params    | Description                |
| :-------- | :------- | :------------------------- |
| `https://sim-checker.vercel.app/` | `/phone_number` | Json of all sims |

#### Get item

```http
  GET https://sim-checker.vercel.app/phone_number/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |




## Acknowledgements

 - [Abubakar Zakari](https://github.com/maesterzak)

## Data gotten from
 - [Wikipedia](https://en.wikipedia.org/wiki/Telephone_numbers_in_Nigeria)
 