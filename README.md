# TV Series Finder

TV Series Finder is a simple tool to get TV Series details by passing a search query. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies. Please test in a virtual environment.

```bash
pip install -r requirements.txt
```

## Demo

  [Click Here](https://tvseries.mohitdevda.com/) to check the live version.

## API Usage

  Returns json data of TV Series details matching the search query.

* **URL**

  /api/tv-series-finder

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `search_query=[string] | length=[integer]`
   
   **Optional:**
 
   `page=[integer]`


* **Response:**

    **Content:** `List of TV Series matching similar to search query`
 


* **Sample Call:**

  ```javascript
    $.ajax({
		method: "GET",
		url: '/api/tv-series-finder',
		data: {'search_query': search_query, 'length': 5, 'page': page},
		success: function (data) {
        	console.log(data);
      	}
	});
  ```

## License
[MIT](https://choosealicense.com/licenses/mit/)
