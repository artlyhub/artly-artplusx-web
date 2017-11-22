$(document).ready(function() {
  $(function() {
    var elem = document.querySelector('.masonry-grid')
    var msnry = new Masonry(elem, {
      itemSelector: '.grid-item',
      columnWidth: 200,
      gutter: 10
    })
  })
})

// String.prototype.format = function() {
//   a = this;
//   for (k in arguments) {
//     a = a.replace('{' + k + '}', arguments[k])
//   }
//   return a
// }
//
// function show_artist_info_elmts(img, artist, description) {
//   $('#home-banner').hide()
//   $('#artist-banner').show()
//
//   $('.search-form').hide()
//
//   var artistImg = $('#artist-img')
//   var artistName = $('#artist-name')
//   var artistDesc = $('#artist-description')
//
//   artistImg.attr('src', img)
//   artistName.text(artist)
//   artistDesc.text(description)
// }
//
// function search_artist_api(search_url) {
//   $.ajax({
//     method: 'GET',
//     url: search_url,
//     success: function(data) {
//       result = data[0]
//       console.log(result)
//       console.log(result.profile_img)
//       show_artist_info_elmts(result.profile_img, result.name, result.description)
//     },
//     error: function(data) {
//       console.log(data)
//     }
//   })
// }

// on click button submit form
$('.red.search.icon').click(function(e) {
  var artist = $('input[name=q]').val()
  var reverse_url = '/?q=' + artist
  location.href = reverse_url
})

// // on enter/submit form send api request
// $('.search-form').on('submit', function(e) {
//   e.preventDefault()
//   var artist = $('input[name=q]').val()
//   var search_url = '/api/search/artist/?q=' + artist
//   search_artist_api(search_url)
// })
