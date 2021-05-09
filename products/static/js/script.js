$(document).ready(function () {
    $('table').DataTable({
        columnDefs: [{
            type: 'natural', targets: 2
        }],
        searching: false,
        paging: false,
        info: false,
    });
    $('.dataTables_length').addClass('bs-select');
});