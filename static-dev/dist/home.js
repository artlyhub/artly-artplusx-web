$(document).ready(function() {
  $('#artist-banner').hide()
})

function search_artist_api(search_url) {
  $.ajax({
    method: 'GET',
    url: search_url,
    success: function(data) {
      console.log(data[0])
      $('#home-banner').hide()
      $('#artist-banner').show()
    },
    error: function(data) {
      console.log(data)
    }
  })
}

// on click button submit form
$('.ui.red.button').click(function(e) {
  var artist = $('input[name=q]').val()
  var search_url = '/api/search/artist/?q=' + artist

  search_artist_api(search_url)
})

// on enter/submit form send api request
$('.search-form').on('submit', function(e) {
  e.preventDefault()
  var artist = $('input[name=q]').val()
  var search_url = '/api/search/artist/?q=' + artist

  search_artist_api(search_url)
})
