DATA_ACCESS = {
	"valid_credential": [
	    {"username": "amazon.test.jessica@gmail.com",
     	 "password": "amazontest123",
         },
    ],

	"email_not_registered": [
	    {"username": "amazon.test.jessic@gmail.com",
     	 "password": "amazontest123"}
    ],

    "invalid_credential": [
	    {"username": "amazon.test.jessica@gmail.com",
     	 "password": "amazontest12"}
    ],

    "invalid_email_format": [
		{"username": "amazon.test.jessicagmail.com",
         "password": "amazontest123"}
	],

    "no_email": [
		{"username": "",
         "password": "amazontest123"}
	],

	"no_password": [
		{"username": "amazon.test.jessica@gmail.com",
         "password": ""}
	],
}