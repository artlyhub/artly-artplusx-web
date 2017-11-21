// on click button submit form
$('.ui.red.button').click(function(e) {
  var artist = $('input[name=q]').val()
  var search_url = '/api/search/artist/?q=' + artist

  $.ajax({
    method: 'GET',
    url: search_url,
    success: function(data) {
      console.log(data)
    },
    error: function(data) {
      console.log(data)
    }
  })
})

// on enter/submit form send api request
$('.search-form').on('submit', function(e) {
  e.preventDefault()
  var artist = $('input[name=q]').val()
  var search_url = '/api/search/artist/?q=' + artist

  $.ajax({
    method: 'GET',
    url: search_url,
    success: function(data) {
      console.log(data)
    },
    error: function(data) {
      console.log(data)
    }
  })
})
