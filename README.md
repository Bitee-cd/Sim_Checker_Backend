
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

#### Get all Routes of API

```
  GET https://sim-checker.vercel.app/phone_number/details/
```

#### Get all phone numbers

```
  GET https://sim-checker.vercel.app/phone_number/
```


#### Get all sim networks 

```
  GET https://sim-checker.vercel.app/phone_number/sim/
```



#### Get Details using Id

```
  GET https://sim-checker.vercel.app/phone_number/${id}
```

#### Find Details using Phone Number

```
  GET https://sim-checker.vercel.app/phone_number/find/${phone_number}
```

 Parameter 
 - First 4 digits of a phone number OR First 5 digits for numbers starting with 0702       
 Returns 
 - Json file containing data(details of number) and message successful
 - error 404 if number not found with a message





## Acknowledgements

 - [Abubakar Zakari](https://github.com/maesterzak)

## Data gotten from
 - [Wikipedia](https://en.wikipedia.org/wiki/Telephone_numbers_in_Nigeria)
  