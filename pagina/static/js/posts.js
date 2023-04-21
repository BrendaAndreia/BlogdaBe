$(document).ready(function() {
    var items_per_page = 5;
    var num_items = $('.card').length;
    var num_pages = Math.ceil(num_items / items_per_page);

    // hide all items except for the first page
    $('.card').slice(items_per_page).hide();

    // add pagination links
    for (var i = 0; i < num_pages; i++) {
        $('<li><a href="#" class="page-link">' + (i + 1) + '</a></li>').appendTo('#pagination');
    }

    // highlight the first page link
    $('#pagination li:first-child').addClass('active');

    // handle pagination clicks
    $('#pagination').on('click', '.page-link', function(event) {
        event.preventDefault();
        var page_num = $(this).text();
        var start_index = (page_num - 1) * items_per_page;
        var end_index = start_index + items_per_page;
        $('.card').hide().slice(start_index, end_index).fadeIn();
        $('#pagination li').removeClass('active');
        $(this).parent().addClass('active');
    });
});