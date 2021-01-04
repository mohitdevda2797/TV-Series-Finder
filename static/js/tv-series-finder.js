let search_button_selector = $('#tv-series-search-button');
let search_input_selector = $('#tv-series-search-box');

function replaceNull(data) {
    if (data === null) {
        return "NA";
    }
    return data;
}

function handleRating(rating) {
    let className = 'badge-danger'
    if (rating === 'NA'){
        className = 'badge-secondary'
    }
    else if (rating > 7){
        className = 'badge-success'
    }
    return `<span class="badge ${className}">${rating}</span>`
}

function handleNullImage(image_url) {
    if (image_url === null){
        return '/static/img/placeholder.png&text=Image+Not+Available'
    }
    return image_url;
}

function loadSearchResults(page = 1) {
    let search_query = search_input_selector.val();
    let url = '/api/tv-series-finder';
    let search_results_div = $("#search_results");

    $.ajax({
        method: "GET",
        url: url,
        data: {'search_query': search_query, 'length': 5, 'page': page},
        success: function (data) {
            if (data.total === 0) {
                search_results_div.html(`<div class="alert alert-danger text-center" role="alert">No Data Found!</div>`);
            } else {
                console.log(data);
                $('#recent-search-terms').hide();
                $('#popular-search-terms').hide();
                search_results_div.html('');
                for (let x of data.data) {
                    search_results_div.append(
                        `<div class="row">
                        <div class="card shadow mb-3 w-100 mx-3"><div class="card-body">
                        <div class="row no-gutters align-items-center">
                        <div class="col-auto">
                            <img class="img-fluid img-rounded" src="${handleNullImage(x.image)}" alt="x${replaceNull(x.name)}">
                        </div>
                        <span class="col mx-4 my-2">
                        <a target="_blank" rel="nofollow" href="${x.url}">
                            <div class="text-primary lead font-weight-bold">${replaceNull(x.name)}</div>
                        </a>
                        <span class="small text-gray-500">Language: ${replaceNull(x.language)} | Avg. Rating: ${handleRating(replaceNull(x.rating))}</span>
                        <div class="mt-2 text-medium-size text-gray-800">${replaceNull(x.summary)}</p></div></div></div></div></div>`
                    );
                }
                paginate(data.total, data.current, data.length)
            }
        },
        error: function () {
            console.log('Something went wrong!')
        }
    });
}

search_button_selector.click(function (e) {
    e.preventDefault();
    loadSearchResults();
});

function paginate(total, current, length) {
    $('#results-paginator').pagination({
        total: total,
        current: current,
        length: length,
        size: 2,
        click: function (options) {
            console.log(options);
            loadSearchResults(options.current);
            $('html, body').animate({
                scrollTop: search_input_selector.offset().top
            }, 500);
        }
    });
}

function autoSearch(search_term) {
    search_input_selector.val(search_term);
    search_button_selector.click();
}